# Mid-Willamette Palette (Simplified)

Two six-color schemes with tinted backgrounds (no pure white/black). Chips list **HEX** and **RGB**.

<style>
  .chips{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:.75rem;margin:1rem 0}
  .chip{display:flex;align-items:center;gap:.75rem;padding:.6rem .8rem;border:1px solid var(--mwa-border,rgba(0,0,0,.14));border-radius:.6rem;background:var(--mwa-surface,transparent)}
  .swatch{width:2rem;height:2rem;border-radius:.4rem;border:1px solid rgba(0,0,0,.1)}
  .meta{display:flex;flex-direction:column;line-height:1.2}
  .name{font-weight:600}
  .code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono","Courier New",monospace;font-size:.85em;opacity:.85}
  [data-md-color-scheme="slate"] .chip{border-color:var(--mwa-border,rgba(255,255,255,.22))}
  [data-md-color-scheme="slate"] .swatch{border-color:rgba(255,255,255,.18)}
</style>

## Valley Morning (Light)

<div class="chips">

  <div class="chip"><span class="swatch" style="background:#EAF3F1"></span><div class="meta"><span class="name">Background · River Mist</span><span class="code">HEX #EAF3F1</span><span class="code">RGB 234, 243, 241</span></div></div>

  <div class="chip"><span class="swatch" style="background:#F4F8F6"></span><div class="meta"><span class="name">Surface · Lichen Veil</span><span class="code">HEX #F4F8F6</span><span class="code">RGB 244, 248, 246</span></div></div>

  <div class="chip"><span class="swatch" style="background:#2F3437"></span><div class="meta"><span class="name">Text · Basalt</span><span class="code">HEX #2F3437</span><span class="code">RGB 47, 52, 55</span></div></div>

  <div class="chip"><span class="swatch" style="background:#2D767F"></span><div class="meta"><span class="name">Primary · Santiam Teal</span><span class="code">HEX #2D767F</span><span class="code">RGB 45, 118, 127</span></div></div>

  <div class="chip"><span class="swatch" style="background:#2E4A3B"></span><div class="meta"><span class="name">Secondary · Douglas Fir</span><span class="code">HEX #2E4A3B</span><span class="code">RGB 46, 74, 59</span></div></div>

  <div class="chip"><span class="swatch" style="background:#B6872E"></span><div class="meta"><span class="name">Accent · Oak Savanna</span><span class="code">HEX #B6872E</span><span class="code">RGB 182, 135, 46</span></div></div>

</div>

## River Dusk (Dark)

<div class="chips">

  <div class="chip"><span class="swatch" style="background:#0F1617"></span><div class="meta"><span class="name">Background · River Night</span><span class="code">HEX #0F1617</span><span class="code">RGB 15, 22, 23</span></div></div>

  <div class="chip"><span class="swatch" style="background:#141D1C"></span><div class="meta"><span class="name">Surface · Deep Forest</span><span class="code">HEX #141D1C</span><span class="code">RGB 20, 29, 28</span></div></div>

  <div class="chip"><span class="swatch" style="background:#E8ECEB"></span><div class="meta"><span class="name">Text · Fog</span><span class="code">HEX #E8ECEB</span><span class="code">RGB 232, 236, 235</span></div></div>

  <div class="chip"><span class="swatch" style="background:#6FBABF"></span><div class="meta"><span class="name">Primary · Santiam Teal 400</span><span class="code">HEX #6FBABF</span><span class="code">RGB 111, 186, 191</span></div></div>

  <div class="chip"><span class="swatch" style="background:#6E9C87"></span><div class="meta"><span class="name">Secondary · Moss</span><span class="code">HEX #6E9C87</span><span class="code">RGB 110, 156, 135</span></div></div>

  <div class="chip"><span class="swatch" style="background:#D2AC5C"></span><div class="meta"><span class="name">Accent · Oak Savanna 300</span><span class="code">HEX #D2AC5C</span><span class="code">RGB 210, 172, 92</span></div></div>

</div>

---

### Minimal tokens (optional)

```css
/* Light */
[data-md-color-scheme="default"]{
  --md-default-bg-color:#EAF3F1;   /* Background */
  --mwa-surface:#F4F8F6;           /* Surface */
  --md-default-fg-color:#2F3437;   /* Text */
  --md-primary-fg-color:#2D767F;   /* Primary */
  --mwa-secondary:#2E4A3B;         /* Secondary */
  --md-accent-fg-color:#B6872E;    /* Accent */
}

/* Dark */
[data-md-color-scheme="slate"]{
  --md-default-bg-color:#0F1617;   /* Background */
  --mwa-surface:#141D1C;           /* Surface */
  --md-default-fg-color:#E8ECEB;   /* Text */
  --md-primary-fg-color:#6FBABF;   /* Primary */
  --mwa-secondary:#6E9C87;         /* Secondary */
  --md-accent-fg-color:#D2AC5C;    /* Accent */
}
