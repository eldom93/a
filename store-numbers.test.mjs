import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import test from 'node:test';
import assert from 'node:assert/strict';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(root, 'index.html'), 'utf8');
const block = html.match(/\/\* __store_numbers_pure__ \*\/([\s\S]*?)\/\* __store_numbers_pure_end__ \*\//);
assert.ok(block, 'pure helpers present in index.html');
const pure = block[1];
const { localISODate, mergeDay } = new Function(pure + '\nreturn { localISODate, mergeDay };')();

function localIn(tz, iso) {
  const script = pure + `\nprocess.stdout.write(localISODate(new Date(${JSON.stringify(iso)})));`;
  const result = spawnSync(process.execPath, ['-e', script], {
    env: { ...process.env, TZ: tz },
    encoding: 'utf8',
  });
  assert.equal(result.status, 0, result.stderr);
  return result.stdout;
}

test('date inputs use the local calendar day', () => {
  assert.equal(html.includes('valueAsDate'), false);
  assert.match(html, /\$\('t_date'\)\.value = localISODate\(new Date\(\)\)/);
  assert.match(html, /\$\('s_date'\)\.value=localISODate\(new Date\(\)\)/);
});

test('shift CSV exports the stored ISO timestamp', () => {
  assert.match(html, /\[e\.saved,e\.date,e\.name/);
  assert.equal(html.includes('e.savedLocal,e.date'), false);
});

test('an evening close in US Central stays on that local day', () => {
  // 03:30 UTC on Nov 21 is 9:30pm on Nov 20 in Chicago.
  // valueAsDate would stamp Nov 21 and the next afternoon's save would overwrite it.
  assert.equal(localIn('America/Chicago', '2026-11-21T03:30:00.000Z'), '2026-11-20');
});

test('an early morning east of UTC stays on that local day', () => {
  // 12:30 UTC on Nov 20 is 1:30am on Nov 21 in Auckland.
  assert.equal(localIn('Pacific/Auckland', '2026-11-20T12:30:00.000Z'), '2026-11-21');
});

test('re-saving one field keeps the other stored numbers', () => {
  const existing = {
    date: '2026-11-20', sales: 773.87, guests: 58, drink: 97.1,
    fc: 31, hours: 21, open: 13, wage: 13,
  };
  const incoming = {
    date: '2026-11-20', sales: 800, guests: null, drink: null,
    fc: null, hours: null, open: null, wage: null,
  };
  assert.deepEqual(mergeDay(existing, incoming), {
    date: '2026-11-20', sales: 800, guests: 58, drink: 97.1,
    fc: 31, hours: 21, open: 13, wage: 13,
  });
});

test('a typed zero replaces the stored number', () => {
  const existing = {
    date: '2026-11-20', sales: 100, guests: 10, drink: 5,
    fc: 30, hours: 8, open: 10, wage: 13,
  };
  const incoming = {
    date: '2026-11-20', sales: 0, guests: 0, drink: null,
    fc: null, hours: null, open: null, wage: null,
  };
  const out = mergeDay(existing, incoming);
  assert.equal(out.sales, 0);
  assert.equal(out.guests, 0);
  assert.equal(out.drink, 5);
  assert.equal(out.wage, 13);
});

test('a stored zero is kept when that field is left blank', () => {
  const existing = {
    date: '2026-11-20', sales: 0, guests: 0, drink: null,
    fc: null, hours: null, open: null, wage: null,
  };
  const incoming = {
    date: '2026-11-20', sales: null, guests: null, drink: null,
    fc: null, hours: null, open: null, wage: null,
  };
  const out = mergeDay(existing, incoming);
  assert.equal(out.sales, 0);
  assert.equal(out.guests, 0);
});

test('the first save stores only what was entered', () => {
  const incoming = {
    date: '2026-11-20', sales: 10, guests: null, drink: null,
    fc: null, hours: null, open: null, wage: null,
  };
  assert.equal(mergeDay(null, incoming), incoming);
});
