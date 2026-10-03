---
name: research-video-guide
description: Summarize videos into portable, source-linked HTML research guides with practical actions, configuration prompts, materials, and a prioritized watch table; publish requested guides to Lars's research library.
---

# Research video guide

Create one separate guide per video unless Lars requests a combined treatment. The approved HTML references are in `assets/`. The canonical repository is `larsklanderpe/research-documents-pe`; its `content/*.json` and `scripts/render.py` define the current document structure. Use that renderer rather than redesigning each summary.

## Source and synthesis

Read the full available caption track and expanded video description. In the Chrome extension, use `getTabContext` first for the selected tab and read any returned temporary file in the same turn. Use the configured browser instance for UI inspection. Inspect relevant video frames when captions cannot establish a key detail, such as an on-screen prompt or setting. State the coverage and unresolved gaps.

Extract what Lars can use: key points, actions, configuration choices, prerequisites, materials, and practical limitations. Distinguish presenter claims, demonstrated behavior, and your proposed PE applications. Summarize in original wording and link to the source; retain only necessary short quotations. Keep full transcripts and private source material out of the public repository.

## Approved layout

Read one existing content JSON as the schema example. Preserve the PE visual system, action checklist, ready-to-use prompts, linked materials, evidence/limits, local notes, and print/PDF support. A comparison video may include a comparison table.

The watch table is essential: choose the key sections Lars SHOULD watch, link each starting timestamp, give an ending timestamp and a concrete reason. Aim for 10 to 15 minutes of relevant material where possible; calculate the total rather than assuming it. Exclude introductions, promotions, repetitions, and unrelated demonstrations. Match the selection to Lars's work.

Use a stable descriptive slug and source metadata: title, video ID, summary date, named author and publication date when established. Label original prompts as adaptations. List directly linked materials and identify references whose download links were not found. Explain material limitations without presenting a personal comparison as a controlled benchmark.

## Render and publish

Work on a branch and respect the active global/repository instructions. Add the content JSON, run `python scripts/render.py`, inspect the rendered page at desktop and narrow widths, and check timestamps, navigation, print behavior, and script syntax. Preserve previous guides and their stable URLs. Completion means a useful artifact, not a chat-only summary.

When publication is requested, commit and push the source repository, then run `scripts/Publish-Research.ps1` with the source and existing site repository paths. Publication copies only `site/` into `agents-phone/research-documents-pe/`; the existing domain owner and CNAME remain unchanged. The script stages a dedicated branch and PR. Follow the active merge authorization rules before integration; user intent to publish does not override an explicit governing merge gate. If approved, merge, verify deployment and public URLs, then clean up merged branches.

Finish with the verified library URL and direct guide URL. If awaiting approval or deployment, report the exact pending action and PR; call a URL live only after it returns the expected guide. The target base URL is `https://larsklander.com/research-documents-pe/`.
