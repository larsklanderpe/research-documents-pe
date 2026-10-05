# Session notes

## 2026-10-04: Lenny and Tibo Dots reading guide

- CURRENT BRANCH: feat/lenny-dots-reading-guide, isolated publication clone.
- OPEN PRs: source and website publication PRs being prepared.
- EXTERNAL DEPENDENCIES: merge authorization and GitHub Pages deployment.
- Added an original summary based on the complete available caption track and expanded description, with PE adaptations and a 12:53 prioritized watch route.
- Validation: five guides render; all four earlier guide files remain unchanged; timestamps, navigation, offline support and script syntax checked. Local browser preview was blocked by browser security policy.
- Next: integrate approved publication PRs and verify the public guide and library index.

## 2026-10-02: Lauren Tan preliminary brief

- CURRENT BRANCH: feat/lauren-tan-brief
- OPEN PRs: source and domain publication PRs being prepared.
- EXTERNAL DEPENDENCIES: merge approval and GitHub Pages deployment.
- Added the source-grounded implementation brief with explicit incomplete video coverage and a provisional watch route.
- Added preliminary coverage support to the renderer so rebuilds preserve the evidence limits.
- Validation: four guides render; previous guide files unchanged; new brief previously checked at desktop and narrow widths.
- Next: merge approval, publication, and verify public guide and library index.


## 2026-10-02: Published research library

- CURRENT BRANCH: feat/research-guides (completion notes; canonical default is main).
- OPEN PRs: site publication PR #5 merged as 502c92d; completion notes PR pending.
- EXTERNAL DEPENDENCIES: GitHub Pages serves agents-phone/main. larsklander.com remains bound to agents-phone.
- Canonical repository: https://github.com/larsklanderpe/research-documents-pe
- Live library: https://larsklander.com/research-documents-pe/
- All three guide URLs returned HTTP 200 with the library navigation and linked watch table present.
- Installed and validated research-video-guide under C:\Users\Lars\.codex\skills. The repository keeps the canonical skill and approved layout references.
- Renderer rebuilds all guides and the index from content JSON. Publish-Research.ps1 was exercised end to end through the merged site PR.
- Lars approved keeping the existing domain path and requested an automatically maintained index. No new domain or DNS configuration is needed.
- Future summaries: use the skill, add source content, render, publish through the existing site repository, verify URLs, return the direct guide and index links.
