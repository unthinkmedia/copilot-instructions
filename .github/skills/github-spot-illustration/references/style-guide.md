# GitHub spot-icon reference

Reviewed on 2026-11-09. This file separates published guidance from visual
observations and local working conventions. It contains no official vector
assets and grants no rights to reproduce or redistribute GitHub artwork.

## Official sources

- Iconography: https://brand.github.com/graphic-elements/iconography
- Color: https://brand.github.com/foundations/color
- Illustration: https://brand.github.com/graphic-elements/illustration
- Octicons: https://primer.style/octicons/

## Published guidance

The iconography guidance identifies Octicons as the default product icons.
Spot icons supplement them at larger sizes; they are not replacements for
Octicons and should not be used at small sizes.

Spot icons derive from gitline shapes: the timeline and commit circle are
adapted into recognizable product-icon forms. They can support content and
card layouts outside navigation and product-icon lockups. Color should be
restrained, using neutrals and selected primary or secondary hero colors.

The broader illustration system is separate. Contribution squares form its
foundation; expressive key art may feature mascots and richer patterns.
Do not treat every GitHub brand illustration as a spot-icon reference.

The color guidance anchors the primary palette in neutrals with green as its
hero color, while showing mostly neutral applications with small green moments.
It does not require every spot icon to be green.

Selected published palette values:

| Published name | Value |
| --- | --- |
| GitHub Green / Green 4 | `#0FBF3E` |
| Gray 1 | `#F2F5F3` |
| Gray 2 | `#E4EBE6` |
| Gray 3 | `#B6BFB8` |
| Gray 4 | `#909692` |
| Gray 5 | `#232925` |
| Gray 6 | `#101411` |
| Green 5 | `#08872B` |

These are palette options, not a prescribed spot-icon mapping or accessible
foreground/background pairing. Evaluate contrast and visual hierarchy on the
actual surface; pure hero green is not automatically suitable for a fine line.

## Visual observations

The spot-icon grid on the reviewed iconography page shows thin dark outlines,
muted gray-green secondary lines, open geometric forms, and clusters or runs of
commit-circle-like dots. Some subjects combine strong and muted contours.
The images illustrate shape language, not editable path definitions.

The page provides no legend saying gray denotes a primary-color replacement.
Treating all gray regions as accent targets would erase the distinction between
context and emphasis.

Rounded forms, restrained detail, and abundant space are observed tendencies,
not a published numeric construction specification. Do not infer exact strokes,
spacing ratios, official minimum sizes, or source colors from a screenshot.

## Local working conventions

These conventions support consistent custom work but are not GitHub standards:

- Start with a transparent 256 by 256 view box unless the destination differs.
- Keep main outline, supporting detail, accent, and optional surface roles
  separate, even when some currently use identical colors.
- Keep essential geometry neutral and strong enough for the actual surface.
- Keep contextual paths and dots muted; promote only a meaningful focal detail
  to the accent role. An accent is optional.
- Prefer one subject and no more than one supporting motif.
- Choose stroke weight by inspection at the intended size, not by scaling a
  screenshot measurement.
- Support light and dark surfaces through resolved role mappings, not wholesale
  inversion or automatic primary-color replacement.

For example, a protected-repository concept could have a neutral repository
outline, a muted contextual gitline, and a selective accent on the protection
indicator. This is a composition suggestion, not an existing official asset.

## Custom Azure/cloud-component adaptation

This optional treatment is a user-directed product adaptation, not official
GitHub or Azure guidance. Use it only when requested; do not silently change a
GitHub subject into cloud imagery.

Keep the flat outlines, rounded joins, negative space, and semantic theme roles.
Replace timeline dots and merge branches with component slots and small
rounded-square ports attached to app/resource outlines. Use short connectors
only where they explain a real relationship. An app outline can supply the
shared boundary; it is not evidence of security or runtime isolation.

Examples: Create retains its app window and plus with a component slot;
Assemble connects source and resource inputs separately into app ports;
Open and No apps yet remove decorative routing; Awaiting a result connects
the intake tray to a port on an empty result window without a success cue.
Functional icons and spot artwork should feel related, not be scaled copies.

## Source handling

For reused or adapted assets, record the source and applicable license or user
authorization with the deliverable, preserving required notices. Do not call an
adapted asset unchanged, and do not call original geometry an official icon.
Do not download and redistribute the reference grid as a substitute for an
authorized vector library.

For original artwork, identify the chosen vocabulary: custom GitHub-style SVG,
or a custom Azure/cloud-component adaptation. Do not imply official GitHub or
Azure endorsement or fabricate provenance.
