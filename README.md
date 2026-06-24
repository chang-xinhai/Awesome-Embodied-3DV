<div align="center">

<h1 id="awesome-embodied-3dv">Awesome-Embodied-3DV</h1>

<p>
  <strong>A curated map of 3D/4D perception, reconstruction, generation, simulation-ready assets, and world models for embodied AI.</strong>
</p>

<!-- [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) -->
<!-- [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) -->

<p>
  <a href="#-1-data-perception"><img alt="Perception" src="https://img.shields.io/badge/3D-Perception-a8d8ff?style=for-the-badge"></a>
  <a href="#-2-3d4d-representation"><img alt="Representation" src="https://img.shields.io/badge/3D%2F4D-Representation-b8e6c9?style=for-the-badge"></a>
  <a href="#-3-3d-reconstruction"><img alt="Reconstruction" src="https://img.shields.io/badge/3D-Reconstruction-ffd6a5?style=for-the-badge"></a>
  <a href="#-4-3d-generation"><img alt="Generation" src="https://img.shields.io/badge/3D-Generation-d7c5ff?style=for-the-badge"></a>
  <a href="#-5-embodiment--world-models"><img alt="Embodiment" src="https://img.shields.io/badge/Embodied-3D-c7f9cc?style=for-the-badge"></a>
  <a href="#-6-datasets-benchmarks--infrastructure"><img alt="Infrastructure" src="https://img.shields.io/badge/Benchmarks-Infrastructure-ffb7b2?style=for-the-badge"></a>
</p>

</div>

## About

**Awesome-Embodied-3DV** is a curated list for the research space where **3D vision, 3D/4D reconstruction, 3D generation, simulation-ready assets, and embodied world models** meet.

This repository focuses on:
- **Data Perception**: depth, normals, active imaging, panoramic/fisheye, dense mapping, and 3D semantic understanding (detection, segmentation, grounding) that feed downstream systems
- **3D/4D Representation**: 3DGS, 4DGS, NeRF/SDF, mesh, voxel, point, and hybrid structures
- **3D Reconstruction**: offline, feed-forward, streaming, online, semantic, instance-level, and dynamic reconstruction
- **3D Generation**: object-level, part-level, articulated, scene-level, editable, and simulation-ready asset generation
- **Embodiment & World Models**: reconstruction-based world models, dynamic scene graphs, physical interaction & affordance, human-centric 3D, robotics integration, and agent-facing 3D grounding
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
| Build articulated objects | [ArtGS](https://arxiv.org/abs/2502.19459), [Articulate Anything](https://openreview.net/forum?id=6akuzEqP38), [URDF-Anything](https://openreview.net/forum?id=g3EF5XsapH), [URDF-Anything+](https://arxiv.org/abs/2603.14010), [PartNet-Mobility](https://sapien.ucsd.edu/browse) |
| Pick datasets and benchmarks | [ScanNet](http://www.scan-net.org/), [Tanks and Temples](https://www.tanksandtemples.org/), [DTU](https://roboimagedata.compute.dtu.dk/), [Objaverse](https://objaverse.allenai.org/), [GSO](https://app.gazebosim.org/GoogleResearch/fuel/collections/Scanned%20Objects%20by%20Google%20Research), [HM3D](https://aihabitat.org/datasets/hm3d/) |

## News

- [2026-06-15] Added a dedicated **3D Editing** taxonomy under 3D Generation, covering object-level, scene-level, and dynamic / 4D editing methods.
- [2026-04-30] Initialized **Awesome-Embodied-3DV** with a six-part taxonomy for data perception, representations, reconstruction, generation, embodied world models, and infrastructure.
- [2026-04-30] Added `AGENTS.md` to define curation scope, metadata rules, and maintenance workflow.

## Contents

- [Awesome-Embodied-3DV](#awesome-embodied-3dv)
  - [About](#about)
  - [Must Read](#must-read)
  - [News](#news)
  - [Data Perception](#-1-data-perception)
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
    - [3D Editing](#44-3d-editing)
  - [Embodiment & World Models](#-5-embodiment--world-models)
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

<h2 id="-1-data-perception">📡 1. Data Perception</h2>

Data perception covers the sensor-facing and semantic layers: extracting geometric priors (depth, normals), understanding 3D semantics (detection, segmentation, grounding), active-imaging signals, and dense maps from 2D images, video, or physical sensors.

<a id="11-geometric-priors"></a>

### 1.1 Geometric Priors

#### 1.1.1 Monocular High-Fidelity Depth

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-05-15 | VLM, Dense Metric Depth, Spatial Reasoning | Zhejiang Univ | [Unlocking Dense Metric Depth Estimation in VLMs](https://arxiv.org/abs/2605.15876) | arXiv | [project](https://depthvlm.github.io/) / [github](https://github.com/hanxunyu/DepthVLM) |
| 2026-01-06 | Arbitrary-Resolution, Neural Implicit, Fine Details | Zhejiang Univ | [InfiniDepth: Arbitrary-Resolution and Fine-Grained Depth Estimation with Neural Implicit Fields](https://arxiv.org/abs/2601.03252) | CVPR 2026 | [project](https://zju3dv.github.io/InfiniDepth/) / [github](https://github.com/zju3dv/InfiniDepth) |
| 2025-12-13 | Defocus Cue, Bokeh Stack, Metric Depth | Nanyang Tech Univ | [Boosting Monocular Metric Depth Estimation via Bokeh Rendering](https://arxiv.org/abs/2512.12425) | ICML 2026 | [project](https://fogradio.github.io/BokehDepth_Project/) / [github](https://github.com/fogradio/BokehDepth) |
| 2025-11-30 | Deterministic Diffusion, Dense Geometry, Fine Details | HKUST(GZ) | [Lotus-2: Advancing Geometric Dense Prediction with Powerful Image Generative Model](https://arxiv.org/abs/2512.01030) | arXiv | [project](https://lotus-2.github.io/) / [github](https://github.com/EnVision-Research/Lotus-2) |
| 2025-11-13 | Any-View Depth, Metric Geometry, Multi-View | ByteDance | [Depth Anything 3: Recovering the Visual Space from Any Views](https://arxiv.org/abs/2511.10647) | ICLR 2026 | [project](https://depth-anything-3.github.io/) / [github](https://github.com/ByteDance-Seed/depth-anything-3) |
| 2025-10-08 | Pixel-Space Diffusion, Flying-Pixel-Free, Point Clouds | HUST | [Pixel-Perfect Depth with Semantics-Prompted Diffusion Transformers](https://arxiv.org/abs/2510.07316) | NeurIPS 2025 | [project](https://pixel-perfect-depth.github.io/) / [github](https://github.com/gangweix/pixel-perfect-depth) |
| 2025-09-29 | VLM, Metric Depth, Sparse Supervision | Meta AI | [DepthLM: Metric Depth From Vision Language Models](https://arxiv.org/abs/2509.25413) | ICLR 2026 Oral | [github](https://github.com/facebookresearch/DepthLM_Official) |
| 2025-07-03 | Monocular Geometry, Metric Scale, Sharp Details | USTC / Microsoft | [MoGe-2: Accurate Monocular Geometry with Metric Scale and Sharp Details](https://arxiv.org/abs/2507.02546) | NeurIPS 2025 | [project](https://wangrc.site/MoGe2Page/) / [github](https://github.com/microsoft/MoGe) |
| 2025-04-16 | Sliding Anchor, Unknown Intrinsics, Metric Scale | Shanghai Univ | [Metric-Solver: Sliding Anchored Metric Depth Estimation from a Single Image](https://arxiv.org/abs/2504.12103) | arXiv | [project](https://tele-ai.github.io/MetricSolver/) / [github](https://github.com/Tele-AI/MetricSolver) |
| 2025-02-27 | Metric 3D Points, Self-Prompt Camera, Uncertainty | ETH Zurich | [UniDepthV2: Universal Monocular Metric Depth Estimation Made Simpler](https://arxiv.org/abs/2502.20110) | TPAMI 2026 | [github](https://github.com/lpiccinelli-eth/UniDepth) |
| 2024-11-27 | Diffusion Distillation, Metric + Sharp, Boundary Detail | Qualcomm AI Research | [SharpDepth: Sharpening Metric Depth Predictions Using Diffusion Distillation](https://arxiv.org/abs/2411.18229) | CVPR 2025 | [project](https://sharpdepth.github.io/) / [github](https://github.com/Qualcomm-AI-research/SharpDepth) |
| 2024-10-01 | Metric Depth, Zero-Shot, Image Priors | Apple | [Depth Pro: Sharp Monocular Metric Depth in Less Than a Second](https://arxiv.org/abs/2410.02073) | ICLR 2025 | [github](https://github.com/apple/ml-depth-pro) |
| 2024-09-26 | Diffusion, Single-Step, Dense Geometry | HKUST(GZ) | [Lotus: Diffusion-based Visual Foundation Model for High-quality Dense Prediction](https://arxiv.org/abs/2409.18124) | ICLR 2025 | [project](https://lotus3d.github.io/) / [github](https://github.com/EnVision-Research/Lotus) |
| 2024-06-14 | Monocular Depth, Foundation Model, Metric Depth | TikTok / HKU | [Depth Anything V2](https://arxiv.org/abs/2406.09414) | NeurIPS 2024 | [project](https://depth-anything-v2.github.io/) / [github](https://github.com/DepthAnything/Depth-Anything-V2) |
| 2024-06-05 | Metric Depth, Universal, Zero-Shot | ETH Zurich | [UniDepth: Universal Monocular Metric Depth Estimation](https://arxiv.org/abs/2403.18913) | CVPR 2024 | [github](https://github.com/lpiccinelli-eth/unidepth) |
| 2023-12-22 | Monocular Depth, Relative Depth, Foundation Model | TikTok / HKU | [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891) | CVPR 2024 | [project](https://depth-anything.github.io/) |
| 2023-07-01 | Metric 3D, Zero-Shot, Canonical Space | Alibaba | [Metric3D: Towards Zero-shot Metric 3D Prediction from A Single Image](https://arxiv.org/abs/2307.10984) | ICCV 2023 | [github](https://github.com/YvanYin/Metric3D) |
| 2023-04-24 | Monocular Depth, Zero-Shot, Affine-Invariant | Intel Labs | [Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](https://arxiv.org/abs/2312.02145) | CVPR 2024 | [project](https://marigoldmonodepth.github.io/) |
| 2021-03 | ViT, Dense Prediction, Foundation, Depth | Intel Labs | [DPT: Vision Transformers for Dense Prediction](https://arxiv.org/abs/2103.13413) | ICCV 2021 | [github](https://github.com/isl-org/DPT) |
| 2019-07 | Robust Depth, Zero-Shot, Cross-Dataset, MiDaS | Intel Labs | [MiDaS: Towards Robust Monocular Depth Estimation](https://arxiv.org/abs/1907.01341) | TPAMI 2022 | [github](https://github.com/isl-org/MiDaS) |

#### 1.1.2 Geometric Consistency Prior

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-07-22 | Foundation Model, Depth/Normal/Pointmap, Multi-View | SJTU | [Dens3R: A Foundation Model for 3D Geometry Prediction](https://arxiv.org/abs/2507.16290) | ICLR 2026 | [paper](https://arxiv.org/abs/2507.16290) |
| 2025-05-20 | Scalable Depth, Autoregressive, 2B Parameters | Baidu | [DAR: Scalable Autoregressive Monocular Depth Estimation](https://arxiv.org/abs/2503.17310) | CVPR 2025 | [project](https://depth-ar.github.io/) |
| 2025-04-15 | Panoramic / Fisheye Depth, Zero-Shot Metric | Intel | [Depth Any Camera: Zero-Shot Metric Depth from Any Camera](https://arxiv.org/abs/2412.08204) | CVPR 2025 | [project](https://depth-any-camera.github.io/) |
| 2025-03-18 | Metric 3D, Multi-Task, Geometry Foundation | Shanghai AI Lab | [Metric3D v2: A Versatile Monocular Geometric Foundation Model](https://arxiv.org/abs/2404.15506) | TPAMI 2025 | [project](https://jugghm.github.io/Metric3Dv2/) |
| 2025-03-01 | Monocular Geometry, Pointmap, Affine-Invariant | USTC / Microsoft | [MoGe: Unlocking Accurate Monocular Geometry Estimation for Open-Domain Images](https://arxiv.org/abs/2410.19115) | CVPR 2025 Oral | [github](https://github.com/microsoft/MoGe) |
| 2025-03 | LiDAR Surface Normal, Dataset, Point Cloud | TU Graz | [LiSu: A Dataset and Method for LiDAR Surface Normal Estimation](https://arxiv.org/abs/2503.08601) | CVPR 2025 | [github](https://github.com/malicd/LiSu) |
| 2025-01-01 | Universal Camera, Spherical 3D, Any Camera | ETH Zurich | [UniK3D: Universal Camera Monocular 3D Estimation](https://openreview.net/forum?id=UGOKG9iD3R) | CVPR 2025 | [github](https://github.com/lpiccinelli-eth/UniK3D) |
| 2025-01 | Stereo, Foundation Model, RAFT-Style, Zero-Shot | NVIDIA | [FoundationStereo: Zero-Shot Stereo Matching](https://arxiv.org/abs/2501.09898) | CVPR 2025 Oral / Best Paper Nomination | [github](https://github.com/NVlabs/FoundationStereo) |
| 2025-01 | Stereo, Robust, Zero-Shot, Non-Lambertian | Univ of Bologna | [Stereo Anywhere: Robust Zero-Shot Deep Stereo Matching](https://arxiv.org/abs/2501.09958) | CVPR 2025 | [project](https://stereoanywhere.github.io/) |
| 2024-10-02 | Normal Estimation, 3D Priors, Surface Geometry | Nvidia | [StableNormal: Reducing Diffusion Variance for Stable and Sharp Normal](https://arxiv.org/abs/2406.16864) | SIGGRAPH Asia 2024 | [project](https://stable-x.github.io/StableNormal/) |
| 2024-07 | Surface Normals, Foundation Model, Video, Temporal | Authors | [NormalCrafter: Learning Temporally Consistent Normals from Video Diffusion Priors](https://openaccess.thecvf.com/content/ICCV2025/html/Bin_NormalCrafter_Learning_Temporally_Consistent_Normals_from_Video_Diffusion_Priors_ICCV_2025_paper.html) | ICCV 2025 | [project](https://normalcrafter.github.io/) |
| 2024-03-19 | High-Res, Patch-Wise, Model-Agnostic | KAUST | [PatchFusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth](https://arxiv.org/abs/2312.02240) | CVPR 2024 | [project](https://patchfusion.github.io/) |
| 2024-03 | Inductive Biases, Surface Normal, Oral | Imperial College London | [DSINE: Rethinking Inductive Biases for Surface Normal Estimation](https://arxiv.org/abs/2403.00712) | CVPR 2024 Oral | [github](https://github.com/baegwangbin/DSINE) |
| 2024-03 | Diffusion, Effective Conditioning, ViT Priors | IIT Delhi | [ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth](https://arxiv.org/abs/2403.18807) | CVPR 2024 | [github](https://github.com/Aradhye2002/EcoDepth) |
| 2023-12-08 | Geometry, Normals, Depth, Multi-Task | Apple | [GeoWizard: Unleashing the Diffusion Priors for 3D Geometry Estimation from a Single Image](https://arxiv.org/abs/2403.12013) | ECCV 2024 | [project](https://fuxiao0719.github.io/projects/geowizard/) |
| 2023-09 | Iterative Bins, Elastic, GRU, Classification-Regression | Beihang Univ | [IEBins: Iterative Elastic Bins for Monocular Depth Estimation](https://arxiv.org/abs/2309.14137) | NeurIPS 2023 | [github](https://github.com/ShuweiShao/IEBins) |
| 2023-04 | Internal Discretization, Continuous-Discrete, Depth | ETH Zurich | [iDisc: Internal Discretization for Monocular Depth Estimation](https://arxiv.org/abs/2304.06334) | CVPR 2023 | [github](https://github.com/SysCV/idisc) |

<a id="12-3d-semantic-understanding"></a>

### 1.2 3D Semantic Understanding

#### 1.2.1 Open-Vocabulary 3D Segmentation & Grounding

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Open-Vocabulary BEV, 3DGS, Geometric Constraints | KAIST AI | [Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353) | ECCV 2026 | [paper](https://arxiv.org/abs/2606.24353) |
| 2026-06-04 | Open-Vocabulary, Functionality Segmentation, Robotics | Authors | [T-FunS3D: Task-Driven Hierarchical Open-Vocabulary 3D Functionality Segmentation](https://arxiv.org/abs/2606.05975) | arXiv | [paper](https://arxiv.org/abs/2606.05975) |
| 2026-05-07 | Open-Vocabulary, Gaussian Feature Field, Codebook | TU Munich / Google | [OpenGaFF: Open-Vocabulary Gaussian Feature Field with Codebook Attention](https://arxiv.org/abs/2605.06088) | arXiv | [paper](https://arxiv.org/abs/2605.06088) |
| 2026-01-01 | Open-Vocabulary, SAM3, Promptable, DETR | Meta | [SAM 3: Segment Anything with Concepts](https://github.com/facebookresearch/sam3) | ICLR 2026 | [github](https://github.com/facebookresearch/sam3) |
| 2025-07-10 | Open-Vocabulary, Dual-Level Contrastive, Instance-Aware | BIGAI / Tsinghua | [MPEC: Masked Point-Entity Contrast for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2504.02238) | CVPR 2025 | [project](https://mpec-3d.github.io/) |
| 2025-06-15 | Panoptic, Open-Vocabulary, 3D Gaussian Splatting | NUS | [PanoGS: Gaussian-based Panoptic Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2501.02007) | CVPR 2025 | [project](https://panogs.github.io/) |
| 2025-06-01 | Open-Vocabulary, Foundation Dataset, Mask-Text Pairs | NVIDIA | [Mosaic3D: Foundation Dataset and Model for Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2501.10369) | CVPR 2025 | [github](https://github.com/NVlabs/Mosaic3D) |
| 2025-03-19 | SAM-2, 3D Tracking, Dynamic Programming | VinAI | [Any3DIS: Open-Vocabulary 3D Instance Segmentation with SAM-2](https://arxiv.org/abs/2503.15486) | CVPR 2025 | [paper](https://arxiv.org/abs/2503.15486) |
| 2025-03-12 | Functional 3D, CoT, VLM, Training-Free, Highlight | Authors | [Fun3DU: Functional 3D Scene Understanding via Chain-of-Thought](https://arxiv.org/abs/2503.09433) | CVPR 2025 Highlight | [paper](https://arxiv.org/abs/2503.09433) |
| 2025-03-01 | Open-Vocabulary, LLM Canonical, Part Segmentation | Shandong Univ / Tencent | [CoSMo3D: Open-World Promptable 3D Semantic Part Segmentation via LLM-Guided Canonical Spatial Modeling](https://arxiv.org/abs/2503.10278) | CVPR 2026 Oral | [github](https://github.com/JinLi998/CoSMo3D) |
| 2025-03-01 | Training-Free, MLLM Caption, Voxel Grouping | NVIDIA Research Taiwan | [OpenVoxel: Training-Free Grouping and Captioning Voxels for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2503.17600) | CVPR 2026 | [project](https://research.nvidia.com/labs/twn/publication/cvpr_2026_openvoxel/) |
| 2024-12-18 | Open-Vocabulary 3DGS, Segmentation, Language | ETH Zurich | [LangSplat: 3D Language Gaussian Splatting](https://arxiv.org/abs/2312.16084) | CVPR 2024 Highlight | [project](https://langsplat.github.io/) / [github](https://github.com/minghanqin/LangSplat) |
| 2024-07-12 | Region-Level, Point-Language Contrastive, Multi-VLM | HKU | [RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding](https://arxiv.org/abs/2404.00962) | CVPR 2024 | [project](https://regionplc.github.io/) / [github](https://github.com/CVMI-Lab/RegionPLC) |
| 2024-07-02 | Open-Vocabulary, Mask-Snap-Lookup, Indoor/Outdoor | HKUST | [OpenIns3D: Open-Vocabulary 3D Segmentation with Mask-Snap-Lookup](https://arxiv.org/abs/2407.01987) | ECCV 2024 | [github](https://github.com/OpenIns3D/OpenIns3D) |
| 2024-05-15 | Open-Vocabulary, 3D Scene, Language Field | UC Berkeley | [LERF: Language Embedded Radiance Fields](https://arxiv.org/abs/2303.09553) | ICCV 2023 | [project](https://lerf.io/) / [github](https://github.com/kerrj/lerf) |
| 2024-04-01 | Zero-Shot, Superpoint, SAM, Scene Graph | PKU | [SAI3D: Zero-Shot 3D Instance Segmentation by Scene-Aware Incremental Merging](https://arxiv.org/abs/2403.06347) | CVPR 2024 | [github](https://github.com/yinmolin/SAI3D) |
| 2024-03-28 | Segment Anything 3D, Point Cloud, Interactive | VAST AI | [SAM3D: Segment Anything in 3D Scenes](https://arxiv.org/abs/2306.03908) | CVPR 2024 | [github](https://github.com/Pointcept/SegmentAnything3D) |
| 2024-03-19 | Open-Vocabulary, MLLM, Point-Entity-Text, nuScenes | MPI | [OV3D: Open-Vocabulary 3D Understanding with Multi-Modal Alignment](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_OV3D_Open-Vocabulary_3D_Understanding_Multi-Modal_Alignment_CVPR_2024_paper.html) | CVPR 2024 | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_OV3D_Open-Vocabulary_3D_Understanding_Multi-Modal_Alignment_CVPR_2024_paper.html) |
| 2024-03-19 | 2D-Guided, 3D Proposals, SAM, Instance | VinAI / IBM | [Open3DIS: Open-Vocabulary 3D Instance Segmentation with 2D-Guided Mask Generation](https://arxiv.org/abs/2403.12382) | CVPR 2024 | [github](https://github.com/VinAIResearch/Open3DIS) |
| 2024-03-15 | Training-Free, View-Consensus, Instance | PKU | [MaskClustering: View-Consensus for 3D Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Yan_MaskClustering_View-Consensus_for_3D_Instance_Segmentation_CVPR_2024_paper.html) | CVPR 2024 | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Yan_MaskClustering_View-Consensus_for_3D_Instance_Segmentation_CVPR_2024_paper.html) |
| 2024-01-19 | Segment Anything, 3D Gaussians, Interactive | Zhejiang University | [SAGD: Boundary-Enhanced Segment Anything in 3D Gaussians](https://arxiv.org/abs/2401.17857) | arXiv | [github](https://github.com/XuHu0529/SAGS) |
| 2024-01-04 | 2D+3D Unified, Single Model, Highlight | Authors | [ODIN: A Single Model for 2D and 3D Segmentation](https://arxiv.org/abs/2401.02416) | CVPR 2024 Highlight | [github](https://github.com/sssoy/odin) |
| 2023-12-05 | Open-Vocabulary 3D, Point Cloud, Segmentation | ETH Zurich | [OpenScene: 3D Scene Understanding with Open Vocabularies](https://arxiv.org/abs/2211.15654) | CVPR 2023 | [project](https://pengsongyou.github.io/openscene) / [github](https://github.com/pengsongyou/openscene) |
| 2023-11-17 | Unified, Semantic+Instance+Panoptic, Single Transformer | Samsung | [OneFormer3D: One Transformer for Unified 3D Segmentation](https://arxiv.org/abs/2311.10244) | CVPR 2024 | [github](https://github.com/Ailman/oneformer3d) |
| 2023-06-23 | Open-Vocabulary 3D Instance, Mask Proposals, CLIP | ETH Zurich | [OpenMask3D: Open-Vocabulary 3D Instance Segmentation](https://arxiv.org/abs/2306.13613) | NeurIPS 2023 | [project](https://openmask3d.github.io/) |

#### 1.2.2 3D Instance & Panoptic Segmentation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-08 | Feed-Forward, Open-Vocabulary, Panoptic | Authors | [EPS3D: End-to-End Feed-Forward 3D Panoptic Segmentation](https://arxiv.org/abs/2606.08980) | ICML 2026 | [github](https://github.com/Runsong123/EPS3D) |
| 2025-07 | Feed-Forward, Panoramic, DUSt3R-Based | Authors | [PanSt3R: Single-Feed 3D Geometry and Panoptic Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Zust_PanSt3R_3D_Geometry_and_Panoptic_Segmentation_in_a_Single_Feed_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zust_PanSt3R_3D_Geometry_and_Panoptic_Segmentation_in_a_Single_Feed_ICCV_2025_paper.html) |
| 2025-05-01 | MoE, Multi-Dataset, PTv3, CLIP Alignment | UVA | [Point-MoE: Large-Scale Multi-Dataset Training with Mixture-of-Experts for 3D Semantic Segmentation](https://arxiv.org/abs/2505.09178) | ICLR 2026 | [project](https://uva-computer-vision-lab.github.io/point-moe/) |
| 2025-03-01 | Bayesian 3DGS, Training-Free, EIG | Sony | [B3-Seg: Camera-Free, Training-Free 3DGS Segmentation via Analytic EIG](https://sony.github.io/B3-Seg-project/) | CVPR 2026 | [project](https://sony.github.io/B3-Seg-project/) |
| 2025-01-01 | End-to-End, 2D-to-3D Lifting, 3DGS | CUHK | [Unified-Lift: Rethinking End-to-End 2D to 3D Scene Segmentation in Gaussian Splatting](https://arxiv.org/abs/2501.07867) | CVPR 2025 | [github](https://github.com/Runsong123/Unified-Lift) |
| 2025-01-01 | Unsupervised Panoptic, Scene-Centric | TU Darmstadt | [CUPS: Scene-Centric Unsupervised Panoptic Segmentation](https://arxiv.org/abs/2501.06302) | CVPR 2025 Highlight | [github](https://github.com/visinf/cups) |
| 2025-01-01 | Zero-Shot Instance, SAM Prompts in 3D | CUHK-SZ / MSRA | [SAMPro3D: Locating SAM Prompts in 3D for Zero-Shot Instance Segmentation](https://arxiv.org/abs/2501.02704) | 3DV 2025 | [github](https://github.com/GAP-LAB-CUHK-SZ/SAMPro3D) |
| 2024-03 | Unified 6 Tasks, Single Transformer | HUST | [UniSeg3D: Unified 3D Segmentation with Transformer](https://arxiv.org/abs/2403.16258) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2403.16258) |
| 2024-03 | Unsupervised 3D Instance, Indoor | Authors | [UnScene3D: Unsupervised 3D Instance Segmentation](https://arxiv.org/abs/2403.16735) | CVPR 2024 | [paper](https://arxiv.org/abs/2403.16735) |
| 2023-12-27 | 3D Instance Segmentation, Transformer, Point Cloud | ETH Zurich | [Mask3D: Mask Transformer for 3D Semantic Instance Segmentation](https://arxiv.org/abs/2210.03105) | ICRA 2023 | [github](https://github.com/JonasSchult/Mask3D) |
| 2023-08-22 | Point Cloud, Foundation Model, 3D Understanding | Shanghai AI Lab | [Point Transformer V3: Simpler, Faster, Stronger](https://arxiv.org/abs/2312.10035) | CVPR 2024 | [github](https://github.com/Pointcept/PointTransformerV3) |
| 2023-02-28 | 3D Panoptic, LiDAR, Multi-Scene | Tsinghua | [UniSeg3D: Unified 3D Panoptic Segmentation](https://arxiv.org/abs/2407.03263) | CVPR 2023 | [github](https://github.com/PJLab-ADG/UniSeg3D) |

#### 1.2.3 3D Visual Grounding & Spatial Reasoning

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Agentic, Cognitive Map, Zero-Shot 3D | Sichuan University | [Agentic Collaborative Cognition for Zero-Shot 3D Understanding](https://arxiv.org/abs/2606.24649) | ECCV 2026 | [project](https://zhangbo135.github.io/agentic-collaborative-cognition/) |
| 2026-06-22 | Map-Grounded, MV3D-VQA, Dense Reward | KAIST | [Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views](https://arxiv.org/abs/2606.23557) | ECCV 2026 | [paper](https://arxiv.org/abs/2606.23557) |
| 2026-06-17 | Panoramic Reprojection, 3D VLM, Spatial Reasoning | Technical University of Munich | [OneCanvas: 3D Scene Understanding via Panoramic Reprojection](https://arxiv.org/abs/2606.19253) | arXiv | [project](https://baranowskibrt.github.io/onecanvas/) |
| 2026-06-04 | Part-Aware 3D-MLLM, Scene Understanding, Grounding | Xiamen University | [PAR3D: A Unified 3D-MLLM with Part-Aware Representation for Scene Understanding](https://arxiv.org/abs/2606.06485) | arXiv | [project](https://atrovast.github.io/PAR3D/) |
| 2025-10-23 | Grounded CoT, 3D Reasoning, SceneCOT-185K Dataset | BIGAI / PKU / Tsinghua | [SceneCOT: Eliciting Grounded Chain-of-Thought Reasoning in 3D Scenes](https://arxiv.org/abs/2510.16714) | ICLR 2026 | [paper](https://arxiv.org/abs/2510.16714) |
| 2025-07 | Scene Graph, LLM, Relation Encoding | AIRI | [3DGraphLLM: 3D Scene Graph Learning with LLMs](https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_3D_Scene_Graph_Learning_with_Large_Language_Models_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_3D_Scene_Graph_Learning_with_Large_Language_Models_ICCV_2025_paper.html) |
| 2025-06-01 | Generalist 3D LMM, Omni Superpoint Transformer | Adelaide / Microsoft | [3D-LLaVA: Towards Generalist 3D LMMs with Omni Superpoint Transformer](https://arxiv.org/abs/2501.02363) | CVPR 2025 | [github](https://github.com/Pauljsw/3D-LLaVA_sw) |
| 2025-03-19 | Gesture+Language, Embodied Reference, +30% | Authors | [Ges3ViG: 3D Embodied Reference Understanding with Pointing Gestures](https://openaccess.thecvf.com/content/CVPR2025/html/Mane_Ges3ViG_3D_Embodied_Reference_Understanding_with_Pointing_Gestures_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Mane_Ges3ViG_3D_Embodied_Reference_Understanding_with_Pointing_Gestures_CVPR_2025_paper.html) |
| 2025-03-12 | Dense Grounding, 6.2M Pairs, Hallucination Benchmark | UMich | [3D-GRAND: A Million-Scale Dataset for 3D Grounding](https://arxiv.org/abs/2503.09243) | CVPR 2025 | [project](https://3d-grand.github.io/) |
| 2025-03-11 | 3D-Informed, Spatial Reasoning, Highlight | JHU | [SpatialLLM: Spatial Reasoning with 3D-Informed LLMs](https://arxiv.org/abs/2503.08322) | CVPR 2025 Highlight | [paper](https://arxiv.org/abs/2503.08322) |
| 2025-03-10 | LLM Attention, Scene Magnifier, Cross-Room | SCUT | [LSceneLLM: LLM-Attention Adaptive 3D Scene Understanding](https://openaccess.thecvf.com/content/CVPR2025/html/Zhi_LSceneLLM_Enhancing_Large_3D_Scene_Understanding_with_Adaptive_LLM_Attention_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhi_LSceneLLM_Enhancing_Large_3D_Scene_Understanding_with_Adaptive_LLM_Attention_CVPR_2025_paper.html) |
| 2025-03-01 | Geometry VLM, Unified 3D Recon + Spatial Reasoning | Shanghai AI Lab / UCLA / SJTU | [G2VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning](https://arxiv.org/abs/2503.15681) | CVPR 2026 | [github](https://github.com/InternRobotics/G2VLM) |
| 2025-01-01 | LVLM-Guided, Hierarchical Feature, 3DGS | Fudan / NTU | [ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding](https://arxiv.org/abs/2501.06903) | CVPR 2025 | [project](https://ZhenyangLiu.github.io/ReasonGrounder) |
| 2024-11-15 | Zero-Shot 3D Grounding, 2D VLM Transfer | NUS | [SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding](https://arxiv.org/abs/2406.03857) | CVPR 2025 | [project](https://seeground.github.io/) |
| 2024-10-07 | 3D-LLM, 3D Grounding, Scene Understanding | Shanghai AI Lab | [LLaVA-3D: A Simple yet Effective Pathway to Empowering LMMs with 3D Awareness](https://arxiv.org/abs/2410.06250) | ICCV 2025 | [github](https://github.com/ZCMax/LLaVA-3D) |
| 2024-07 | Interactive 3D, Language Assistant, Point Cloud | CUHK | [LL3DA: Visual Interactive Instruction Tuning for 3D Language Assistant](https://arxiv.org/abs/2403.05289) | CVPR 2024 | [github](https://github.com/Open3DA/LL3DA) |
| 2024-07 | Object Identifiers, 3D VL, Unified Tasks | ZJU | [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://arxiv.org/abs/2407.13268) | NeurIPS 2024 | [github](https://github.com/ActiveVisionLab/Chat-Scene) |
| 2024-07 | Million-Scale 3D VL, Multi-Level Contrastive | BIGAI | [SceneVerse: Scaling 3D Vision-Language Learning for Grounding](https://arxiv.org/abs/2407.10520) | ECCV 2024 | [project](https://scene-verse.github.io/) |
| 2024-04 | Open-Vocabulary 3D Scene Graph, Open Relations | Bosch | [Open3DSG: Open-Vocabulary 3D Scene Graph Generation](https://arxiv.org/abs/2404.02794) | CVPR 2024 | [paper](https://arxiv.org/abs/2404.02794) |
| 2024-04 | Generalist Embodied 3D Agent, VLA, ICML | BIGAI | [LEO: An Embodied Generalist Agent in 3D World](https://arxiv.org/abs/2311.12886) | ICML 2024 | [project](https://embodied-generalist.github.io/) |
| 2024-03 | CLIP Cross-Modal, Contrastive, Scene Graph | Authors | [CCL-3DSGG: CLIP-Driven Contrastive Learning for 3D Scene Graph Generation](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CCL-3DSGG_CLIP-Driven_Contrastive_Learning_for_3D_Scene_Graph_Generation_CVPR_2024_paper.html) | CVPR 2024 | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CCL-3DSGG_CLIP-Driven_Contrastive_Learning_for_3D_Scene_Graph_Generation_CVPR_2024_paper.html) |
| 2023-12-29 | 3D VQA, 3D Captioning, Scene Understanding | Shanghai AI Lab | [3D-LLM: Injecting the 3D World into Large Language Models](https://arxiv.org/abs/2307.12981) | NeurIPS 2023 | [project](https://vis-www.cs.umass.edu/3dllm/) / [github](https://github.com/UMass-Foundation-Model/3D-LLM) |
| 2023-08-16 | 3D Visual Grounding, Referring Expression, Point Cloud | Peking University | [3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment](https://arxiv.org/abs/2308.04352) | ICCV 2023 | [github](https://github.com/3d-vista/3D-VisTA) |
| 2023-03 | 3D Language Pre-training, Captioning, QA | Authors | [3D-VLP: 3D Vision-Language Pre-training with Contextual Scene](https://openaccess.thecvf.com/content/CVPR2023/html/Jin_3D-VLP_3D_Vision-Language_Pre-Training_CVPR_2023_paper.html) | CVPR 2023 | [paper](https://openaccess.thecvf.com/content/CVPR2023/html/Jin_3D-VLP_3D_Vision-Language_Pre-Training_CVPR_2023_paper.html) |

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
| 2026-03-19 | Panoramic Reconstruction, Permutation-Equivariant, 360° | Cornell | [PanoVGGT: Feed-Forward 3D Reconstruction from Panoramic Imagery](https://arxiv.org/abs/2603.17571) | CVPR 2026 | [paper](https://arxiv.org/abs/2603.17571) |
| 2026-01-26 | RGB-D, Depth Completion, Reflective/Transparent | Robbyant | [LingBot-Depth: Masked Depth Modeling for Spatial Perception](https://huggingface.co/robbyant/lingbot-depth) | arXiv | [github](https://github.com/robbyant/lingbot-depth) |
| 2025-01 | Fisheye, Real-Time, Cassini, Multi-View | Sun Yat-Sen Univ | [OmniStereo: Real-time Omnidirectional Depth with Multiview Fisheye Cameras](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_OmniStereo_Real-time_Omnidireactional_Depth_Estimation_with_Multiview_Fisheye_Cameras_CVPR_2025_paper.html) | CVPR 2025 | [github](https://github.com/DengJiaxi1/OmniStereo) |
| 2024-06 | Panoramic Depth, Semi-Supervised, Mobius | HKUST(GZ) | [PanDA: Panoramic Depth Anything with Mobius Spatial Augmentation](https://arxiv.org/abs/2406.13378) | CVPR 2025 | [project](https://caozidong.github.io/PanDA_Depth/) |
| 2024-03 | 360 Depth, Bi-Projection, ERP+ICOSAP | HKUST(GZ) | [Elite360D: Efficient 360 Depth Estimation via Bi-Projection Fusion](https://arxiv.org/abs/2403.16376) | CVPR 2024 | [github](https://github.com/haoai-1997/Elite360D) |
| 2021-09-06 | 360 Depth, Indoor, Panoramic Images | CERTH | [Pano3D: A Holistic Benchmark and a Solid Baseline for 360 Depth Estimation](https://arxiv.org/abs/2109.02749) | CVPRW 2021 | [project](https://vcl3d.github.io/Pano3D/) / [github](https://github.com/VCL3D/Pano3D) |

#### 1.3.3 Neural Structured Light & Event-Based Imaging

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-09-18 | Event Camera, Depth Estimation, Any-to-Any | Shanghai AI Lab | [Depth AnyEvent: Event Camera Based Monocular Depth Estimation via Dense Correspondence Distillation](https://arxiv.org/abs/2509.15224) | arXiv | [paper](https://arxiv.org/abs/2509.15224) |
| 2025-07 | ToF, Sparse Depth, 3DGS, SLAM | Authors | [ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth](https://openaccess.thecvf.com/content/ICCV2025/html/Conti_ToF-Splatting_Dense_SLAM_using_Sparse_Time-of-Flight_Depth_and_Multi-Frame_Integration_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Conti_ToF-Splatting_Dense_SLAM_using_Sparse_Time-of-Flight_Depth_and_Multi-Frame_Integration_ICCV_2025_paper.html) |
| 2025-05 | Event, Distillation, Confidence-Guided, Pseudo-Labels | NUS | [Distil-E2D: Distilling Image-to-Depth Priors for Event-Based Depth](https://nips.cc/virtual/2025/poster/115168) | NeurIPS 2025 | [paper](https://nips.cc/virtual/2025/poster/115168) |
| 2025-04 | Event Camera, Ray Density, 3D Conv, Spotlight | TU Berlin | [DERD-Net: Learning Depth from Event-based Ray Densities](https://arxiv.org/abs/2504.15863) | NeurIPS 2025 Spotlight | [github](https://github.com/tub-rip/DERD-Net) |
| 2025-01 | dToF, Video Depth Completion, Frequency Selective | Authors | [SVDC: Consistent Direct Time-of-Flight Video Depth Completion](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_SVDC_Consistent_Direct_Time-of-Flight_Video_Depth_Completion_with_Frequency_Selective_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_SVDC_Consistent_Direct_Time-of-Flight_Video_Depth_Completion_with_Frequency_Selective_CVPR_2025_paper.html) |
| 2024-10 | Event Camera, Pose-Free, Gaussian Splatting, Highlight | Zhejiang Univ | [IncEventGS: Pose-Free Gaussian Splatting from a Single Event Camera](https://arxiv.org/abs/2410.08107) | CVPR 2025 Highlight | [github](https://github.com/WU-CVGL/IncEventGS) |
| 2024-06 | Structured Light, Neural Inverse, 3-4 Patterns | U. Toronto | [TurboSL: Dense, Accurate and Fast 3D by Neural Inverse Structured Light](https://openaccess.thecvf.com/content/CVPR2024/html/Mirdehghan_TurboSL_Dense_Accurate_and_Fast_3D_by_Neural_Inverse_Structured_CVPR_2024_paper.html) | CVPR 2024 | [project](https://www.dgp.toronto.edu/projects/turbosl/) |
| 2023-08-15 | LiDAR, ZIP Encoding, 3D Reconstruction | Stanford | [LiZIP: Learned LiDAR Compression for Efficient and Effective 3D Reconstruction](https://arxiv.org/abs/2603.23162) | ICCV 2023 | [paper](https://arxiv.org/abs/2603.23162) |

<a id="14-dense-mapping-systems"></a>

### 1.4 Dense Mapping Systems

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-07 | 4DGS SLAM, Dynamic/Static, Tracking | Authors | [4D Gaussian Splatting SLAM](https://openaccess.thecvf.com/content/ICCV2025/html/Lin_4D_Gaussian_Splatting_SLAM_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Lin_4D_Gaussian_Splatting_SLAM_ICCV_2025_paper.html) |
| 2025-07 | Dynamic Surface, Non-Rigid, 4D Tracking | Imperial College | [4DTAM: Dynamic Surface Gaussian SLAM](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_4DTAM_Non-Rigid_Tracking_and_Mapping_with_Dynamic_Surface_Gaussians_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_4DTAM_Non-Rigid_Tracking_and_Mapping_with_Dynamic_Surface_Gaussians_CVPR_2025_paper.html) |
| 2025-06-18 | Gaussian SLAM, Dynamic Environments, Monocular | Stanford / ETH | [WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2501.15038) | CVPR 2025 | [project](https://wildgs-slam.github.io/) |
| 2025-05-10 | Gaussian SLAM, Global BA, Monocular RGB | ETH / Meta | [Splat-SLAM: Globally Optimized RGB-only SLAM with 3D Gaussians](https://arxiv.org/abs/2411.01687) | CVPR 2025 | [project](https://splat-slam.github.io/) |
| 2025-05-07 | Language-Embedded, Open-Vocabulary, 3DGS SLAM | KAIST | [LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM](https://arxiv.org/abs/2511.16144) | arXiv | [paper](https://arxiv.org/abs/2511.16144) |
| 2025-03-11 | Gaussian SLAM, Dense Reconstruction, RGB-D | Zhejiang University | [GigaSLAM: Gaussian Splatting-based Large-Scale Dense SLAM](https://arxiv.org/abs/2503.08071) | arXiv | [github](https://github.com/DengKaiCQ/GigaSLAM) |
| 2025-03 | Multi-Agent, 3DGS SLAM, Loop Closure | Authors | [MAGiC-SLAM: Multi-Agent 3DGS SLAM](https://openaccess.thecvf.com/content/CVPR2025/html/Lan_MAGiC-SLAM_Multi-Agent_3D_Gaussian_Splatting_SLAM_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lan_MAGiC-SLAM_Multi-Agent_3D_Gaussian_Splatting_SLAM_CVPR_2025_paper.html) |
| 2025-01-24 | Multi-Robot, Semantic, Heterogeneous, 3DGS | Stanford | [HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](https://arxiv.org/abs/2501.14147) | RAL 2025 | [project](http://hammer-project.github.io/) |
| 2025-01-19 | Real-Time Mapping, Open-Vocabulary, 3D Semantics | MIT | [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650) | ICRA 2024 | [project](https://concept-graphs.github.io/) / [github](https://github.com/concept-graphs/concept-graphs) |
| 2025-01-16 | Neural SLAM, Dense Mapping, Self-Supervised | Shanghai AI Lab | [DINO-SLAM: Dense Tracking and Mapping with Self-Supervised Feature Learning](https://arxiv.org/abs/2507.19474) | arXiv | [paper](https://arxiv.org/abs/2507.19474) |
| 2024-09 | Single-Image Calibration, Geometric Optimization | ETH / Meta | [GeoCalib: Learning Single-image Calibration](https://arxiv.org/abs/2409.06704) | ECCV 2024 | [paper](https://arxiv.org/abs/2409.06704) |
| 2024-06-17 | Dense SLAM, Gaussian Splatting, RGB-D | TUM | [Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741) | CVPR 2024 | [github](https://github.com/muskie82/MonoGS) |
| 2024-06-15 | Gaussian SLAM, RGB-D, Volumetric | CMU / MIT | [SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM](https://arxiv.org/abs/2312.02126) | CVPR 2024 | [project](https://spla-tam.github.io/) / [github](https://github.com/spla-tam/SplaTAM) |
| 2024-04-15 | Neural SLAM, Survey, Radiance Fields | TUM | [How NeRFs and 3D Gaussian Splatting are Reshaping SLAM: a Survey](https://arxiv.org/abs/2402.13255) | arXiv | [project](https://github.com/fabiotosi92/Awesome-SLAM) |
| 2024-04 | End-to-End SfM, Differentiable BA | Meta AI / Oxford | [VGGSfM: Visual Geometry Grounded Deep SfM](https://arxiv.org/abs/2312.04516) | CVPR 2024 | [github](https://github.com/facebookresearch/vggsfm) |
| 2024-04 | Detector-Free SfM, Texture-Poor | Zhejiang Univ | [Detector-Free Structure from Motion](https://arxiv.org/abs/2404.07519) | CVPR 2024 | [github](https://github.com/zju3dv/DetectorFreeSfM) |
| 2024-04 | Pose Regression, Map-Relative, Multi-Scene, Highlight | Niantic / Oxford | [Marepo: Map-Relative Pose Regression for Visual Re-Localization](https://nianticlabs.github.io/marepo/) | CVPR 2024 Highlight | [github](https://github.com/nianticlabs/marepo) |
| 2023-05-30 | Neural Mapping, Dense RGB-D SLAM, SDF | HKUST | [NICE-SLAM: Neural Implicit Scalable Encoding for SLAM](https://arxiv.org/abs/2112.12130) | CVPR 2022 | [project](https://pengsongyou.github.io/nice-slam) |

<h2 id="-2-3d4d-representation">🧱 2. 3D/4D Representation</h2>

This section focuses on the mathematical and data-structure layer used to represent geometry, appearance, and motion.

<a id="21-explicit--hybrid-representations"></a>

### 2.1 Explicit & Hybrid Representations

#### 2.1.1 Structure-Aware 3D Gaussian Splatting

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-04-16 | Feed-Forward 3DGS, Global Scene Tokens, Compact | Tel Aviv University | [GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284) | arXiv | [paper](https://arxiv.org/abs/2604.15284) |
| 2026-04-16 | TokenGS, Learnable Gaussian Tokens, Pose-Robust | NVIDIA | [TokenGS: Decoupling 3D Gaussian Prediction from Pixels](https://arxiv.org/abs/2604.15239) | CVPR 2026 Highlight | [project](https://research.nvidia.com/labs/toronto-ai/tokengs/) |
| 2026-04-12 | UniSplat, Unposed Multi-View, Feed-Forward | UC Berkeley | [UniSplat: Learning 3D Representations from Unposed Multi-View Images](https://arxiv.org/abs/2604.10573) | CVPR 2026 | [paper](https://arxiv.org/abs/2604.10573) |
| 2026-03-12 | Sparse-View 4D, Monocular Fusion, Cross-Video | Meta AI | [MonoFusion: Sparse-View 4D Reconstruction via Monocular Fusion](https://arxiv.org/abs/2507.23782) | ICCV 2025 | [paper](https://arxiv.org/abs/2507.23782) |
| 2026-03-07 | Few-Shot, Diffusion Prior, Repair + Inpainting | ZJU / Alibaba | [RI3D: Few-Shot Gaussian Splatting With Repair and Inpainting Diffusion Priors](https://arxiv.org/abs/2503.10860) | ICCV 2025 | [paper](https://arxiv.org/abs/2503.10860) |
| 2026-02-02 | Feed-Forward 2DGS, Surface Continuity, Sparse Views | Shanghai Jiao Tong | [SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors](https://arxiv.org/abs/2602.02000) | ICLR 2026 | [paper](https://arxiv.org/abs/2602.02000) |
| 2025-07-10 | 3DGS, Structure, Sparse Views | USTC | [SparseGS: Real-Time 360 Sparse View Synthesis using Gaussian Splatting](https://arxiv.org/abs/2312.00206) | 3DV 2025 | [project](https://formycat.github.io/SparseGS-Real-Time-360-Sparse-View-Synthesis-using-Gaussian-Splatting/) |
| 2025-07 | Anti-Aliasing, Gaussian, 3D, Adaptive | CUHK | [AAA-Gaussians: Anti-Aliasing 3D Gaussian Splatting](https://openaccess.thecvf.com/content/ICCV2025/html/Xu_AAA-Gaussians_Anti-Aliasing_Gaussian_Splatting_for_3D_Scene_Rendering_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://arxiv.org/abs/2506.14538) |
| 2025-06-01 | Sparse-View Surface, Geometry-Prioritized, 2DGS | Nankai Univ | [Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Sparse2DGS_Geometry-Prioritized_Gaussian_Splatting_for_Surface_Reconstruction_from_Sparse_Views_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://arxiv.org/abs/2505.15072) |
| 2025-04 | Feed-Forward, No Camera, FreeSplatter | ZJU | [FreeSplatter: Pose-Free 3DGS from Sparse Views](https://arxiv.org/abs/2504.02513) | CVPR 2025 | [paper](https://arxiv.org/abs/2504.02513) |
| 2024-12 | Large-Scale Dynamic, City, 4DGS, Spotlight | ZJU | [DynamicCity: Large-Scale 4D Gaussian City Modeling](https://openreview.net/forum?id=K3PN1Ye8nC) | ICLR 2025 Spotlight | [paper](https://arxiv.org/abs/2412.06153) |
| 2024-09 | Progressive, Pruning, 3DGS, CVPR | S-Lab | [PUP 3D-GS: Progressive Pruning for 3DGS](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_PUP_3D-GS_Progressive_3D_Gaussian_Splatting_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://arxiv.org/abs/2409.18122) |
| 2024-09 | Scene-Level, 3DGS, Open-Vocabulary, 4D LangSplat | UPenn | [4D LangSplat: 4D Language Gaussian Splatting](https://arxiv.org/abs/2501.06470) | CVPR 2025 | [paper](https://arxiv.org/abs/2501.06470) |
| 2024-07-15 | Feed-Forward 3DGS, Sparse Views, Generalizable | Monash / Tübingen | [MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2403.14624) | ECCV 2024 Oral | [project](https://mvsplat.github.io/) / [github](https://github.com/donydchen/mvsplat) |
| 2024-07-02 | 2DGS, Surface Reconstruction, Geometry | TUM | [2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://arxiv.org/abs/2403.17888) | SIGGRAPH 2024 | [project](https://surfsplatting.github.io/) |
| 2024-06 | Anti-Aliasing, Mip, 3DGS, Best Student Paper | Inria | [Mip-Splatting: Alias-free 3DGS](https://arxiv.org/abs/2311.16493) | CVPR 2024 Oral / Best Student Paper | [github](https://github.com/autonomousvision/mip-splatting) |
| 2024-06 | Compression, Compact, 3DGS, Highlight | Tsinghua | [Compact 3D Gaussian Splatting](https://arxiv.org/abs/2311.15708) | CVPR 2024 Highlight | [paper](https://arxiv.org/abs/2311.15708) |
| 2024-06 | Distillation, Lightweight, 3DGS, Spotlight | Virginia Tech | [LightGaussian: Distilled 3D Gaussian Splatting](https://arxiv.org/abs/2312.00749) | NeurIPS 2024 Spotlight | [paper](https://arxiv.org/abs/2312.00749) |
| 2024-03-27 | Feed-Forward 3DGS, Image Pairs, Epipolar | MIT | [pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction](https://arxiv.org/abs/2312.12337) | CVPR 2024 Oral | [github](https://github.com/dcharatan/pixelsplat) |
| 2024-03 | Multi-Scale, 3DGS, Level-of-Detail | Shanghai Jiao Tong | [Multi-Scale 3DGS](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Multi-Scale_3D_Gaussian_Splatting_for_Multi-Resolution_Rendering_CVPR_2024_paper.html) | CVPR 2024 | [paper](https://arxiv.org/abs/2403.09316) |
| 2023-11-21 | 3DGS, Mesh Extraction, Surface | ETH Zurich | [SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction](https://arxiv.org/abs/2311.12775) | CVPR 2024 | [project](https://anttwo.github.io/sugar/) |
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
| 2025-07 | Unbiased SDF, Neural Implicit Surface, SDF-to-Density | CUHK | [UNIS: Unified Framework for Unbiased Neural Implicit Surfaces](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_UNIS_A_Unified_Framework_for_Unbiased_Neural_Implicit_Surfaces_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://arxiv.org/abs/2507.11466) |
| 2024-09 | α-NeuS, Alpha, SDF, Volume Rendering | ZJU | [α-NeuS: Alpha-Governed Neural Implicit Surfaces](https://arxiv.org/abs/2409.04166) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2409.04166) |
| 2024-03 | Objects as Volumes, NeRF, 3D Reconstruction, Oral | UPenn | [Objects as Volumes: Feed-Forward 3D from a Single Image](https://arxiv.org/abs/2401.05417) | CVPR 2024 Oral | [paper](https://arxiv.org/abs/2401.05417) |
| 2023-10 | Zip-NeRF, Anti-Aliasing, Mip, Grid | Google Research | [Zip-NeRF: Anti-Aliased Grid-Based NeRF](https://arxiv.org/abs/2304.06706) | ICCV 2023 | [project](https://jonbarron.info/zipnerf/) |
| 2023-10 | EG3D, Triplane, 3D GAN, Generative | NVIDIA | [EG3D: Efficient Geometry-aware 3D Generative Adversarial Networks](https://arxiv.org/abs/2112.07945) | CVPR 2022 Oral | [github](https://github.com/NVlabs/eg3d) |
| 2023-01-31 | Unbounded Scenes, Anti-Aliasing, NeRF | Google Research | [Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](https://arxiv.org/abs/2111.12077) | CVPR 2022 | [project](https://jonbarron.info/mipnerf360/) |
| 2022-06 | Ref-NeRF, Reflection, Specular, Best Student Paper HM | Google Research | [Ref-NeRF: Structured View-Dependent Appearance for NeRF](https://arxiv.org/abs/2112.03907) | CVPR 2022 Best Student Paper HM | [project](https://dorverbin.github.io/refnerf/) |
| 2022-03 | Plenoxels, No Neural Network, Fast, Oral | UC Berkeley | [Plenoxels: Radiance Fields without Neural Networks](https://arxiv.org/abs/2112.05131) | CVPR 2022 Oral | [github](https://github.com/sxyu/plenoxels) |
| 2022-01-14 | Hash Grid, Real-Time NeRF, Neural Graphics | NVIDIA | [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](https://nvlabs.github.io/instant-ngp/) | SIGGRAPH 2022 | [github](https://github.com/NVlabs/instant-ngp) |
| 2021-12-11 | Tensor Factorization, Radiance Fields, Compression | Tsinghua | [TensoRF: Tensorial Radiance Fields](https://arxiv.org/abs/2203.09517) | ECCV 2022 | [project](https://apchenstu.github.io/TensoRF/) |
| 2021-12 | NeRF-W, Unbounded, In-the-Wild | Google Research | [NeRF in the Wild: Neural Radiance Fields for Unconstrained Photo Collections](https://arxiv.org/abs/2008.02268) | CVPR 2021 | [github](https://github.com/creiser/nerf-w) |
| 2021-06-01 | SDF, Surface Reconstruction, Neural Rendering | MPI-IS | [NeuS: Learning Neural Implicit Surfaces by Volume Rendering](https://arxiv.org/abs/2106.10689) | NeurIPS 2021 | [project](https://lingjie0206.github.io/papers/NeuS/) |
| 2021-06 | BARF, Bundle-Adjusting NeRF, Oral | UC Berkeley | [BARF: Bundle-Adjusting Neural Radiance Fields](https://arxiv.org/abs/2104.06405) | ICCV 2021 Oral | [github](https://github.com/chenhsuanlin/bundle-adjusting-NeRF) |
| 2020-03-19 | NeRF, View Synthesis, Neural Rendering | UC Berkeley | [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://www.matthewtancik.com/nerf) | ECCV 2020 | [github](https://github.com/bmild/nerf) |

<a id="23-dynamic--spatiotemporal-4d"></a>

### 2.3 Dynamic & Spatiotemporal 4D

#### 2.3.1 4D Gaussian Splatting (4DGS)

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-22 | Dynamic 3DGS, Visibility-Aware Densification, Temporal Lifespan | Indian Institute of Science | [Temporally Aware Densification for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.23212) | arXiv | [paper](https://arxiv.org/abs/2606.23212) |
| 2025-07 | 7DGS, Spatial-Temporal-Angular, Unified | Authors | [7D Gaussian Splatting: Unified Spatial-Temporal-Angular GS](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_7DGS_A_Unified_Spatial-Temporal-Angular_Gaussian_Splatting_Framework_for_Arbitrary-Scale_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_7DGS_A_Unified_Spatial-Temporal-Angular_Gaussian_Splatting_Framework_for_Arbitrary-Scale_ICCV_2025_paper.html) |
| 2024-10 | Event Camera, High-Speed, 4D, STD-GS | Authors | [STD-GS: SpatioTemporal-Disentangled Gaussian Splatting with Event Cameras](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_STD-GS_SpatioTemporal-Disentangled_Gaussian_Splatting_for_High-Speed_Dynamic_3D_Reconstruction_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_STD-GS_SpatioTemporal-Disentangled_Gaussian_Splatting_for_High-Speed_Dynamic_3D_Reconstruction_ICCV_2025_paper.html) |
| 2023-11-30 | 4DGS, Dynamic Scenes, Real-Time Rendering | Zhejiang University | [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2310.08528) | CVPR 2024 | [project](https://guanjunwu.github.io/4dgs/) |
| 2023-10-16 | Dynamic 3DGS, Scene Motion, Multi-View Video | Cornell | [Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis](https://dynamic3dgaussians.github.io/) | 3DV 2025 | [github](https://github.com/JonathonLuiten/Dynamic3DGaussians) |
| 2023-08-21 | Dynamic NeRF, Deformation, Canonical Space | Google Research | [HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields](https://arxiv.org/abs/2106.13228) | SIGGRAPH Asia 2021 | [project](https://hypernerf.github.io/) |
| 2023-03 | HexPlane, 4D Representation, Space-Time | CMU | [HexPlane: A Fast Representation for Dynamic Scenes](https://arxiv.org/abs/2301.09680) | CVPR 2023 | [project](https://caoang327.github.io/HexPlane/) |
| 2023-03 | K-Planes, Explicit, 4D, Space-Time | Authors | [K-Planes: Explicit Radiance Fields in Space, Time, and Appearance](https://arxiv.org/abs/2301.10241) | CVPR 2023 | [github](https://github.com/sarafridov/K-Planes) |

#### 2.3.2 Deformation Graphs & Canonical Spaces

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-04-18 | Deformation, Dynamic Radiance Fields, Canonical | ETH Zurich | [SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](https://arxiv.org/abs/2312.14937) | CVPR 2024 | [project](https://yihua7.github.io/SC-GS-web/) |
| 2023-05-17 | Non-Rigid Tracking, Neural Deformation, 4D | Tsinghua | [Neuralangelo: High-Fidelity Neural Surface Reconstruction](https://arxiv.org/abs/2306.03092) | CVPR 2023 | [project](https://research.nvidia.com/labs/dir/neuralangelo/) |

<h2 id="-3-3d-reconstruction">🏗️ 3. 3D Reconstruction</h2>

Reconstruction systems recover objects or scenes from images, video, RGB-D, or multi-sensor streams under offline, online, and dynamic conditions.

<a id="31-static-reconstruction"></a>

### 3.1 Static Reconstruction

#### 3.1.1 Object-Centric Reconstruction

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-17 | Sparse-View Object, Flow Steering, 3DGS Refinement | Graz University of Technology | [FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity](https://arxiv.org/abs/2606.19019) | arXiv | [project](https://yuchenrao.github.io/projects/flowObject/flowObject.html) |
| 2026-05-05 | Generative Reconstruction, Multi-View Alignment, Pose | Tsinghua | [Mix3R: Mixing Feed-forward Reconstruction and Generative 3D Priors for Joint Multi-view Aligned 3D Reconstruction and Pose Estimation](https://arxiv.org/abs/2605.03359) | arXiv | [project](https://jsnln.github.io/mix3r/) |
| 2025-11-19 | Single Image, Object Mesh, SAM 3D | Meta AI | [SAM 3D Objects](https://github.com/facebookresearch/sam-3d-objects) | GitHub | [github](https://github.com/facebookresearch/sam-3d-objects) |
| 2025-06 | Feed-Forward, Densification, Gaussian, Detail | Authors | [Generative Densification: Feed-Forward 3DGS Densification](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Generative_Densification_Learning_to_Densify_Gaussians_for_Generalizable_3D_Reconstruction_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Generative_Densification_Learning_to_Densify_Gaussians_for_Generalizable_3D_Reconstruction_CVPR_2025_paper.html) |
| 2025-06 | Photogrammetry Foundation, Multi-Task, Highlight | Authors | [Matrix3D: A Foundation Model for Photogrammetry](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_Matrix3D_A_Foundation_Model_for_Photogrammetry_CVPR_2025_paper.html) | CVPR 2025 Highlight | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_Matrix3D_A_Foundation_Model_for_Photogrammetry_CVPR_2025_paper.html) |
| 2025-04-01 | Sparse-View, Feed-Forward, Camera, Geometry | Ant Research / Stanford | [FLARE: Feed-forward Geometry, Appearance and Camera Estimation from Uncalibrated Sparse Views](https://arxiv.org/abs/2504.03252) | CVPR 2025 | [project](https://zhanghe3z.github.io/FLARE/) |
| 2024-07 | Ego-Centric, Autonomous Driving, Sparse-View | Authors | [Omni-Scene: Omni-Gaussian for Ego-Centric Sparse-View Reconstruction](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Omni-Scene_Omni-Gaussian_for_Ego-Centric_3D_Scene_Reconstruction_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Omni-Scene_Omni-Gaussian_for_Ego-Centric_3D_Scene_Reconstruction_CVPR_2025_paper.html) |
| 2024-06-05 | Multi-View, Stereo, Feed-Forward | NAVER Labs | [MASt3R: Grounding Image Matching in 3D with MASt3R](https://arxiv.org/abs/2406.09756) | ECCV 2024 | [project](https://europe.naverlabs.com/research/publications/mast3r-grounding-image-matching-in-3d-with-mast3r/) / [github](https://github.com/naver/mast3r) |
| 2023-12-19 | Multi-View, Pointmap, Pose-Free | NAVER Labs | [DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132) | CVPR 2024 | [project](https://dust3r.europe.naverlabs.com/) / [github](https://github.com/naver/dust3r) |
| 2023-12-04 | Object Pose, Reconstruction, Model-Based | NVIDIA | [FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects](https://arxiv.org/abs/2312.08344) | CVPR 2024 | [project](https://nvlabs.github.io/FoundationPose/) |

#### 3.1.2 Large-Scale Scene Reconstruction

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-09 | RGB-T, Thermal Geometry, Low-Light | University of Minnesota | [DarkVGGT: Seeing Through Darkness Using Thermal Geometry without Daylight Tax](https://arxiv.org/abs/2606.11326) | arXiv | [project](https://darkvggt.github.io/) |
| 2026-06-02 | Single Image, Physics-in-the-Loop, Simulation-Ready | Seoul National University | [SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image](https://arxiv.org/abs/2606.03994) | arXiv | [project](https://snuvclab.github.io/SimuScene/) |
| 2026-05-14 | VGGT, Scaling, Static+Dynamic | University of Oxford | [VGGT-Omega: Scaling VGGT to Large-Scale 3D Reconstruction](https://arxiv.org/abs/2605.15195) | CVPR 2026 Oral | [project](https://vggt-omega.github.io/) / [github](https://github.com/facebookresearch/vggt-omega) / [demo](https://huggingface.co/spaces/facebook/vggt-omega) / [model](https://huggingface.co/facebook/vggt-omega) |
| 2026-05-07 | Feed-Forward 3D, Token Reduction, Long Sequence | Peking University | [Spark3R: Asymmetric Token Reduction Makes Fast Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2605.06270) | arXiv | [paper](https://arxiv.org/abs/2605.06270) |
| 2026-04-30 | Generalizable, Sparse-View, Unposed Images, Outdoor | UIUC / NVIDIA | [GenWildSplat: Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193) | arXiv | [paper](https://arxiv.org/abs/2604.28193) |
| 2026-02-26 | VGGT, TTT, Large-Scale | NVIDIA | [VGG-T^3: Offline Feed-Forward 3D Reconstruction at Scale](https://arxiv.org/abs/2602.23361) | CVPR 2026 | [project](https://research.nvidia.com/labs/dvl/publication/elflein2026vggt3/) |
| 2025-10-15 | Multi-View Reconstruction, Matching, MVS | NAVER Labs | [MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion](https://arxiv.org/abs/2409.19152) | 3DV 2025 | [github](https://github.com/naver/mast3r) |
| 2025-09-16 | Universal 3D, Metric Reconstruction, Optional Priors | Meta AI | [MapAnything: Universal Feed-Forward Metric 3D Reconstruction](https://arxiv.org/abs/2509.13414) | 3DV 2026 | [project](https://map-anything.github.io/) |
| 2025-07-17 | Permutation-Equivariant, Visual Geometry, Point Maps | Oxford / Meta | [π³: Permutation-Equivariant Visual Geometry Learning](https://arxiv.org/abs/2507.13347) | ICLR 2026 | [github](https://github.com/yyfz/Pi3) |
| 2025-07 | Feed-Forward, Surface, MVS, Multi-View | Authors | [MVSAnywhere: Zero-Shot Multi-View Stereo](https://openaccess.thecvf.com/content/CVPR2025/html/Karchevskiy_MVSAnywhere_Zero-Shot_Multi-View_Stereo_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Karchevskiy_MVSAnywhere_Zero-Shot_Multi-View_Stereo_CVPR_2025_paper.html) |
| 2025-07 | Monocular Prior, MVS, DTU/Tanks SOTA | Authors | [MonoMVSNet: Monocular Prior Guided MVS](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_MonoMVSNet_Monocular_Prior_Guided_Multi-View_Stereo_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_MonoMVSNet_Monocular_Prior_Guided_Multi-View_Stereo_ICCV_2025_paper.html) |
| 2025-07 | Latent Align, Stereo+Monocular, Highlight | Authors | [BridgeDepth: Unified Monocular and Stereo Depth](https://openaccess.thecvf.com/content/ICCV2025/html/Li_BridgeDepth_Unified_Monocular_and_Stereo_Depth_Estimation_ICCV_2025_paper.html) | ICCV 2025 Highlight | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Li_BridgeDepth_Unified_Monocular_and_Stereo_Depth_Estimation_ICCV_2025_paper.html) |
| 2025-06-10 | Feed-Forward, Multi-View, Auxiliary Priors | ETH / Microsoft | [Pow3R: Empowering Unconstrained 3D Reconstruction with Camera and Scene Priors](https://arxiv.org/abs/2503.17388) | CVPR 2025 | [project](https://pow3r.github.io/) |
| 2025-06-01 | Monocular Depth, Dynamic Video, Alignment | HKUST / CUHK / HKU | [Align3R: Aligned Monocular Depth Estimation for Dynamic Videos](https://arxiv.org/abs/2506.03426) | CVPR 2025 | [github](https://github.com/jiah-cloud/Align3R) |
| 2025-06 | Aerial-Ground, Large-Scale, 3DGS | Authors | [Horizon-GS: Unified Aerial-Ground 3DGS](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Horizon-GS_Unified_Aerial-Ground_3D_Gaussian_Splatting_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Horizon-GS_Unified_Aerial-Ground_3D_Gaussian_Splatting_CVPR_2025_paper.html) |
| 2025-06 | Autonomous Driving, Feed-Forward, 3DGS | Authors | [EVolSplat: Feed-Forward 3DGS for Urban Driving](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_EVolSplat_Efficient_Volumetric_3D_Gaussian_Splatting_for_Autonomous_Driving_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_EVolSplat_Efficient_Volumetric_3D_Gaussian_Splatting_for_Autonomous_Driving_CVPR_2025_paper.html) |
| 2025-06 | Sparse-View, Super-Resolution, 3DGS | Authors | [S2Gaussian: Sparse-View Super-Resolution 3DGS](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_S2Gaussian_Sparse-View_Super-Resolution_3D_Gaussian_Splatting_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_S2Gaussian_Sparse-View_Super-Resolution_3D_Gaussian_Splatting_CVPR_2025_paper.html) |
| 2025-05-31 | Multi-View, Symmetric, 1000+ Images, O(N) | NAVER Labs | [MUSt3R: Multi-view Network for Stereo 3D Reconstruction](https://arxiv.org/abs/2503.01661) | CVPR 2025 | [project](https://must3r.github.io/) |
| 2025-05-30 | Feed-Forward, 1500+ Images, 251 FPS | Meta AI | [Fast3R: Towards 3D Reconstruction of 1000+ Images in One Forward Pass](https://arxiv.org/abs/2501.13928) | CVPR 2025 | [project](https://fast3r-3d.github.io/) |
| 2025-05-01 | Relative Camera Pose, Regression, Localization | Aalto / HKU | [Reloc3r: Large-Scale Training of Relative Camera Pose Regression](https://arxiv.org/abs/2505.02832) | CVPR 2025 | [github](https://github.com/ffrivera0/reloc3r) |
| 2025-03-18 | Feed-Forward 3D, Pose-Free, Point Map | Meta AI | [VGGT: Visual Geometry Grounded Transformer](https://arxiv.org/abs/2503.11651) | CVPR 2025 Best Paper | [project](https://vgg-t.github.io/) / [github](https://github.com/facebookresearch/vggt) |
| 2025-01-20 | Sparse View, Single-Stage, 2 Seconds | Meta AI | [MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974) | CVPR 2025 Oral | [project](https://mv-dust3rp.github.io/) |
| 2024-12-11 | Feed-Forward, Online, Dense, Monocular | Shanghai AI Lab / PKU | [SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos](https://arxiv.org/abs/2412.09401) | CVPR 2025 Highlight | [project](https://slam3r.github.io/) |
| 2024-08-28 | Spatial Memory, Feed-Forward, Multi-View | HKU | [Spann3R: 3D Reconstruction with Spatial Memory](https://arxiv.org/abs/2408.16061) | 3DV 2025 Oral (Best Paper Candidate) | [project](https://hengyiwang.github.io/projects/spann3r) |

<a id="32-streaming--online-reconstruction"></a>

### 3.2 Streaming & Online Reconstruction

#### 3.2.1 Dense Semantic/Instance Mapping

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Object-Level Map, Open-Vocabulary, Relocalization | Zhejiang University | [Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization](https://arxiv.org/abs/2606.24767) | arXiv | [paper](https://arxiv.org/abs/2606.24767) |
| 2026-05-05 | Online, Voxel+Instance, Open-Vocabulary Mapping | Örebro University | [FUS3DMaps: Scalable and Accurate Open-Vocabulary Semantic Mapping](https://arxiv.org/abs/2605.03669) | arXiv | [project](https://githanonymous.github.io/FUS3DMaps/) |
| 2026-05-03 | Gaussian-Language Map, Zero-Shot Navigation, Multi-Scale | CASIA | [Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736) | arXiv | [github](https://github.com/sx-zhang/GLMap) |
| 2026-03-04 | Semantic 3DGS, Online, CLIP, Open-Vocabulary | National University of Singapore | [EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2603.04254) | CVPR 2026 | [project](https://0nandon.github.io/EmbodiedSplat/) |
| 2025-08-02 | Open-Vocabulary, Hybrid 3DGS+TSDF, Dense Mapping | Tsinghua | [OpenGS-Fusion: Open-Vocabulary Dense Mapping with Hybrid 3D Gaussian Splatting](https://arxiv.org/abs/2508.01150) | arXiv | [project](https://young-bit.github.io/opengs-fusion.github.io/) |
| 2025-07 | Feed-Forward, Panoramic Segmentation, DUSt3R | Authors | [PanSt3R: Single-Feed 3D and Panoptic Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Zust_PanSt3R_3D_Geometry_and_Panoptic_Segmentation_in_a_Single_Feed_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zust_PanSt3R_3D_Geometry_and_Panoptic_Segmentation_in_a_Single_Feed_ICCV_2025_paper.html) |
| 2023-09-28 | Open-Vocabulary, 3D Scene Graph, Mapping | MIT | [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650) | ICRA 2024 | [project](https://concept-graphs.github.io/) |

#### 3.2.2 Continuous Neural Tracking & Mapping

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | 3DGS-SLAM, Memory-Efficient, Outdoor Mapping | University of Minnesota | [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796) | ICRA 2026 | [github](https://github.com/UMN-ZhaoLab/Pocket-SLAM) |
| 2026-06-20 | RGB+Pose, 3DGS Scene Regression, Robot Capture | Peking University | [ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091) | arXiv | [paper](https://arxiv.org/abs/2606.22091) |
| 2026-06-19 | 3DGS-SLAM, Degeneracy-Robust, Real-Time Tracking | Nanyang Technological University | [Spectral GS-SLAM: Observability-Aware, Degeneracy-Robust Tracking for Real-Time 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2606.21258) | IROS 2026 | [paper](https://arxiv.org/abs/2606.21258) |
| 2026-06-18 | LiDAR-Inertial-Thermal, 3DGS Mapping, Illumination-Robust | Shenzhen University | [LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping](https://arxiv.org/abs/2606.20424) | IROS 2026 | [paper](https://arxiv.org/abs/2606.20424) |
| 2026-06-03 | Streaming, Transient Anchors, Long-Horizon Mapping | Authors | [Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping](https://arxiv.org/abs/2606.05035) | arXiv | [paper](https://arxiv.org/abs/2606.05035) |
| 2026-05-10 | VGGT, Retrieval, Constant Memory | Fudan University | [RetrieveVGGT: Training-Free Long Context Streaming 3D Reconstruction via Query-Key Similarity Retrieval](https://arxiv.org/abs/2605.09644) | arXiv | [github](https://github.com/zzctmd/RetrieveVGGT) |
| 2026-04-15 | Streaming, Feed-Forward, Long Video | Robbyant | [LingBot-Map: Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141) | arXiv | [github](https://github.com/robbyant/lingbot-map) |
| 2026-02-13 | Streaming, Autoregressive, Long Sequence | 3DAgentWorld | [LongStream: Long-Sequence Streaming Autoregressive Visual Geometry](https://arxiv.org/abs/2602.13172) | CVPR 2026 | [project](https://3dagentworld.github.io/longstream/) |
| 2026-01-03 | StreamVGGT, KV Cache, Memory Compression | Sun Yat-sen University | [XStreamVGGT: Extremely Memory-Efficient Streaming Vision Geometry Grounded Transformer](https://arxiv.org/abs/2601.01204) | arXiv | [github](https://github.com/ywh187/XStreamVGGT/) |
| 2025-09-26 | TTT, Online, Long Context | Shanghai AI Lab | [TTT3R: 3D Reconstruction as Test-Time Training](https://arxiv.org/abs/2509.26645) | arXiv | [project](https://rover-xingyu.github.io/TTT3R/) |
| 2025-08-01 | Streaming, Causal Transformer, Sequential | NTU / Shanghai AI Lab | [STream3R: Scalable Sequential 3D Reconstruction with Causal Transformer](https://arxiv.org/abs/2508.10893) | arXiv | [project](https://nirvanalan.github.io/projects/stream3r) |
| 2025-01-20 | Online 3D, Recurrent Pointmap, Streaming | Meta AI | [CUT3R: Continuous 3D Perception Model with Persistent State](https://arxiv.org/abs/2501.12387) | CVPR 2025 Oral | [project](https://cut3r.github.io/) / [github](https://github.com/CUT3R/CUT3R) |
| 2024-12-16 | MASt3R, Dense SLAM, Real-Time | Imperial College London | [MASt3R-SLAM: Real-Time Dense SLAM with 3D Reconstruction Priors](https://arxiv.org/abs/2412.12392) | CVPR 2025 | [github](https://github.com/rmurai0610/MASt3R-SLAM) |

<a id="33-dynamic-3d-reconstruction"></a>

### 3.3 Dynamic 3D Reconstruction

#### 3.3.1 Non-Rigid Tracking & Reconstruction

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Articulated Digital Twin, RGB-D, URDF Export | ETH Zurich | [ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D Videos](https://arxiv.org/abs/2606.24628) | ICRA 2026 Workshop | [paper](https://arxiv.org/abs/2606.24628) |
| 2026-06-22 | Monocular Video, 4DGS, In-the-Wild Non-Rigid | Carnegie Mellon University | [Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://arxiv.org/abs/2606.23688) | arXiv | [project](https://lift4d.github.io/) |
| 2026-06-22 | Dynamic Driving, Sparse Voxels, LiDAR-Guided | Huawei Paris Research Center | [DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031) | arXiv | [paper](https://arxiv.org/abs/2606.23031) |
| 2026-06-09 | Future Extrapolation, 4DGS, Autonomous Driving | Tsinghua University | [Envision4D: Envisioning Visual Futures via Feed-forward 4D Gaussian Splatting for Autonomous Driving](https://arxiv.org/abs/2606.10656) | arXiv | [project](https://maggiesong7.github.io/research/Envision4D/) |
| 2026-06-09 | Manipulation Video, Decoupled 3DGS, Scene Graph | Authors | [ManiSplat: Manipulation Trajectory Synthesis from Monocular Video via Decoupled 3D Gaussian Splatting](https://arxiv.org/abs/2606.10645) | arXiv | [paper](https://arxiv.org/abs/2606.10645) |
| 2026-06-02 | Object Permanence, Differentiable Physics, 4DGS | Authors | [PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting](https://arxiv.org/abs/2606.03479) | CVPR 2026 Workshop | [paper](https://arxiv.org/abs/2606.03479) |
| 2026-04-21 | Functional Scenes, Egocentric Interaction, URDF/USD | Stanford | [FunRec: Reconstructing Functional 3D Scenes from Egocentric Interaction Videos](https://arxiv.org/abs/2604.05621) | CVPR 2026 | [paper](https://arxiv.org/abs/2604.05621) |
| 2026-04-10 | Feed-Forward, Unconstrained Views, Semantic-Geometry | Nanyang Tech | [FF3R: Feedforward Feature 3D Reconstruction from Unconstrained Views](https://arxiv.org/abs/2604.09862) | CVPR 2026 Findings | [paper](https://arxiv.org/abs/2604.09862) |
| 2026-04-10 | Dynamic/Static Disentanglement, Uncertainty-Aware, Feed-Forward | Zhejiang University | [Robust 4D VGT: Robust 4D Visual Geometry Transformer with Uncertainty-Aware Priors](https://arxiv.org/abs/2604.09366) | arXiv | [paper](https://arxiv.org/abs/2604.09366) |
| 2026-03-21 | RayMap, Dynamic, Streaming | University of Illinois Chicago | [RayMap3R: Inference-Time RayMap for Dynamic 3D Reconstruction](https://arxiv.org/abs/2603.20588) | arXiv | [project](https://raymap3r.github.io/) / [github](https://github.com/Brack-Wang/raymap3r) |
| 2026-03-09 | Dynamic VGGT, Autonomous Driving, 4D | Fudan University | [DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving](https://arxiv.org/abs/2603.08254) | arXiv | [paper](https://arxiv.org/abs/2603.08254) |
| 2025-11-23 | Dynamic Geometry, Spatiotemporal, VGGT | Huazhong University of Science and Technology | [4D-VGGT: A General Foundation Model with SpatioTemporal Awareness for Dynamic Scene Geometry Estimation](https://arxiv.org/abs/2511.18416) | arXiv | [paper](https://arxiv.org/abs/2511.18416) |
| 2025-11-07 | Motion-Aware, Monocular Video, Bundle Adjustment | KAIST | [4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes](https://arxiv.org/abs/2511.05229) | NeurIPS 2025 | [paper](https://arxiv.org/abs/2511.05229) |
| 2025-10-20 | VGGT-4D, Pose/Geometry, Dynamic Mask | Harvard | [PAGE-4D: Disentangled Pose and Geometry Estimation for 4D Perception](https://arxiv.org/abs/2510.17568) | ICLR 2026 | [project](https://page4d.github.io/) |
| 2025-10 | 4D Tracking, Feed-Forward, Pointmap, Tracking | MPI / UC Berkeley | [St4RTrack: Simultaneous 4D Reconstruction and Tracking](https://openaccess.thecvf.com/content/ICCV2025/html/Bae_St4RTrack_Simultaneous_4D_Reconstruction_and_Tracking_in_the_World_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Bae_St4RTrack_Simultaneous_4D_Reconstruction_and_Tracking_in_the_World_ICCV_2025_paper.html) |
| 2025-08-18 | 3D Reconstruction, Human Motion, Video | Shanghai AI Lab | [Human3R: Reconstructing 3D Human Avatars from Monocular Video](https://arxiv.org/abs/2508.09983) | CVPR 2025 | [project](https://human3r.github.io/) |
| 2025-07 | Sparse Camera, 4DGS, Neural Decay, CVPR 2026 | Authors | [4C4D: 4 Camera 4D Gaussian Splatting](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_4C4D_4_Camera_4D_Gaussian_Splatting_CVPR_2026_paper.html) | CVPR 2026 | [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_4C4D_4_Camera_4D_Gaussian_Splatting_CVPR_2026_paper.html) |
| 2025-07 | Human, Multi-View, Sparse, Robust, RoGSplat | Authors | [RoGSplat: Robust Generalizable Human Gaussian Splatting](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_RoGSplat_Robust_Generalizable_Human_Gaussian_Splatting_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_RoGSplat_Robust_Generalizable_Human_Gaussian_Splatting_CVPR_2025_paper.html) |
| 2025-06-10 | Online, Dynamic 3DGS, Uncalibrated Video | University of British Columbia | [StreamSplat: Towards Online Dynamic 3D Reconstruction from Uncalibrated Video Streams](https://arxiv.org/abs/2506.08862) | ICLR 2026 | [project](https://streamsplat3d.github.io/) / [github](https://github.com/wwsource/StreamSplat) |
| 2025-06-09 | 4DGS, Transformer, Monocular Video | Meta Reality Labs | [4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](https://arxiv.org/abs/2506.08015) | NeurIPS 2025 Spotlight | [project](https://4dgt.github.io/) |
| 2025-06-09 | Dynamic Human, Temporal Consistency, 4D | Tsinghua | [CARI4D: Cross-Modal Alignment and Reconstruction for Interactive 4D Human](https://arxiv.org/abs/2506.09623) | CVPR 2025 | [project](https://cari4d.github.io/) |
| 2025-06-01 | Multi-Object, 4D, In-the-Wild Videos | CMU | [GenMOJO: Robust Multi-Object 4D Generation for In-the-wild Videos](https://arxiv.org/abs/2503.18594) | CVPR 2025 | [project](https://genmojo.github.io/) |
| 2025-06-01 | 4D, Dual Correspondences, Dynamic Video | NUS / Shanghai AI Lab | [C4D: 4D Made from 3D through Dual Correspondences](https://arxiv.org/abs/2505.20738) | ICCV 2025 | [project](https://littlepure2333.github.io/C4D/) |
| 2025-06-01 | Video Generators, 4D Geometry | Oxford VGG / NAVER LABS | [Geo4D: Leveraging Video Generators for Geometric 4D Scene Reconstruction](https://arxiv.org/abs/2506.01417) | ICCV 2025 Highlight | [paper](https://arxiv.org/abs/2506.01417) |
| 2025-06 | Self-Supervised, Dynamic, Driving, Flow | Authors | [SplatFlow: Self-Supervised Dynamic 3DGS with Neural Motion Flow](https://openaccess.thecvf.com/content/CVPR2025/html/Han_SplatFlow_Self-Supervised_Dynamic_Gaussian_Splatting_for_Autonomous_Driving_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Han_SplatFlow_Self-Supervised_Dynamic_Gaussian_Splatting_for_Autonomous_Driving_CVPR_2025_paper.html) |
| 2025-06 | Single Image, Animatable, Avatar, 4DGS | Authors | [AniGS: Animatable Gaussian Avatar from a Single Image](https://openaccess.thecvf.com/content/CVPR2025/html/Shao_AniGS_Animatable_Gaussian_Avatar_from_a_Single_Image_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Shao_AniGS_Animatable_Gaussian_Avatar_from_a_Single_Image_CVPR_2025_paper.html) |
| 2025-06 | Few-Shot, Personal Avatar, Highlight | Authors | [FRESA: Personalized 3D Human Avatar from Few Images](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_FRESA_Personalized_3D_Human_Avatar_from_Few_Images_CVPR_2025_paper.html) | CVPR 2025 Highlight | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_FRESA_Personalized_3D_Human_Avatar_from_Few_Images_CVPR_2025_paper.html) |
| 2025-06 | Real-Time Avatar, 166fps, Gaussian, Highlight | Authors | [MMLP-Human: Real-Time High-Fidelity Gaussian Human Avatar](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_MMLP-Human_Real-Time_High-Fidelity_Human_Avatar_with_Gaussian_Splatting_CVPR_2025_paper.html) | CVPR 2025 Highlight | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_MMLP-Human_Real-Time_High-Fidelity_Human_Avatar_with_Gaussian_Splatting_CVPR_2025_paper.html) |
| 2025-06 | Layered Avatar, Hair, Face, Meta | Authors | [LUCAS: Layered Universal Codec Avatars](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_LUCAS_Layered_Universal_Codec_Avatars_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_LUCAS_Layered_Universal_Codec_Avatars_CVPR_2025_paper.html) |
| 2025-05-25 | 4D Generation, Multi-View Video, Diffusion | Google | [CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models](https://arxiv.org/abs/2411.18613) | CVPR 2025 | [project](https://cat-4d.github.io/) |
| 2025-05-01 | 4D Pointmaps, Dynamic-Static Disentanglement | KAIST / ETH / Sony | [D2USt3R: Enhancing 3D Reconstruction with 4D Pointmaps for Dynamic Scenes](https://arxiv.org/abs/2505.09491) | NeurIPS 2025 | [project](https://cvlab-kaist.github.io/DDUSt3R/) |
| 2025-05-01 | Training-Free, Motion Disentangle, DUSt3R | Westlake / MPI | [Easi3R: Estimating Disentangled Motion from DUSt3R Without Training](https://arxiv.org/abs/2505.01513) | ICCV 2025 | [project](https://easi3r.github.io/) |
| 2025-04-08 | Neural Rendering, Human, No Eyes | University of Cambridge | [Seeing Without Eyes: Neural Human Rendering from Monocular Video](https://arxiv.org/abs/2504.04667) | CVPR 2025 | [project](https://seeing-without-eyes.github.io/) |
| 2025-01-22 | 3D Reconstruction, Canonical, Multi-View | Stanford | [UniCon3R: Unified 3D Reconstruction and Recognition](https://arxiv.org/abs/2501.12887) | CVPR 2025 | [project](https://unicon3r.github.io/) |
| 2024-12-05 | Dynamic Geometry, DUSt3R, Motion | University of Oxford | [MonST3R: Estimating Geometry in the Presence of Motion](https://arxiv.org/abs/2410.21193) | ICLR 2025 | [project](https://monst3r.github.io/) / [github](https://github.com/Junyi42/monst3r) |

#### 3.3.2 Deformation Graphs & Canonical Spaces

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-02-12 | 4D Dynamic, Monocular Video, Tree-Chains | Cornell | [WorldTree: Towards 4D Dynamic Worlds from Monocular Video using Tree-Chains](https://arxiv.org/abs/2602.11845) | ICLR 2026 | [paper](https://arxiv.org/abs/2602.11845) |
| 2025-11-12 | 4D Scene, Feed-Forward, Controllable, Video Diffusion | Shanghai AI Lab | [Diff4Splat: Controllable 4D Scene Generation with Latent Dynamic Reconstruction Models](https://arxiv.org/abs/2511.00503) | CVPR 2026 | [paper](https://arxiv.org/abs/2511.00503) |
| 2025-10-15 | Dynamic 4D, Gaussian, Canonical | Zhejiang University | [Director: Directed Generative Models for 4D Scene Evolution](https://arxiv.org/abs/2510.13229) | CVPR 2025 | [project](https://director-4d.github.io/) |
| 2025-07 | Surface, Gaussian Surfels, 2DGS, Sparse-View, Spotlight | Authors | [MAtCha Gaussians: Atlas Charting with 2D Gaussian Surfels](https://openaccess.thecvf.com/content/CVPR2025/html/Li_MAtCha_Gaussians_Atlas_Charting_with_2D_Gaussian_Surfels_CVPR_2025_paper.html) | CVPR 2025 Spotlight | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Li_MAtCha_Gaussians_Atlas_Charting_with_2D_Gaussian_Surfels_CVPR_2025_paper.html) |
| 2025-07 | SDF+3DGS, Hybrid, Surface, ICCV | Authors | [SurfaceSplat: SDF+3DGS Hybrid Surface Reconstruction](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_SurfaceSplat_Hybrid_Surface_Reconstruction_with_SDF_and_3DGS_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_SurfaceSplat_Hybrid_Surface_Reconstruction_with_SDF_and_3DGS_ICCV_2025_paper.html) |
| 2025-07 | Sparse-View, Implicit, Voxel, Consistency | Authors | [SparseRecon: Sparse-View Implicit Surface Reconstruction](https://openaccess.thecvf.com/content/ICCV2025/html/Li_SparseRecon_Voxel_Rendering_for_Sparse-View_Implicit_Surface_Reconstruction_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Li_SparseRecon_Voxel_Rendering_for_Sparse-View_Implicit_Surface_Reconstruction_ICCV_2025_paper.html) |
| 2025-07 | Low-Texture, Reflection, Unified, +21% | Authors | [HiNeuS: Unified Neural Implicit Surface Reconstruction](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_HiNeuS_A_Unified_Neural_Implicit_Surface_Reconstruction_Framework_CVPR_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_HiNeuS_A_Unified_Neural_Implicit_Surface_Reconstruction_Framework_CVPR_2025_paper.html) |
| 2025-07 | Multi-Baseline, Generalizable, Gaussian | Authors | [MuGS: Multi-Baseline Generalizable Gaussian Splatting](https://openaccess.thecvf.com/content/ICCV2025/html/Wei_MuGS_Multi-Baseline_Generalizable_Gaussian_Splatting_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wei_MuGS_Multi-Baseline_Generalizable_Gaussian_Splatting_ICCV_2025_paper.html) |
| 2025-06 | Joint Human+Scene, MASt3R Extension | Authors | [HAMSt3R: Joint Human and Scene 3D Reconstruction](https://openaccess.thecvf.com/content/ICCV2025/html/Pang_HAMSt3R_Joint_Human_and_Scene_3D_Reconstruction_ICCV_2025_paper.html) | ICCV 2025 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Pang_HAMSt3R_Joint_Human_and_Scene_3D_Reconstruction_ICCV_2025_paper.html) |
| 2024-11-20 | 4D Reconstruction, Gaussian Splatting, Forward | Shanghai AI Lab | [Forge4D: Gaussian Splatting for Forward Facing 4D Reconstruction](https://arxiv.org/abs/2411.13456) | arXiv | [paper](https://arxiv.org/abs/2411.13456) |

<h2 id="-4-3d-generation">🎛️ 4. 3D Generation</h2>

This section tracks methods that create new 3D assets, parts, articulated objects, scenes, and editable 3D worlds, with emphasis on physical and simulation use.

<a id="41-object-level-generation"></a>

### 4.1 Object-Level Generation

#### 4.1.1 Image/Text to 3D Mesh

##### Single Image / Text-Conditioned Object Mesh

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Image-to-3DGS, Sparse Voxel, High-Fidelity Assets | The Australian National University | [FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874) | arXiv | [paper](https://arxiv.org/abs/2606.24874) |
| 2026-06-23 | Vehicle Assets, 3D-Consistent Views, Simulation | Shanghai Jiao Tong University | [3DCarGen: Scalable 3D Car Generation via 3D-consistent Multi-view Synthesis](https://arxiv.org/abs/2606.24257) | arXiv | [paper](https://arxiv.org/abs/2606.24257) |
| 2026-06-22 | Constraint Meshes, Controllable Assets, TRELLIS | University of Tübingen | [Arbor: Explicit Geometric Conditioning for Controllable 3D Asset Generation](https://arxiv.org/abs/2606.23514) | arXiv | [project](https://arbor.jdihlmann.com/) |
| 2026-05-22 | Image-to-3D, Deployable Mesh, UV, Real-Time | Meta Reality Labs | [AssetGen: Deployable 3D Asset Generation at Interactive Speed](https://arxiv.org/abs/2605.26137) | arXiv | [paper](https://arxiv.org/abs/2605.26137) |
| 2026-05-11 | Pixel-Aligned, Image-to-3D, PBR, Multi-View | Tencent ARC | [Pixal3D: Pixel-Aligned 3D Generation from Images](https://arxiv.org/abs/2605.10922) | SIGGRAPH 2026 | [project](https://ldyang694.github.io/projects/pixal3d/) / [github](https://github.com/TencentARC/Pixal3D) / [demo](https://huggingface.co/spaces/TencentARC/Pixal3D) |
| 2026-05-01 | Pose-Aware, Diffusion, 3D Geometry, Direct | Renmin University | [PAD: Pose-Aware Diffusion for 3D Generation](https://arxiv.org/abs/2605.00345) | arXiv | [paper](https://arxiv.org/abs/2605.00345) |
| 2026-04-22 | Simulation-Ready, PBR, Part-Aware, Articulation | ByteDance Seed | [Seed3D 2.0: Advancing High-Fidelity Simulation-Ready 3D Content Generation](https://arxiv.org/abs/2605.13862) | arXiv | [demo](https://exp.volcengine.com/ark/vision?mode=vision&modelId=doubao-seed3d-2-0-260328&tab=Gen3D) |
| 2025-12-16 | Image-to-3D, O-Voxel, PBR Materials | Microsoft | [Native and Compact Structured Latents for 3D Generation](https://arxiv.org/abs/2512.14692) | arXiv | [github](https://github.com/microsoft/TRELLIS.2) / [model](https://huggingface.co/microsoft/TRELLIS.2-4B) |
| 2025-11-20 | Single Image, Multi-Object, Layout, SAM 3D | Meta AI | [SAM 3D: 3Dfy Anything in Images](https://arxiv.org/abs/2511.16624) | arXiv | [github](https://github.com/facebookresearch/sam-3d-objects) |
| 2025-10-23 | Single Image, Pose-Grounded, Flow Matching | Meta AI | [CUPID: Generative 3D Reconstruction via Joint Object and Pose Modeling](https://arxiv.org/abs/2510.20776) | arXiv | [project](https://cupid3d.github.io/) |
| 2025-10-09 | PBR, Material Diffusion, Relighting, Single Image | Stability AI | [SViM3D: Stable Video Material Diffusion for Single Image 3D Generation](https://arxiv.org/abs/2510.08271) | arXiv | [paper](https://arxiv.org/abs/2510.08271) |
| 2025-06-18 | Image-to-3D, PBR Materials, Production Assets | Tencent | [Hunyuan3D 2.1: From Images to High-Fidelity 3D Assets with Production-Ready PBR Material](https://arxiv.org/abs/2506.15442) | arXiv | [github](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) / [model](https://huggingface.co/tencent/Hunyuan3D-2.1) |
| 2025-06-12 | Text-to-3D, 3D-DiT, Interactive Refinement | HKUST | [CraftsMan3D: High-fidelity Mesh Generation with 3D Native Generation and Interactive Geometry Refiner](https://arxiv.org/abs/2405.14979) | arXiv | [github](https://github.com/wyysf-98/CraftsMan3D) |
| 2025-06-10 | Text/Image-to-3D, Bundle Image, Data-Efficient (147K) | HKUST(GZ) | [Kiss3DGen: Repurposing Image Diffusion Models for 3D Asset Generation](https://arxiv.org/abs/2503.01370) | arXiv | [github](https://github.com/jimmy-766/Kiss3DGen) |
| 2025-05-23 | Gigascale 3D, Sparse Volume, Image Conditioning | Nanjing University | [Direct3D-S2: Gigascale 3D Generation Made Easy with Spatial Sparse Attention](https://arxiv.org/abs/2505.17412) | NeurIPS 2025 | [project](https://nju3dv.github.io/projects/Direct3D-S2/) / [github](https://github.com/DreamTechAI/Direct3D-S2) |
| 2025-05-12 | Textured Assets, Controllable 3D, Open Framework | StepFun | [Step1X-3D: Towards High-Fidelity and Controllable Generation of Textured 3D Assets](https://arxiv.org/abs/2505.07747) | arXiv | [github](https://github.com/stepfun-ai/Step1X-3D) |
| 2025-05-07 | Image-to-3D, PBR Textured Mesh, Render-Enhanced Auto-Encoder | Tsinghua | [MeshGen: Generating PBR Textured Mesh with Render-Enhanced Auto-Encoder and Generative Data Augmentation](https://arxiv.org/abs/2505.04656) | CVPR 2025 | [project](https://heheyas.github.io/MeshGen/) |
| 2025-03-28 | Geometry Detail, Normal Bridging, Image-to-3D | Cornell | [Hi3DGen: High-fidelity 3D Geometry Generation from Images via Normal Bridging](https://arxiv.org/abs/2503.22236) | arXiv | [project](https://stable-x.github.io/Hi3DGen/) |
| 2025-03 | 3DTopia-XL, Primitive Diffusion, Large Scale, Highlight | NTU / PKU | [3DTopia-XL: Scaling High-quality 3D Asset Generation via Primitive Diffusion](https://arxiv.org/abs/2409.12957) | CVPR 2025 Highlight | [project](https://3dtopia.github.io/3DTopia-XL/) |
| 2025-02-10 | Shape Synthesis, Rectified Flow, Image-to-3D | VAST AI / Tripo | [TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models](https://arxiv.org/abs/2502.06608) | arXiv | [github](https://github.com/VAST-AI-Research/TripoSG) / [model](https://huggingface.co/VAST-AI/TripoSG) |
| 2025-01-21 | Image/Text-to-3D, Mesh, Texture | Tencent | [Hunyuan3D 2.0: Scaling Diffusion Models for High Resolution Textured 3D Assets Generation](https://arxiv.org/abs/2501.12202) | arXiv | [github](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) |
| 2025-01-08 | Point-Aware, Interactive Editing, Single Image | Stability AI / UIUC | [SPAR3D: Stable Point-Aware Reconstruction of 3D Objects from Single Images](https://arxiv.org/abs/2501.04689) | arXiv | [project](https://spar3d.github.io/) / [model](https://huggingface.co/stabilityai/stable-point-aware-3d) |
| 2024-11-11 | Text/Image-to-3D, PBR, Multi-View Diffusion | NVIDIA | [Edify 3D: Scalable High-Quality 3D Asset Generation](https://arxiv.org/abs/2411.07135) | arXiv | [project](https://research.nvidia.com/labs/dir/edify-3d/) |
| 2024-11-05 | Text-to-Mesh, PBR, Geometry+Texture | Meta | [Meta 3D AssetGen: Text-to-Mesh Generation with High-Quality Geometry, Texture, and PBR Materials](https://assetgen.github.io/static/AssetGen.pdf) | NeurIPS 2024 | [project](https://assetgen.github.io/) |
| 2024-09 | PolyGen, Autoregressive, Mesh, DeepMind | DeepMind | [PolyGen: An Autoregressive Generative Model of 3D Meshes](https://arxiv.org/abs/2002.10880) | ICML 2020 | [paper](https://arxiv.org/abs/2002.10880) |
| 2024-08-01 | Fast Mesh, UV Unwrap, Material Disentanglement | Stability AI | [Stable Fast 3D: Stable Fast 3D Mesh Reconstruction with UV-unwrapping and Illumination Disentanglement](https://arxiv.org/abs/2408.00653) | arXiv | [project](https://stable-fast-3d.github.io/) / [github](https://github.com/Stability-AI/stable-fast-3d) |
| 2024-08 | MVDiffusion++, Dense High-Res, Sparse-View | Simon Fraser / Meta | [MVDiffusion++: A Dense High-Resolution Multi-view Diffusion Model](https://arxiv.org/abs/2402.12712) | ECCV 2024 | [paper](https://arxiv.org/abs/2402.12712) |
| 2024-06 | GET3D, Generative, Textured Shapes, Images Only | NVIDIA | [GET3D: A Generative Model of High Quality 3D Textured Shapes](https://arxiv.org/abs/2209.11163) | NeurIPS 2022 | [github](https://github.com/nvlabs/get3d) |
| 2024-05-30 | High-Quality Mesh, Multi-View Normals, ISOMER | Tsinghua | [Unique3D: High-Quality and Efficient 3D Mesh Generation from a Single Image](https://arxiv.org/abs/2405.20343) | arXiv | [project](https://wukailu.github.io/Unique3D/) |
| 2024-05-19 | Multi-View Diffusion, Row-Wise Attention, Mesh | University of Hong Kong | [Era3D: High-Resolution Multiview Diffusion using Efficient Row-wise Attention](https://arxiv.org/abs/2405.11616) | arXiv | [project](https://penghtyx.github.io/Era3D/) |
| 2024-04-10 | Single Image, Sparse-View LRM, Mesh | Tencent ARC | [InstantMesh: Efficient 3D Mesh Generation from a Single Image with Sparse-view Large Reconstruction Models](https://arxiv.org/abs/2404.07191) | arXiv | [github](https://github.com/TencentARC/InstantMesh) |
| 2024-04 | Magic123, One Image to 3D, 2D+3D Priors | KAUST / Snap | [Magic123: One Image to High-Quality 3D Object Using Both 2D and 3D Diffusion Priors](https://arxiv.org/abs/2306.17843) | CVPR 2024 | [project](https://magic123-project.github.io/) |
| 2024-04 | MVDiffusion, Multi-View, Consistent, Single Image | Simon Fraser | [MVDiffusion: Multi-view Consistent Image Generation from a Single Image](https://arxiv.org/abs/2310.17220) | CVPR 2024 | [github](https://github.com/Tosca18/MVDiffusion) |
| 2024-04 | MeshGPT, Triangle Mesh, Decoder-Only, Transformer | TUM | [MeshGPT: Generating Triangle Meshes with Decoder-Only Transformers](https://arxiv.org/abs/2311.15475) | CVPR 2024 | [project](https://nihalsid.github.io/mesh-gpt/) |
| 2024-04 | LION, Latent Point Diffusion, Shape | NVIDIA | [LION: Latent Point Diffusion Models for 3D Shape Generation](https://arxiv.org/abs/2210.06978) | NeurIPS 2023 | [github](https://github.com/nvlabs/lion) |
| 2024-04 | AutoSDF, Shape Prior, 3D Completion | CMU | [AutoSDF: Shape Priors for 3D Completion, Reconstruction and Generation](https://arxiv.org/abs/2203.09516) | CVPR 2022 | [paper](https://arxiv.org/abs/2203.09516) |
| 2024-03-18 | Single Image, Orbital Video, Multi-View Prior | Stability AI | [SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image using Latent Video Diffusion](https://arxiv.org/abs/2403.12008) | arXiv | [project](https://sv3d.github.io/) |
| 2024-03-07 | Textured Mesh, Convolutional Reconstruction, Single Image | Shanghai AI Lab | [CRM: Single Image to 3D Textured Mesh with Convolutional Reconstruction Model](https://arxiv.org/abs/2403.05034) | arXiv | [project](https://ml.cs.tsinghua.edu.cn/~zhengyi/CRM/) |
| 2024-03 | LucidDreamer, Interval Score, Text-to-3D, Highlight | HKUST(GZ) | [LucidDreamer: Towards High-Fidelity Text-to-3D via Interval Score Matching](https://arxiv.org/abs/2311.11284) | CVPR 2024 Highlight | [project](https://luciddreamer-cvpr24.github.io/) |
| 2024-03 | 3DTopia, Hybrid Diffusion, Text-to-3D | NTU / PKU | [3DTopia: Large Text-to-3D Generation Model with Hybrid Diffusion Priors](https://arxiv.org/abs/2403.02234) | CVPR 2024 | [project](https://3dtopia.github.io/) |
| 2024-03 | GaussianDreamer, Text-to-3DGS, 2D+3D Diffusion | HUST | [GaussianDreamer: Fast Generation from Text to 3D Gaussians](https://arxiv.org/abs/2406.18462) | CVPR 2024 | [github](https://github.com/hustvl/GaussianDreamer) |
| 2024-03 | ReconFusion, Diffusion Prior, 3D Reconstruction | Columbia / Google | [ReconFusion: 3D Reconstruction with Diffusion Priors](https://arxiv.org/abs/2312.02981) | CVPR 2024 | [paper](https://arxiv.org/abs/2312.02981) |
| 2024-03 | XCube, Sparse Voxel, Large-Scale, Highlight | NVIDIA | [XCube: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies](https://arxiv.org/abs/2312.03806) | CVPR 2024 Highlight | [project](https://research.nvidia.com/labs/toronto-ai/xcube/) |
| 2024-03 | DiffRF, Rendering-Guided, Radiance Field Diffusion, Highlight | TUM / Meta | [DiffRF: Rendering-Guided 3D Radiance Field Diffusion](https://arxiv.org/abs/2212.01206) | CVPR 2023 Highlight | [paper](https://arxiv.org/abs/2212.01206) |
| 2024-02-07 | Multi-View Gaussian, Fast 3D Content, Image/Text | Peking University | [LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation](https://arxiv.org/abs/2402.05054) | ECCV 2024 Oral | [github](https://github.com/3DTopia/LGM) |
| 2024-01 | DreamCraft3D, Bootstrapped, Hierarchical, 3D | DeepSeek / Tsinghua | [DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior](https://arxiv.org/abs/2310.16818) | ICLR 2024 | [project](https://dreamcraft3d.github.io/) |
| 2024-01 | DreamTime, Improved SDS, Optimization | IDEA / HKU | [DreamTime: An Improved Optimization for Diffusion-Guided 3D](https://arxiv.org/abs/2306.12422) | ICLR 2024 | [paper](https://arxiv.org/abs/2306.12422) |
| 2024-01 | HiFA, High-Fidelity, Text-to-3D, Advanced Guidance | UIUC | [HiFA: High-fidelity Text-to-3D with Advanced Diffusion Guidance](https://arxiv.org/abs/2305.18766) | ICLR 2024 | [paper](https://arxiv.org/abs/2305.18766) |
| 2024-01 | DMV3D, Multi-View Diffusion, 3D LRM, NeRF | Adobe / Stanford | [DMV3D: Denoising Multi-View Diffusion using 3D Large Reconstruction Model](https://arxiv.org/abs/2311.09217) | NeurIPS 2023 | [paper](https://arxiv.org/abs/2311.09217) |
| 2024-01 | 3DShape2VecSet, Neural Fields, Diffusion, Mesh | KAUST / TUM | [3DShape2VecSet: A 3D Shape Representation for Neural Fields and Diffusion](https://arxiv.org/abs/2301.11445) | SIGGRAPH 2023 (ACM TOG) | [github](https://github.com/1zb/3DShape2VecSet) |
| 2023-10-23 | Cross-Domain Diffusion, Multi-View Normals, Mesh | HKUST | [Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://arxiv.org/abs/2310.15008) | CVPR 2024 Highlight | [github](https://github.com/xxlong0/Wonder3D) |
| 2023-10-23 | Single Image, Consistent Multi-View Diffusion | UC San Diego | [Zero123++: a Single Image to Consistent Multi-view Diffusion Base Model](https://arxiv.org/abs/2310.15110) | arXiv | [github](https://github.com/SUDO-AI-3D/zero123plus) |
| 2023-09-01 | GS, SDS, Efficient 3D Content Creation | PKU / NTU | [DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://arxiv.org/abs/2309.16653) | ICLR 2024 Oral | [github](https://github.com/dreamgaussian/dreamgaussian) |
| 2023-09-01 | Multi-View Consistent Images, Single Image | HKU | [SyncDreamer: Generating Multiview-consistent Images from a Single-view Image](https://arxiv.org/abs/2309.01388) | ICLR 2024 Spotlight | [github](https://github.com/liuyuan-pal/SyncDreamer) |
| 2023-09 | Make-It-3D, Single Image, Diffusion Prior | SJTU / Microsoft | [Make-It-3D: High-Fidelity 3D Creation from A Single Image with Diffusion Prior](https://arxiv.org/abs/2303.14184) | ICCV 2023 | [project](https://make-it-3d.github.io/) |
| 2023-09 | ATT3D, Amortized, Text-to-3D | NVIDIA | [ATT3D: Amortized Text-to-3D Object Synthesis](https://arxiv.org/abs/2306.07349) | ICCV 2023 | [paper](https://arxiv.org/abs/2306.07349) |
| 2023-08-01 | Multi-View Diffusion, 3D Generation | UCSD / ByteDance | [MVDream: Multi-view Diffusion for 3D Generation](https://arxiv.org/abs/2308.16512) | ICLR 2024 | [project](https://mv-dream.github.io/) |
| 2023-08 | RealFusion, Single Image, 360°, 3D | Oxford VGG | [RealFusion: 360° Reconstruction of Any Object from a Single Image](https://arxiv.org/abs/2302.10663) | CVPR 2023 | [project](https://lukemelas.github.io/realfusion/) |
| 2023-08 | IT3D, Explicit View, Text-to-3D | NTU | [IT3D: Improved Text-to-3D with Explicit View Synthesis](https://arxiv.org/abs/2308.11473) | NeurIPS 2023 | [paper](https://arxiv.org/abs/2308.11473) |
| 2023-07 | Text-to-3D, Geometry+Appearance Disentangle | SCUT | [Fantasia3D: Disentangling Geometry and Appearance for Text-to-3D](https://arxiv.org/abs/2303.13873) | ICCV 2023 | [project](https://fantasia3d.github.io/) |
| 2023-06-27 | Single Image, Optimization-Free, Mesh | Shanghai AI Lab | [One-2-3-45: Any Single Image to 3D Mesh in 45 Seconds without Per-Shape Optimization](https://arxiv.org/abs/2306.16928) | NeurIPS 2023 | [github](https://github.com/One-2-3-45/One-2-3-45) |
| 2023-06 | Text-to-3D, Score Jacobian Chaining, 2D Diffusion | TTI-Chicago | [Score Jacobian Chaining: Lifting Pretrained 2D Diffusion for 3D](https://arxiv.org/abs/2212.00774) | CVPR 2023 | [paper](https://arxiv.org/abs/2212.00774) |
| 2023-05 | Text-to-3D, Variational SDS, High-Fidelity, Spotlight | Tsinghua | [ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation](https://arxiv.org/abs/2305.16213) | NeurIPS 2023 Spotlight | [project](https://ml.cs.tsinghua.edu.cn/~zhengyi/prolificdreamer/) |
| 2023-04 | Text-to-3D, High-Res, Coarse-to-Fine, Highlight | NVIDIA | [Magic3D: High-Resolution Text-to-3D Content Creation](https://arxiv.org/abs/2211.10440) | CVPR 2023 Highlight | [paper](https://arxiv.org/abs/2211.10440) |
| 2023-03 | Zero-1-to-3, Zero-Shot, Single Image to 3D | Columbia / TRI | [Zero-1-to-3: Zero-shot One Image to 3D Object](https://arxiv.org/abs/2303.11328) | ICCV 2023 | [github](https://github.com/cvlab-columbia/zero123) |
| 2023-01 | Text-to-3D, Score Distillation, SDS, 2D Diffusion, Outstanding Paper | Google Research | [DreamFusion: Text-to-3D using 2D Diffusion](https://arxiv.org/abs/2209.14988) | ICLR 2023 Outstanding Paper | [project](https://dreamfusion3d.github.io/) |

##### Multi-Image / Multi-View Object Mesh

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Multi-View + LiDAR, Vehicle Assets, TRELLIS | Shanghai Jiao Tong University | [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301) | arXiv | [github](https://github.com/HongliXiao/MM-TRELLIS) |
| 2026-05-05 | Feed-Forward, Generative Priors, Pose, Multi-View | Tsinghua | [Mix3R: Mixing Feed-forward Reconstruction and Generative 3D Priors for Joint Multi-view Aligned 3D Reconstruction and Pose Estimation](https://arxiv.org/abs/2605.03359) | arXiv | [project](https://jsnln.github.io/mix3r/) |
| 2026-03-12 | Multi-View, SAM3D, Layout-Aware, Physical Plausibility | Peking University | [MV-SAM3D: Adaptive Multi-View Fusion for Layout-Aware 3D Generation](https://arxiv.org/abs/2603.11633) | arXiv | [github](https://github.com/devinli123/MV-SAM3D) |
| 2026-01-16 | Casual Capture, Posed Multi-View, Metric Shape | Meta AI | [ShapeR: Robust Conditional 3D Shape Generation from Casual Captures](https://arxiv.org/abs/2601.11514) | arXiv | [paper](https://arxiv.org/abs/2601.11514) |
| 2025-11-12 | Multi-Image Fusion, Region Control, TRELLIS | Zhejiang University | [Fuse3D: Generating 3D Assets Controlled by Multi-Image Fusion](https://arxiv.org/abs/2602.17040) | SIGGRAPH Asia 2025 | [project](https://fuse3d.org/) / [github](https://github.com/JINNMnm/Fuse3D) |
| 2025-03-18 | Multi-View Image-to-Shape, Hunyuan3D-DiT | Tencent | [Hunyuan3D 2.0 MV](https://huggingface.co/tencent/Hunyuan3D-2mv) | Model | [github](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) / [model](https://huggingface.co/tencent/Hunyuan3D-2mv) |
| 2024-02-05 | Scalable View Synthesis, Single/Multi-Image 3D | KAUST | [EscherNet: A Generative Model for Scalable View Synthesis](https://arxiv.org/abs/2402.03908) | CVPR 2024 | [project](https://kxhit.github.io/EscherNet/) |
| 2019-08-05 | Multi-View Images, Mesh Deformation, Shape Refinement | National Tsing Hua University | [Pixel2Mesh++: Multi-View 3D Mesh Generation via Deformation](https://arxiv.org/abs/1908.01491) | ICCV 2019 | [github](https://github.com/walsvid/Pixel2MeshPlusPlus) |

#### 4.1.2 Texture & Material Generation (PBR)

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-03-01 | VLM-Guided, PBR Texture | 3D AIGC | [TexGaussian: Generating High-quality PBR Material via Octree-based 3D Gaussian Splatting](https://arxiv.org/abs/2411.06334) | CVPR 2025 | [project](https://3d-aigc.github.io/TexGaussian/) |
| 2024-10-18 | PBR Material, SVBRDF, Text-to-Material | Adobe | [MatFuse: Controllable Material Generation with Diffusion Models](https://arxiv.org/abs/2308.11408) | SIGGRAPH Asia 2024 | [project](https://gvecchio.com/matfuse/) |
| 2024-03-12 | Texture Generation, Mesh, Multi-View Consistency | Tencent | [Paint3D: Paint Anything 3D with Lighting-Less Texture Diffusion Models](https://arxiv.org/abs/2312.13913) | CVPR 2024 | [project](https://paint3d.github.io/) |
| 2024-03 | SyncMVD, Multi-View, Text-to-Texture | CUHK | [SyncMVD: Text-Guided Texturing by Synchronized Multi-View Diffusion](https://arxiv.org/abs/2311.12891) | CVPR 2024 | [paper](https://arxiv.org/abs/2311.12891) |
| 2024-03 | TextureDreamer, Geometry-Aware, Diffusion | UCSD / Meta | [TextureDreamer: Image-Guided Texture Synthesis](https://arxiv.org/abs/2401.09416) | CVPR 2024 | [paper](https://arxiv.org/abs/2401.09416) |
| 2024-03 | SceneTex, Indoor, Texture, Diffusion, Highlight | TUM / Snap | [SceneTex: High-Quality Texture Synthesis for Indoor Scenes](https://arxiv.org/abs/2311.17261) | CVPR 2024 Highlight | [paper](https://arxiv.org/abs/2311.17261) |
| 2023-09-21 | Texture, Material, Text-to-Texture | KAIST | [Text2Tex: Text-driven Texture Synthesis via Diffusion Models](https://arxiv.org/abs/2303.11396) | ICCV 2023 | [project](https://daveredrum.github.io/Text2Tex/) |
| 2023-03 | TEXTure, Text-Guided, 3D Texture, Diffusion | Tel Aviv University | [TEXTure: Text-Guided Texturing of 3D Shapes](https://arxiv.org/abs/2302.01721) | SIGGRAPH 2023 | [project](https://texturepaper.github.io/) |
| 2022-03 | nvdiffrec, 3D Mesh, Material, Lighting, Oral | NVIDIA | [nvdiffrec: Extracting Triangular 3D Models, Materials, and Lighting](https://arxiv.org/abs/2207.02446) | CVPR 2022 Oral | [github](https://github.com/NVlabs/nvdiffrec) |

<a id="42-part-level--articulated-generation"></a>

### 4.2 Part-Level & Articulated Generation

#### 4.2.1 Kinematic Structure Generation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-05-14 | Agentic Generation, Articraft-10K, URDF Assets | Authors | [Articraft: An Agentic System for Scalable Articulated 3D Asset Generation](https://arxiv.org/abs/2605.15187) | arXiv | [project](https://articraft3d.github.io/) / [github](https://github.com/mattzh72/articraft) |
| 2026-05-06 | Physics-Grounded, Kinematic, Simulation-Ready Assets | HKU | [PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World](https://arxiv.org/abs/2605.05163) | ICML 2026 | [project](https://hku-mmlab.github.io/PhysForge/) / [github](https://github.com/HKU-MMLab/PhysForge) |
| 2026-03-14 | URDF, Autoregressive, Simulation-Ready Assets | Authors | [URDF-Anything+: End-to-End Generation for Simulation-Ready Articulated Assets](https://arxiv.org/abs/2603.14010) | arXiv | [paper](https://arxiv.org/abs/2603.14010) |
| 2026-03-01 | Articulated Assets, 3D LLM, Kinematic Structure | Tsinghua | [ArtLLM: Generating Articulated Assets via 3D LLM](https://arxiv.org/abs/2603.01142) | CVPR 2026 | [paper](https://arxiv.org/abs/2603.01142) |
| 2025-12-12 | Articulation, Kinematic Tree, Feed-Forward, URDF-Ready | University of Oxford | [Particulate: Feed-Forward 3D Object Articulation](https://arxiv.org/abs/2512.11798) | arXiv | [project](https://ruiningli.com/particulate) |
| 2025-11-26 | Single Image, Open-Set Articulation, Unified Latent | ShanghaiTech | [UniArt: Unified 3D Representation for Generating 3D Articulated Objects with Open-Set Articulation](https://arxiv.org/abs/2511.21887) | arXiv | [paper](https://arxiv.org/abs/2511.21887) |
| 2025-11-17 | Sim-Ready Assets, Physical Properties, Single Image | NTU | [PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image](https://arxiv.org/abs/2511.13648) | CVPR 2026 | [paper](https://arxiv.org/abs/2511.13648) |
| 2025-11-02 | URDF, 3D MLLM, Articulated Objects | Tsinghua | [URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model](https://openreview.net/forum?id=g3EF5XsapH) | NeurIPS 2025 | [paper](https://arxiv.org/abs/2511.00940) |
| 2025-07-16 | Physical Properties, Scale, Material, Affordance | Nanyang Technological University | [PhysX-3D: Physical-Grounded 3D Asset Generation](https://arxiv.org/abs/2507.12465) | NeurIPS 2025 Spotlight | [project](https://physx-3d.github.io/) / [github](https://github.com/ziangcao0312/PhysX-3D) |
| 2025-04-17 | Simulation-Ready, Physical Materials, Dynamics | University of Massachusetts Amherst | [SOPHY: Generating Simulation-Ready Objects with Physical Materials](https://arxiv.org/abs/2504.12684) | WACV 2026 | [project](https://xjay18.github.io/SOPHY/) / [github](https://github.com/XJay18/SOPHY) |
| 2025-02-26 | Articulated Objects, 3DGS, Joint Estimation | Tsinghua | [ArtGS: Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459) | ICLR 2025 | [project](https://articulate-gs.github.io/) |
| 2025-02-17 | Articulation-Ready, Skeleton, Skinning, Benchmark | Nanyang Technological University | [MagicArticulate: Make Your 3D Models Articulation-Ready](https://arxiv.org/abs/2502.12135) | CVPR 2025 | [project](https://chaoyuesong.github.io/MagicArticulate) / [github](https://github.com/Seed3D/MagicArticulate) |
| 2024-09-26 | Open-Vocabulary, URDF, Articulation | Stanford | [Articulate Anything: Open-vocabulary 3D Articulated Object Generation](https://openreview.net/forum?id=6akuzEqP38) | ICLR 2025 | [project](https://articulate-anything.github.io/) |

#### 4.2.2 Part-Aware Assembly & Editing

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Garment Patterns, Simulation-Ready, Editing | University of Hong Kong | [PatternGSL: A Structured Specification Language for Template-Free and Simulation-Ready 3D Garments](https://arxiv.org/abs/2606.24564) | arXiv | [github](https://github.com/PatternGSL/PatternGSL) |
| 2026-05-27 | Part-Controllable, Open-Vocabulary, Game-Ready | Roblox | [CubePart: An Open-Vocabulary Part-Controllable 3D Generator](https://arxiv.org/abs/2605.28763) | SIGGRAPH 2026 | [project](https://cubepart.github.io/) / [model](https://huggingface.co/Roblox/cubepart) |
| 2025-09-10 | Part Decomposition, Editable, Production-Ready Assets | Tencent | [X-Part: High-Fidelity and Structure-Coherent Shape Decomposition](https://arxiv.org/abs/2509.08643) | Tech Report | [project](https://yanxinhao.github.io/X-Part/) |
| 2025-08-14 | Rigging, Animation, Skeleton, Skinning | Nanyang Technological University | [Puppeteer: Rig and Animate Your 3D Models](https://arxiv.org/abs/2508.10898) | NeurIPS 2025 Spotlight | [project](https://chaoyuesong.github.io/Puppeteer) / [github](https://github.com/Seed3D/Puppeteer) |
| 2025-06-05 | Part-Level Mesh, Compositional DiT, Single Image | University of Waterloo | [PartCrafter: Structured 3D Mesh Generation via Compositional Latent Diffusion Transformers](https://arxiv.org/abs/2506.05573) | arXiv | [project](https://wgsxm.github.io/projects/partcrafter/) |
| 2024-12-16 | Articulated Mesh, Part-by-Part, Hierarchical Transformer | Cornell | [MeshArt: Generating Articulated Meshes with Structure-Guided Transformers](https://arxiv.org/abs/2412.11596) | arXiv | [paper](https://arxiv.org/abs/2412.11596) |
| 2024-06-13 | Part-Aware, Shape Assembly, 3D Generation | Shanghai AI Lab | [Michelangelo: Conditional 3D Shape Generation based on Shape-Image-Text Aligned Latent Representation](https://arxiv.org/abs/2306.17115) | NeurIPS 2023 | [github](https://github.com/NeuralCarver/Michelangelo) |
| 2023-12-04 | Shape Program, Structure, Editable Assets | MIT | [Shape2Program: Learning to Infer Shape Programs from 3D Shapes](https://arxiv.org/abs/2312.08307) | arXiv | [project](https://shape2prog.csail.mit.edu/) |

<a id="43-scene-level-generation"></a>

### 4.3 Scene-Level Generation

#### 4.3.1 Layout & Procedural Generation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Triangle Splatting, Single-Image Scene, Game-Ready | Google Research | [FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876) | arXiv | [project](https://flat-splat.github.io/) |
| 2026-06-23 | Text-to-Scene, Video Priors, 3DGS Orbit | University of Bern | [OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799) | arXiv | [paper](https://arxiv.org/abs/2606.24799) |
| 2026-06-23 | Compositional 3D, Physical Interaction, Multi-View Consistency | China University of Petroleum (East China) | [Inclusive Interactive Collisions for Multi-View Consistent Compositional 3D Generation](https://arxiv.org/abs/2606.24206) | arXiv | [paper](https://arxiv.org/abs/2606.24206) |
| 2026-06-23 | Satellite-to-City, Textured Mesh, Urban Simulation | HKUST(GZ) | [Sat2City v2: Native 3D City Asset Generation from a Single Satellite Image](https://arxiv.org/abs/2606.24138) | arXiv | [paper](https://arxiv.org/abs/2606.24138) |
| 2026-06-08 | Satellite-to-3D, 3DGS, UAV Simulation | Amap-cvlab / Alibaba | [ABot-Earth 0.5: Generative 3D Earth Model](https://arxiv.org/abs/2606.09967) | arXiv | [project](https://abot-earth.amap.com/) |
| 2026-06-04 | Whole-Home Scenes, Floorplans, Interactive | Authors | [HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes](https://arxiv.org/abs/2606.06390) | arXiv | [paper](https://arxiv.org/abs/2606.06390) |
| 2026-05-28 | Physical Stability, Single Image, Scene Tree, Simulation | Carnegie Mellon University | [REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image](https://arxiv.org/abs/2605.30338) | arXiv | [project](https://rest3d.org/) |
| 2026-05-01 | Segment Map, Text-to-World, Controllable 3D Worlds | Seoul National University | [Map2World: Segment Map Conditioned Text to 3D World Generation](https://arxiv.org/abs/2605.00781) | arXiv | [paper](https://arxiv.org/abs/2605.00781) |
| 2026-04-15 | Multi-Modal World Model, 3D Gaussian, Navigation | Tencent | [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268) | arXiv | [project](https://3d-models.hunyuan.tencent.com/world/) |
| 2026-04-14 | Explorable 3D Worlds, Long Trajectory, 3DGS | NVIDIA | [Lyra 2.0: Explorable Generative 3D Worlds](https://arxiv.org/abs/2604.13036) | arXiv | [project](https://research.nvidia.com/labs/toronto-ai/lyra-2/) |
| 2026-04-06 | Single-Image Scene, In-Place Completion, ARSG-110K | Nankai University | [3D-Fixer: Coarse-to-Fine In-place Completion for 3D Scenes from a Single Image](https://arxiv.org/abs/2604.04406) | CVPR 2026 | [project](https://zx-yin.github.io/3dfixer/) / [github](https://github.com/HorizonRobotics/3D-Fixer) / [dataset](https://huggingface.co/datasets/HorizonRobotics/ARSG-110K) |
| 2026-03-31 | Town-Scale, Single Image, Latent Extension | Seoul National University | [Extend3D: Town-Scale 3D Generation](https://arxiv.org/abs/2603.29387) | CVPR 2026 | [project](https://seungwoo-yoon.github.io/extend3d-page/) |
| 2026-03-31 | Unbounded World, Flow Matching, Layouts | Princeton University | [WorldFlow3D: Flowing Through 3D Distributions for Unbounded World Generation](https://arxiv.org/abs/2603.29089) | arXiv | [project](https://light.princeton.edu/worldflow3d) |
| 2026-03-12 | Multi-Floor, Language-to-3D, Long-Horizon Tasks | Tsinghua | [MANSION: Multi-floor lANguage-to-3D Scene generatIOn for loNg-horizon tasks](https://arxiv.org/abs/2603.11554) | CVPR 2026 | [paper](https://arxiv.org/abs/2603.11554) |
| 2026-03-06 | Compositional Scene, Panoramic Image, Feed-Forward | NTU | [Pano3DComposer: Feed-Forward Compositional 3D Scene Generation from Single Panoramic Image](https://arxiv.org/abs/2603.05908) | CVPR 2026 | [paper](https://arxiv.org/abs/2603.05908) |
| 2026-02-10 | Agentic Scene Generation, Sim-Ready, SAGE-10k | NVIDIA | [SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://arxiv.org/abs/2602.10116) | CVPR 2026 | [project](https://research.nvidia.com/labs/dir/sage/) / [github](https://github.com/NVlabs/sage) |
| 2026-01-09 | Language-Guided, Infinite Worlds, Articulated Furniture | National Taiwan Univ | [SceneFoundry: Generating Interactive Infinite 3D Worlds](https://arxiv.org/abs/2601.05810) | arXiv | [project](https://anc891203.github.io/SceneFoundry/) |
| 2025-12-01 | Tabletop, Instance-Level, Interactive Scene, Text/Image | D-Robotics | [TabletopGen: Instance-Level Interactive 3D Tabletop Scene Generation from Text or Single Image](https://d-robotics-ai-lab.github.io/TabletopGen.project/) | arXiv | [project](https://d-robotics-ai-lab.github.io/TabletopGen.project/) |
| 2025-11-18 | Single-Image Scene, Gaussian World, Scene Generation | Tsinghua University | [GEN3D: Generating Domain-Free 3D Scenes from a Single Image](https://arxiv.org/abs/2511.14291) | arXiv | [paper](https://arxiv.org/abs/2511.14291) |
| 2025-08-11 | Panoramic, Explorable World, Matrix-Pano | Kunlun Wanwei | [Matrix-3D: Omnidirectional Explorable 3D World Generation](https://arxiv.org/abs/2508.08086) | arXiv | [project](https://matrix-3d.github.io/) / [github](https://github.com/SkyworkAI/Matrix-3D) |
| 2025-07-29 | Panoramic, Text/Image-to-World, Mesh Export | Tencent Hunyuan | [HunyuanWorld 1.0: Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels](https://arxiv.org/abs/2507.21809) | arXiv | [github](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) |
| 2025-06-25 | Explorable Scene, Novel-View Restoration, Consistency | Beijing Academy of AI | [WonderFree: Enhancing Novel View Quality and Cross-View Consistency for 3D Scene Exploration](https://arxiv.org/abs/2506.20590) | arXiv | [paper](https://arxiv.org/abs/2506.20590) |
| 2025-03-18 | Scene Layout, Optimization, Generation | Tsinghua | [HOG-Layout: Layout-Enhanced Scene Generation via Hierarchical Optimization](https://arxiv.org/abs/2503.10462) | arXiv | [project](https://hog-layout.github.io/) |
| 2025-02-28 | Octree, 3D Diffusion, Scene Generation | Zhejiang University | [Octree Diffusion: Hierarchical Scene Generation via Octree Structures](https://arxiv.org/abs/2502.14832) | arXiv | [project](https://octree-diffusion.github.io/) |
| 2025-01-15 | Gaussian, GPT, Scene Generation | Shanghai AI Lab | [GaussianGPT: Language-Driven Scene Generation with Gaussian Representation](https://arxiv.org/abs/2501.08734) | arXiv | [paper](https://arxiv.org/abs/2501.08734) |
| 2025-01 | GenXD, Any 3D and 4D, Scene Generation | NUS | [GenXD: Generating Any 3D and 4D Scenes](https://arxiv.org/abs/2411.02319) | ICLR 2025 | [paper](https://arxiv.org/abs/2411.02319) |
| 2024-12-20 | Scene Generation, Growing, Incremental | Tsinghua | [WorldGrow: Incremental 3D Scene Generation](https://arxiv.org/abs/2412.14572) | CVPR 2025 | [project](https://worldgrow.github.io/) |
| 2024-11-05 | Splatting, Fluents, Scene Understanding | University of Cambridge | [FluSplat: Fluent Scene Generation via Gaussian Splatting](https://arxiv.org/abs/2411.03472) | CVPR 2025 | [project](https://flusplat.github.io/) |
| 2024-10-17 | Procedural Scenes, Synthetic Data, Embodied AI | Princeton | [Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation](https://arxiv.org/abs/2406.11824) | NeurIPS 2024 | [project](https://infinigen.org/) / [github](https://github.com/princeton-vl/infinigen) |
| 2024-10 | SceneScape, Text-Driven, Consistent, Scene | Weizmann | [SceneScape: Text-Driven Consistent Scene Generation](https://arxiv.org/abs/2402.08108) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2402.08108) |
| 2024-09 | BlockFusion, Expandable, Tri-plane, SIGGRAPH | Tencent / UTokyo | [BlockFusion: Expandable 3D Scene Generation](https://arxiv.org/abs/2401.17053) | SIGGRAPH 2024 (ACM TOG) | [paper](https://arxiv.org/abs/2401.17053) |
| 2024-07 | EchoScene, Scene Graph, Diffusion, Indoor | TUM / JHU | [EchoScene: Indoor Scene Generation via Information Echo](https://arxiv.org/abs/2405.00915) | ECCV 2024 | [paper](https://arxiv.org/abs/2405.00915) |
| 2024-07 | Ctrl-Room, Text-to-3D, Layout Constraints | Simon Fraser | [Ctrl-Room: Controllable Text-to-3D Room Meshes Generation](https://arxiv.org/abs/2310.03602) | ECCV 2024 | [paper](https://arxiv.org/abs/2310.03602) |
| 2024-06-13 | Interactive 3D Scene, FLAGS, Single Image | Stanford University | [WonderWorld: Interactive 3D Scene Generation from a Single Image](https://arxiv.org/abs/2406.09394) | CVPR 2025 | [project](https://kovenyu.com/WonderWorld/) |
| 2024-03 | DiffuScene, Diffusion, Indoor Scene Synthesis | TUM | [DiffuScene: Denoising Diffusion for Generative Indoor Scene Synthesis](https://arxiv.org/abs/2303.14207) | CVPR 2024 | [paper](https://arxiv.org/abs/2303.14207) |
| 2024-03 | ControlRoom3D, Semantic Proxy, Room Generation | TUM / Meta | [ControlRoom3D: Room Generation using Semantic Proxy Rooms](https://arxiv.org/abs/2312.00406) | CVPR 2024 | [paper](https://arxiv.org/abs/2312.00406) |
| 2024-01 | MagicDrive, Street View, 3D Geometry Control | CUHK / HKUST | [MagicDrive: Street View Generation with Diverse 3D Geometry Control](https://arxiv.org/abs/2310.02601) | ICLR 2024 | [project](https://magicdrive.github.io/) |
| 2023-11-15 | Procedural World, Synthetic Data, Simulation | Princeton | [Infinite Photorealistic Worlds using Procedural Generation](https://arxiv.org/abs/2306.09310) | CVPR 2023 | [project](https://infinigen.org/) |
| 2023-11-02 | Text-to-3D Room, Indoor Scenes, Mesh | LMU Munich | [Text2Room: Extracting Textured 3D Meshes from 2D Text-to-Image Models](https://arxiv.org/abs/2303.11989) | ICCV 2023 | [project](https://lukashoel.github.io/text-to-room/) |
| 2023-02-23 | Unbounded 3D Scene, Generative Model, Driving | NVIDIA | [SceneDreamer: Unbounded 3D Scene Generation from 2D Image Collections](https://arxiv.org/abs/2302.01330) | CVPR 2023 | [project](https://scene-dreamer.github.io/) |

#### 4.3.2 Semantic Scene Generation & Spatial Intelligence

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-01-28 | Rover, Semantic, 3D Scene | Carnegie Mellon University | [SEM-ROVER: Semantic Scene Exploration with Hierarchical Spatial Reasoning](https://arxiv.org/abs/2501.14782) | ICLR 2025 | [project](https://sem-rover.github.io/) |
| 2024-09-30 | Spatial, Generation, Language | Tsinghua | [SpatialGen: Language-Driven Spatial Scene Generation](https://arxiv.org/abs/2409.20197) | NeurIPS 2024 | [project](https://spatialgen.github.io/) |

#### 4.3.3 4D / Dynamic Scene Generation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-12 | 4Real-Video, Photo-Realistic, Video Diffusion, CVPR | Snap / KAUST | [4Real-Video: Generalizable Photo-Realistic 4D Video Diffusion](https://arxiv.org/abs/2412.04462) | CVPR 2025 | [paper](https://arxiv.org/abs/2412.04462) |
| 2024-10 | Diffusion4D, Video Diffusion, 4D, NeurIPS | Toronto / BJTU | [Diffusion4D: Fast Spatial-temporal Consistent 4D Generation](https://arxiv.org/abs/2405.16645) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2405.16645) |
| 2024-10 | 4Diffusion, Multi-View Video, 4D, NeurIPS | CASIA / Shanghai AI Lab | [4Diffusion: Multi-view Video Diffusion Model for 4D Generation](https://arxiv.org/abs/2405.20674) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2405.20674) |
| 2024-10 | Animate3D, Multi-View, Video Diffusion, NeurIPS | CASIA / Alibaba | [Animate3D: Animating Any 3D Model with Multi-view Video Diffusion](https://arxiv.org/abs/2407.11398) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2407.11398) |
| 2024-10 | DreamScene4D, Multi-Object, Dynamic, NeurIPS | CMU | [DreamScene4D: Dynamic Multi-Object Scene Generation](https://arxiv.org/abs/2405.02280) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2405.02280) |
| 2024-07 | STAG4D, Spatial-Temporal, 4D Gaussians, ECCV | Nanjing / CASIA | [STAG4D: Spatial-Temporal Anchored Generative 4D Gaussians](https://arxiv.org/abs/2403.14939) | ECCV 2024 | [paper](https://arxiv.org/abs/2403.14939) |
| 2024-03 | 4D-fy, Text-to-4D, Score Distillation, CVPR | KAUST / Snap | [4D-fy: Text-to-4D Generation Using Hybrid Score Distillation Sampling](https://arxiv.org/abs/2311.17984) | CVPR 2024 | [project](https://4d-fy.github.io/) |
| 2024-01 | Consistent4D, 360° Dynamic, Monocular Video, ICLR | CASIA / Nanjing | [Consistent4D: Consistent 360° Dynamic Object Generation](https://arxiv.org/abs/2311.10348) | ICLR 2024 | [project](https://consistent4d.github.io/) |
| 2024-01 | Animate124, Image-to-4D, Animation, ICLR | NUS / Huawei | [Animate124: Animating One Image to 4D Dynamic Scene](https://arxiv.org/abs/2311.14603) | ICLR 2024 | [paper](https://arxiv.org/abs/2311.14603) |

<a id="44-3d-editing"></a>

### 4.4 3D Editing

3D editing covers methods that modify existing 3D assets, Gaussian / NeRF fields, meshes, voxel or latent states, and dynamic scenes. Entries are grouped by editable state: object-level, scene-level, and dynamic / 4D.

#### 4.4.1 Object-Level Editing

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-05-26 | Latent Editing, Object-Level, Semantic-Part Transformation | Nanyang Technological University | [Feedforward 3D Editing Learns from Semantic-Part Transformation](https://arxiv.org/abs/2605.27351) | arXiv | [project](https://dennis-jwweng.github.io/pxform/) |
| 2026-05-01 | Latent Editing, Object-Level, Structured 3D Latents | Seoul National University | [InpaintSLat: Inpainting Structured 3D Latents via Initial Noise Optimization](https://arxiv.org/abs/2605.00664) | arXiv | [project](https://robot0321.github.io/InpaintSLat/index.html) |
| 2026-03-30 | 3DGS Editing, Object-Level, Single-View | Zhejiang Gongshang University | [SVGS: Single-View to 3D Object Editing via Gaussian Splatting](https://arxiv.org/abs/2603.28126) | ACM TOMM 2026 | [project](https://amateurc.github.io/svgs.github.io/) |
| 2026-02-25 | Voxel Editing, Object-Level, Rectified Voxel Flow | USTC | [Easy3E: Feed-Forward 3D Asset Editing via Rectified Voxel Flow](https://arxiv.org/abs/2602.21499) | CVPR 2026 | [project](https://ustc3dv.github.io/Easy3E/) |
| 2026-02-04 | Mesh Editing, Object-Level, Single-Image LRM | National Yang Ming Chiao Tung University | [VecSet-Edit: Unleashing Pre-trained LRM for Mesh Editing from Single Image](https://arxiv.org/abs/2602.04349) | arXiv | [github](https://github.com/BlueDyee/VecSet-Edit) |
| 2025-11-21 | Native Editing, Object-Level, Full Attention | Fudan University / StepFun | [Native 3D Editing with Full Attention](https://arxiv.org/abs/2511.17501) | arXiv | [paper](https://arxiv.org/abs/2511.17501) |
| 2025-10-16 | Latent Editing, Object-Level, Mask-Free | Tsinghua University | [NANO3D: A Training-Free Approach for Efficient 3D Editing Without Masks](https://arxiv.org/abs/2510.15019) | arXiv | [project](https://jamesyjl.github.io/Nano3D) |
| 2024-12-11 | Mesh Editing, Object-Level, Masked LRM | University of Chicago | [3D Mesh Editing using Masked LRMs](https://arxiv.org/abs/2412.08641) | ICCV 2025 | [project](https://chocolatebiscuit.github.io/MaskedLRM/) |
| 2024-12-09 | Mesh Editing, Object-Level, Fast Shape Editing | Technical University of Munich | [PrEditor3D: Fast and Precise 3D Shape Editing](https://arxiv.org/abs/2412.06592) | CVPR 2025 | [project](https://ziyaerkoc.com/preditor3d/) |
| 2024-11-30 | Multiview Editing, Object-Level, Inpainting | Tel Aviv University | [Instant3dit: Multiview Inpainting for Fast Editing of 3D Objects](https://arxiv.org/abs/2412.00518) | CVPR 2025 | [project](https://amirbarda.github.io/Instant3dit.github.io/) |
| 2023-03-21 | Voxel Editing, Object-Level, Text-Guided | Tel Aviv University | [Vox-E: Text-guided Voxel Editing of 3D Objects](https://arxiv.org/abs/2303.12048) | ICCV 2023 | [github](https://github.com/TAU-VAILab/Vox-E) |

#### 4.4.2 Scene-Level Editing

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-11 | Latent Editing, Scene-Level, RGB-Geometry | East China Normal Univ / Shanghai AI Lab | [JointEdit3D: Feed-Forward 3D Scene Editing in a Unified Latent Space](https://arxiv.org/abs/2606.13345) | arXiv | [paper](https://arxiv.org/abs/2606.13345) |
| 2026-05-15 | Object-Centric Editing, Scene-Level, Interactive Worlds | Shanghai Jiao Tong Univ | [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843) | arXiv | [project](https://sjtu-deepvisionlab.github.io/WorldAct/) |
| 2026-05-14 | Native 3D Editing, Scene-Level, VGGT Residual Field | Peking University | [VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction](https://arxiv.org/abs/2605.15186) | arXiv | [project](https://chriszkxxx.github.io/VGGT-Edit/) |
| 2026-04-21 | 3DGS Editing, Scene-Level, Sparse-View | Goertek Alpha Labs | [FluSplat: Sparse-View 3D Editing without Test-Time Optimization](https://arxiv.org/abs/2604.20038) | arXiv | [paper](https://arxiv.org/abs/2604.20038) |
| 2026-01-12 | 3DGS Editing, Scene-Level, Drag Control | UIUC | [3DGS-Drag: Dragging Gaussians for Intuitive Point-Based 3D Editing](https://arxiv.org/abs/2601.07963) | ICLR 2025 | [github](https://github.com/Dongjiahua/3DGS-Drag) |
| 2025-12-31 | Feed-Forward Editing, Scene-Level, Sparse Unposed Images | University of Massachusetts Amherst | [Edit3r: Instant 3D Scene Editing from Sparse Unposed Images](https://arxiv.org/abs/2512.25071) | arXiv | [project](https://edit3r.github.io/edit3r/) |
| 2025-08-20 | 3DGS Editing, Scene-Level, Sparse Inputs | Zhejiang University | [Tinker: Diffusion's Gift to 3D--Multi-View Consistent Editing From Sparse Inputs without Per-Scene Optimization](https://arxiv.org/abs/2508.14811) | arXiv | [project](https://aim-uofa.github.io/Tinker) |
| 2025-06-03 | Autoregressive Editing, Scene-Level, Indoor Scenes | Stanford University | [ReSpace: Text-Driven Autoregressive 3D Indoor Scene Synthesis and Editing](https://arxiv.org/abs/2506.02459) | arXiv | [paper](https://arxiv.org/abs/2506.02459) |
| 2024-12-16 | 3DGS Editing, Scene-Level, View-Consistent Fusion | Korea University | [EditSplat: Multi-View Fusion and Attention-Guided Optimization for View-Consistent 3D Scene Editing with 3D Gaussian Splatting](https://arxiv.org/abs/2412.11520) | CVPR 2025 | [paper](https://arxiv.org/abs/2412.11520) |
| 2024-12-02 | 3DGS Editing, Scene-Level, Direct Manipulation | Fondazione Bruno Kessler / University of Trento | [3DSceneEditor: Controllable 3D Scene Editing with Gaussian Splatting](https://arxiv.org/abs/2412.01583) | WACV 2026 | [project](https://ziyangyan.github.io/3DSceneEditor/) |
| 2024-11-07 | 3DGS Editing, Scene-Level, Progressive Localization | UIUC | [ProEdit: Simple Progression is All You Need for High-Quality 3D Scene Editing](https://arxiv.org/abs/2411.05006) | NeurIPS 2024 | [project](https://immortalco.github.io/ProEdit/) |
| 2024-03-13 | 3DGS Editing, Scene-Level, Multi-View Consistency | University of Oxford | [GaussCtrl: Multi-View Consistent Text-Driven 3D Gaussian Splatting Editing](https://arxiv.org/abs/2403.08733) | ECCV 2024 | [paper](https://arxiv.org/abs/2403.08733) |
| 2023-12-14 | Latent Editing, Scene-Level, Local Text Edits | University of Central Florida | [LatentEditor: Text Driven Local Editing of 3D Scenes](https://arxiv.org/abs/2312.09313) | ECCV 2024 | [project](https://latenteditor.github.io/) |
| 2023-11-24 | 3DGS Editing, Scene-Level, Text Prompt | National University of Singapore | [GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting](https://arxiv.org/abs/2311.14521) | CVPR 2024 | [project](https://buaacyw.github.io/gaussian-editor/) |
| 2023-03-22 | NeRF Editing, Scene-Level, Instruction | UC Berkeley | [Instruct-NeRF2NeRF: Editing 3D Scenes with Instructions](https://arxiv.org/abs/2303.12789) | ICCV 2023 | [project](https://instruct-nerf2nerf.github.io/) |

#### 4.4.3 Dynamic & 4D Editing

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-22 | Thermomechanical 3DGS, Phase Change, Dynamic Editing | Zhejiang University | [MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455) | ECCV 2026 | [github](https://github.com/zju3dv/MeGAS) |
| 2026-03-13 | 4D Editing, Dynamic Scene, Dynamic Propagation | Beihang University | [Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation](https://arxiv.org/abs/2603.12766) | arXiv | [project](https://junliao2025.github.io/Catalyst4D-ProjectPage/) |
| 2025-10-02 | 4DGS Editing, Dynamic Scene, Interactive Editing | The University of Hong Kong | [4DGS-Craft: Consistent and Interactive 4D Gaussian Splatting Editing](https://arxiv.org/abs/2510.01991) | arXiv | [paper](https://arxiv.org/abs/2510.01991) |
| 2025-02-04 | 4DGS Editing, Dynamic Scene, Static-Dynamic Separation | DGIST | [Instruct-4DGS: Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://arxiv.org/abs/2502.02091) | arXiv | [paper](https://arxiv.org/abs/2502.02091) |
| 2024-12-02 | Dynamic Editing, Dynamic Scene, Personalized Diffusion | University of Toronto | [CTRL-D: Controllable Dynamic 3D Scene Editing with Personalized 2D Diffusion](https://arxiv.org/abs/2412.01792) | CVPR 2025 | [project](https://ihe-kaii.github.io/CTRL-D/) |
| 2024-06-13 | 4D Editing, Dynamic Scene, Pseudo-3D Diffusion | Zhejiang University | [Instruct 4D-to-4D: Editing 4D Scenes as Pseudo-3D Scenes Using 2D Diffusion](https://arxiv.org/abs/2406.09402) | CVPR 2024 | [paper](https://arxiv.org/abs/2406.09402) |
| 2023-10-25 | NeRF Editing, Dynamic Scene, 4D Semantic Distillation | Tianjin University | [4D-Editor: Interactive Object-level Editing in Dynamic Neural Radiance Fields via Semantic Distillation](https://arxiv.org/abs/2310.16858) | 3DV 2025 | [project](https://patrickddj.github.io/4D-Editor/) |
| 2023-05-31 | 4D Editing, Dynamic Portrait, Text-Guided | Tsinghua University | [Control4D: Efficient 4D Portrait Editing with Text](https://arxiv.org/abs/2305.20082) | arXiv | [project](https://control4darxiv.github.io/) |

<h2 id="-5-embodiment--world-models">🌐 5. Embodiment & World Models</h2>

This section focuses on how 3D perception, reconstruction, and generation translate into physical interaction, world models, human understanding, and agent-facing 3D intelligence.

<a id="51-dynamic-scene-graphs--tracking"></a>

### 5.1 Dynamic Scene Graphs & Tracking

#### 5.1.1 Topologically Aware Tracking

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Observation Scene Graph, Exploration, Hierarchical Memory | Seoul National University | [ObsGraph: Hierarchical Observation Representation for Embodied Reasoning and Exploration](https://arxiv.org/abs/2606.24068) | arXiv | [paper](https://arxiv.org/abs/2606.24068) |
| 2026-06-22 | 3D Scene Graph Forests, Foundation Models, Robot Retrieval | FZI Research Center | [From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models](https://arxiv.org/abs/2606.23312) | IROS 2026 | [paper](https://arxiv.org/abs/2606.23312) |
| 2025-05-29 | Dynamic Memory, Open-Vocabulary, Mobile Manipulation | New York University | [DynaMem: Online Dynamic Spatio-Semantic Memory for Open World Mobile Manipulation](https://arxiv.org/abs/2411.04999) | arXiv | [project](https://dynamem.github.io/) |
| 2025-03-19 | Dynamic 3DSG, Open-Vocabulary, Mobile Manipulation | Beijing Univ. of Posts and Telecommunications | [Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation](https://arxiv.org/abs/2410.11989) | RA-L 2025 | [project](https://bjhyzj.github.io/dovsg-web/) / [github](https://github.com/BJHYZJ/DovSG) |
| 2024-03-15 | Hierarchical Spatial Perception, 3D Scene Graph | MIT | [Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems](https://arxiv.org/abs/2305.07154) | IJRR 2024 | [paper](https://arxiv.org/abs/2305.07154) |
| 2023-09-28 | 3D Scene Graph, Open-Vocabulary, Planning | MIT | [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650) | ICRA 2024 | [project](https://concept-graphs.github.io/) |
| 2023-05-22 | Scene Graph, 3D Perception, Robotics | MIT | [Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization](https://arxiv.org/abs/2201.13360) | RSS 2022 | [github](https://github.com/MIT-SPARK/Hydra) |

<a id="52-reconstruction-based-world-models"></a>

### 5.2 Reconstruction-Based World Models

#### 5.2.1 Physics-Grounded World Models

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-11 | Panoramic Gaussian Scaffold, Real-Time World Model | Authors | [MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold](https://arxiv.org/abs/2606.13376) | arXiv | [paper](https://arxiv.org/abs/2606.13376) |
| 2026-06-05 | Egocentric Simulation, View Evolution, Human Motion | Authors | [AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization](https://arxiv.org/abs/2606.07326) | arXiv | [paper](https://arxiv.org/abs/2606.07326) |
| 2026-05-12 | Belief, 3D World, Uncertainty | Johns Hopkins University | [3D-Belief: Embodied Belief Inference via Generative 3D World Modeling](https://arxiv.org/abs/2605.11367) | arXiv | [paper](https://arxiv.org/abs/2605.11367) |
| 2026-05-03 | Embodied 4D World Model, Novel View, Robot Videos | Shanghai AI Lab | [Embody4D: A Generalist 4D World Model for Embodied AI](https://arxiv.org/abs/2605.01799) | arXiv | [paper](https://arxiv.org/abs/2605.01799) |
| 2026-04-15 | 3DGS Worlds, Reconstruction, Generation, Simulation | Tencent | [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268) | arXiv | [project](https://3d-models.hunyuan.tencent.com/world/) |
| 2026-02-09 | 4D VAE, Dense Geometry, Motion Reconstruction | Tencent ARC | [MotionCrafter: Dense Geometry and Motion Reconstruction with a 4D VAE](https://arxiv.org/abs/2602.08961) | CVPR 2026 | [project](https://ruijiezhu94.github.io/MotionCrafter_Page/) |
| 2026-01-24 | 3DGS, Real-to-Sim, VLA, Physics | University of Melbourne | [Mirage2Matter: A Physically Grounded Gaussian World Model from Video](https://arxiv.org/abs/2602.00096) | arXiv | [paper](https://arxiv.org/abs/2602.00096) |
| 2026-01-08 | 4D Geometric Control, Video World Model, Dynamic | Fudan / Tencent ARC | [VerseCrafter: Dynamic Realistic Video World Model with 4D Geometric Control](https://arxiv.org/abs/2601.05138) | CVPR 2026 | [project](https://sixiaozheng.github.io/VerseCrafter_page/) |
| 2026-01-01 | 4D World Model, Monocular Video, Reconstruction | CASIA | [NeoVerse: Enhancing 4D World Model with in-the-wild Monocular Videos](https://arxiv.org/abs/2601.00393) | CVPR 2026 | [project](https://neoverse-4d.github.io/) / [github](https://github.com/IamCreateAI/NeoVerse) |
| 2025-12-04 | 4D Language, StreamVGGT, Open-Vocabulary | HUST | [4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer](https://arxiv.org/abs/2512.05060) | arXiv | [github](https://github.com/hustvl/4DLangVGGT) |
| 2025-10-13 | Interactive Scenes, Articulation Recovery, Simulation | ETH Zurich | [REACT3D: Recovering Articulations for Interactive Physical 3D Scenes](https://arxiv.org/abs/2510.11340) | arXiv | [project](https://react3d.github.io/) |
| 2025-06-12 | Generative 3D World Engine, Embodied AI, Simulation | Horizon Robotics | [EmbodiedGen: Towards a Generative 3D World Engine for Embodied Intelligence](https://arxiv.org/abs/2506.10600) | arXiv | [paper](https://arxiv.org/abs/2506.10600) |
| 2025-03-05 | 3D Cache, Camera Control, World-Consistent Video | NVIDIA | [GEN3C: 3D-Informed World-Consistent Video Generation with Precise Camera Control](https://arxiv.org/abs/2503.03751) | CVPR 2025 Highlight | [project](https://research.nvidia.com/labs/toronto-ai/GEN3C/) |
| 2025-03 | Genesis, Universal Physics Engine, 43M+ FPS, Diff Physics | CMU | [Genesis: Universal Physics Engine for Embodied AI](https://genesis-embodied-ai.github.io/) | Open Source 2024 | [github](https://github.com/Genesis-Embodied-AI/Genesis) |
| 2025-01 | World Foundation Model Platform, Physical AI, Cosmos | NVIDIA | [Cosmos: World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) | arXiv 2025 | [project](https://www.nvidia.com/en-us/ai/cosmos/) |
| 2024-10-04 | World Model, 3D Consistency, Video Generation | Google DeepMind | [Genie 2: A Large-Scale Foundation World Model](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) | Blog | [page](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) |
| 2024-06-16 | 3DGS, Particles, Correctable World Model | QUT | [Physically Embodied Gaussian Splatting: A Realtime Correctable World Model for Robotics](https://arxiv.org/abs/2406.10788) | CoRL 2024 | [project](https://embodied-gaussians.github.io/) / [OpenReview](https://openreview.net/forum?id=AEq0onGrN2) |
| 2024-01 | WorldDreamer, Action-Conditioned, Mask Tokens, NeurIPS | Tsinghua | [WorldDreamer: Towards General World Models via Predicting Masked Tokens](https://arxiv.org/abs/2401.09985) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2401.09985) |
| 2024-01 | RoboGen, Generative Simulation, LLM, Infinite Data, ICML | CMU / MIT | [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning](https://arxiv.org/abs/2311.01455) | ICML 2024 | [project](https://robogen-ai.github.io/) |
| 2023-01 | UniSim, Action-Conditioned Video, Robot Learning, CoRL | Google DeepMind | [UniSim: Action-Conditioned Video Prediction for Robot Learning](https://uni-sim.github.io/) | CoRL 2023 | [project](https://uni-sim.github.io/) |

#### 5.2.2 Action-Conditioned Dynamics Synthesis

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Navigation World Model, Visual Foresight, Planning | CASIA | [NavWM: A Unified Navigation World Model for Foresight-Driven Planning](https://arxiv.org/abs/2606.24101) | ECCV 2026 | [paper](https://arxiv.org/abs/2606.24101) |
| 2026-06-23 | Locomotion World Model, Terrain Geometry, Sim-to-Real | Beijing Institute of Technology | [DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs](https://arxiv.org/abs/2606.24089) | IROS 2026 | [paper](https://arxiv.org/abs/2606.24089) |
| 2026-06-22 | Interactive World Model, URDF Kinematics, Policy Evaluation | Beijing Innovation Center of Humanoid Robotics | [IOI: Decoupling Kinematics and Physics for Interactive World Models](https://arxiv.org/abs/2606.23296) | arXiv | [paper](https://arxiv.org/abs/2606.23296) |
| 2026-06-22 | Quadrotor World Model, Long-Horizon Dynamics, Sim-to-Real | Authors | [SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors](https://arxiv.org/abs/2606.23444) | arXiv | [paper](https://arxiv.org/abs/2606.23444) |
| 2026-06-01 | Object-Centric 3DGS, Action-Conditional, Rigid Objects | Authors | [Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects](https://arxiv.org/abs/2606.01950) | arXiv | [paper](https://arxiv.org/abs/2606.01950) |
| 2026-04-29 | X-WAM, 4D World Action Model, RGB-D Future | Tsinghua | [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694) | arXiv | [project](https://sharinka0715.github.io/X-WAM/) |
| 2026-03-17 | 4D Simulator, URDF, Kinematic Action | Nanyang Technological University | [Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669) | arXiv | [project](https://mutianxu.github.io/Kinema4D/) |
| 2026-03-13 | 4D World, Dual-Tower, Policy Optimization | Tsinghua University | [RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization](https://arxiv.org/abs/2603.12639) | arXiv | [paper](https://arxiv.org/abs/2603.12639) |
| 2025-11-25 | World Model, Data Engine, VLA, 3DGS | Cornell | [GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861) | arXiv | [project](https://giga-world-0.github.io/) |
| 2025-07-01 | 4D Generation, Multi-View Consistency, Robot Manipulation | Stanford | [Geometry-aware 4D Video Generation for Robot Manipulation](https://arxiv.org/abs/2507.01099) | ICLR 2026 | [paper](https://arxiv.org/abs/2507.01099) |
| 2025-03-24 | World Model, Geometric-Aware, 4D Reconstruction | Shanghai AI Lab | [AETHER: Geometric-Aware Unified World Modeling](https://arxiv.org/abs/2503.18945) | ICCV 2025 + RIWM Outstanding Paper | [project](https://aether-world.github.io/) |
| 2025-02-28 | Embodied Video Anticipation, Reflection | HKUST | [EVA: An Embodied World Model for Future Video Anticipation](https://arxiv.org/abs/2410.15461) | ICML 2025 | [project](https://eva-world.github.io/) |
| 2024-07-15 | Physics-Based Interaction, 3DGS, Young's Modulus, ECCV Oral | MIT / Stanford | [PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation](https://physdreamer.github.io/) | ECCV 2024 Oral | [project](https://physdreamer.github.io/) |
| 2024-07-10 | Physical Reasoning, Benchmark, NeurIPS | MIT / Stanford | [Physion++: Physical Reasoning Benchmark for Embodied AI](https://physion-benchmark.github.io/) | NeurIPS 2024 | [project](https://physion-benchmark.github.io/) |
| 2024-02-26 | Interactive Environment, Generative World, Agent | Google DeepMind | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | ICML 2024 | [project](https://sites.google.com/view/genie-2024/) |

<a id="53-physical-interaction--affordance"></a>

### 5.3 Physical Interaction & Affordance

#### 5.3.1 Affordance Prediction & Grasp Detection

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Tactile Exploration, Object Localization, Shape Completion | Amazon Robotics | [TACTFUL: Tactile-Driven Exploration For Object Localization and Identification in Confined Environments](https://arxiv.org/abs/2606.24712) | IROS 2026 | [paper](https://arxiv.org/abs/2606.24712) |
| 2026-06-16 | Asset Annotation, Affordance, Physics Labels | Northwestern University | [AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation](https://arxiv.org/abs/2606.17446) | arXiv | [project](https://tourmaline-caramel-169490.netlify.app/) |
| 2024-11-20 | Open-Vocabulary, Task-Oriented Grasp, LLM | CMU | [GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping](https://arxiv.org/abs/2411.12286) | CoRL 2024 | [project](https://glover-grasp.github.io/) |
| 2024-10-30 | Generative Dexterous Grasping, Large-Scale, CoRL | PKU / Galbot | [DexGraspNet 2.0: Learning Generative Dexterous Grasping in Cluttered Scenes](https://arxiv.org/abs/2410.23004) | CoRL 2024 | [project](https://pku-epic.github.io/DexGraspNet2.0/) |
| 2024-10-15 | SE(3)-Equivariant, 6-DoF Grasp, Flow | Seoul Nat'l Univ | [EquiGraspFlow: SE(3)-Equivariant 6-DoF Grasp Pose Generative Flows](https://arxiv.org/abs/2407.08216) | CoRL 2024 | [project](https://equigraspflow.github.io/) |
| 2024-09-03 | Zero-Shot Affordance, 3DGS, Feature Splatting, CoRL | UCSD | [GraspSplats: Efficient Manipulation with 3D Feature Splatting](https://arxiv.org/abs/2409.02084) | CoRL 2024 | [paper](https://arxiv.org/abs/2409.02084) |
| 2024-07-15 | AnyGrasp, 6-DoF Grasp, Point Cloud | Tsinghua | [AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains](https://arxiv.org/abs/2212.08333) | T-RO 2023 | [github](https://github.com/graspnet/anygrasp_sdk) |
| 2024-07-15 | Dynamic GS, Multi-Task, World Model, ECCV | Tsinghua / CMU | [ManiGaussian: Dynamic Gaussian Splatting for Robotic Manipulation](https://arxiv.org/abs/2403.08321) | ECCV 2024 | [paper](https://arxiv.org/abs/2403.08321) |
| 2024-07-10 | SE(3)-Equivariant, Grasp, Point Cloud | Northeastern | [OrbitGrasp: SE(3)-Equivariant Grasp Learning](https://arxiv.org/abs/2407.03531) | CoRL 2024 | [project](https://orbitgrasp.github.io/) |
| 2024-06-01 | Affordance, Interactive Perception, 3D | MIT | [Where2Act: From Pixels to Actions for Articulated 3D Objects](https://arxiv.org/abs/2101.02692) | ICCV 2021 | [project](https://cs.stanford.edu/~kaichun/where2act/) |
| 2024-02-23 | Multi-Stage, Open-Vocab, Editable 3DGS, Manipulation, CoRL | Stanford | [Splat-MOVER: Multi-Stage Manipulation via Editable Gaussian Splatting](https://arxiv.org/abs/2405.04378) | CoRL 2024 | [project](https://splatmover.github.io/) |
| 2024-02-23 | Interactive Exploration, Action-Conditioned Scene Graph, CoRL | Columbia / UIUC | [RoboEXP: Action-Conditioned Scene Graph via Interactive Exploration](https://arxiv.org/abs/2402.15487) | CoRL 2024 | [project](https://jianghanxiao.github.io/roboexp-web/) |
| 2023-12-15 | Affordance, Point Cloud, Interaction | Stanford | [IAGNet: Interaction-Aware 3D Generative Model for Affordance Prediction](https://arxiv.org/abs/2303.10437) | CoRL 2023 | [paper](https://arxiv.org/abs/2303.10437) |
| 2023-11-28 | Contact Prediction, Object Interaction, Point Cloud | Meta AI | [ContactGen: Generative Contact Modeling for 3D Object Interactions](https://arxiv.org/abs/2310.03740) | NeurIPS 2023 | [paper](https://arxiv.org/abs/2310.03740) |
| 2023-08-31 | NeRF Feature, Diffusion Semantics, Robot Learning, CoRL | Tsinghua / HKU | [GNFactor: Multi-Task Real Robot Learning with Generalizable Neural Feature Fields](https://arxiv.org/abs/2308.16891) | CoRL 2023 | [paper](https://arxiv.org/abs/2308.16891) |

#### 5.3.2 Physical Property & Material Estimation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-11-23 | Physical Property, Bayesian 3DGS, Mass/Hardness/Friction | CMU | [PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570) | CVPR 2026 | [paper](https://arxiv.org/abs/2511.18570) |
| 2025-08-01 | Physical Gaussian, Feed-Forward 4D, Single Image | BIT / Li Auto | [PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911) | CVPR 2026 Highlight | [paper](https://arxiv.org/abs/2508.13911) |
| 2024-12-15 | Physical Property, 3DGS, LMM | HKUST | [GaussianProperty: Integrating Physical Properties to 3D Gaussians with LMMs](https://arxiv.org/abs/2412.11258) | ICCV 2025 | [project](https://gaussianproperty.github.io/) |
| 2024-11-20 | MLLM, Physical Property, 3DGS, Physics Sim | Wuhan Univ | [PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting](https://arxiv.org/abs/2411.12789) | ICCV 2025 | [paper](https://arxiv.org/abs/2411.12789) |
| 2024-03-28 | Mass, Friction, Compliance, LLM, Adaptive Grasp | MIT | [DeliGrasp: Inferring Object Mass, Friction, and Compliance with LLMs for Adaptive Grasp Policies](https://arxiv.org/abs/2403.07832) | CoRL 2024 | [project](https://deligrasp.github.io/) |
| 2023-10-05 | Physical Properties, Visual Estimation, Liquids | MIT | [Visual Estimation of Physical Properties of Objects and Liquids](https://arxiv.org/abs/2310.03163) | CoRL 2023 | [project](https://mit-genai.github.io/) |
| 2023-06-01 | Mass Estimation, Vision, Physics | CMU | [Learning to Estimate Object Mass from Vision and Force](https://arxiv.org/abs/2306.00280) | RSS 2023 | [project](https://robin-lab.cs.cmu.edu/) |

<a id="54-human-centric-3d-for-embodiment"></a>

### 5.4 Human-Centric 3D for Embodiment

#### 5.4.1 Human Pose & Shape Estimation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-17 | Egocentric, 4D Hand, Feed-Forward 3DGS | Yonsei University | [Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos](https://arxiv.org/abs/2606.19156) | arXiv | [project](https://jeongminb.github.io/hand-4dgs/) |
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
| 2025-03-10 | Close Interaction, Dynamic Video, Multi-Person | MPI-IS | [Harmony4D: A Video Dataset for In-The-Wild Close Human Interactions](https://arxiv.org/abs/2503.05483) | NeurIPS 2024 | [project](https://harmony4d.github.io/) |
| 2024-12-03 | Human-to-Robot, Teleoperation, 3D Hand Pose | Stanford | [AnyTeleop: A General Vision-Based Teleoperation System](https://arxiv.org/abs/2307.06275) | CoRL 2023 | [project](https://anyteleop.com/) |
| 2024-08-01 | Template-Free, 4D HOI Tracking | MPI-IS | [InterTrack: Tracking Human Object Interaction without Object Templates](https://arxiv.org/abs/2408.13953) | ECCV 2024 | [project](https://virtualhumans.mpi-inf.mpg.de/InterTrack/) |
| 2024-06-15 | HOI4D, Dynamic Interaction, Point Cloud | Peking University | [HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction](https://arxiv.org/abs/2203.01577) | CVPR 2022 | [project](https://hoi4d.github.io/) |
| 2024-03-01 | HOI, 3D Interaction, Motion Capture | MPI-IS | [BEHAVE: Dataset and Method for Tracking Human Object Interactions](https://arxiv.org/abs/2204.06950) | CVPR 2022 | [project](https://virtualhumans.mpi-inf.mpg.de/behave/) |
| 2023-06-01 | Visibility, HOI Tracking, Single RGB | MPI-IS | [VisTracker: Visibility Aware Human-Object Interaction Tracking from Single RGB Camera](https://arxiv.org/abs/2305.13977) | CVPR 2023 | [github](https://github.com/xiexh20/VisTracker) |

<a id="55-robotics-integration--vlm-agents"></a>

### 5.5 Robotics Integration & VLM Agents

#### 5.5.1 Sim-to-Real via Generated Assets

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Synthetic Robot Video, Geometry-Guided VLA, Waypoints | National University of Singapore | [Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos](https://arxiv.org/abs/2606.24448) | arXiv | [paper](https://arxiv.org/abs/2606.24448) |
| 2026-06-23 | Articulated Digital Twin, URDF, Isaac Sim | ETH Zurich | [ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D Videos](https://arxiv.org/abs/2606.24628) | ICRA 2026 Workshop | [paper](https://arxiv.org/abs/2606.24628) |
| 2026-06-23 | Cloth Manipulation, Real-to-Sim, Simulator-in-the-Loop | National University of Singapore | [Enabling Robust Cloth Manipulation via Inference-Time Simulator-in-the-Loop Refinement](https://arxiv.org/abs/2606.24552) | arXiv | [project](https://silr-cloth.github.io/) |
| 2026-06-20 | World-Model Data, Dexterous VLA, 50K Episodes | Shanghai Innovation Institute | [Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data](https://arxiv.org/abs/2606.22136) | arXiv | [project](https://chenyt31.github.io/wh0.github.io/) |
| 2026-06-19 | 3DGS Assets, Heterogeneous Physics, Scene-Level Simulation | The University of Hong Kong | [Scene-Level Heterogeneous Physics Simulation with 3D Gaussian Splats](https://arxiv.org/abs/2606.21753) | arXiv | [project](https://visual-ai.github.io/raf/) |
| 2026-06-18 | Multi-View Object Swapping, 6D Pose, VLA Augmentation | KAIST | [Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation](https://arxiv.org/abs/2606.20118) | arXiv | [paper](https://arxiv.org/abs/2606.20118) |
| 2026-06-17 | Fisheye 3DGS, Action-View Augmentation, Manipulation Data | Stanford | [One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies](https://arxiv.org/abs/2606.19586) | CoRL 2025 | [project](https://chuerpan.com/1001-demos.github.io/) |
| 2026-06-16 | 3DGS Simulation Environments, Inpainting, Sim-to-Real | Shanghai Jiao Tong University | [GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments](https://arxiv.org/abs/2606.17520) | arXiv | [project](https://jar7visz.github.io/gase-page/) |
| 2026-06-05 | Quadruped Simulation, 3DGS Scenes, Contact Calibration | Authors | [QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation](https://arxiv.org/abs/2606.07118) | arXiv | [paper](https://arxiv.org/abs/2606.07118) |
| 2026-06-03 | Humanoid Loco-Manipulation, 3D Assets, Video Priors | NVIDIA | [GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160) | arXiv | [project](https://research.nvidia.com/labs/dair/grail/) / [github](https://github.com/NVlabs/GRAIL) |
| 2026-06-02 | Semantic Reconstruction, LLM Planning, Simulation | Mila / Université de Montréal | [PerceptTwin: Semantic Scene Reconstruction for Iterative LLM Planning and Verification](https://arxiv.org/abs/2606.04226) | ICRA 2026 | [project](https://percept-twin.github.io/) |
| 2026-04-20 | Driving Logs, Sparse Views, Simulation-Ready AV Assets | NVIDIA | [Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation](https://arxiv.org/abs/2604.18468) | NVIDIA White Paper | [project](https://research.nvidia.com/labs/sil/projects/asset-harvester/) / [github](https://github.com/NVlabs/asset-harvester) |
| 2026-03-05 | 3DGS, Digital Twin, PBD, Robotics | TU Darmstadt | [GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108) | ICRA 2026 | [project](https://6cyc6.github.io/gstwin/) |
| 2025-10-12 | 3DGS, Real2Sim2Real, Manipulation | Shanghai AI Lab | [High-Fidelity Simulated Data Generation for Real-World Zero-Shot Robotic Manipulation Learning with Gaussian Splatting](https://arxiv.org/abs/2510.10637) | arXiv | [paper](https://arxiv.org/abs/2510.10637) |
| 2025-09-26 | Personalized Navigation, 3DGS, Real-to-Sim | CMU | [EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats from a Mobile Device](https://arxiv.org/abs/2509.17430) | ICCV 2025 | [project](https://gchhablani.github.io/embodied-splat/) / [github](https://github.com/gchhablani/embodied-splat-v1) |
| 2025-04-05 | Dynamic Digital Twin, Sim2Real, 60Hz | Stanford | [Real-is-Sim: Bridging the Sim-to-Real Gap with a Dynamic Digital Twin](https://arxiv.org/abs/2504.03597) | CoRL 2025 | [paper](https://arxiv.org/abs/2504.03597) |
| 2025-02-26 | Articulated Objects, URDF, Manipulation | Tsinghua | [ArtGS: Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459) | ICLR 2025 | [project](https://articulate-gs.github.io/) |
| 2024-10-08 | Navigation, World Model, Embodied Agent | Stanford | [NavDreamer: Dreaming with World Models for Embodied Navigation](https://arxiv.org/abs/2410.08234) | CoRL 2024 | [project](https://navdreamer.github.io/) |
| 2024-09-25 | 3D Descriptor Fields, Zero-Shot, Rearrangement | Columbia / Stanford | [D3Fields: Dynamic 3D Descriptor Fields for Zero-Shot Generalizable Rearrangement](https://arxiv.org/abs/2409.09408) | CoRL 2024 | [project](https://robopil.github.io/d3fields/) |
| 2024-09-15 | Gaussian Splatting, Sim2Real, RGB Policy | CMU | [SplatSim: Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using Gaussian Splatting](https://arxiv.org/abs/2409.10161) | CoRL 2024 / ICRA 2025 | [project](https://splatsim.github.io/) |
| 2024-08-15 | Digital Cousins, Real→Sim→Real, Zero-Shot 90% | Stanford | [Automated Creation of Digital Cousins for Robust Policy Learning](https://arxiv.org/abs/2410.07408) | CoRL 2024 | [project](https://digital-cousins.github.io/) |
| 2024-07-10 | City-Scale, 100K Scenes, Interactive, Embodied | Shanghai AI Lab | [GRUtopia: Dream General Robots in a City at Scale](https://arxiv.org/abs/2407.10943) | arXiv 2024 / WAIC | [paper](https://arxiv.org/abs/2407.10943) |
| 2024-07-08 | DROID, In-The-Wild, 76K Trajectories, RSS | Multi-institution | [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://droid-dataset.github.io/) | RSS 2024 | [project](https://droid-dataset.github.io/) |
| 2024-04-30 | Cross-Embodiment, Open X-Embodiment, RT-X, ICRA Best Paper | Multi-institution | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://robotics-transformer-x.github.io/) | ICRA 2024 Best Paper | [project](https://robotics-transformer-x.github.io/) |
| 2024-04-10 | Large-Scale, Simulation, Everyday Tasks, RSS | UT Austin / NVIDIA | [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://robocasa.ai/) | RSS 2024 | [project](https://robocasa.ai/) |
| 2024-03-28 | Real-to-Sim-to-Real, Digital Twin, Manipulation | MIT | [RialTo: Reconciling Reality through Simulation for Robust Manipulation](https://arxiv.org/abs/2403.03949) | RSS 2024 | [project](https://real-to-sim-to-real.github.io/RialTo/) |
| 2023-06-16 | Digital Twin, Synthetic Scenes, Embodied AI | NVIDIA | [ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://arxiv.org/abs/2206.06994) | NeurIPS 2022 | [project](https://procthor.allenai.org/) |

#### 5.5.2 VLMs for 3D Grounding & Planning

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-23 | Scene Graph State, Manipulation Reasoning, 1.6M Dataset | Authors | [RoBoSR: Structured Scene Representations for Embodied Robotic Reasoning](https://arxiv.org/abs/2606.24338) | arXiv | [paper](https://arxiv.org/abs/2606.24338) |
| 2026-06-22 | Embodied Agent, 3D Spatial Memory, Skill Graph | Horizon Robotics | [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](https://arxiv.org/abs/2606.23565) | arXiv | [github](https://github.com/HorizonRobotics/HoloAgent) |
| 2026-03-10 | Priori-Map, Navigation, Functional Buildings | Xi'an Jiaotong University | [PM-Nav: Priori-Map Guided Embodied Navigation in Functional Buildings](https://arxiv.org/abs/2603.09113) | arXiv | [paper](https://arxiv.org/abs/2603.09113) |
| 2025-04-05 | 3D Spatial Memory, Multimodal, Robot Navigation | Meta AI | [M3: 3D-Spatial MultiModal Memory](https://arxiv.org/abs/2503.16413) | ICLR 2025 | [project](https://m3-spatial-memory.github.io) |
| 2025-03-06 | 3D VQA, Gaussian Splatting, Zero-Shot | Tsinghua | [SplatTalk: 3D VQA with Gaussian Splatting](https://arxiv.org/abs/2503.06271) | ICCV 2025 | [paper](https://arxiv.org/abs/2503.06271) |
| 2025-02-10 | Agent, VLN, 3D Navigation | Stanford | [AgentVLN: Vision-Language Navigation with 3D Scene Understanding](https://arxiv.org/abs/2502.05376) | CVPR 2025 | [project](https://agent-vln.github.io/) |
| 2024-11-11 | 3D Grounding, VLM, Point Cloud | Shanghai AI Lab | [LLaVA-3D: A Simple yet Effective Pathway to Empowering LMMs with 3D Awareness](https://arxiv.org/abs/2410.06250) | arXiv | [github](https://github.com/ZCMax/LLaVA-3D) |
| 2024-10-31 | Zero-Shot Semantic Navigation, VLFM, ICRA Best Paper | Boston Dynamics AI / Georgia Tech | [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](https://github.com/bdaiinstitute/vlfm) | ICRA 2024 Best Paper in Cognitive Robotics | [github](https://github.com/bdaiinstitute/vlfm) |
| 2024-10-10 | 3DSG, LLM, ObjectNav | Tsinghua University | [SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation](https://arxiv.org/abs/2410.08189) | NeurIPS 2024 | [project](https://bagh2178.github.io/SG-Nav/) |
| 2024-07-18 | UMI, In-The-Wild, Data Collection, RSS Finalist | Stanford | [UMI: Universal Manipulation Interface for In-The-Wild Robot Teaching](https://umi-gripper.github.io/) | RSS 2024 Best Systems Paper Finalist | [project](https://umi-gripper.github.io/) |
| 2024-07-18 | HumanPlus, Humanoid, Shadowing, Imitation, CoRL | Stanford | [HumanPlus: Humanoid Shadowing and Imitation from Humans](https://humanoid-ai.github.io/) | CoRL 2024 | [project](https://humanoid-ai.github.io/) |
| 2024-07-15 | OpenVLA, Open-Source VLA, 7B, ICML | Stanford / UC Berkeley | [OpenVLA: An Open-Source Vision-Language-Action Model](https://openvla.github.io/) | ICML 2024 | [github](https://github.com/openvla/openvla) |
| 2024-07-15 | EmbodiedScan, Multi-Modal, 3D Perception, CVPR+NeurIPS | Shanghai AI Lab | [EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite](https://tai-wang.github.io/embodiedscan/) | CVPR 2024 + NeurIPS Datasets | [project](https://tai-wang.github.io/embodiedscan/) |
| 2024-07-15 | 3D Diffusion Policy, Point Cloud, RSS | Tsinghua / HKU | [3D Diffusion Policy: Generalizable Visuomotor Policy via 3D Representations](https://3d-diffusion-policy.github.io/) | RSS 2024 | [project](https://3d-diffusion-policy.github.io/) |
| 2024-07-12 | Spatial VLM, 3D Reasoning, Robotics | Stanford | [SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities](https://arxiv.org/abs/2401.12168) | CVPR 2024 | [project](https://spatial-vlm.github.io/) |
| 2023-12-06 | DexMimicGen, Bimanual Dexterous, Auto Data, ICRA | NVIDIA / UCSD | [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation](https://dexmimicgen.github.io/) | ICRA 2025 | [project](https://dexmimicgen.github.io/) |
| 2023-11-13 | Embodied Planning, 3D Scene, LLM | MIT | [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](https://arxiv.org/abs/2307.06135) | CoRL 2023 | [project](https://sayplan.github.io/) |
| 2023-07-14 | RT-2, VLA, Web Knowledge Transfer, CoRL | Google DeepMind | [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) | CoRL 2023 | [paper](https://arxiv.org/abs/2307.15818) |
| 2023-07-13 | VoxPoser, 3D Value Maps, Zero-Shot Manipulation, CoRL | Stanford / UIUC | [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with LLMs](https://voxposer.github.io/) | CoRL 2023 | [project](https://voxposer.github.io/) |
| 2023-04-02 | DexGrasp++, Dexterous, Curriculum, NeurIPS | PKU | [UniDexGrasp++: Improving Dexterous Grasping via Geometry-aware Curriculum](https://arxiv.org/abs/2304.00464) | NeurIPS 2024 | [paper](https://arxiv.org/abs/2304.00464) |
| 2023-03-06 | PaLM-E, Embodied Multimodal LLM, 562B, ICML | Google Research | [PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378) | ICML 2023 | [paper](https://arxiv.org/abs/2303.03378) |
| 2021-12-06 | PerAct, Perceiver-Actor, Multi-Task, 6-DoF, CoRL | UW / NVIDIA | [PerAct: Perceiver-Actor for Robotic Manipulation](https://peract.github.io/) | CoRL 2022 | [project](https://peract.github.io/) |

<h2 id="-6-datasets-benchmarks--infrastructure">🧰 6. Datasets, Benchmarks & Infrastructure</h2>

This section is the toolbox and dictionary for quickly choosing datasets, benchmarks, metrics, simulators, and reference surveys.

<a id="61-surveys--taxonomies"></a>

### 6.1 Surveys & Taxonomies

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-04-26 | Production-Ready, PBR, Rigging, Scene Assembly, Survey | Hong Kong Polytechnic University | [From Visual Synthesis to Interactive Worlds: Toward Production-Ready 3D Asset Generation](https://arxiv.org/abs/2604.23629) | arXiv | [paper](https://arxiv.org/abs/2604.23629) |
| 2026-04-15 | Feed-Forward 3D, Problem-Driven, Survey | Zhejiang University | [Feed-Forward 3D Scene Modeling: A Problem-Driven Perspective](https://arxiv.org/abs/2604.14025) | arXiv | [project](https://ff3d-survey.github.io/) / [github](https://github.com/WeijieWang2000/FF3D-Survey) |
| 2026-04-15 | 3D Generation, Embodied AI, Robotic Simulation, Survey | HKUST / Tencent | [3D Generation for Embodied AI and Robotic Simulation: A Survey](https://arxiv.org/abs/2604.26509) | arXiv | [paper](https://arxiv.org/abs/2604.26509) |
| 2026-02-01 | Visual Grounding, 2D & 3D, Unified Perspective | Multiple | [Visual Grounding in 2D and 3D: A Unified Perspective and Survey](https://www.sciencedirect.com/science/article/abs/pii/S1566253525006979) | Information Fusion 2026 | [paper](https://www.sciencedirect.com/science/article/abs/pii/S1566253525006979) |
| 2025-07-30 | Depth Foundation Model, Monocular/Stereo/Video, Survey | Authors | [Towards Depth Foundation Model: Recent Trends in Vision-Based Depth Estimation](https://arxiv.org/abs/2507.11540) | arXiv 2025 | [paper](https://arxiv.org/abs/2507.11540) |
| 2025-07-15 | 4D Spatial Intelligence, 5-Level Framework, Survey | NTU / HKUST | [Reconstructing 4D Spatial Intelligence: A Survey](https://arxiv.org/abs/2507.21045) | arXiv | [project](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence) |
| 2025-07-11 | Feed-Forward 3D, DUSt3R, VGGT, Survey | Xidian University | [Review of Feed-forward 3D Reconstruction: From DUSt3R to VGGT](https://arxiv.org/abs/2507.08448) | arXiv | [paper](https://arxiv.org/abs/2507.08448) |
| 2025-06-11 | 3D Point Cloud, Foundation Model, Survey | Authors | [Foundational Models for 3D Point Clouds: A Survey and Outlook](https://arxiv.org/abs/2501.18594) | arXiv 2025 | [paper](https://arxiv.org/abs/2501.18594) |
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
| 2022-03-07 | Scalable Synthetic, 13 Tasks, Blender + PyBullet, CVPR | Google / DeepMind | [Kubric: A Scalable Synthetic Data Generation Framework](https://arxiv.org/abs/2203.03570) | CVPR 2022 | [github](https://github.com/google-research/kubric) |
| 2020-11-18 | 3D-FRONT, 6813 Houses, 9992 Furniture, Generation | Authors | [3D-FRONT: 3D Furnished Rooms with Layouts and Semantics](https://tianchi.aliyun.com/specials/promotion/3dfront) | arXiv 2020 | [dataset](https://tianchi.aliyun.com/specials/promotion/3dfront) |
| 2020-08-18 | Object-Centric, Real Images, NeRF | Google Research | [Nerf Synthetic and LLFF Datasets](https://www.matthewtancik.com/nerf) | Dataset | [project](https://www.matthewtancik.com/nerf) |
| 2019-12-10 | Autonomous Driving, 1150 Scenes, 5 LiDAR+5 Camera | Waymo | [Waymo Open Dataset: Autonomous Driving](https://waymo.com/open/) | CVPR 2020 | [dataset](https://waymo.com/open/) |
| 2019-04-02 | 3D Scene, Semantic, LiDAR, SemanticKITTI | Authors | [SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences](http://www.semantic-kitti.org/) | ICCV 2019 | [dataset](http://www.semantic-kitti.org/) |
| 2019-03-26 | Autonomous Driving, 1000 Scenes, 23 Classes, 6 Cam+LiDAR+Radar | nuTonomy | [nuScenes: A Multimodal Dataset for Autonomous Driving](https://www.nuscenes.org/) | CVPR 2020 | [dataset](https://www.nuscenes.org/) |
| 2017-09-18 | Indoor 3D, 90 Buildings, RGB-D, Mesh | Authors | [Matterport3D: Learning from RGB-D Data in Indoor Environments](https://niessnerlab.org/projects/matterport.html) | 3DV 2017 | [dataset](https://niessnerlab.org/projects/matterport.html) |
| 2017-08-10 | MVS, Large-Scale, Benchmark | Princeton / Intel | [Tanks and Temples](https://www.tanksandtemples.org/) | TOG 2017 | [benchmark](https://www.tanksandtemples.org/) |
| 2015-10-15 | RGB-D, 10K, 3D Bounding Boxes, Layout | Authors | [SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite](https://rgbd.cs.princeton.edu/) | CVPR 2015 | [dataset](https://rgbd.cs.princeton.edu/) |
| 2014-10-24 | MVS, Controlled Capture, DTU | Technical University of Denmark | [DTU Robot Image Dataset](https://roboimagedata.compute.dtu.dk/) | IJCV 2014 | [dataset](https://roboimagedata.compute.dtu.dk/) |
| 2012-07-26 | Autonomous Driving, Foundational, Stereo/Flow/Odometry/Detection | KIT / Toyota | [KITTI: The Karlsruhe Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/) | CVPR 2012 | [dataset](http://www.cvlibs.net/datasets/kitti/) |

#### 6.2.2 Dense View & Streaming Sequences

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-22 | Panoramic Stereo, Humanoid Occupancy, 155K Samples | Wuhan University | [Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI](https://arxiv.org/abs/2606.22971) | arXiv | [project](https://d-robotics-ai-lab.github.io/humanoid-omniocc) |
| 2026-06-22 | Stereo RGB + LiDAR, Construction Depth, 11K Samples | Technical University of Denmark | [ShotcreteDepth: A Bi-modal Dataset for Robust Robotic Depth Perception in Shotcrete Construction Environments](https://arxiv.org/abs/2606.23152) | arXiv | [github](https://github.com/dtu-pas/shotcrete-depth) |
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
| 2026-06-23 | Garments, Sewing Patterns, 300K, Simulation | University of Hong Kong | [PatternGSLData](https://arxiv.org/abs/2606.24564) | Dataset | [github](https://github.com/PatternGSL/PatternGSL) |
| 2026-06-22 | 4D Humans, Volumetric Meshes, 104 Subjects | Authors | [VolHuMe: a High-Resolution Large Scale Dataset of Volumetric Human Meshes](https://arxiv.org/abs/2606.23062) | Dataset | [paper](https://arxiv.org/abs/2606.23062) |
| 2025-02-17 | Articulation, 33K Models, Objaverse-XL | Nanyang Technological University | [Articulation-XL](https://chaoyuesong.github.io/MagicArticulate) | Dataset | [paper](https://arxiv.org/abs/2502.12135) / [github](https://github.com/Seed3D/MagicArticulate) |
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
| 2026-06-23 | T2V Evaluation, 3D Consistency, Reconstruction Profile | University of Bern | [GeoT2V-Bench: Benchmarking 3D Consistency in Text-to-Video Models via 3D Reconstruction](https://arxiv.org/abs/2606.24829) | arXiv | [paper](https://arxiv.org/abs/2606.24829) |
| 2026-06-22 | Robot Camera Rotation, Mesh Reconstruction, Evaluation | Southern University of Science and Technology | [Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?](https://arxiv.org/abs/2606.22987) | arXiv | [paper](https://arxiv.org/abs/2606.22987) |
| 2026-06-21 | World Model Evaluation, Physical Consistency, 3D/Flow Metrics | Hanyang University ERICA | [Reference-Free Assessment of Physical Consistency in World Model-based Video Generation](https://arxiv.org/abs/2606.22363) | arXiv | [paper](https://arxiv.org/abs/2606.22363) |
| 2026-06-09 | World Model Evaluation, 3D Consistency, Interaction | Zhejiang University | [WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129) | arXiv | [project](https://alibaba-damo-academy.github.io/WorldOlympiad) / [github](https://github.com/alibaba-damo-academy/WorldOlympiad) |
| 2026-02-03 | 3D Assets, Evaluation, Hunyuan3D, Benchmark | Tencent Hunyuan | [HY3D-Bench: Generation of 3D Assets](https://arxiv.org/abs/2602.03907) | arXiv | [paper](https://arxiv.org/abs/2602.03907) |
| 2025-06-22 | Bimanual Manipulation, Sim2Real, Benchmark | Shanghai Jiao Tong University | [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization](https://arxiv.org/abs/2506.18088) | arXiv | [project](https://robotwin-platform.github.io/) / [github](https://github.com/RoboTwin-Platform/RoboTwin) |
| 2025-04-25 | 3D Generation, Fine-Grained Evaluation, Asset Quality | MIT | [Eval3D: Interpretable and Fine-grained Evaluation for 3D Generation](https://arxiv.org/abs/2504.18509) | CVPR 2025 | [project](https://eval3d.github.io/) / [github](https://github.com/eval3d/eval3d-codebase) |
| 2025-03 | 3D Generation, Unified Benchmark, Human Preference | Authors | [3DGen-Bench: Unified Benchmark for Text-to-3D and Image-to-3D](https://arxiv.org/abs/2503.21745) | arXiv 2025 | [paper](https://arxiv.org/abs/2503.21745) |
| 2025-03 | vLLM-Based, 3D Generation Evaluation, No GT, CVPR | Authors | [Gen3DEval: Automatic Evaluation for 3D Generation Quality](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Gen3DEval_vLLM-Based_Automatic_3D_Generation_Evaluation_CVPR_2025_paper.html) | CVPR 2025 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Gen3DEval_vLLM-Based_Automatic_3D_Generation_Evaluation_CVPR_2025_paper.html) |
| 2025-03 | Robot Learning, 30K+ FPS, GPU-Parallelized | Authors | [ManiSkill3: GPU-Parallelized Robotics Simulator and Benchmark](https://arxiv.org/abs/2410.00425) | arXiv 2024 | [project](https://maniskill.ai/) |
| 2024-12-12 | Image-to-3D, Evaluation, Asset Quality | University of Oxford | [GSO / OmniObject3D Evaluation Protocols](https://omniobject3d.github.io/) | Dataset | [dataset](https://omniobject3d.github.io/) |
| 2024-06-07 | Reconstruction, Geometry, Feed-Forward | NAVER Labs | [DUSt3R Evaluation Suite](https://github.com/naver/dust3r) | GitHub | [github](https://github.com/naver/dust3r) |
| 2024-01 | Manipulation, 74 Tasks, Franka Panda, CoRL | Authors | [RLBench: A Robot Learning Benchmark and Learning Environment](https://arxiv.org/abs/2309.07918) | CoRL 2023 | [github](https://github.com/stepjam/RLBench) |
| 2024-01 | Long-Horizon, Language-Conditioned, 34 Tasks, RA-L Best Paper | Authors | [CALVIN: A Benchmark for Language-Conditioned Policy Learning](https://arxiv.org/abs/2112.03227) | RA-L 2022 Best Paper | [github](https://github.com/mees/calvin) |
| 2024-01 | Lifelong Robot Learning, 130 Tasks, 4 Suites, RSS | Authors | [LIBERO: Lifelong Robot Learning Benchmark](https://arxiv.org/abs/2306.03310) | RSS 2023 | [github](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| 2024-01 | Multi-Task, Meta-RL, 50 Tasks, Manipulation, CoRL | Authors | [Meta-World: A Benchmark and Evaluation for Multi-Task and Meta RL](https://meta-world.github.io/) | CoRL 2019 | [github](https://github.com/Farama-Foundation/Metaworld) |
| 2023-10-04 | Text-to-3D, Benchmark, Multi-View Metrics | Tsinghua | [T3Bench: Benchmarking Current Progress in Text-to-3D Generation](https://arxiv.org/abs/2310.02977) | arXiv | [project](https://t3bench.com/) |
| 2017-08-10 | MVS Benchmark, Mesh Accuracy, Completeness | Princeton / Intel | [Tanks and Temples Benchmark](https://www.tanksandtemples.org/) | TOG 2017 | [benchmark](https://www.tanksandtemples.org/) |

<a id="65-simulators--toolchains"></a>

### 6.5 Simulators & Toolchains

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2026-06-22 | UE5 Simulator, Multi-Robot SLAM, UAV+UGV | Georgia Tech | [HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration](https://arxiv.org/abs/2606.22756) | arXiv | [project](https://lunarlab-gatech.github.io/HERCULES-website/) |
| 2026-06-21 | Tactile Simulation, Dexterous Hands, 20K Envs | Authors | [Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks](https://arxiv.org/abs/2606.22332) | arXiv | [project](https://neuroagents-lab.github.io/2026-tactile-genesis/) |
| 2026-06-20 | Deformable Linear Objects, Isaac Sim, Cosserat Rods | Carnegie Mellon University | [DeformX: A Versatile Co-Simulation Framework for Deformable Linear Objects](https://arxiv.org/abs/2606.22116) | IROS 2026 | [project](https://deformx.github.io/) |
| 2024-05-20 | Robot Learning, Simulation, Isaac Lab | NVIDIA | [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) | GitHub | [github](https://github.com/isaac-sim/IsaacLab) |
| 2023-10-26 | Simulation, Asset Generation, Manipulation | NVIDIA | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](https://arxiv.org/abs/2310.17596) | CoRL 2023 | [github](https://github.com/NVlabs/mimicgen_environments) |
| 2023-07 | 3D Data Processing, Point Cloud, Mesh, ICP, Registration | Intel Labs | [Open3D: A Modern Library for 3D Data Processing](https://www.open3d.org/) | arXiv 2018 | [github](https://github.com/isl-org/Open3D) |
| 2023-07 | 3D Deep Learning, Differentiable Renderer, Mesh | Meta FAIR | [PyTorch3D: A Library for 3D Deep Learning](https://pytorch3d.org/) | arXiv 2020 | [github](https://github.com/facebookresearch/pytorch3d) |
| 2023-07 | Procedural Rendering, Blender, Data Pipeline | DLR | [BlenderProc: Procedural Pipeline for Photorealistic Rendering](https://arxiv.org/abs/1911.01911) | arXiv 2023 | [github](https://github.com/DLR-RM/BlenderProc) |
| 2023-07 | Grasping, 6-DoF, 1B+ Grasps, 88 Objects, CVPR | Authors | [GraspNet-1Billion: A Large-Scale Benchmark for Robotic Grasping](https://arxiv.org/abs/2003.01531) | CVPR 2020 | [github](https://github.com/graspnet/graspnet) |
| 2023-07 | Human Motion, MoCap, SMPL, 40+ Hours, ICCV | Authors | [AMASS: Archive of Motion Capture as Surface Shapes](https://amass.is.tue.mpg.de/) | ICCV 2019 | [dataset](https://amass.is.tue.mpg.de/) |
| 2023-07 | Human Pose, 3.6M Poses, 11 Actors, TPAMI | Authors | [Human3.6M: 3D Human Pose Estimation Benchmark](http://vision.imar.ro/human3.6m/) | TPAMI 2016 | [dataset](http://vision.imar.ro/human3.6m/) |
| 2023-02-03 | Robotics Simulation, Digital Twin, USD | NVIDIA | [Isaac Sim](https://developer.nvidia.com/isaac/sim) | Software | [docs](https://docs.isaacsim.omniverse.nvidia.com/) |
| 2021-10-18 | Robotics Simulator, Articulated Objects, SAPIEN | UC San Diego | [SAPIEN: A SimulAted Part-based Interactive ENvironment](https://sapien.ucsd.edu/) | CVPR 2020 | [github](https://github.com/haosulab/SAPIEN) |
| 2021-05-11 | Physics Engine, Robotics, Differentiable Simulation | DeepMind | [MuJoCo](https://mujoco.org/) | Software | [github](https://github.com/google-deepmind/mujoco) |
| 2019-06-14 | Embodied AI, Navigation, Simulation | Meta AI | [Habitat: A Platform for Embodied AI Research](https://aihabitat.org/) | ICCV 2019 | [github](https://github.com/facebookresearch/habitat-lab) |

## Acknowledgement

This repository is inspired by and complementary to:
- [Awesome-3D-Reconstruction-and-Generation](https://github.com/PolySummit/Awesome-3D-Reconstruction-and-Generation)
- [Awesome-3D-Generation](https://github.com/BunnySoCrazy/Awesome-3D-Generation)
- [awesome-3d-diffusion](https://github.com/cwchenwang/awesome-3d-diffusion)
- [awesome-3D-4D-Editing](https://github.com/2hiTee/awesome-3D-4D-Editing)
- [Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications)
- [awesome-nerf-editing](https://github.com/EricLee0224/awesome-nerf-editing)
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
