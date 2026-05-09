<div align="center">

<h1 id="awesome-embodied-3dv">Awesome-Embodied-3DV</h1>

<p>
  <strong>A curated map of 3D/4D perception, reconstruction, generation, simulation-ready assets, and world models for embodied AI.</strong>
</p>

<!-- [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) -->
<!-- [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) -->

<p>
  <a href="#-1-3d-perception"><img alt="Perception" src="https://img.shields.io/badge/3D-Perception-a8d8ff?style=for-the-badge"></a>
  <a href="#-2-3d4d-representation"><img alt="Representation" src="https://img.shields.io/badge/3D%2F4D-Representation-b8e6c9?style=for-the-badge"></a>
  <a href="#-3-3d-reconstruction"><img alt="Reconstruction" src="https://img.shields.io/badge/3D-Reconstruction-ffd6a5?style=for-the-badge"></a>
  <a href="#-4-3d-generation"><img alt="Generation" src="https://img.shields.io/badge/3D-Generation-d7c5ff?style=for-the-badge"></a>
  <a href="#-5-embodied-3d"><img alt="Embodiment" src="https://img.shields.io/badge/Embodied-3D-c7f9cc?style=for-the-badge"></a>
  <a href="#-6-datasets-benchmarks--infrastructure"><img alt="Infrastructure" src="https://img.shields.io/badge/Benchmarks-Infrastructure-ffb7b2?style=for-the-badge"></a>
</p>

</div>

## About

**Awesome-Embodied-3DV** is a curated list for the research space where **3D vision, 3D/4D reconstruction, 3D generation, simulation-ready assets, and embodied world models** meet.

This repository focuses on:
- **3D Perception**: depth, normals, active imaging, panoramic/fisheye, dense mapping, and 3D semantic understanding (detection, segmentation, grounding) that feed downstream systems
- **3D/4D Representation**: 3DGS, 4DGS, NeRF/SDF, mesh, voxel, point, and hybrid structures
- **3D Reconstruction**: offline, feed-forward, streaming, online, semantic, instance-level, and dynamic reconstruction
- **3D Generation**: object-level, part-level, articulated, scene-level, and simulation-ready asset generation
- **Embodied 3D**: reconstruction-based world models, dynamic scene graphs, physical interaction & affordance, human-centric 3D, robotics integration, and agent-facing 3D grounding
- **Datasets, Benchmarks & Infrastructure**: datasets, metrics, simulators, toolchains, and surveys for fast research orientation

This list is intentionally **embodied-3DV-first**. It includes 3D generation and 3DGS work only when it helps understand, build, evaluate, or deploy 3D assets and world models for embodied agents. It is not a generic catalog of all 3D generation, editing, rendering, compression, or graphics papers.

## Must Read

Start here if you want the shortest path through the field.

| Goal | Start with |
| :-- | :-- |
| Understand feed-forward 3D reconstruction | [Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501), [DUSt3R](https://arxiv.org/abs/2312.14132), [MASt3R](https://arxiv.org/abs/2406.09756), [VGGT](https://vgg-t.github.io/) |
| Track online / streaming 3D reconstruction | [Dynamic 3D Gaussians](https://dynamic3dgaussians.github.io/), [CUT3R](https://arxiv.org/abs/2501.12387), [Spann3R](https://arxiv.org/abs/2408.16061), [SLAM3R](https://arxiv.org/abs/2412.09401) |
| Study dynamic 4D feed-forward geometry | [PAGE-4D](https://page4d.github.io/), [4D-VGGT](https://arxiv.org/abs/2511.18416), [DynamicVGGT](https://arxiv.org/abs/2603.08254) |
| Learn representation foundations | [3D Gaussian Splatting](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/), [NeRF](https://www.matthewtancik.com/nerf), [Instant-NGP](https://nvlabs.github.io/instant-ngp/), [TensoRF](https://apchenstu.github.io/TensoRF/) |
| Generate object and simulation-ready assets | [TRELLIS](https://trellis3d.github.io/), [Hunyuan3D 2.0](https://github.com/Tencent-Hunyuan/Hunyuan3D-2), [TripoSR](https://arxiv.org/abs/2403.02151), [PartCrafter](https://wgsxm.github.io/projects/partcrafter/) |
| Generate scenes and worlds | [Infinigen](https://infinigen.org/), [SceneDreamer](https://scene-dreamer.github.io/), [Text2Room](https://lukashoel.github.io/text-to-room/), [WonderWorld](https://kovenyu.com/wonderworld/) |
| Build articulated objects | [ArtGS](https://arxiv.org/abs/2502.19459), [Articulate Anything](https://openreview.net/forum?id=6akuzEqP38), [URDF-Anything](https://openreview.net/forum?id=g3EF5XsapH), [PartNet-Mobility](https://sapien.ucsd.edu/browse) |
| Pick datasets and benchmarks | [ScanNet](http://www.scan-net.org/), [Tanks and Temples](https://www.tanksandtemples.org/), [DTU](https://roboimagedata.compute.dtu.dk/), [Objaverse](https://objaverse.allenai.org/), [GSO](https://app.gazebosim.org/GoogleResearch/fuel/collections/Scanned%20Objects%20by%20Google%20Research), [HM3D](https://aihabitat.org/datasets/hm3d/) |

## News

- [2026-04-30] Initialized **Awesome-Embodied-3DV** with a six-part taxonomy for data perception, representations, reconstruction, generation, embodied world models, and infrastructure.
- [2026-04-30] Added `AGENTS.md` to define curation scope, metadata rules, and maintenance workflow.

## Contents

- [Awesome-Embodied-3DV](#awesome-embodied-3dv)
  - [About](#about)
  - [Must Read](#must-read)
  - [News](#news)
  - [3D Perception](#-1-3d-perception)
    - [Geometric Priors](#11-geometric-priors)
    - [3D Semantic Understanding](#12-3d-semantic-understanding)
    - [Active Imaging & Sensors](#13-active-imaging--sensors)
    - [Dense Mapping Systems](#14-dense-mapping-systems)
  - [3D/4D Representation](#-2-3d4d-representation)
    - [Explicit & Hybrid Representations](#21-explicit--hybrid-representations)
    - [Neural Implicit Representations](#22-neural-implicit-representations)
    - [Dynamic & Spatiotemporal 4D](#23-dynamic--spatiotemporal-4d)
  - [3D Reconstruction](#-3-3d-reconstruction)
    - [Static Reconstruction](#31-static-reconstruction)
    - [Streaming & Online Reconstruction](#32-streaming--online-reconstruction)
    - [Dynamic 3D Reconstruction](#33-dynamic-3d-reconstruction)
  - [3D Generation](#-4-3d-generation)
    - [Object-Level Generation](#41-object-level-generation)
    - [Part-Level & Articulated Generation](#42-part-level--articulated-generation)
    - [Scene-Level Generation](#43-scene-level-generation)
  - [Embodied 3D](#-5-embodied-3d)
    - [Dynamic Scene Graphs & Tracking](#51-dynamic-scene-graphs--tracking)
    - [Reconstruction-Based World Models](#52-reconstruction-based-world-models)
    - [Physical Interaction & Affordance](#53-physical-interaction--affordance)
    - [Human-Centric 3D for Embodiment](#54-human-centric-3d-for-embodiment)
    - [Robotics Integration & VLM Agents](#55-robotics-integration--vlm-agents)
  - [Datasets, Benchmarks & Infrastructure](#-6-datasets-benchmarks--infrastructure)
    - [Surveys & Taxonomies](#61-surveys--taxonomies)
    - [Datasets for 3D Reconstruction](#62-datasets-for-3d-reconstruction)
    - [Datasets for 3D Generation](#63-datasets-for-3d-generation)
    - [Specific Benchmarks & Metrics](#64-specific-benchmarks--metrics)
    - [Simulators & Toolchains](#65-simulators--toolchains)
  - [Acknowledgement](#acknowledgement)
  - [Citation](#citation)

<h2 id="-1-3d-perception">📡 1. 3D Perception</h2>

3D perception covers the sensor-facing and semantic layers: extracting geometric priors (depth, normals), understanding 3D semantics (detection, segmentation, grounding), active-imaging signals, and dense maps from 2D images, video, or physical sensors.

<a id="11-geometric-priors"></a>

### 1.1 Geometric Priors

#### 1.1.1 Monocular High-Fidelity Depth

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-05-07 | Feed-Forward 3D, Token Reduction, MVS | Peking University | [Spark3R: Asymmetric Token Reduction Makes Fast Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2605.06270) | arXiv | [paper](https://arxiv.org/abs/2605.06270) |
| 2026-05-05 | Feed-Forward, Generative Priors, Mixture-of-Transformers | Tsinghua | [Mix3R: Mixing Feed-forward Reconstruction and Generative 3D Priors](https://arxiv.org/abs/2605.03359) | arXiv | [paper](https://arxiv.org/abs/2605.03359) |
| 2026-05-06 | Physics-Grounded, Kinematic, Simulation-Ready Assets | HKU | [PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World](https://arxiv.org/abs/2605.05163) | ICML 2026 | [paper](https://arxiv.org/abs/2605.05163) |
| 2026-05-03 | 4D World Model, Novel View Synthesis, Embodied AI | Shanghai AI Lab | [Embody4D: A Generalist 4D World Model for Embodied AI](https://arxiv.org/abs/2605.01799) | arXiv | [paper](https://arxiv.org/abs/2605.01799) |
| 2026-05-03 | Gaussian-Language Map, Zero-Shot Navigation, Multi-Scale | CASIA | [GLMap: Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation](https://arxiv.org/abs/2605.01736) | CVPR 2026 | [paper](https://arxiv.org/abs/2605.01736) |
| 2025-11-06 | Any-View Depth, Metric Geometry, Multi-View | ByteDance | [Depth Anything 3: Recovering the Visual Space from Any Views](https://arxiv.org/abs/2511.10647) | arXiv | [project](https://depth-anything-3.github.io/) |
| 2025-06-20 | Diffusion Distillation, Metric + Sharp, Single-Step | VinAI | [SharpDepth: Bridging Discriminative and Generative Monocular Depth Estimation](https://arxiv.org/abs/2503.21670) | CVPR 2025 | [project](https://sharpdepth.github.io/) |
| 2025-01-28 | Diffusion, Single-Step, Dense Prediction | Shanghai AI Lab | [Lotus: Diffusion-based Visual Foundation Model for Dense Geometry Estimation](https://arxiv.org/abs/2501.06467) | ICLR 2025 | [project](https://lotus3d.github.io/) / [github](https://github.com/EnVision-Research/Lotus) |
| 2024-06-14 | Monocular Depth, Foundation Model, Metric Depth | TikTok / HKU | [Depth Anything V2](https://arxiv.org/abs/2406.09414) | NeurIPS 2024 | [project](https://depth-anything-v2.github.io/) / [github](https://github.com/DepthAnything/Depth-Anything-V2) |
| 2024-06-05 | Metric Depth, Zero-Shot, Image Priors | Apple | [Depth Pro: Sharp Monocular Metric Depth in Less Than a Second](https://arxiv.org/abs/2410.02073) | arXiv | [github](https://github.com/apple/ml-depth-pro) |
| 2024-06-05 | Metric Depth, Universal, Zero-Shot | ETH Zurich | [UniDepth: Universal Monocular Metric Depth Estimation](https://arxiv.org/abs/2403.18913) | CVPR 2024 | [github](https://github.com/lpiccinelli-eth/unidepth) |
| 2023-12-22 | Monocular Depth, Relative Depth, Foundation Model | TikTok / HKU | [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891) | CVPR 2024 | [project](https://depth-anything.github.io/) |
| 2023-04-24 | Monocular Depth, Zero-Shot, Affine-Invariant | Intel Labs | [Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](https://arxiv.org/abs/2312.02145) | CVPR 2024 | [project](https://marigoldmonodepth.github.io/) |

#### 1.1.2 Geometric Consistency Prior

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-07-22 | Foundation Model, Depth/Normal/Pointmap, Multi-View | SJTU | [Dens3R: A Foundation Model for 3D Geometry Prediction](https://arxiv.org/abs/2507.16290) | ICLR 2026 | [paper](https://arxiv.org/abs/2507.16290) |
| 2025-07-19 | Feed-Forward 3D, Survey, Geometry Priors | NUS | [Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501) | arXiv | [project](https://fnzhan.com/3D-Reconstruction-and-Generation-Survey/) |
| 2025-05-20 | Scalable Depth, Autoregressive, 2B Parameters | Baidu | [DAR: Scalable Autoregressive Monocular Depth Estimation](https://arxiv.org/abs/2503.17310) | CVPR 2025 | [project](https://depth-ar.github.io/) |
| 2025-04-15 | Panoramic / Fisheye Depth, Zero-Shot Metric | Intel | [Depth Any Camera: Zero-Shot Metric Depth from Any Camera](https://arxiv.org/abs/2412.08204) | CVPR 2025 | [project](https://depth-any-camera.github.io/) |
| 2025-03-18 | Metric 3D, Multi-Task, Geometry Foundation | Shanghai AI Lab | [Metric3D v2: A Versatile Monocular Geometric Foundation Model](https://arxiv.org/abs/2404.15506) | TPAMI 2025 | [project](https://jugghm.github.io/Metric3Dv2/) |
| 2024-10-02 | Normal Estimation, 3D Priors, Surface Geometry | Nvidia | [StableNormal: Reducing Diffusion Variance for Stable and Sharp Normal](https://arxiv.org/abs/2406.16864) | SIGGRAPH Asia 2024 | [project](https://stable-x.github.io/StableNormal/) |
| 2024-03-19 | High-Res, Patch-Wise, Model-Agnostic | KAUST | [PatchFusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth](https://arxiv.org/abs/2312.02240) | CVPR 2024 | [project](https://patchfusion.github.io/) |
| 2023-12-08 | Geometry, Normals, Depth, Multi-Task | Apple | [GeoWizard: Unleashing the Diffusion Priors for 3D Geometry Estimation from a Single Image](https://arxiv.org/abs/2403.12013) | ECCV 2024 | [project](https://fuxiao0719.github.io/projects/geowizard/) |

<a id="12-3d-semantic-understanding"></a>

### 1.2 3D Semantic Understanding

#### 1.2.1 Open-Vocabulary 3D Segmentation & Grounding

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-05-07 | Open-Vocabulary, Gaussian Feature Field, Codebook | TU Munich / Google | [OpenGaFF: Open-Vocabulary Gaussian Feature Field with Codebook Attention](https://arxiv.org/abs/2605.06088) | arXiv | [paper](https://arxiv.org/abs/2605.06088) |
| 2025-07-10 | Open-Vocabulary, Dual-Level Contrastive, Instance-Aware | BIGAI / Tsinghua | [MPEC: Masked Point-Entity Contrast for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2504.02238) | CVPR 2025 | [project](https://mpec-3d.github.io/) |
| 2025-06-15 | Panoptic, Open-Vocabulary, 3D Gaussian Splatting | NUS | [PanoGS: Gaussian-based Panoptic Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2501.02007) | CVPR 2025 | [project](https://panogs.github.io/) |
| 2024-12-18 | Open-Vocabulary 3DGS, Segmentation, Language | ETH Zurich | [LangSplat: 3D Language Gaussian Splatting](https://arxiv.org/abs/2312.16084) | CVPR 2024 | [project](https://langsplat.github.io/) / [github](https://github.com/minghanqin/LangSplat) |
| 2024-07-12 | Region-Level, Point-Language Contrastive, Multi-VLM | HKU | [RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding](https://arxiv.org/abs/2404.00962) | CVPR 2024 | [project](https://regionplc.github.io/) / [github](https://github.com/CVMI-Lab/RegionPLC) |
| 2024-05-15 | Open-Vocabulary, 3D Scene, Language Field | UC Berkeley | [LERF: Language Embedded Radiance Fields](https://arxiv.org/abs/2303.09553) | ICCV 2023 | [project](https://lerf.io/) / [github](https://github.com/kerrj/lerf) |
| 2024-03-28 | Segment Anything 3D, Point Cloud, Interactive | VAST AI | [SAM3D: Segment Anything in 3D Scenes](https://arxiv.org/abs/2306.03908) | CVPR 2024 | [github](https://github.com/Pointcept/SegmentAnything3D) |
| 2024-01-19 | Segment Anything, 3D Gaussians, Interactive | Zhejiang University | [SAGD: Boundary-Enhanced Segment Anything in 3D Gaussians](https://arxiv.org/abs/2401.17857) | arXiv | [github](https://github.com/XuHu0529/SAGS) |
| 2023-12-05 | Open-Vocabulary 3D, Point Cloud, Segmentation | ETH Zurich | [OpenScene: 3D Scene Understanding with Open Vocabularies](https://arxiv.org/abs/2211.15654) | CVPR 2023 | [project](https://pengsongyou.github.io/openscene) / [github](https://github.com/pengsongyou/openscene) |

#### 1.2.2 3D Instance & Panoptic Segmentation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2023-12-27 | 3D Instance Segmentation, Transformer, Point Cloud | ETH Zurich | [Mask3D: Mask Transformer for 3D Semantic Instance Segmentation](https://arxiv.org/abs/2210.03105) | ICRA 2023 | [github](https://github.com/JonasSchult/Mask3D) |
| 2023-08-22 | Point Cloud, Foundation Model, 3D Understanding | Shanghai AI Lab | [Point Transformer V3: Simpler, Faster, Stronger](https://arxiv.org/abs/2312.10035) | CVPR 2024 | [github](https://github.com/Pointcept/PointTransformerV3) |
| 2023-02-28 | 3D Panoptic, LiDAR, Multi-Scene | Tsinghua | [UniSeg3D: Unified 3D Panoptic Segmentation](https://arxiv.org/abs/2407.03263) | CVPR 2023 | [github](https://github.com/PJLab-ADG/UniSeg3D) |

#### 1.2.3 3D Visual Grounding & Spatial Reasoning

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-11-15 | Zero-Shot 3D Grounding, 2D VLM Transfer | NUS | [SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding](https://arxiv.org/abs/2406.03857) | CVPR 2025 | [project](https://seeground.github.io/) |
| 2024-10-07 | 3D-LLM, 3D Grounding, Scene Understanding | Shanghai AI Lab | [LLaVA-3D: A Simple yet Effective Pathway to Empowering LMMs with 3D Awareness](https://arxiv.org/abs/2410.06250) | arXiv | [github](https://github.com/ZCMax/LLaVA-3D) |
| 2023-12-29 | 3D VQA, 3D Captioning, Scene Understanding | Shanghai AI Lab | [3D-LLM: Injecting the 3D World into Large Language Models](https://arxiv.org/abs/2307.12981) | NeurIPS 2023 | [project](https://vis-www.cs.umass.edu/3dllm/) / [github](https://github.com/UMass-Foundation-Model/3D-LLM) |
| 2023-08-16 | 3D Visual Grounding, Referring Expression, Point Cloud | Peking University | [3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment](https://arxiv.org/abs/2308.04352) | ICCV 2023 | [github](https://github.com/3d-vista/3D-VisTA) |

<a id="13-active-imaging--sensors"></a>

### 1.3 Active Imaging & Sensors

#### 1.3.1 Structured Light & Neural Decoding

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-08-05 | Structured Light, Single-Shot, Neural Decoding | ShanghaiTech | [Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding](https://arxiv.org/abs/2512.14028) | arXiv | [paper](https://arxiv.org/abs/2512.14028) |
| 2024-04-29 | Event Camera, Active Stereo, Depth | Tsinghua | [Event-Based Structured Light for Depth Reconstruction](https://arxiv.org/abs/1811.10771) | IJCAS 2024 | [paper](https://arxiv.org/abs/1811.10771) |
| 2023-06-15 | Structured Light, Phase Unwrapping, Learning | Nanjing University | [Deep Learning-Based Structured Light 3D Imaging: A Survey](https://arxiv.org/abs/2306.10409) | arXiv | [survey](https://arxiv.org/abs/2306.10409) |

#### 1.3.2 Panoramic & Fisheye Perception

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-06-23 | Panoramic Depth, 360 Vision, Foundation Model | Lingbo AI | [Lingbo-Depth](https://arxiv.org/abs/2601.17895) | arXiv | [github](https://github.com/robbyant/lingbot-depth) |
| 2026-03-19 | Panoramic Reconstruction, Permutation-Equivariant, 360° | Cornell | [PanoVGGT: Feed-Forward 3D Reconstruction from Panoramic Imagery](https://arxiv.org/abs/2603.17571) | CVPR 2026 | [paper](https://arxiv.org/abs/2603.17571) |
| 2025-06-23 | Panoramic Mapping, Large-Scale, 3D Map | Lingbo AI | [Lingbo-Map](https://arxiv.org/abs/2604.14141) | arXiv | [github](https://github.com/robbyant/lingbot-map) |
| 2021-09-06 | 360 Depth, Indoor, Panoramic Images | CERTH | [Pano3D: A Holistic Benchmark and a Solid Baseline for 360 Depth Estimation](https://arxiv.org/abs/2109.02749) | CVPRW 2021 | [project](https://vcl3d.github.io/Pano3D/) / [github](https://github.com/VCL3D/Pano3D) |

#### 1.3.3 Neural Structured Light & Event-Based Imaging

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-01-24 | Event Camera, Depth Estimation, Any-to-Any | Shanghai AI Lab | [Depth AnyEvent: Event Camera Based Monocular Depth Estimation via Dense Correspondence Distillation](https://arxiv.org/abs/2509.15224) | CVPR 2025 |
| 2023-08-15 | LiDAR, ZIP Encoding, 3D Reconstruction | Stanford | [LiZIP: Learned LiDAR Compression for Efficient and Effective 3D Reconstruction](https://arxiv.org/abs/2603.23162) | ICCV 2023 | [paper](https://arxiv.org/abs/2603.23162) |

<a id="14-dense-mapping-systems"></a>

### 1.4 Dense Mapping Systems

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-06-18 | Gaussian SLAM, Dynamic Environments, Monocular | Stanford / ETH | [WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2501.15038) | CVPR 2025 | [project](https://wildgs-slam.github.io/) |
| 2025-05-10 | Gaussian SLAM, Global BA, Monocular RGB | ETH / Meta | [Splat-SLAM: Globally Optimized RGB-only SLAM with 3D Gaussians](https://arxiv.org/abs/2411.01687) | CVPR 2025 | [project](https://splat-slam.github.io/) |
| 2025-05-07 | Language-Embedded, Open-Vocabulary, 3DGS SLAM | KAIST | [LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM](https://arxiv.org/abs/2511.16144) | arXiv | [paper](https://arxiv.org/abs/2511.16144) |
| 2025-01-24 | Multi-Robot, Semantic, Heterogeneous, 3DGS | Stanford | [HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](https://arxiv.org/abs/2501.14147) | RAL 2025 | [project](http://hammer-project.github.io/) |
| 2025-03-11 | Gaussian SLAM, Dense Reconstruction, RGB-D | Zhejiang University | [GigaSLAM: Gaussian Splatting-based Large-Scale Dense SLAM](https://arxiv.org/abs/2503.08071) | arXiv | [github](https://github.com/DengKaiCQ/GigaSLAM) |
| 2025-01-19 | Real-Time Mapping, Open-Vocabulary, 3D Semantics | MIT | [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650) | ICRA 2024 | [project](https://concept-graphs.github.io/) / [github](https://github.com/concept-graphs/concept-graphs) |
| 2025-01-16 | Neural SLAM, Dense Mapping, Self-Supervised | Shanghai AI Lab | [DINO-SLAM: Dense Tracking and Mapping with Self-Supervised Feature Learning](https://arxiv.org/abs/2507.19474) | arXiv | [paper](https://arxiv.org/abs/2507.19474) |
| 2024-06-17 | Dense SLAM, Gaussian Splatting, RGB-D | TUM | [Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741) | CVPR 2024 | [github](https://github.com/muskie82/MonoGS) |
| 2024-06-15 | Gaussian SLAM, RGB-D, Volumetric | CMU / MIT | [SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM](https://arxiv.org/abs/2312.02126) | CVPR 2024 | [project](https://spla-tam.github.io/) / [github](https://github.com/spla-tam/SplaTAM) |
| 2024-04-15 | Neural SLAM, Survey, Radiance Fields | TUM | [How NeRFs and 3D Gaussian Splatting are Reshaping SLAM: a Survey](https://arxiv.org/abs/2402.13255) | arXiv | [project](https://github.com/fabiotosi92/Awesome-SLAM) |
| 2023-05-30 | Neural Mapping, Dense RGB-D SLAM, SDF | HKUST | [NICE-SLAM: Neural Implicit Scalable Encoding for SLAM](https://arxiv.org/abs/2112.12130) | CVPR 2022 | [project](https://pengsongyou.github.io/nice-slam) |

<h2 id="-2-3d4d-representation">🧱 2. 3D/4D Representation</h2>

This section focuses on the mathematical and data-structure layer used to represent geometry, appearance, and motion.

<a id="21-explicit--hybrid-representations"></a>

### 2.1 Explicit & Hybrid Representations

#### 2.1.1 Structure-Aware 3D Gaussian Splatting

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-04-16 | Feed-Forward 3DGS, Global Scene Tokens, Compact | Tel Aviv University | [GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284) | arXiv | [paper](https://arxiv.org/abs/2604.15284) |
| 2026-03-07 | Few-Shot, Diffusion Prior, Repair + Inpainting | ZJU / Alibaba | [RI3D: Few-Shot Gaussian Splatting With Repair and Inpainting Diffusion Priors](https://arxiv.org/abs/2503.10860) | ICCV 2025 | [paper](https://arxiv.org/abs/2503.10860) |
| 2026-02-02 | Feed-Forward 2DGS, Surface Continuity, Sparse Views | Shanghai Jiao Tong | [SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors](https://arxiv.org/abs/2602.02000) | ICLR 2026 | [paper](https://arxiv.org/abs/2602.02000) |
| 2026-04-16 | TokenGS, Learnable Gaussian Tokens, Pose-Robust | NVIDIA | [TokenGS: Decoupling 3D Gaussian Prediction from Pixels](https://arxiv.org/abs/2604.15239) | arXiv | [paper](https://arxiv.org/abs/2604.15239) |
| 2026-04-12 | UniSplat, Unposed Multi-View, Feed-Forward | UC Berkeley | [UniSplat: Learning 3D Representations from Unposed Multi-View Images](https://arxiv.org/abs/2604.10573) | CVPR 2026 | [paper](https://arxiv.org/abs/2604.10573) |
| 2026-03-12 | Sparse-View 4D, Monocular Fusion, Cross-Video | Meta AI | [MonoFusion: Sparse-View 4D Reconstruction via Monocular Fusion](https://arxiv.org/abs/2507.23782) | ICCV 2025 | [paper](https://arxiv.org/abs/2507.23782) |
| 2025-07-10 | 3DGS, Structure, Sparse Views | USTC | [SparseGS: Real-Time 360 Sparse View Synthesis using Gaussian Splatting](https://arxiv.org/abs/2312.00206) | 3DV 2025 | [project](https://formycat.github.io/SparseGS-Real-Time-360-Sparse-View-Synthesis-using-Gaussian-Splatting/) |
| 2024-07-15 | Feed-Forward 3DGS, Sparse Views, Generalizable | Monash / Tübingen | [MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2403.14624) | ECCV 2024 Oral | [project](https://mvsplat.github.io/) / [github](https://github.com/donydchen/mvsplat) |
| 2024-07-02 | 2DGS, Surface Reconstruction, Geometry | TUM | [2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://arxiv.org/abs/2403.17888) | SIGGRAPH 2024 | [project](https://surfsplatting.github.io/) |
| 2024-03-27 | Feed-Forward 3DGS, Image Pairs, Epipolar | MIT | [pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction](https://arxiv.org/abs/2312.12337) | CVPR 2024 Oral | [github](https://github.com/dcharatan/pixelsplat) |
| 2023-11-21 | 3DGS, Mesh Extraction, Surface | ETH Zurich | [SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction](https://arxiv.org/abs/2311.12775) | arXiv | [project](https://anttwo.github.io/sugar/) |
| 2023-07-03 | 3DGS, Real-Time Rendering, Explicit Radiance | Inria | [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | SIGGRAPH 2023 | [github](https://github.com/graphdeco-inria/gaussian-splatting) |

#### 2.1.2 Voxel, Mesh & Point-Cloud Innovations

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-12-02 | Structured Latent, 3D Generation, Mesh | Microsoft | [TRELLIS: Structured 3D Latents for Scalable and Versatile 3D Generation](https://arxiv.org/abs/2412.01506) | CVPR 2025 | [project](https://trellis3d.github.io/) / [github](https://github.com/microsoft/TRELLIS) |
| 2024-03-04 | Sparse Voxel, Text/Image-to-3D, Mesh | Stability AI | [TripoSR: Fast 3D Object Reconstruction from a Single Image](https://arxiv.org/abs/2403.02151) | arXiv | [github](https://github.com/VAST-AI-Research/TripoSR) |
| 2022-12-19 | Point Cloud, Diffusion, Shape Generation | OpenAI | [Point-E: A System for Generating 3D Point Clouds from Complex Prompts](https://arxiv.org/abs/2212.08751) | arXiv | [github](https://github.com/openai/point-e) |

<a id="22-neural-implicit-representations"></a>

### 2.2 Neural Implicit Representations

#### 2.2.1 Advanced NeRF & SDF Architectures

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2023-01-31 | Unbounded Scenes, Anti-Aliasing, NeRF | Google Research | [Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](https://arxiv.org/abs/2111.12077) | CVPR 2022 | [project](https://jonbarron.info/mipnerf360/) |
| 2022-01-14 | Hash Grid, Real-Time NeRF, Neural Graphics | NVIDIA | [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](https://nvlabs.github.io/instant-ngp/) | SIGGRAPH 2022 | [github](https://github.com/NVlabs/instant-ngp) |
| 2021-12-11 | Tensor Factorization, Radiance Fields, Compression | Tsinghua | [TensoRF: Tensorial Radiance Fields](https://arxiv.org/abs/2203.09517) | ECCV 2022 | [project](https://apchenstu.github.io/TensoRF/) |
| 2021-06-01 | SDF, Surface Reconstruction, Neural Rendering | MPI-IS | [NeuS: Learning Neural Implicit Surfaces by Volume Rendering](https://arxiv.org/abs/2106.10689) | NeurIPS 2021 | [project](https://lingjie0206.github.io/papers/NeuS/) |
| 2020-03-19 | NeRF, View Synthesis, Neural Rendering | UC Berkeley | [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://www.matthewtancik.com/nerf) | ECCV 2020 | [github](https://github.com/bmild/nerf) |

<a id="23-dynamic--spatiotemporal-4d"></a>

### 2.3 Dynamic & Spatiotemporal 4D

#### 2.3.1 4D Gaussian Splatting (4DGS)

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2023-11-30 | 4DGS, Dynamic Scenes, Real-Time Rendering | Zhejiang University | [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2310.08528) | CVPR 2024 | [project](https://guanjunwu.github.io/4dgs/) |
| 2023-10-16 | Dynamic 3DGS, Scene Motion, Multi-View Video | Cornell | [Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis](https://dynamic3dgaussians.github.io/) | 3DV 2025 | [github](https://github.com/JonathonLuiten/Dynamic3DGaussians) |
| 2023-08-21 | Dynamic NeRF, Deformation, Canonical Space | Google Research | [HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields](https://arxiv.org/abs/2106.13228) | SIGGRAPH Asia 2021 | [project](https://hypernerf.github.io/) |

#### 2.3.2 Deformation Graphs & Canonical Spaces

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-04-18 | Deformation, Dynamic Radiance Fields, Canonical | ETH Zurich | [SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](https://arxiv.org/abs/2312.14937) | arXiv | [project](https://yihua7.github.io/SC-GS-web/) |
| 2023-05-17 | Non-Rigid Tracking, Neural Deformation, 4D | Tsinghua | [Neuralangelo: High-Fidelity Neural Surface Reconstruction](https://arxiv.org/abs/2306.03092) | CVPR 2023 | [project](https://research.nvidia.com/labs/dir/neuralangelo/) |

<h2 id="-3-3d-reconstruction">🏗️ 3. 3D Reconstruction</h2>

Reconstruction systems recover objects or scenes from images, video, RGB-D, or multi-sensor streams under offline, online, and dynamic conditions.

<a id="31-static-reconstruction"></a>

### 3.1 Static Reconstruction

#### 3.1.1 Object-Centric Reconstruction

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-11-19 | Single Image, Object Mesh, SAM 3D | Meta AI | [SAM 3D Objects](https://github.com/facebookresearch/sam-3d-objects) | GitHub | [github](https://github.com/facebookresearch/sam-3d-objects) |
| 2024-06-05 | Multi-View, Stereo, Feed-Forward | NAVER Labs | [MASt3R: Grounding Image Matching in 3D with MASt3R](https://arxiv.org/abs/2406.09756) | ECCV 2024 | [project](https://europe.naverlabs.com/research/publications/mast3r-grounding-image-matching-in-3d-with-mast3r/) / [github](https://github.com/naver/mast3r) |
| 2023-12-19 | Multi-View, Pointmap, Pose-Free | NAVER Labs | [DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132) | CVPR 2024 | [project](https://dust3r.europe.naverlabs.com/) / [github](https://github.com/naver/dust3r) |
| 2023-12-04 | Object Pose, Reconstruction, Model-Based | NVIDIA | [FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects](https://arxiv.org/abs/2312.08344) | CVPR 2024 | [project](https://nvlabs.github.io/FoundationPose/) |

#### 3.1.2 Large-Scale Scene Reconstruction

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-04-30 | Generalizable, Sparse-View, Unposed Images, Outdoor | UIUC / NVIDIA | [GenWildSplat: Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193) | arXiv | [paper](https://arxiv.org/abs/2604.28193) |
| 2025-10-15 | Multi-View Reconstruction, Matching, MVS | NAVER Labs | [MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion](https://arxiv.org/abs/2409.19152) | 3DV 2025 | [github](https://github.com/naver/mast3r) |
| 2025-06-12 | Permutation-Equivariant, Near-Zero Variance, Feed-Forward | Oxford / Meta | [π³ (Pi3): A Permutation-Equivariant 3D Foundation Model](https://arxiv.org/abs/2506.07347) | CVPR 2025 | [project](https://pi3-3d.github.io/) |
| 2025-06-10 | Feed-Forward, Multi-View, Auxiliary Priors | ETH / Microsoft | [Pow3R: Empowering Unconstrained 3D Reconstruction with Camera and Scene Priors](https://arxiv.org/abs/2503.17388) | CVPR 2025 | [project](https://pow3r.github.io/) |
| 2025-05-31 | Multi-View, Symmetric, 1000+ Images, O(N) | NAVER Labs | [MUSt3R: Multi-view Network for Stereo 3D Reconstruction](https://arxiv.org/abs/2504.01661) | CVPR 2025 | [project](https://must3r.github.io/) |
| 2025-05-30 | Feed-Forward, 1500+ Images, 251 FPS | Meta AI | [Fast3R: Towards 3D Reconstruction of 1000+ Images in One Forward Pass](https://arxiv.org/abs/2501.13928) | CVPR 2025 | [project](https://fast3r.github.io/) |
| 2025-03-18 | Feed-Forward 3D, Pose-Free, Point Map | Meta AI | [VGGT: Visual Geometry Grounded Transformer](https://vgg-t.github.io/) | CVPR 2025 | [github](https://github.com/facebookresearch/vggt) |
| 2025-01-20 | Sparse View, Single-Stage, 2 Seconds | Meta AI | [MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2501.08210) | CVPR 2025 Oral | [project](https://mv-dust3rp.github.io/) |
| 2024-12-11 | Feed-Forward, SLAM, DUSt3R, Online | Shanghai AI Lab | [SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos](https://arxiv.org/abs/2412.09401) | arXiv | [project](https://slam3r.github.io/) |
| 2024-08-28 | Spatial Memory, Feed-Forward, Multi-View | HKU | [Spann3R: 3D Reconstruction with Spatial Memory](https://arxiv.org/abs/2408.16061) | arXiv | [project](https://hengyiwang.github.io/projects/spann3r) |

<a id="32-streaming--online-reconstruction"></a>

### 3.2 Streaming & Online Reconstruction

#### 3.2.1 Dense Semantic/Instance Mapping

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-03-12 | Multi-View, SAM3D, Layout-Aware Generation | Peking University | [MV-SAM3D: Adaptive Multi-View Fusion for Layout-Aware 3D Generation](https://arxiv.org/abs/2603.11633) | arXiv | [github](https://github.com/devinli123/MV-SAM3D) |
| 2025-11-19 | Image-to-3D, Object Reconstruction, Segmentation | Meta AI | [SAM 3D Objects](https://github.com/facebookresearch/sam-3d-objects) | GitHub | [github](https://github.com/facebookresearch/sam-3d-objects) |
| 2023-09-28 | Open-Vocabulary, 3D Scene Graph, Mapping | MIT | [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650) | ICRA 2024 | [project](https://concept-graphs.github.io/) |

#### 3.2.2 Continuous Neural Tracking & Mapping

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-01-20 | Online 3D, Recurrent Pointmap, Streaming | Meta AI | [CUT3R: Continuous 3D Perception Model with Persistent State](https://arxiv.org/abs/2501.12387) | CVPR 2025 | [project](https://cut3r.github.io/) / [github](https://github.com/CUT3R/CUT3R) |
| 2024-12-11 | Online Reconstruction, Monocular Video, Dense Map | Shanghai AI Lab | [SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos](https://arxiv.org/abs/2412.09401) | arXiv | [project](https://slam3r.github.io/) |
| 2024-06-17 | Online 3DGS, RGB-D SLAM, Real-Time | TUM | [Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741) | CVPR 2024 | [github](https://github.com/muskie82/MonoGS) |

<a id="33-dynamic-3d-reconstruction"></a>

### 3.3 Dynamic 3D Reconstruction

#### 3.3.1 Non-Rigid Tracking & Reconstruction

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-04-10 | Feed-Forward, Unconstrained Views, Semantic-Geometry | Nanyang Tech | [FF3R: Feedforward Feature 3D Reconstruction from Unconstrained Views](https://arxiv.org/abs/2604.09862) | CVPR 2026 Findings | [paper](https://arxiv.org/abs/2604.09862) |
| 2026-04-10 | Dynamic/Static Disentanglement, Uncertainty-Aware, Feed-Forward | Zhejiang University | [Robust 4D VGT: Robust 4D Visual Geometry Transformer with Uncertainty-Aware Priors](https://arxiv.org/abs/2604.09366) | arXiv | [paper](https://arxiv.org/abs/2604.09366) |
| 2026-04-21 | Functional Scenes, Egocentric Interaction, URDF/USD | Stanford | [FunRec: Reconstructing Functional 3D Scenes from Egocentric Interaction Videos](https://arxiv.org/abs/2604.05621) | CVPR 2026 | [paper](https://arxiv.org/abs/2604.05621) |
| 2026-03-09 | Dynamic VGGT, Autonomous Driving, 4D | Fudan University | [DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving](https://arxiv.org/abs/2603.08254) | arXiv | [paper](https://arxiv.org/abs/2603.08254) |
| 2025-11-23 | Dynamic Geometry, Spatiotemporal, VGGT | Huazhong University of Science and Technology | [4D-VGGT: A General Foundation Model with SpatioTemporal Awareness for Dynamic Scene Geometry Estimation](https://arxiv.org/abs/2511.18416) | arXiv | [paper](https://arxiv.org/abs/2511.18416) |
| 2025-10-20 | VGGT-4D, Pose/Geometry, Dynamic Mask | Harvard | [PAGE-4D: Disentangled Pose and Geometry Estimation for 4D Perception](https://arxiv.org/abs/2510.17568) | ICLR 2026 | [project](https://page4d.github.io/) |
| 2025-08-18 | 3D Reconstruction, Human Motion, Video | Shanghai AI Lab | [Human3R: Reconstructing 3D Human Avatars from Monocular Video](https://arxiv.org/abs/2508.09983) | CVPR 2025 | [project](https://human3r.github.io/) |
| 2025-06-10 | Multi-Object, 4D, In-the-Wild Videos | CMU | [GenMOJO: Robust Multi-Object 4D Generation for In-the-wild Videos](https://arxiv.org/abs/2503.18594) | CVPR 2025 | [project](https://genmojo.github.io/) |
| 2025-06-09 | Dynamic Human, Temporal Consistency, 4D | Tsinghua | [CARI4D: Cross-Modal Alignment and Reconstruction for Interactive 4D Human](https://arxiv.org/abs/2506.09623) | CVPR 2025 | [project](https://cari4d.github.io/) |
| 2025-11-07 | Motion-Aware, Monocular Video, Bundle Adjustment | KAIST | [4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes](https://arxiv.org/abs/2511.05229) | NeurIPS 2025 | [paper](https://arxiv.org/abs/2511.05229) |
| 2025-05-25 | 4D Generation, Multi-View Video, Diffusion | Google | [CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models](https://arxiv.org/abs/2411.18613) | CVPR 2025 | [project](https://cat-4d.github.io/) |
| 2025-04-08 | Neural Rendering, Human, No Eyes | University of Cambridge | [Seeing Without Eyes: Neural Human Rendering from Monocular Video](https://arxiv.org/abs/2504.04667) | CVPR 2025 | [project](https://seeing-without-eyes.github.io/) |
| 2025-01-22 | 3D Reconstruction, Canonical, Multi-View | Stanford | [UniCon3R: Unified 3D Reconstruction and Recognition](https://arxiv.org/abs/2501.12887) | CVPR 2025 | [project](https://unicon3r.github.io/) |
| 2024-12-05 | Dynamic Geometry, DUSt3R, Motion | University of Oxford | [MonST3R: Estimating Geometry in the Presence of Motion](https://arxiv.org/abs/2410.21193) | ECCV 2024 | [project](https://monst3r.github.io/) / [github](https://github.com/Junyi42/monst3r) |

#### 3.3.2 Deformation Graphs & Canonical Spaces

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-02-12 | 4D Dynamic, Monocular Video, Tree-Chains | Cornell | [WorldTree: Towards 4D Dynamic Worlds from Monocular Video using Tree-Chains](https://arxiv.org/abs/2602.11845) | ICLR 2026 | [paper](https://arxiv.org/abs/2602.11845) |
| 2025-11-12 | 4D Scene, Feed-Forward, Controllable, Video Diffusion | Shanghai AI Lab | [Diff4Splat: Controllable 4D Scene Generation with Latent Dynamic Reconstruction Models](https://arxiv.org/abs/2511.00503) | CVPR 2026 | [paper](https://arxiv.org/abs/2511.00503) |
| 2025-10-15 | Dynamic 4D, Gaussian, Canonical | Zhejiang University | [Director: Directed Generative Models for 4D Scene Evolution](https://arxiv.org/abs/2510.13229) | CVPR 2025 | [project](https://director-4d.github.io/) |
| 2024-11-20 | 4D Reconstruction, Gaussian Splatting, Forward | Shanghai AI Lab | [Forge4D: Gaussian Splatting for Forward Facing 4D Reconstruction](https://arxiv.org/abs/2411.13456) | arXiv | [paper](https://arxiv.org/abs/2411.13456) |
| 2024-04-18 | Deformation, Dynamic Radiance Fields, Canonical | ETH Zurich | [SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](https://arxiv.org/abs/2312.14937) | arXiv | [project](https://yihua7.github.io/SC-GS-web/) |
| 2023-05-17 | Non-Rigid Tracking, Neural Deformation, 4D | Tsinghua | [Neuralangelo: High-Fidelity Neural Surface Reconstruction](https://arxiv.org/abs/2306.03092) | CVPR 2023 | [project](https://research.nvidia.com/labs/dir/neuralangelo/) |

<h2 id="-4-3d-generation">🎛️ 4. 3D Generation</h2>

This section tracks methods that create new 3D assets, parts, articulated objects, scenes, and editable 3D worlds, with emphasis on physical and simulation use.

<a id="41-object-level-generation"></a>

### 4.1 Object-Level Generation

#### 4.1.1 Image/Text to 3D Mesh

##### Single Image / Text-Conditioned Object Mesh

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-05-01 | Pose-Aware, Diffusion, 3D Geometry, Direct | Renmin University | [PAD: Pose-Aware Diffusion for 3D Generation](https://arxiv.org/abs/2605.00345) | arXiv | [paper](https://arxiv.org/abs/2605.00345) |
| 2025-12-16 | Image-to-3D, O-Voxel, PBR Materials | Microsoft | [TRELLIS.2: Native and Compact Structured Latents for 3D Generation](https://arxiv.org/abs/2512.14692) | arXiv | [github](https://github.com/microsoft/TRELLIS.2) / [model](https://huggingface.co/microsoft/TRELLIS.2-4B) |
| 2025-11-20 | Single Image, Multi-Object, Layout, SAM 3D | Meta AI | [SAM 3D: 3Dfy Anything in Images](https://arxiv.org/abs/2511.16624) | arXiv | [github](https://github.com/facebookresearch/sam-3d-objects) |
| 2025-10-23 | Single Image, Pose-Grounded, Flow Matching | Meta AI | [CUPID: Generative 3D Reconstruction via Joint Object and Pose Modeling](https://arxiv.org/abs/2510.20776) | arXiv | [project](https://cupid3d.github.io/) |
| 2025-06-18 | Image-to-3D, PBR Materials, Production Assets | Tencent | [Hunyuan3D 2.1: From Images to High-Fidelity 3D Assets with Production-Ready PBR Material](https://arxiv.org/abs/2506.15442) | arXiv | [github](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) / [model](https://huggingface.co/tencent/Hunyuan3D-2.1) |
| 2025-06-12 | Text-to-3D, 3D-DiT, Interactive Refinement | HKUST | [CraftsMan3D: High-fidelity Mesh Generation with 3D Native Generation and Interactive Geometry Refiner](https://arxiv.org/abs/2405.14979) | arXiv | [github](https://github.com/wyysf-98/CraftsMan3D) |
| 2025-06-10 | Text/Image-to-3D, Bundle Image, Data-Efficient (147K) | HKUST(GZ) | [Kiss3DGen: Repurposing Image Diffusion Models for 3D Asset Generation](https://arxiv.org/abs/2503.01370) | arXiv | [github](https://github.com/jimmy-766/Kiss3DGen) |
| 2025-05-07 | Image-to-3D, PBR Textured Mesh, Render-Enhanced Auto-Encoder | Tsinghua | [MeshGen: Generating PBR Textured Mesh with Render-Enhanced Auto-Encoder and Generative Data Augmentation](https://arxiv.org/abs/2505.04656) | CVPR 2025 | [project](https://heheyas.github.io/MeshGen/) |
| 2025-05-23 | Gigascale 3D, Sparse Volume, Image Conditioning | Nanjing University | [Direct3D-S2: Gigascale 3D Generation Made Easy with Spatial Sparse Attention](https://arxiv.org/abs/2505.17412) | NeurIPS 2025 | [project](https://nju3dv.github.io/projects/Direct3D-S2/) / [github](https://github.com/DreamTechAI/Direct3D-S2) |
| 2025-05-12 | Textured Assets, Controllable 3D, Open Framework | StepFun | [Step1X-3D: Towards High-Fidelity and Controllable Generation of Textured 3D Assets](https://arxiv.org/abs/2505.07747) | arXiv | [github](https://github.com/stepfun-ai/Step1X-3D) |
| 2025-03-28 | Geometry Detail, Normal Bridging, Image-to-3D | Cornell | [Hi3DGen: High-fidelity 3D Geometry Generation from Images via Normal Bridging](https://arxiv.org/abs/2503.22236) | arXiv | [project](https://stable-x.github.io/Hi3DGen/) |
| 2025-02-10 | Shape Synthesis, Rectified Flow, Image-to-3D | VAST AI / Tripo | [TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models](https://arxiv.org/abs/2502.06608) | arXiv | [github](https://github.com/VAST-AI-Research/TripoSG) / [model](https://huggingface.co/VAST-AI/TripoSG) |
| 2025-01-21 | Image/Text-to-3D, Mesh, Texture | Tencent | [Hunyuan3D 2.0: Scaling Diffusion Models for High Resolution Textured 3D Assets Generation](https://arxiv.org/abs/2501.12202) | arXiv | [github](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) |
| 2025-01-08 | Point-Aware, Interactive Editing, Single Image | Stability AI / UIUC | [SPAR3D: Stable Point-Aware Reconstruction of 3D Objects from Single Images](https://arxiv.org/abs/2501.04689) | arXiv | [project](https://spar3d.github.io/) / [model](https://huggingface.co/stabilityai/stable-point-aware-3d) |
| 2024-12-02 | Structured Latents, Text/Image-to-3D, Mesh | Microsoft | [TRELLIS: Structured 3D Latents for Scalable and Versatile 3D Generation](https://arxiv.org/abs/2412.01506) | CVPR 2025 | [project](https://trellis3d.github.io/) / [github](https://github.com/microsoft/TRELLIS) |
| 2024-08-01 | Fast Mesh, UV Unwrap, Material Disentanglement | Stability AI | [Stable Fast 3D: Stable Fast 3D Mesh Reconstruction with UV-unwrapping and Illumination Disentanglement](https://arxiv.org/abs/2408.00653) | arXiv | [project](https://stable-fast-3d.github.io/) / [github](https://github.com/Stability-AI/stable-fast-3d) |
| 2024-05-30 | High-Quality Mesh, Multi-View Normals, ISOMER | Tsinghua | [Unique3D: High-Quality and Efficient 3D Mesh Generation from a Single Image](https://arxiv.org/abs/2405.20343) | arXiv | [project](https://wukailu.github.io/Unique3D/) |
| 2024-05-19 | Multi-View Diffusion, Row-Wise Attention, Mesh | University of Hong Kong | [Era3D: High-Resolution Multiview Diffusion using Efficient Row-wise Attention](https://arxiv.org/abs/2405.11616) | arXiv | [project](https://penghtyx.github.io/Era3D/) |
| 2024-04-10 | Single Image, Sparse-View LRM, Mesh | Tencent ARC | [InstantMesh: Efficient 3D Mesh Generation from a Single Image with Sparse-view Large Reconstruction Models](https://arxiv.org/abs/2404.07191) | arXiv | [github](https://github.com/TencentARC/InstantMesh) |
| 2024-03-18 | Single Image, Orbital Video, Multi-View Prior | Stability AI | [SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image using Latent Video Diffusion](https://arxiv.org/abs/2403.12008) | arXiv | [project](https://sv3d.github.io/) |
| 2024-03-07 | Textured Mesh, Convolutional Reconstruction, Single Image | Shanghai AI Lab | [CRM: Single Image to 3D Textured Mesh with Convolutional Reconstruction Model](https://arxiv.org/abs/2403.05034) | arXiv | [project](https://ml.cs.tsinghua.edu.cn/~zhengyi/CRM/) |
| 2024-03-04 | Single Image, Fast 3D, Mesh | Stability AI | [TripoSR: Fast 3D Object Reconstruction from a Single Image](https://arxiv.org/abs/2403.02151) | arXiv | [github](https://github.com/VAST-AI-Research/TripoSR) |
| 2024-02-07 | Multi-View Gaussian, Fast 3D Content, Image/Text | Peking University | [LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation](https://arxiv.org/abs/2402.05054) | ECCV 2024 Oral | [github](https://github.com/3DTopia/LGM) |
| 2023-10-23 | Cross-Domain Diffusion, Multi-View Normals, Mesh | HKUST | [Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://arxiv.org/abs/2310.15008) | CVPR 2024 Highlight | [github](https://github.com/xxlong0/Wonder3D) |
| 2023-10-23 | Single Image, Consistent Multi-View Diffusion | UC San Diego | [Zero123++: a Single Image to Consistent Multi-view Diffusion Base Model](https://arxiv.org/abs/2310.15110) | arXiv | [github](https://github.com/SUDO-AI-3D/zero123plus) |
| 2023-06-27 | Single Image, Optimization-Free, Mesh | Shanghai AI Lab | [One-2-3-45: Any Single Image to 3D Mesh in 45 Seconds without Per-Shape Optimization](https://arxiv.org/abs/2306.16928) | NeurIPS 2023 | [github](https://github.com/One-2-3-45/One-2-3-45) |

##### Multi-Image / Multi-View Object Mesh

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-03-12 | Multi-View, SAM3D, Layout-Aware, Physical Plausibility | Peking University | [MV-SAM3D: Adaptive Multi-View Fusion for Layout-Aware 3D Generation](https://arxiv.org/abs/2603.11633) | arXiv | [github](https://github.com/devinli123/MV-SAM3D) |
| 2026-01-16 | Casual Capture, Posed Multi-View, Metric Shape | Meta AI | [ShapeR: Robust Conditional 3D Shape Generation from Casual Captures](https://arxiv.org/abs/2601.11514) | arXiv | [paper](https://arxiv.org/abs/2601.11514) |
| 2025-11-12 | Multi-Image Fusion, Region Control, TRELLIS | Zhejiang University | [Fuse3D: Generating 3D Assets Controlled by Multi-Image Fusion](https://arxiv.org/abs/2602.17040) | SIGGRAPH Asia 2025 | [project](https://fuse3d.org/) / [github](https://github.com/JINNMnm/Fuse3D) |
| 2025-10-23 | Multi-View Extension, Pose-Grounded, Flow Matching | Meta AI | [CUPID: Generative 3D Reconstruction via Joint Object and Pose Modeling](https://arxiv.org/abs/2510.20776) | arXiv | [project](https://cupid3d.github.io/) |
| 2025-03-18 | Multi-View Image-to-Shape, Hunyuan3D-DiT | Tencent | [Hunyuan3D 2.0 MV](https://huggingface.co/tencent/Hunyuan3D-2mv) | Model | [github](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) / [model](https://huggingface.co/tencent/Hunyuan3D-2mv) |
| 2024-02-05 | Scalable View Synthesis, Single/Multi-Image 3D | KAUST | [EscherNet: A Generative Model for Scalable View Synthesis](https://arxiv.org/abs/2402.03908) | CVPR 2024 | [project](https://kxhit.github.io/EscherNet/) |
| 2019-08-05 | Multi-View Images, Mesh Deformation, Shape Refinement | National Tsing Hua University | [Pixel2Mesh++: Multi-View 3D Mesh Generation via Deformation](https://arxiv.org/abs/1908.01491) | ICCV 2019 | [github](https://github.com/walsvid/Pixel2MeshPlusPlus) |

#### 4.1.2 Texture & Material Generation (PBR)

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-10-18 | PBR Material, SVBRDF, Text-to-Material | Adobe | [MatFuse: Controllable Material Generation with Diffusion Models](https://arxiv.org/abs/2308.11408) | SIGGRAPH Asia 2024 | [project](https://gvecchio.com/matfuse/) |
| 2024-03-12 | Texture Generation, Mesh, Multi-View Consistency | Tencent | [Paint3D: Paint Anything 3D with Lighting-Less Texture Diffusion Models](https://arxiv.org/abs/2312.13913) | CVPR 2024 | [project](https://paint3d.github.io/) |
| 2023-09-21 | Texture, Material, Text-to-Texture | KAIST | [Text2Tex: Text-driven Texture Synthesis via Diffusion Models](https://arxiv.org/abs/2303.11396) | ICCV 2023 | [project](https://daveredrum.github.io/Text2Tex/) |

<a id="42-part-level--articulated-generation"></a>

### 4.2 Part-Level & Articulated Generation

#### 4.2.1 Kinematic Structure Generation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-03-01 | Articulated Assets, 3D LLM, Kinematic Structure | Tsinghua | [ArtLLM: Generating Articulated Assets via 3D LLM](https://arxiv.org/abs/2603.01142) | CVPR 2026 | [paper](https://arxiv.org/abs/2603.01142) |
| 2025-11-17 | Sim-Ready Assets, Physical Properties, Single Image | NTU | [PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image](https://arxiv.org/abs/2511.13648) | CVPR 2026 | [paper](https://arxiv.org/abs/2511.13648) |
| 2025-11-02 | URDF, 3D MLLM, Articulated Objects | Tsinghua | [URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model](https://openreview.net/forum?id=g3EF5XsapH) | NeurIPS 2025 | [paper](https://arxiv.org/abs/2511.00940) |
| 2025-02-26 | Articulated Objects, 3DGS, Joint Estimation | Peking University | [ArtGS: Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459) | ICLR 2025 | [project](https://buzz-beater.github.io/artgs/) |
| 2024-09-26 | Open-Vocabulary, URDF, Articulation | Stanford | [Articulate Anything: Open-vocabulary 3D Articulated Object Generation](https://openreview.net/forum?id=6akuzEqP38) | ICLR 2025 | [project](https://articulate-anything.github.io/) |

#### 4.2.2 Part-Aware Assembly & Editing

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-12-16 | Articulated Mesh, Part-by-Part, Hierarchical Transformer | Cornell | [MeshArt: Generating Articulated Meshes with Structure-Guided Transformers](https://arxiv.org/abs/2412.11596) | arXiv | [paper](https://arxiv.org/abs/2412.11596) |
| 2025-01-20 | Part-Level 3D, Object Decomposition, Generation | University of Waterloo | [PartCrafter: Structured 3D Mesh Generation via Compositional Latent Diffusion Transformers](https://arxiv.org/abs/2501.11015) | arXiv | [project](https://wgsxm.github.io/projects/partcrafter/) |
| 2024-06-13 | Part-Aware, Shape Assembly, 3D Generation | Shanghai AI Lab | [Michelangelo: Conditional 3D Shape Generation based on Shape-Image-Text Aligned Latent Representation](https://arxiv.org/abs/2306.17115) | NeurIPS 2023 | [github](https://github.com/NeuralCarver/Michelangelo) |
| 2023-12-04 | Shape Program, Structure, Editable Assets | MIT | [Shape2Program: Learning to Infer Shape Programs from 3D Shapes](https://arxiv.org/abs/2312.08307) | arXiv | [project](https://shape2prog.csail.mit.edu/) |

<a id="43-scene-level-generation"></a>

### 4.3 Scene-Level Generation

#### 4.3.1 Layout & Procedural Generation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-04-29 | 4D World Model, Robotic Action, Video + 3D | Tsinghua | [X-WAM: Unified 4D World Action Modeling from Video Priors](https://arxiv.org/abs/2604.26694) | arXiv | [paper](https://arxiv.org/abs/2604.26694) |
| 2026-04-15 | Multi-Modal World Model, 3D Gaussian, Navigation | Tencent | [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268) | arXiv | [paper](https://arxiv.org/abs/2604.14268) |
| 2026-03-12 | Multi-Floor, Language-to-3D, Long-Horizon Tasks | Tsinghua | [MANSION: Multi-floor lANguage-to-3D Scene generatIOn for loNg-horizon tasks](https://arxiv.org/abs/2603.11554) | CVPR 2026 | [paper](https://arxiv.org/abs/2603.11554) |
| 2026-03-06 | Compositional Scene, Panoramic Image, Feed-Forward | NTU | [Pano3DComposer: Feed-Forward Compositional 3D Scene Generation from Single Panoramic Image](https://arxiv.org/abs/2603.05908) | CVPR 2026 | [paper](https://arxiv.org/abs/2603.05908) |
| 2025-03-18 | Scene Layout, Optimization, Generation | Tsinghua | [HOG-Layout: Layout-Enhanced Scene Generation via Hierarchical Optimization](https://arxiv.org/abs/2503.10462) | arXiv | [project](https://hog-layout.github.io/) |
| 2025-02-28 | Octree, 3D Diffusion, Scene Generation | Zhejiang University | [Octree Diffusion: Hierarchical Scene Generation via Octree Structures](https://arxiv.org/abs/2502.14832) | arXiv | [project](https://octree-diffusion.github.io/) |
| 2025-01-15 | Gaussian, GPT, Scene Generation | Shanghai AI Lab | [GaussianGPT: Language-Driven Scene Generation with Gaussian Representation](https://arxiv.org/abs/2501.08734) | arXiv | [paper](https://arxiv.org/abs/2501.08734) |
| 2024-12-20 | Scene Generation, Growing, Incremental | Tsinghua | [WorldGrow: Incremental 3D Scene Generation](https://arxiv.org/abs/2412.14572) | CVPR 2025 | [project](https://worldgrow.github.io/) |
| 2024-11-05 | Splatting, Fluents, Scene Understanding | University of Cambridge | [FluSplat: Fluent Scene Generation via Gaussian Splatting](https://arxiv.org/abs/2411.03472) | CVPR 2025 | [project](https://flusplat.github.io/) |
| 2024-10-17 | Procedural Scenes, Synthetic Data, Embodied AI | Princeton | [Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation](https://arxiv.org/abs/2406.11824) | NeurIPS 2024 | [project](https://infinigen.org/) / [github](https://github.com/princeton-vl/infinigen) |
| 2023-11-15 | Procedural World, Synthetic Data, Simulation | Princeton | [Infinite Photorealistic Worlds using Procedural Generation](https://arxiv.org/abs/2306.09310) | CVPR 2023 | [project](https://infinigen.org/) |
| 2023-11-02 | Text-to-3D Room, Indoor Scenes, Mesh | LMU Munich | [Text2Room: Extracting Textured 3D Meshes from 2D Text-to-Image Models](https://arxiv.org/abs/2303.11989) | ICCV 2023 | [project](https://lukashoel.github.io/text-to-room/) |
| 2023-02-23 | Unbounded 3D Scene, Generative Model, Driving | NVIDIA | [SceneDreamer: Unbounded 3D Scene Generation from 2D Image Collections](https://arxiv.org/abs/2302.01330) | CVPR 2023 | [project](https://scene-dreamer.github.io/) |

#### 4.3.2 3D Scene Editing

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-02-17 | Flow Editing, 3D Editing, Dynamics | Google DeepMind | [FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models](https://arxiv.org/abs/2412.08629) | ICLR 2025 | [project](https://matankleiner.github.io/flowedit/) |
| 2024-07-01 | 3DGS Editing, Scene Editing, Text Prompt | National University of Singapore | [GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting](https://arxiv.org/abs/2311.14521) | CVPR 2024 | [project](https://buaacyw.github.io/gaussian-editor/) |
| 2023-11-15 | NeRF Editing, Text, Local Edits | UC Berkeley | [Instruct-NeRF2NeRF: Editing 3D Scenes with Instructions](https://arxiv.org/abs/2303.12789) | ICCV 2023 | [project](https://instruct-nerf2nerf.github.io/) |

#### 4.3.3 Semantic Scene Generation & Spatial Intelligence

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-01-28 | Rover, Semantic, 3D Scene | Carnegie Mellon University | [SEM-ROVER: Semantic Scene Exploration with Hierarchical Spatial Reasoning](https://arxiv.org/abs/2501.14782) | ICLR 2025 | [project](https://sem-rover.github.io/) |
| 2024-09-30 | Spatial, Generation, Language | Tsinghua | [SpatialGen: Language-Driven Spatial Scene Generation](https://arxiv.org/abs/2409.20197) | NeurIPS 2024 | [project](https://spatialgen.github.io/) |

<h2 id="-5-embodied-3d">🌐 5. Embodied 3D</h2>

This section focuses on how 3D perception, reconstruction, and generation translate into physical interaction, world models, human understanding, and agent-facing 3D intelligence.

<a id="51-dynamic-scene-graphs--tracking"></a>

### 5.1 Dynamic Scene Graphs & Tracking

#### 5.1.1 Topologically Aware Tracking

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-10-20 | Dynamic VGGT, Pose, Geometry, 4D | Harvard | [PAGE-4D: Disentangled Pose and Geometry Estimation for 4D Perception](https://arxiv.org/abs/2510.17568) | ICLR 2026 | [project](https://page4d.github.io/) |
| 2023-09-28 | 3D Scene Graph, Open-Vocabulary, Planning | MIT | [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650) | ICRA 2024 | [project](https://concept-graphs.github.io/) |
| 2023-05-22 | Scene Graph, 3D Perception, Robotics | MIT | [Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization](https://arxiv.org/abs/2201.13360) | RSS 2022 | [github](https://github.com/MIT-SPARK/Hydra) |

<a id="52-reconstruction-based-world-models"></a>

### 5.2 Reconstruction-Based World Models

#### 5.2.1 Physics-Grounded World Models

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-01-01 | 4D World Model, Monocular Video, Reconstruction | CASIA | [NeoVerse: Enhancing 4D World Model with in-the-wild Monocular Videos](https://arxiv.org/abs/2601.00393) | arXiv | [project](https://neoverse-4d.github.io/) / [github](https://github.com/IamCreateAI/NeoVerse) |
| 2025-06-12 | Generative 3D World Engine, Embodied AI, Simulation | Horizon Robotics | [EmbodiedGen: Towards a Generative 3D World Engine for Embodied Intelligence](https://arxiv.org/abs/2506.10600) | arXiv | [paper](https://arxiv.org/abs/2506.10600) |
| 2025-03-05 | 3D Cache, Camera Control, World-Consistent Video | NVIDIA | [GEN3C: 3D-Informed World-Consistent Video Generation with Precise Camera Control](https://arxiv.org/abs/2503.03751) | CVPR 2025 Highlight | [project](https://research.nvidia.com/labs/toronto-ai/GEN3C/) |
| 2024-10-04 | World Model, 3D Consistency, Video Generation | Google DeepMind | [Genie 2: A Large-Scale Foundation World Model](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) | Blog | [page](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) |

#### 5.2.2 Action-Conditioned Dynamics Synthesis

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-05-20 | World Model, Unified Reconstruction+Predict+Planning | Shanghai AI Lab | [AETHER: Geometric-Aware Unified World Modeling](https://arxiv.org/abs/2503.18945) | arXiv | [project](https://aether-world.github.io/) |
| 2025-03-24 | World Model, Geometric-Aware, 4D Reconstruction | Shanghai AI Lab | [Aether: Geometric-Aware Unified World Modeling](https://arxiv.org/abs/2503.18945) | arXiv | [project](https://aether-world.github.io/) |
| 2025-11-25 | World Model, Data Engine, VLA, 3DGS | Cornell | [GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861) | arXiv | [project](https://giga-world-0.github.io/) |
| 2025-07-01 | 4D Generation, Multi-View Consistency, Robot Manipulation | Stanford | [Geometry-aware 4D Video Generation for Robot Manipulation](https://arxiv.org/abs/2507.01099) | ICLR 2026 | [paper](https://arxiv.org/abs/2507.01099) |
| 2025-02-28 | Embodied Video Anticipation, Reflection | HKUST | [EVA: An Embodied World Model for Future Video Anticipation](https://arxiv.org/abs/2410.15461) | ICML 2025 | [project](https://eva-world.github.io/) |
| 2024-02-26 | Interactive Environment, Generative World, Agent | Google DeepMind | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | ICML 2024 | [project](https://sites.google.com/view/genie-2024/) |

<a id="53-physical-interaction--affordance"></a>

### 5.3 Physical Interaction & Affordance

#### 5.3.1 Affordance Prediction & Grasp Detection

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-11-20 | Open-Vocabulary, Task-Oriented Grasp, LLM | CMU | [GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping](https://arxiv.org/abs/2411.12286) | CoRL 2024 | [project](https://glover-grasp.github.io/) |
| 2024-10-15 | SE(3)-Equivariant, 6-DoF Grasp, Flow | Seoul Nat'l Univ | [EquiGraspFlow: SE(3)-Equivariant 6-DoF Grasp Pose Generative Flows](https://arxiv.org/abs/2407.08216) | CoRL 2024 | [project](https://equigraspflow.github.io/) |
| 2024-07-15 | AnyGrasp, 6-DoF Grasp, Point Cloud | Tsinghua | [AnyGrasp: Robust and Efficient Grasp Detection in Cluttered Scenes](https://arxiv.org/abs/2212.08333) | RSS 2024 | [github](https://github.com/graspnet/anygrasp_sdk) |
| 2024-07-10 | SE(3)-Equivariant, Grasp, Point Cloud | Northeastern | [OrbitGrasp: SE(3)-Equivariant Grasp Learning](https://arxiv.org/abs/2407.03531) | CoRL 2024 | [project](https://orbitgrasp.github.io/) |
| 2024-06-01 | Affordance, Interactive Perception, 3D | MIT | [Where2Act: From Pixel to Action (via 3D)](https://arxiv.org/abs/2101.02692) | CVPR 2024 | |
| 2023-12-15 | Affordance, Point Cloud, Interaction | Stanford | [IAGNet: Interaction-Aware 3D Generative Model for Affordance Prediction](https://arxiv.org/abs/2303.10437) | CoRL 2023 | |
| 2023-11-28 | Contact Prediction, Object Interaction, Point Cloud | Meta AI | [ContactGen: Generative Contact Modeling for 3D Object Interactions](https://arxiv.org/abs/2310.03740) | NeurIPS 2023 | |

#### 5.3.2 Physical Property & Material Estimation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-11-23 | Physical Property, Bayesian 3DGS, Mass/Hardness/Friction | CMU | [PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570) | CVPR 2026 | [paper](https://arxiv.org/abs/2511.18570) |
| 2024-12-15 | Physical Property, 3DGS, LMM | Multiple | [GaussianProperty: Integrating Physical Properties to 3D Gaussians with LMMs](https://arxiv.org/abs/2412.11258) | arXiv | [project](https://gaussianproperty.github.io/) |
| 2024-03-28 | Mass, Friction, Compliance, LLM, Adaptive Grasp | MIT | [DeliGrasp: Inferring Object Mass, Friction, and Compliance with LLMs for Adaptive Grasp Policies](https://arxiv.org/abs/2403.07832) | CoRL 2024 | [project](https://deligrasp.github.io/) |
| 2023-10-05 | Physical Properties, Visual Estimation, Liquids | MIT | [Visual Estimation of Physical Properties of Objects and Liquids](https://arxiv.org/abs/2310.03163) | CoRL 2023 | [project](https://mit-genai.github.io/) |
| 2023-06-01 | Mass Estimation, Vision, Physics | CMU | [Learning to Estimate Object Mass from Vision and Force](https://arxiv.org/abs/2306.00280) | RSS 2023 | [project](https://robin-lab.cs.cmu.edu/) |

<a id="54-human-centric-3d-for-embodiment"></a>

### 5.4 Human-Centric 3D for Embodiment

#### 5.4.1 Human Pose & Shape Estimation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-01-03 | Joint Scene+Human, Feed-Forward, Metric-Scale | HKUST | [UniSH: Unifying Scene and Human Reconstruction in a Feed-Forward Pass](https://arxiv.org/abs/2601.01222) | CVPR 2026 | [paper](https://arxiv.org/abs/2601.01222) |
| 2025-06-15 | Real-Time Multi-Person, Scale-Adaptive, 24 FPS | Peking University | [SAT-HMR: Real-Time Multi-Person 3D Mesh Estimation via Scale-Adaptive Tokens](https://arxiv.org/abs/2411.19824) | CVPR 2025 | [github](https://github.com/ChiSu001/SAT-HMR) |
| 2025-06-12 | Perspective Camera, Metric Depth, Single View | NVIDIA | [BLADE: Single-view Body Mesh Learning through Accurate Depth Estimation](https://arxiv.org/abs/2412.15144) | CVPR 2025 | [project](https://research.nvidia.com/labs/amri/projects/blade/) |
| 2025-06-10 | Biomechanical Skeleton, Anatomical Joint Limits, SKEL | UT Austin / ZJU | [HSMR: Reconstructing Humans with a Biomechanically Accurate Skeleton](https://arxiv.org/abs/2503.21751) | CVPR 2025 | [project](https://isshikihugh.github.io/HSMR/) |
| 2024-09-25 | Tokenized Pose, Codebook Prior, VQ-VAE | MPI-IS | [TokenHMR: Advancing Human Mesh Recovery with a Tokenized Pose Representation](https://arxiv.org/abs/2404.04177) | CVPR 2024 | [project](https://tokenhmr.is.tue.mpg.de/) |
| 2024-08-20 | Multi-Person, Whole-Body, Single Shot | NAVER Labs | [Multi-HMR: Multi-Person Whole-Body Human Mesh Recovery in a Single Shot](https://arxiv.org/abs/2402.14654) | ECCV 2024 | [github](https://github.com/naver/multi-hmr) |
| 2024-05-15 | Human Mesh Recovery, Transformer, 3D Body | Meta AI | [HMR 2.0: End-to-End Human Mesh Recovery with Transformers](https://arxiv.org/abs/2307.10868) | ICCV 2023 | [project](https://www.modelscope.cn/studios/damo/HMR2.0) |
| 2024-01-18 | 3D Human Pose, Whole-Body, Multi-Person | CMU | [WHAM: Reconstructing World-grounded Humans with Accurate 3D Motion](https://arxiv.org/abs/2312.07531) | CVPR 2024 | [project](https://wham.is.tue.mpg.de/) |
| 2024-01-08 | 4D Humans, Video, Spatiotemporal | MPI-IS | [4D-Humans: Reconstructing and Tracking Humans with Transformers](https://arxiv.org/abs/2305.14100) | ICCV 2023 | [project](https://www.socangel.dev/4d-humans/) |
| 2023-12-05 | Hand-Object, 3D Reconstruction, Interaction | ETH Zurich | [HOLD: Category-agnostic 3D Reconstruction of Interacting Hands and Objects from Video](https://arxiv.org/abs/2311.18448) | CVPR 2024 | [project](https://www.eth-zurich.ch/hold) / [github](https://github.com/zc-alexfan/hold) |

#### 5.4.2 Human-Object Interaction (HOI) in 3D

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-03-10 | Close Interaction, Dynamic Video, Multi-Person | MPI-IS | [Harmony4D: A Video Dataset for In-The-Wild Close Human Interactions](https://arxiv.org/abs/2503.05483) | CVPR 2025 | [project](https://harmony4d.github.io/) |
| 2024-12-03 | Human-to-Robot, Teleoperation, 3D Hand Pose | Stanford | [AnyTeleop: A General Vision-Based Teleoperation System](https://arxiv.org/abs/2307.06275) | CoRL 2023 | [project](https://anyteleop.com/) |
| 2024-06-15 | HOI4D, Dynamic Interaction, Point Cloud | Peking University | [HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction](https://arxiv.org/abs/2203.01577) | CVPR 2022 | [project](https://hoi4d.github.io/) |
| 2024-03-01 | HOI, 3D Interaction, Motion Capture | MPI-IS | [BEHAVE: Dataset and Method for Tracking Human Object Interactions](https://arxiv.org/abs/2204.06950) | CVPR 2022 | [project](https://virtualhumans.mpi-inf.mpg.de/behave/) |

<a id="55-robotics-integration--vlm-agents"></a>

### 5.5 Robotics Integration & VLM Agents

#### 5.5.1 Sim-to-Real via Generated Assets

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-09-26 | Personalized Navigation, 3DGS, Real-to-Sim | CMU | [EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats](https://arxiv.org/abs/2509.17430) | ICCV 2025 | [paper](https://arxiv.org/abs/2509.17430) |
| 2025-04-05 | Dynamic Digital Twin, Sim2Real, 60Hz | Stanford | [Real-is-Sim: Bridging the Sim-to-Real Gap with a Dynamic Digital Twin](https://arxiv.org/abs/2504.03597) | CoRL 2025 | [paper](https://arxiv.org/abs/2504.03597) |
| 2025-02-26 | Articulated Objects, URDF, Manipulation | Peking University | [ArtGS: Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459) | ICLR 2025 | [project](https://buzz-beater.github.io/artgs/) |
| 2024-10-08 | Navigation, World Model, Embodied Agent | Stanford | [NavDreamer: Dreaming with World Models for Embodied Navigation](https://arxiv.org/abs/2410.08234) | CoRL 2024 | [project](https://navdreamer.github.io/) |
| 2024-09-26 | Open-Vocabulary, Articulation, URDF | Stanford | [Articulate Anything: Open-vocabulary 3D Articulated Object Generation](https://openreview.net/forum?id=6akuzEqP38) | ICLR 2025 | [project](https://articulate-anything.github.io/) |
| 2024-09-25 | 3D Descriptor Fields, Zero-Shot, Rearrangement | Columbia / Stanford | [D3Fields: Dynamic 3D Descriptor Fields for Zero-Shot Generalizable Rearrangement](https://arxiv.org/abs/2409.09408) | CoRL 2024 | [project](https://robopil.github.io/d3fields/) |
| 2024-09-15 | Gaussian Splatting, Sim2Real, RGB Policy | CMU | [SplatSim: Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using Gaussian Splatting](https://arxiv.org/abs/2409.10161) | CoRL 2024 / ICRA 2025 | [project](https://splatsim.github.io/) |
| 2024-08-15 | Digital Cousins, Real→Sim→Real, Zero-Shot 90% | Stanford | [Automated Creation of Digital Cousins for Robust Policy Learning](https://arxiv.org/abs/2410.07408) | CoRL 2024 | [project](https://digital-cousins.github.io/) |
| 2024-03-28 | Real-to-Sim-to-Real, Digital Twin, Manipulation | MIT | [RialTo: Reconciling Reality through Simulation for Robust Manipulation](https://arxiv.org/abs/2403.03949) | RSS 2024 | [project](https://real-to-sim-to-real.github.io/RialTo/) |
| 2023-06-16 | Digital Twin, Synthetic Scenes, Embodied AI | NVIDIA | [ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://arxiv.org/abs/2206.06994) | NeurIPS 2022 | [project](https://procthor.allenai.org/) |

#### 5.5.2 VLMs for 3D Grounding & Planning

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-04-05 | 3D Spatial Memory, Multimodal, Robot Navigation | Meta AI | [M3: 3D-Spatial MultiModal Memory](https://arxiv.org/abs/2503.16413) | ICLR 2025 | [project](https://m3-spatial-memory.github.io) |
| 2025-02-10 | Agent, VLN, 3D Navigation | Stanford | [AgentVLN: Vision-Language Navigation with 3D Scene Understanding](https://arxiv.org/abs/2502.05376) | CVPR 2025 | [project](https://agent-vln.github.io/) |
| 2025-10-23 | Grounded CoT, 3D Reasoning, SceneCOT-185K Dataset | PKU | [SceneCOT: Eliciting Grounded Chain-of-Thought Reasoning in 3D Scenes](https://arxiv.org/abs/2510.16714) | arXiv | [paper](https://arxiv.org/abs/2510.16714) |
| 2025-03-06 | 3D VQA, Gaussian Splatting, Zero-Shot | Tsinghua | [SplatTalk: 3D VQA with Gaussian Splatting](https://arxiv.org/abs/2503.06271) | ICCV 2025 | [paper](https://arxiv.org/abs/2503.06271) |
| 2024-11-11 | 3D Grounding, VLM, Point Cloud | Shanghai AI Lab | [LLaVA-3D: A Simple yet Effective Pathway to Empowering LMMs with 3D Awareness](https://arxiv.org/abs/2410.06250) | arXiv | [github](https://github.com/ZCMax/LLaVA-3D) |
| 2024-07-12 | Spatial VLM, 3D Reasoning, Robotics | Stanford | [SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities](https://arxiv.org/abs/2401.12168) | CVPR 2024 | [project](https://spatial-vlm.github.io/) |
| 2023-11-13 | Embodied Planning, 3D Scene, LLM | MIT | [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](https://arxiv.org/abs/2307.06135) | CoRL 2023 | [project](https://sayplan.github.io/) |

<h2 id="-6-datasets-benchmarks--infrastructure">🧰 6. Datasets, Benchmarks & Infrastructure</h2>

This section is the toolbox and dictionary for quickly choosing datasets, benchmarks, metrics, simulators, and reference surveys.

<a id="61-surveys--taxonomies"></a>

### 6.1 Surveys & Taxonomies

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-04-15 | 3D Generation, Embodied AI, Robotic Simulation, Survey | HKUST / Tencent | [3D Generation for Embodied AI and Robotic Simulation: A Survey](https://arxiv.org/abs/2604.26509) | arXiv | [paper](https://arxiv.org/abs/2604.26509) |
| 2026-02-01 | Visual Grounding, 2D & 3D, Unified Perspective | Multiple | [Visual Grounding in 2D and 3D: A Unified Perspective and Survey](https://www.sciencedirect.com/science/article/abs/pii/S1566253525006979) | Information Fusion 2026 | [paper](https://www.sciencedirect.com/science/article/abs/pii/S1566253525006979) |
| 2025-07-19 | Feed-Forward Reconstruction, View Synthesis, Survey | NUS | [Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501) | arXiv | [project](https://fnzhan.com/3D-Reconstruction-and-Generation-Survey/) |
| 2025-07-15 | 4D Spatial Intelligence, 5-Level Framework, Survey | NTU / HKUST | [Reconstructing 4D Spatial Intelligence: A Survey](https://arxiv.org/abs/2507.21045) | arXiv | [project](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence) |
| 2025-06-01 | 3DGS, Robotics, Scene Understanding, Survey | Multiple | [3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262) | arXiv | [project](https://github.com/dtc111111/awesome-3dgs-for-robotics) |
| 2025-05-20 | Dynamic Scene, Radiance Field, NeRF to 3DGS (200+ papers) | USTC | [Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049) | arXiv | [project](https://github.com/MiliLab/Awesome-DynRF) |
| 2025-05-15 | World Models, Embodied AI, Comprehensive Survey | Tsinghua | [A Comprehensive Survey of Embodied World Models](https://arxiv.org/abs/2506.08518) | arXiv | [project](https://github.com/tsinghua-fib-lab/Awesome-Embodied-World-Model) |
| 2025-05-10 | 3D Scene Generation, 300+ Papers, Survey | NTU | [3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474) | arXiv | [project](https://github.com/hzxie/Awesome-3D-Scene-Generation) |
| 2025-02-05 | 3D-LLM, Multimodal, Scene Understanding, Survey | Multiple | [When LLMs Step into the 3D World: A Survey and Meta-Analysis of 3D Tasks via MLLMs](https://arxiv.org/abs/2405.10255) | arXiv | [project](https://github.com/ActiveVisionLab/Awesome-LLM-3D) |
| 2025-01-07 | 3D Generation, Survey, Diffusion | Tsinghua | [A Survey on 3D Generative Models](https://arxiv.org/abs/2406.15647) | arXiv | [paper](https://arxiv.org/abs/2406.15647) |
| 2024-11-21 | Gaussian Splatting, Survey, Rendering | Zhejiang University | [A Survey on 3D Gaussian Splatting](https://arxiv.org/abs/2401.03890) | arXiv | [paper](https://arxiv.org/abs/2401.03890) |
| 2024-04-12 | Embodied AI, Simulators, Benchmarks | University of Adelaide | [A Survey on Embodied AI: From Simulators to Research Tasks](https://arxiv.org/abs/2103.04918) | TPAMI 2024 | [paper](https://arxiv.org/abs/2103.04918) |

<a id="62-datasets-for-3d-reconstruction"></a>

### 6.2 Datasets for 3D Reconstruction

#### 6.2.1 Sparse View & Multi-View Stereo (MVS)

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2023-10-10 | Outdoor Scenes, NeRF, Real Captures | UC Berkeley | [Mip-NeRF 360 Dataset](https://jonbarron.info/mipnerf360/) | Dataset | [project](https://jonbarron.info/mipnerf360/) |
| 2020-08-18 | Object-Centric, Real Images, NeRF | Google Research | [Nerf Synthetic and LLFF Datasets](https://www.matthewtancik.com/nerf) | Dataset | [project](https://www.matthewtancik.com/nerf) |
| 2017-08-10 | MVS, Large-Scale, Benchmark | Princeton / Intel | [Tanks and Temples](https://www.tanksandtemples.org/) | TOG 2017 | [benchmark](https://www.tanksandtemples.org/) |
| 2014-10-24 | MVS, Controlled Capture, DTU | Technical University of Denmark | [DTU Robot Image Dataset](https://roboimagedata.compute.dtu.dk/) | IJCV 2014 | [dataset](https://roboimagedata.compute.dtu.dk/) |

#### 6.2.2 Dense View & Streaming Sequences

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-01-13 | Object-Centric Video, Full-360, Depth, Sparse Point Cloud | Meta AI | [uCO3D: UnCommon Objects in 3D](https://arxiv.org/abs/2501.07574) | arXiv | [github](https://github.com/facebookresearch/uco3d) |
| 2024-12-02 | Real Objects, 360 Views, Masks, Dense Point Clouds | CUHK-Shenzhen | [MVImgNet2.0: A Larger-scale Dataset of Multi-view Images](https://arxiv.org/abs/2412.01430) | arXiv | [project](https://luyues.github.io/mvimgnet2/) |
| 2024-01-05 | Dynamic Scenes, Multi-View Video, 4D | University of Oxford | [PanopticSports](https://github.com/JonathonLuiten/Dynamic3DGaussians) | Dataset | [github](https://github.com/JonathonLuiten/Dynamic3DGaussians) |
| 2023-12-26 | Real-World Videos, Camera Poses, Scene Complexity | Purdue University | [DL3DV-10K: A Large-Scale Scene Dataset for Deep Learning-based 3D Vision](https://arxiv.org/abs/2312.16256) | CVPR 2024 | [github](https://github.com/DL3DV-10K/Dataset) / [project](https://dl3dv-10k.github.io/DL3DV-10K/) |
| 2023-06-14 | Object-Centric Casual Captures, GT Shape, GT Poses | University of Oxford | [NAVI: Category-Agnostic Image Collections with High-Quality 3D Shape and Pose Annotations](https://arxiv.org/abs/2306.09109) | NeurIPS 2023 | [project](https://navidataset.github.io/) |
| 2023-06-06 | Indoor RGB-D, Habitat, 3D Scenes | Meta AI | [Habitat-Matterport 3D Semantics Dataset](https://aihabitat.org/datasets/hm3d/) | Dataset | [dataset](https://aihabitat.org/datasets/hm3d/) |
| 2023-03-10 | Real Object Videos, Masks, Camera Parameters, Point Clouds | CUHK-Shenzhen | [MVImgNet: A Large-scale Dataset of Multi-view Images](https://arxiv.org/abs/2303.06042) | CVPR 2023 | [github](https://github.com/GAP-LAB-CUHK-SZ/MVImgNet) |
| 2021-09-01 | Object-Centric Videos, Camera Poses, Point Clouds | Meta AI | [Common Objects in 3D: Large-Scale Learning and Evaluation of Real-life 3D Category Reconstruction](https://arxiv.org/abs/2109.00512) | ICCV 2021 | [github](https://github.com/facebookresearch/co3d) |
| 2020-12-18 | Object-Centric AR Videos, Camera Poses, 3D Boxes | Google Research | [Objectron: A Large Scale Dataset of Object-Centric Videos in the Wild with Pose Annotations](https://arxiv.org/abs/2012.09988) | CVPR 2021 | [github](https://github.com/google-research-datasets/Objectron) |
| 2017-07-26 | Indoor RGB-D, Semantic Labels, Reconstruction | Stanford | [ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes](http://www.scan-net.org/) | CVPR 2017 | [dataset](http://www.scan-net.org/) |
| 2012-06-18 | Indoor RGB-D, NYUv2, Semantics | NYU | [NYU Depth Dataset V2](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html) | ECCV 2012 | [dataset](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html) |

<a id="63-datasets-for-3d-generation"></a>

### 6.3 Datasets for 3D Generation

#### 6.3.1 Object-Level 3D/Text-to-3D

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-01-13 | Uncommon Objects, Videos, Depth, 3D Annotations | Meta AI | [uCO3D: UnCommon Objects in 3D](https://arxiv.org/abs/2501.07574) | arXiv | [github](https://github.com/facebookresearch/uco3d) |
| 2024-12-02 | Real Objects, 360 Coverage, Dense Point Clouds | CUHK-Shenzhen | [MVImgNet2.0](https://arxiv.org/abs/2412.01430) | arXiv | [project](https://luyues.github.io/mvimgnet2/) |
| 2023-07-10 | 3D Objects, Web-Scale, Textured Mesh | Allen Institute for AI | [Objaverse-XL: A Universe of 10M+ 3D Objects](https://arxiv.org/abs/2307.05663) | NeurIPS 2023 | [dataset](https://objaverse.allenai.org/) |
| 2023-06-14 | Casual Image Collections, GT Mesh, GT Camera Poses | University of Oxford | [NAVI](https://arxiv.org/abs/2306.09109) | NeurIPS 2023 | [project](https://navidataset.github.io/) |
| 2023-03-10 | Real Object Videos, Multi-View Images, Point Clouds | CUHK-Shenzhen | [MVImgNet](https://arxiv.org/abs/2303.06042) | CVPR 2023 | [github](https://github.com/GAP-LAB-CUHK-SZ/MVImgNet) |
| 2023-01-18 | Real Scans, Multi-View Images, Videos, Meshes | Shanghai AI Lab | [OmniObject3D: Large-Vocabulary 3D Object Dataset for Realistic Perception, Reconstruction and Generation](https://arxiv.org/abs/2301.07525) | CVPR 2023 | [project](https://omniobject3d.github.io/) |
| 2022-12-13 | 3D Objects, LVIS Annotations, Web-Scale | Allen Institute for AI | [Objaverse: A Universe of Annotated 3D Objects](https://arxiv.org/abs/2212.08051) | CVPR 2023 | [dataset](https://objaverse.allenai.org/) |
| 2022-06-24 | Object-Centric Multi-View, Mesh, Depth, Masks | Meta AI / Amazon | [HM3D-ABO: A Photo-realistic Dataset for Object-centric Multi-view 3D Reconstruction](https://arxiv.org/abs/2206.12356) | arXiv | [paper](https://arxiv.org/abs/2206.12356) |
| 2021-10-12 | Product Objects, 3D Models, Multi-View Images | Amazon / UC Berkeley | [ABO: Dataset and Benchmarks for Real-World 3D Object Understanding](https://arxiv.org/abs/2110.06199) | CVPR 2022 | [project](https://amazon-berkeley-objects.s3.amazonaws.com/index.html) |
| 2021-09-16 | Real Scanned Objects, Simulation Assets | Google Research | [Google Scanned Objects](https://app.gazebosim.org/GoogleResearch/fuel/collections/Scanned%20Objects%20by%20Google%20Research) | ICRA 2022 | [dataset](https://app.gazebosim.org/GoogleResearch/fuel/collections/Scanned%20Objects%20by%20Google%20Research) |
| 2021-09-01 | Real Object Videos, Camera Poses, Point Clouds | Meta AI | [CO3D: Common Objects in 3D](https://arxiv.org/abs/2109.00512) | ICCV 2021 | [github](https://github.com/facebookresearch/co3d) |
| 2020-12-18 | Object-Centric Videos, AR Poses, 3D Boxes | Google Research | [Objectron](https://arxiv.org/abs/2012.09988) | CVPR 2021 | [github](https://github.com/google-research-datasets/Objectron) |
| 2015-12-09 | CAD Models, Object Categories, ShapeNet | Stanford | [ShapeNet: An Information-Rich 3D Model Repository](https://shapenet.org/) | arXiv | [dataset](https://shapenet.org/) |

#### 6.3.2 Human & Articulated Objects

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2023-03-08 | Articulated Objects, Mobility, Simulation | UC San Diego | [PartNet-Mobility](https://sapien.ucsd.edu/browse) | Dataset | [dataset](https://sapien.ucsd.edu/browse) |
| 2022-02-07 | Articulated Objects, Manipulation, Interactive | Stanford | [BEHAVIOR-1K](https://behavior.stanford.edu/) | CoRL 2022 | [dataset](https://behavior.stanford.edu/) |
| 2019-06-21 | Part Segmentation, Shape Structure, PartNet | Stanford | [PartNet: A Large-Scale Benchmark for Fine-Grained and Hierarchical Part-Level 3D Object Understanding](https://arxiv.org/abs/1812.02713) | CVPR 2019 | [dataset](https://partnet.cs.stanford.edu/) |

#### 6.3.3 Procedural & Synthetic Scenes

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-10-17 | Procedural Indoor Scenes, Blender, Synthetic Data | Princeton | [Infinigen Indoors](https://infinigen.org/) | NeurIPS 2024 | [github](https://github.com/princeton-vl/infinigen) |
| 2023-11-15 | Procedural Worlds, Natural Scenes, Synthetic Data | Princeton | [Infinigen](https://infinigen.org/) | CVPR 2023 | [github](https://github.com/princeton-vl/infinigen) |
| 2022-06-14 | Indoor Scenes, Procedural, Embodied AI | Allen Institute for AI | [ProcTHOR](https://procthor.allenai.org/) | NeurIPS 2022 | [project](https://procthor.allenai.org/) |
| 2021-06-25 | Embodied AI, Realistic Indoor Scenes | Meta AI | [Habitat 2.0](https://aihabitat.org/) | NeurIPS 2021 | [github](https://github.com/facebookresearch/habitat-lab) |

<a id="64-specific-benchmarks--metrics"></a>

### 6.4 Specific Benchmarks & Metrics

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-04-25 | 3D Generation, Fine-Grained Evaluation, Asset Quality | MIT | [Eval3D: Interpretable and Fine-grained Evaluation for 3D Generation](https://arxiv.org/abs/2504.18509) | CVPR 2025 | [project](https://eval3d.github.io/) / [github](https://github.com/eval3d/eval3d-codebase) |
| 2024-12-12 | Image-to-3D, Evaluation, Asset Quality | University of Oxford | [GSO / OmniObject3D Evaluation Protocols](https://omniobject3d.github.io/) | Dataset | [dataset](https://omniobject3d.github.io/) |
| 2024-06-07 | Reconstruction, Geometry, Feed-Forward | NAVER Labs | [DUSt3R Evaluation Suite](https://github.com/naver/dust3r) | GitHub | [github](https://github.com/naver/dust3r) |
| 2023-10-04 | Text-to-3D, Benchmark, Multi-View Metrics | Tsinghua | [T3Bench: Benchmarking Current Progress in Text-to-3D Generation](https://arxiv.org/abs/2310.02977) | arXiv | [project](https://t3bench.com/) |
| 2017-08-10 | MVS Benchmark, Mesh Accuracy, Completeness | Princeton / Intel | [Tanks and Temples Benchmark](https://www.tanksandtemples.org/) | TOG 2017 | [benchmark](https://www.tanksandtemples.org/) |

<a id="65-simulators--toolchains"></a>

### 6.5 Simulators & Toolchains

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-05-20 | Robot Learning, Simulation, Isaac Lab | NVIDIA | [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) | GitHub | [github](https://github.com/isaac-sim/IsaacLab) |
| 2023-10-26 | Simulation, Asset Generation, Manipulation | NVIDIA | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](https://arxiv.org/abs/2310.17596) | CoRL 2023 | [github](https://github.com/NVlabs/mimicgen_environments) |
| 2023-02-03 | Robotics Simulation, Digital Twin, USD | NVIDIA | [Isaac Sim](https://developer.nvidia.com/isaac/sim) | Software | [docs](https://docs.isaacsim.omniverse.nvidia.com/) |
| 2021-10-18 | Robotics Simulator, Articulated Objects, SAPIEN | UC San Diego | [SAPIEN: A SimulAted Part-based Interactive ENvironment](https://sapien.ucsd.edu/) | CVPR 2020 | [github](https://github.com/haosulab/SAPIEN) |
| 2021-05-11 | Physics Engine, Robotics, Differentiable Simulation | DeepMind | [MuJoCo](https://mujoco.org/) | Software | [github](https://github.com/google-deepmind/mujoco) |
| 2019-06-14 | Embodied AI, Navigation, Simulation | Meta AI | [Habitat: A Platform for Embodied AI Research](https://aihabitat.org/) | ICCV 2019 | [github](https://github.com/facebookresearch/habitat-lab) |

## Acknowledgement

This repository is inspired by and complementary to:
- [Awesome-3D-Reconstruction-and-Generation](https://github.com/PolySummit/Awesome-3D-Reconstruction-and-Generation)
- [Awesome-3D-Generation](https://github.com/BunnySoCrazy/Awesome-3D-Generation)
- [awesome-3d-diffusion](https://github.com/cwchenwang/awesome-3d-diffusion)
- [Awesome-UMI](https://github.com/chang-xinhai/Awesome-UMI)
- [Awesome-Dexterous-Manipulation](https://github.com/chang-xinhai/Awesome-Dexterous-Manipulation)

## Citation

If this repository helps your research, please cite or star the GitHub repository.

```bibtex
@misc{awesome_embodied_3dv,
  title = {Awesome-Embodied-3DV},
  author = {Chang, Xinhai},
  year = {2026},
  howpublished = {\url{https://github.com/chang-xinhai/Awesome-Embodied-3DV}}
}
```
