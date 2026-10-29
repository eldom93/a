# a — a quiet starter

A tiny, zero-dependency landing page you can open in a browser and shape
into whatever this repo turns into. Previously, this `README.md` contained
the single character `a`. You deserved better than that.

## What's in here

```
.
├── index.html    # the page itself
├── styles.css    # theming (CSS custom properties), layout, dark mode
├── script.js     # progressive enhancement: theme toggle + a small nicety
└── README.md     # you are here
```

That's the whole project. There is no build step, no package manager, no
`node_modules`.

## Run it

Open `index.html` directly in your browser, or serve the folder locally:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Any static file server will do.

## Features

- **Zero dependencies.** No npm, no bundler, no lockfile.
- **Dark mode.** Follows your OS preference by default, with a toggle that
  persists your choice in `localStorage`.
- **Accessible.** Semantic landmarks, a skip link, visible focus rings, and
  respect for `prefers-reduced-motion`.
- **Responsive.** Fluid typography with `clamp()` and a layout that reads
  cleanly from phone to wide display.
- **Modern CSS.** CSS custom properties for theming, logical properties,
  and `color-mix()` — no preprocessor required.

## Customize

- **Colors and spacing** live as CSS custom properties at the top of
  `styles.css`. Change `--accent` once and the whole page follows.
- **Copy and sections** live in `index.html`. Delete anything you don't
  need; nothing in the CSS or JS depends on a specific section being
  present.
- **Scripts** in `script.js` are strictly progressive enhancement. The
  page works fully with JavaScript disabled.

## License

No license has been chosen yet. Until one is added, default copyright
applies and others do not have permission to use, modify, or distribute
this code. See [choosealicense.com](https://choosealicense.com/) for help
picking one.
