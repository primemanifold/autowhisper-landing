---
version: alpha
name: AutoWhisper Design System
description: Warm technical minimalism for a local-first transcription product shipping on macOS and Linux, with mobile and the landing page guided by the same system.
colors:
  primary: "#18181B"
  secondary: "#71717A"
  tertiary: "#D97706"
  neutral: "#FBFAF7"
  paper: "#F6F2EA"
  muted: "#EBE6DC"
  border: "#E7E2D8"
  success: "#16A34A"
typography:
  h1:
    fontFamily: ui-sans-serif
    fontSize: 4.4rem
    fontWeight: 760
    lineHeight: 1.02
    letterSpacing: "-0.055em"
  h2:
    fontFamily: ui-sans-serif
    fontSize: 1.9rem
    fontWeight: 720
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  h3:
    fontFamily: ui-sans-serif
    fontSize: 1.1rem
    fontWeight: 720
    lineHeight: 1.3
    letterSpacing: "-0.015em"
  body-md:
    fontFamily: ui-sans-serif
    fontSize: 1rem
    fontWeight: 450
    lineHeight: 1.65
    letterSpacing: "0em"
  mono-sm:
    fontFamily: ui-monospace
    fontSize: 0.92rem
    fontWeight: 450
    lineHeight: 1.6
    letterSpacing: "0em"
  caps-xs:
    fontFamily: ui-sans-serif
    fontSize: 0.74rem
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "0.06em"
rounded:
  sm: 4px
  md: 10px
  lg: 16px
  xl: 24px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: 14px
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 14px
  proof-badge:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 8px
  accent-mark:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 6px
  success-badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 8px
  quiet-note:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: 16px
  border-surface:
    backgroundColor: "{colors.border}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 4px
  panel:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: 32px
  transcript-card:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 20px
  export-pill:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 6px
  contrast-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.lg}"
    padding: 64px
---

## Overview

AutoWhisper uses warm technical minimalism: paper-toned surfaces, ink typography, and a single restrained warm accent. The system reads as privacy-first and evidence-backed across every surface where the product appears, from a notarized macOS bundle to a packaged Linux build to a stacked mobile screen and the static landing page.

The system favors quiet density over hype. A page should feel maintained by a careful builder, not generated from a SaaS template. Headings carry weight, body copy stays readable at long line lengths, and accent color is reserved for marks of authorship and signal.

## Colors

- **Primary:** ink for headings and high-emphasis action.
- **Secondary:** soft graphite for explanatory copy.
- **Tertiary:** warm amber accent for status, signal, and small marks of authorship. Cap usage at roughly 10 percent of any view.
- **Neutral and paper:** off-white surfaces used as the background system. Avoid pure black and pure white in every surface.
- **Muted:** mid-paper used for inert chips, queue rails, and inactive panels.
- **Border:** hairline rule shared across desktop and mobile.
- **Success:** restrained green reserved for completed states only.

CSS implementations should express palette anchors in OKLCH for richer light handling on wide-gamut displays. The YAML header keeps hex values portable for native and design-tool consumers.

## Typography

System fonts only. Sans-serif throughout for readability across macOS, Linux, mobile, and web. Mono is used for install commands, file names, queue items, and inline status. Body text aims to stay under 72 characters per line.

## Layout

The landing page leans on a wide hero, a product preview, a workflow section that walks through the five core verbs of the app, a privacy panel, a single dark contrast block for emotional punch, and a distribution panel. Each surface uses paper cards with hairline borders and generous internal spacing.

Native apps follow the same rhythm: a privacy header, an action list, a transcript surface, and a queue. Mobile stacks these vertically with safe-area inset padding. Desktop uses a two- or three-column layout where horizontal space allows.

## Elevation and Depth

Depth comes from paper layers and hairline borders. No glass, no decorative blur on content, no colored side stripes. The contrast section is a single inverted block per page. Only the topbar may use a soft backdrop blur for legibility against the hero.

## Shapes

Mid radii on panels and transcript cards. Small radii on pills, badges, and code blocks. The contrast section uses the same radius vocabulary, inverted in color. No fully rounded pill buttons, no organic curves.

## Components

- **button-primary:** ink-filled action used at most twice per view.
- **button-secondary:** paper-filled action with a full ink border.
- **proof-badge:** small paper pill used for release facts: notarization, signing, version, and store identifiers.
- **panel:** paper card for content groups with hairline border. Carries panel headings and supporting copy.
- **transcript-card:** dictation surface with a mono filename label and clear two-tone hierarchy for raw and cleaned text.
- **export-pill:** small caps tag for export formats such as SRT, VTT, TXT, and Markdown. Used as a row of equal-weight pills.
- **dropzone:** dashed-edge surface that previews accepted audio and video formats without animating in marketing surfaces.
- **library-search:** mono search bar paired with file rows and timestamps. Implies local index, not a cloud query.
- **batch-queue:** list of items with progress meters and a one-word state. Always shows at least one done, one running, one queued.
- **contrast-section:** single dark block per page used to land the emotional headline. One per page is the maximum.

## Cross-platform implementation notes

- **macOS:** AppKit chrome reads as native. Use the menu bar for surface controls. Map button-primary to NSButton with a bold material; map proof-badge to a capsule label in the title bar. Distribution must remain Developer ID signed, notarized, and stapled.
- **Linux:** GTK or Qt port keeps the same color tokens. Hairline borders may need to be rendered at 1 device pixel on HiDPI to avoid antialiasing washout. The PPA install path is the canonical entry point.
- **Mobile:** the same palette and component vocabulary translates to a stacked layout. Use safe-area inset padding for the contrast block. Treat the queue as the home surface. Mobile is treated as a future cross-platform target in this system, not as a shipped store product.
- **Landing page:** static HTML and CSS only. No runtime JavaScript, no analytics, no remote fonts. Token values mirror the YAML header so the page can be re-derived from this document.

## Privacy posture

The visual language is privacy-first and evidence-backed. Every claim on any surface should map to a release artifact or a code path. Avoid magic security language. State the boundary, name the model, link the release. Where a feature is not yet shipped on a given platform, say so explicitly rather than implying parity.

## Do and Do not

Do use specific release names, install commands, and caveats. Do keep one dark contrast block per page. Do reuse the same tokens across macOS, Linux, mobile, and the landing page. Do prefer mono for file names, queue items, and install commands.

Do not use gradient text, glass cards on content, analytics, runtime JavaScript on the landing page, fake metrics, generic icon grids, inflated copy, or colored side stripes on cards.
