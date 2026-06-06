# GymFlex — Generate Model, Clothes & Photoshoot

Turn Alibaba supplier photos into professional GymFlex product shots. Screenshot → analyze → generate → (optional) add logo.

---

## The problem

Project manager sends you raw product images from China (Alibaba). You need:

1. Professional studio-quality photos
2. The same clothes reproduced accurately
3. GymFlex branding on the apparel (logo placement — next step)

You don't need a photographer on day one — you need **reference analysis + regeneration**.

---

## Step 1 — Capture the supplier image

Can't download? Screenshot a crop:

- **Mac:** `Cmd + Shift + 4` → select the product area
- Save the crop as your reference image

---

## Step 2 — Analyze the photo

Attach the screenshot to ChatGPT (or Gemini) and paste:

```
Analyze this photo and give me a prompt to generate the exact same clothes.
```

You'll get:

- Outfit breakdown (jacket, bra, leggings, accessories)
- Fabric and color notes
- Reusable prompts for different platforms

Save the analysis to `gymflex/products/` for reuse.

---

## Step 3 — Generate the studio product photo

### Option A — Prompt only (no reference attached)

```
Generate photo

Studio product photo of a female model wearing a premium burgundy three-piece activewear set. The outfit includes a cropped fitted zip-up jacket with a high mock neck and long sleeves, a matching scoop-neck sports bra, and high-waisted 7/8-length leggings with a V-shaped waistband. The fabric is smooth matte compression material, nylon-spandex blend, buttery-soft and sculpting. The model stands in a relaxed pose with hands clasped in front. She wears white ribbed crew socks and chunky white athletic sneakers. Minimalist light gray seamless background, soft studio lighting, ultra-realistic product photography, luxury athleisure brand aesthetic, highly detailed fabric texture, 4K.
```

### Option B — Reference image + prompt (more accurate)

Attach the Alibaba screenshot, then:

```
Use the attached image as a reference for the exact clothing. Generate a studio product photo of a female model wearing this same burgundy three-piece activewear set.

Studio product photo of a female model wearing a premium burgundy three-piece activewear set. The outfit includes a cropped fitted zip-up jacket with a high mock neck and long sleeves, a matching scoop-neck sports bra, and high-waisted 7/8-length leggings with a V-shaped waistband. The fabric is smooth matte compression material, nylon-spandex blend, buttery-soft and sculpting. The model stands in a relaxed pose with hands clasped in front. She wears white ribbed crew socks and chunky white athletic sneakers. Minimalist light gray seamless background, soft studio lighting, ultra-realistic product photography, luxury athleisure brand aesthetic, highly detailed fabric texture, 4K.
```

If it only returns text, say:

```
Generate an image (not just the prompt).
```

---

## Step 4 — Platform-specific prompts

### E-commerce listing

```
Women's burgundy seamless yoga set, cropped zip jacket, scoop-neck sports bra, high-waisted compression leggings, matching 3-piece workout outfit, premium athleisure wear, matte nylon-spandex fabric, luxury fitness apparel.
```

### Fashion design brief

```
Design a women's premium athleisure set in deep burgundy featuring a cropped zip-up jacket with mock neck, supportive scoop sports bra, and high-waisted 7/8 leggings with V-cut waistband. Minimal seams, matte performance fabric, sleek sculpted silhouette.
```

### Midjourney / image generators

```
Ultra realistic studio product photography, female model wearing a burgundy 3-piece activewear set, cropped zip-up jacket, scoop neck sports bra, high-waisted V waistband leggings, white socks, chunky white sneakers, light gray seamless background, luxury athleisure campaign, soft studio lighting, detailed fabric texture, clean minimalist aesthetic --ar 2:3 --v 7
```

---

## Step 5 — Add GymFlex logo to the clothes (branded version)

Once you have a generated product shot (or use the generated model image), attach:

- Generated product photo
- GymFlex logo PNG (transparent)

```
Place the GymFlex logo subtly on the left chest of the cropped zip-up jacket in this product photo. Keep the logo small, clean, and embroidered-looking. Do not change the clothing color, fit, or studio background. Ultra-realistic, seamless brand placement.
```

Variations:

```
Add a small white GymFlex logo on the high waistband of the leggings, centered on the front.
```

```
Create a branded campaign version: same outfit and pose, GymFlex logo on jacket chest, slightly warmer studio lighting, premium fitness brand campaign feel.
```

---

## Full workflow checklist

| Step | Action |
|---|---|
| 1 | Screenshot Alibaba product (`Cmd+Shift+4`) |
| 2 | Attach image → *"Analyze this photo and give me a prompt to generate the exact same clothes"* |
| 3 | Save outfit breakdown to product spec file |
| 4 | Generate studio photo (prompt only or reference + prompt) |
| 5 | Iterate pose, lighting, or model until approved |
| 6 | Attach logo PNG → place branding on jacket/leggings |
| 7 | Export finals for website, Amazon, Etsy, ads |

---

## What you're learning

Same pattern as logos and WWE images:

1. **Don't start from scratch** — screenshot the supplier photo
2. **Let AI analyze** — extract clothing details you can't describe yourself
3. **Generate from prompt or reference** — your choice
4. **Brand it** — add GymFlex logo in a second pass
5. **Reuse prompts** — e-commerce, Midjourney, campaign variants

You're not a fashion designer or photographer. You're using AI + references to solve a business problem.

---

## Related files

- `gymflex/gymflex-business-deepdive.md` — brand context
- `gymflex/gymflex-icp.md` — target customer
- `gymflex/products/sculpt-luxe-burgundy-set.md` — this product spec
- `prompts/gymflex-logo-prompt.md` — create the logo first if you don't have one
