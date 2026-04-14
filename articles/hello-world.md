# Building a Portfolio Site with Vanilla HTML, CSS, and Conway's Game of Life

I built a developer portfolio using only vanilla HTML, CSS, and JavaScript — no frameworks, no build tools, no dependencies. The background runs Conway's Game of Life on a full-viewport canvas. Here's how it works and what I learned.

## The constraints

I set a few rules before writing any code:

- **No frameworks, no build tools, no dependencies.** Pure vanilla HTML, CSS, and JS.
- **Single-file architecture.** Each page contains its own styles and scripts inline.
- **Greyscale only.** No color accents. The palette runs from `#111` to `#f0f0f0`.
- **KISS and YAGNI.** If I don't need it today, it doesn't exist.

## Conway's Game of Life

The background is a full-viewport canvas running Conway's Game of Life at ~10fps. Cells are 5px squares — alive cells render as `#1f1f1f` on a `#111` dead background, so the animation is subtle and doesn't compete with the content.

Click anywhere on the background and a **pulsar** (a period-3 oscillator) spawns at that position. The code clears a 15x15 dead zone first so the pattern has room to breathe instead of being consumed by the surrounding population.

The canvas sits behind the content with `z-index: -1` and `pointer-events: none`. The click listener lives on `document` and skips interactive elements.

## Frosted glass

The main content column and footer use a frosted glass effect:

- `background: rgba(17, 17, 17, 0.85)` for slight transparency
- `backdrop-filter: blur(6px)` to blur the Conway grid behind the content
- Thin `1px solid #1a1a1a` side borders

This lets the Game of Life animation remain visible in the margins while keeping text perfectly readable.

## Typography

Two fonts via Google Fonts:

- **Inter** for body text — clean, modern, excellent readability
- **JetBrains Mono** for navigation, metadata, tags, and code-style accents

The hierarchy uses weight and color rather than size variation. Section headings are small, uppercase, monospace, and muted (`#555`). Content headings are slightly larger, bolder, and brighter (`#ccc`).

## What I learned

Building without a framework forces you to understand every line. There's no magic — no virtual DOM diffing, no reactive state management, no CSS-in-JS runtime. Just the platform.

The result is a 22KB single file that loads instantly, scores well on Lighthouse, and does exactly what I need. Nothing more.

---

*This site is open source. You can find the code on [GitHub](https://github.com/tiboitel/tiboitel.github.io), or [get in touch](index.html#contact) if you want to talk shop.*
