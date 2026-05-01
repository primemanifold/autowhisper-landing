---
version: alpha
name: AutoWhisper Field Manual
description: A tactile editorial identity for a local-first desktop dictation utility.
colors:
  primary: "#17130F"
  secondary: "#62584C"
  tertiary: "#8A4E24"
  neutral: "#F3EBDD"
typography:
  h1:
    fontFamily: ui-serif
    fontSize: 5rem
    fontWeight: 760
    lineHeight: 0.9
    letterSpacing: "-0.06em"
  body-md:
    fontFamily: ui-sans-serif
    fontSize: 1rem
    fontWeight: 450
    lineHeight: 1.65
    letterSpacing: "0em"
rounded:
  sm: 8px
  md: 18px
  lg: 32px
spacing:
  sm: 8px
  md: 18px
  lg: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "999px"
    padding: 15px
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "999px"
    padding: 15px
  quiet-note:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.lg}"
    padding: 24px
  command-label:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
    padding: 8px
---

## Overview

The visual system treats AutoWhisper as a quiet desktop tool with the character of a printed field manual. The site is warm, tactile, direct, and sparse. It should feel maintained by a careful builder, not generated from a SaaS template.

## Colors

- **Primary:** carbon ink for headings and high-emphasis action.
- **Secondary:** cooled brown gray for explanatory copy.
- **Tertiary:** oxidized copper for command labels, rules, and small signals.
- **Neutral:** aged paper background. Avoid pure black and pure white.

CSS may use OKLCH for richer implementation tokens, but the palette should remain restrained. Accent usage stays below 15 percent of the page.

## Typography

Use system fonts only. Serif headlines create an editorial, non-generic shape. Sans-serif body copy keeps install commands and navigation practical. Body text should stay under 72 characters per line.

## Layout

The page should not be a wall of identical cards. Use a strong editorial hero, a sidecar device panel, a command ledger, and a small proof strip. Vary spacing deliberately. Keep mobile flow linear and readable.

## Elevation & Depth

Depth comes from paper layers, hairline borders, and low chroma shadows. No glass effects. No decorative blur panels.

## Shapes

Large radii can be used for the hero shell and command panels. Tiny labels and code pills use smaller radii. Avoid colored side stripes.

## Components

- Primary buttons are ink-filled pills.
- Secondary buttons are paper-filled pills with a full border.
- Command blocks are copyable-looking static code panels, not active widgets.
- Notices should be full-width paper notes with direct language.

## Do's and Don'ts

Do use specific release names, install commands, and caveats. Do keep the page static. Do preserve the privacy claim as local-first, not absolute security marketing.

Do not use gradient text, glass cards, analytics, runtime JavaScript, fake metrics, generic icon grids, or inflated copy.