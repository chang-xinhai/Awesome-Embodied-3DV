# AGENTS.md

## Mission

This repository is a curated **Awesome-Embodied-3DV** list for the research space where 3D/4D perception, reconstruction, generation, simulation-ready assets, and embodied world models meet.

The goal is not to be a generic 3D generation, NeRF, 3DGS, graphics, SLAM, or robot-learning bibliography. The goal is to organize the most relevant resources for:
- 2D/physical sensing signals that feed 3D systems: depth, normals, structured light, panoramic/fisheye perception, and dense mapping
- 3D/4D representations: 3DGS, 4DGS, NeRF/SDF, mesh, voxel, point-cloud, hybrid, and dynamic representations
- offline, streaming, online, semantic, instance-level, object-centric, scene-level, and dynamic 3D reconstruction
- object-level, part-level, articulated, scene-level, editable, and simulation-ready 3D generation
- embodied world models, dynamic scene graphs, 3D grounding, robotics integration, and sim-to-real asset pipelines
- datasets, benchmarks, metrics, simulators, and toolchains that help researchers choose what to use

## Single-file content policy

All curated content lives in `README.md`.

Do **not** create `contents/` pages for paper organization.
Do **not** split the awesome list into multiple markdown content files unless the user explicitly requests it.

Allowed root-level files:
- `README.md` - the canonical awesome list
- `AGENTS.md` - governance and maintenance rules
- `LICENSE`
- `.gitignore`
- optional static assets under `assets/` or `imgs/` when they improve presentation

## Canonical section layout

`README.md` should use this top-level structure:
1. `Data Perception`
2. `3D/4D Representation`
3. `3D Reconstruction`
4. `3D Generation`
5. `Embodiment & World Models`
6. `Datasets, Benchmarks & Infrastructure`

Use `About`, `Must Read`, `News`, and `Contents` near the top of the README. Keep subsection anchors stable.

## Section definitions

### Data Perception

Include the sensor-facing and feature-extraction layer:
- monocular, video, and multi-view depth estimation
- normal and geometry prior estimation
- active imaging, structured light, neural decoding, event/active stereo, and physical sensing
- panoramic, fisheye, egocentric, and wide-FOV perception when relevant to 3D reconstruction or mapping
- dense mapping systems that primarily provide features/signals for downstream 3D systems

Do **not** turn this into a generic 2D perception list.

### 3D/4D Representation

Include the underlying representation structures:
- structure-aware 3D Gaussian Splatting and geometry-oriented Gaussian variants
- voxel, mesh, point-cloud, triplane, tensor, and hybrid representations
- NeRF, SDF, neural implicit surfaces, and related neural rendering foundations
- 4DGS, deformation fields, canonical spaces, deformation graphs, and spatiotemporal representations

Usually exclude purely compression-oriented or renderer-engineering-only 3DGS papers unless they materially affect embodied reconstruction, dynamics, editability, or simulation use.

### 3D Reconstruction

Include systems that recover existing objects or scenes:
- feed-forward multi-view and pose-free reconstruction
- object-centric and scene-level reconstruction
- large-scale scene reconstruction and SLAM-like systems
- streaming and online reconstruction, including persistent state models
- dense semantic / instance mapping such as SAM3D, MV-SAM3D, and open-vocabulary 3D mapping
- dynamic, non-rigid, and 4D reconstruction such as PAGE-4D and dynamic VGGT variants

Do **not** include every classical SfM/MVS paper unless it is still a key baseline, dataset anchor, or conceptual reference.

### 3D Generation

Include methods that create new 3D assets or scenes:
- image/text-to-3D object generation with mesh, texture, materials, or simulation-ready outputs
- PBR material and texture generation when relevant to asset quality
- part-level decomposition, part-aware generation, assembly, and editing
- articulated object generation, kinematic structure prediction, URDF export, and interactive assets
- scene-level generation, procedural worlds, layouts, and targeted 3D scene editing

Do **not** broaden into all 3D editing, all diffusion-based 3D papers, or all stylized asset generation. Include selectively when there is a clear embodied-3DV use case.

### Embodiment & World Models

Include work that connects 3D assets and reconstructed scenes to interaction:
- dynamic scene graphs and object/part tracking
- topologically aware dynamic reconstruction and persistent 4D scene state
- reconstruction-based or 3D-consistent world models such as NeoVerse, Gen3C, Tessart/Tessera-style work
- action-conditioned dynamics synthesis
- robotics integration, sim-to-real through generated assets, and VLM/LLM agents grounded in 3D scenes

Do **not** include generic video-generation world models unless their 3D consistency, reconstruction layer, or embodied interaction relevance is explicit.

### Datasets, Benchmarks & Infrastructure

Include the resources researchers need to choose data and evaluate systems:
- surveys and taxonomies
- reconstruction datasets: sparse-view, MVS, dense-view, RGB-D, streaming, dynamic, and semantic sequences
- generation datasets: object-level, text-to-3D, human/articulated objects, procedural/synthetic scenes
- benchmarks and metrics for reconstruction, generation, view synthesis, simulation readiness, and embodied interaction
- simulators and toolchains such as Isaac Sim, Isaac Lab, SAPIEN, MuJoCo, Habitat, Blender, USD, URDF, and related asset pipelines

## Inclusion policy

The repository uses **core + strong adjacent** scope.

### Include first

- papers and projects directly named in the README's Must Read section
- systems around feed-forward 3D reconstruction, streaming 3D, SAM3D/MV-SAM3D, PAGE-4D/dynamic VGGT, 3DGS/4DGS, ArtGS, NeoVerse, Gen3C, Tessart/Tessera, Infinigen, Lingbo-Depth, Lingbo-Map, and structured-light neural decoding
- datasets and benchmarks that help answer practical questions such as "which dataset should I use for dense-view reconstruction, streaming online 3D, object-level generation, articulated generation, or simulation-ready assets?"
- official project pages, official code repositories, official dataset pages, and canonical papers

### Include selectively

- 3D generation papers when they support object-level, part-level, articulated, scene-level, editable, or simulation-ready assets
- 3DGS papers when they affect structure, geometry, dynamics, reconstruction, editing, simulation, or embodied perception
- world-model and video-generation papers when they have explicit 3D consistency, reconstruction-based state, or embodied interaction relevance
- robotics and VLM/LLM-agent papers when 3D scene state is central to grounding, planning, or simulation

### Usually exclude

- generic 3D generation papers with no embodied, reconstructive, physical, part-level, articulated, or simulation angle
- purely aesthetic 3D editing without relevance to geometry, assets, scenes, dynamics, or interaction
- highly specialized 3DGS compression, acceleration, or rendering papers unless they are needed for online/embodied deployment
- general SLAM papers that do not materially help dense 3D reconstruction or embodied scene state
- unverified papers, rumor-like projects, placeholders, or entries without a reliable public source

## Source priority

When adding or updating entries, use sources in this order:
1. official project page, official code repository, or official dataset page
2. arXiv, conference, journal, OpenReview, or proceedings page
3. lab/author pages
4. high-quality awesome lists named in the README acknowledgements
5. Google Scholar / Semantic Scholar citation graph around canonical entries

If multiple sources disagree, prefer the most official public source.

## Verification rule for new entries

Do **not** add an entry unless it has a sufficiently reliable canonical public source.

Minimum bar for inclusion:
- a canonical paper URL such as arXiv / conference page / journal page / OpenReview page,
- and/or an official project page, dataset page, or GitHub repo from the authors / lab / organization.

If a candidate cannot be verified with enough confidence:
- do **not** add it to `README.md`
- do **not** guess missing metadata, URLs, venues, dates, or affiliations
- do **not** include partially confirmed or rumor-like items just because they seem relevant

When in doubt, exclude first and wait for a reliable source.

## Entry format

Each subsection should use the same compact table schema:

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |

### Column rules

- `Date`: use `YYYY-MM-DD` whenever possible; use `YYYY-MM` or `YYYY` only when a canonical precise date is not public.
- `Keywords`: short tags only; keep them scannable.
- `Institute (first)`: first institution / lab / company only, concise and normalized.
- `Paper / Resource`: title linked to the canonical paper or resource URL.
- `Publication`: venue name such as `CVPR 2025`, `ICLR 2026`, `SIGGRAPH 2024`, `arXiv`, `Website`, `GitHub`, or `Dataset`.
- `Others`: compact links such as `project`, `github`, `dataset`, `benchmark`, `docs`, `survey`, `paper`.

## Sorting rules

- Sort every subsection by `Date` descending.
- Newer entries must appear above older ones.
- If only month or year is public, place the row consistently relative to other rows with known dates.

## Overlap policy

Controlled duplication is allowed.

Examples:
- PAGE-4D may appear in both `3D Reconstruction` and `Embodiment & World Models`.
- ArtGS may appear in both `3D Generation` and `Robotics Integration & LLM Agents`.
- Infinigen may appear in both `Scene-Level Generation` and `Datasets, Benchmarks & Infrastructure`.
- a dataset paper may appear in both the method section and the dataset section if both roles are important.

When duplicating an entry:
- keep the metadata consistent across placements
- adjust `Keywords` only if needed to explain the local role
- do not create unnecessary variant titles

## Dataset metadata guidance

For dataset and benchmark entries, preserve as much of the following as possible in keywords or compact `Others` links:
- input: monocular, sparse view, dense view, RGB-D, LiDAR, event, structured light, panoramic, fisheye, multi-view video
- target: depth, normals, point map, mesh, 3DGS, 4DGS, NeRF/SDF, semantic map, instance map, articulated object, URDF, scene graph
- scale: number of objects, scenes, trajectories, videos, frames, annotations, or environments when canonical sources make it explicit
- domain: object-level, scene-level, indoor, outdoor, driving, human, articulated, procedural, synthetic, real scans, robotics
- access: HuggingFace, Google Drive, GitHub, official download, benchmark server, simulator asset library

Use compact summaries in the table itself and keep verbose explanation out of the main row.

## Maintenance workflow

### News policy

Do **not** add `News` entries for routine paper/resource updates.

Only update `News` for major changes or milestone-level progress, such as:
- repository initialization
- adding a large new module, major top-level section, or substantial taxonomy expansion
- major restructuring that changes how readers navigate the list

Adding a few papers, fixing metadata, or refreshing links should not create a `News` item.

When adding entries:
1. decide the primary section first
2. check whether the resource should also appear in a second section
3. normalize the six metadata columns
4. insert in descending date order
5. update the Table of Contents only if headings changed
6. keep the README readable; do not over-tag

When reorganizing:
- prefer adding or refining subsections over inventing many new top-level sections
- keep the user-approved top-level section names unchanged unless explicitly asked

## Commit conventions

Use Conventional Commits.

Recommended types for this repository:
- `docs:` content additions or edits in `README.md` / `AGENTS.md`
- `feat:` meaningful new section or structural capability in the awesome list
- `refactor:` taxonomy reorganization without changing the underlying factual content
- `fix:` broken links, date corrections, venue fixes, naming fixes, anchor fixes
- `chore:` maintenance-only cleanup

Recommended examples:
- `docs(agents): define embodied 3dv curation rules`
- `docs(readme): add streaming reconstruction and articulated generation`
- `refactor(readme): reorganize world models around reconstruction and dynamics`
- `fix(readme): correct page4d venue and project links`

## What to avoid

- Do not add back UMI-specific scope or UMI-only taxonomy.
- Do not revert to a multi-file `contents/` structure.
- Do not add long prose summaries for every paper.
- Do not turn the repo into a general 3D generation, 3DGS, NeRF, SLAM, or robot-learning survey.
- Do not introduce inconsistent table schemas across sections.
- Do not add entries without checking their embodied-3DV relevance.
- Do not add placeholder links such as `https://github.com/` or fake arXiv identifiers.

## Quick checklist before finishing a change

- Is the entry clearly relevant to embodied 3DV core or strong adjacent scope?
- Is it in the right section?
- Should it also appear in another section?
- Does the row use the six required columns?
- Is the date normalized and ordering correct?
- Are `Paper / Resource` and `Others` links canonical and working?
- Does the change preserve the single-README architecture?
