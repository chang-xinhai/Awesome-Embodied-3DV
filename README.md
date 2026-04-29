<div align="center">

<h1 id="awesome-embodied-3dv">Awesome-Embodied-3DV</h1>

<p>
  <strong>A curated map of 3D/4D perception, reconstruction, generation, simulation-ready assets, and world models for embodied AI.</strong>
</p>

<!-- [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) -->
<!-- [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) -->

<p>
  <a href="#-1-data-perception"><img alt="Perception" src="https://img.shields.io/badge/Data-Perception-a8d8ff?style=for-the-badge"></a>
  <a href="#-2-3d4d-representation"><img alt="Representation" src="https://img.shields.io/badge/3D%2F4D-Representation-b8e6c9?style=for-the-badge"></a>
  <a href="#-3-3d-reconstruction"><img alt="Reconstruction" src="https://img.shields.io/badge/3D-Reconstruction-ffd6a5?style=for-the-badge"></a>
  <a href="#-4-3d-generation"><img alt="Generation" src="https://img.shields.io/badge/3D-Generation-d7c5ff?style=for-the-badge"></a>
  <a href="#-5-embodiment--world-models"><img alt="Embodiment" src="https://img.shields.io/badge/Embodiment-World%20Models-c7f9cc?style=for-the-badge"></a>
  <a href="#-6-datasets-benchmarks--infrastructure"><img alt="Infrastructure" src="https://img.shields.io/badge/Benchmarks-Infrastructure-ffb7b2?style=for-the-badge"></a>
</p>

</div>

## About

**Awesome-Embodied-3DV** is a curated list for the research space where **3D vision, 3D/4D reconstruction, 3D generation, simulation-ready assets, and embodied world models** meet.

This repository focuses on:
- **Data Perception**: depth, normals, active imaging, panoramic/fisheye perception, and dense mapping signals that feed 3D systems
- **3D/4D Representation**: 3DGS, 4DGS, NeRF/SDF, mesh, voxel, point, and hybrid structures
- **3D Reconstruction**: offline, feed-forward, streaming, online, semantic, instance-level, and dynamic reconstruction
- **3D Generation**: object-level, part-level, articulated, scene-level, and simulation-ready asset generation
- **Embodiment & World Models**: reconstruction-based world models, dynamic scene graphs, robotics integration, and agent-facing 3D grounding
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
  - [Data Perception](#-1-data-perception)
    - [Depth & Normal Estimation](#11-depth--normal-estimation)
    - [Active Imaging & Sensors](#12-active-imaging--sensors)
    - [Dense Mapping Systems](#13-dense-mapping-systems)
  - [3D/4D Representation](#-2-3d4d-representation)
    - [Explicit & Hybrid Representations](#21-explicit--hybrid-representations)
    - [Neural Implicit Representations](#22-neural-implicit-representations)
    - [Dynamic & Spatiotemporal 4D](#23-dynamic--spatiotemporal-4d)
  - [3D Reconstruction](#-3-3d-reconstruction)
    - [Offline High-Fidelity Reconstruction](#31-offline-high-fidelity-reconstruction)
    - [Streaming & Online Reconstruction](#32-streaming--online-reconstruction)
    - [Dynamic 3D Reconstruction](#33-dynamic-3d-reconstruction)
  - [3D Generation](#-4-3d-generation)
    - [Object-Level Generation](#41-object-level-generation)
    - [Part-Level & Articulated Generation](#42-part-level--articulated-generation)
    - [Scene-Level Generation](#43-scene-level-generation)
  - [Embodiment & World Models](#-5-embodiment--world-models)
    - [Dynamic Scene Graphs & Tracking](#51-dynamic-scene-graphs--tracking)
    - [Reconstruction-Based World Models](#52-reconstruction-based-world-models)
    - [Robotics Integration & LLM Agents](#53-robotics-integration--llm-agents)
  - [Datasets, Benchmarks & Infrastructure](#-6-datasets-benchmarks--infrastructure)
    - [Surveys & Taxonomies](#61-surveys--taxonomies)
    - [Datasets for 3D Reconstruction](#62-datasets-for-3d-reconstruction)
    - [Datasets for 3D Generation](#63-datasets-for-3d-generation)
    - [Specific Benchmarks & Metrics](#64-specific-benchmarks--metrics)
    - [Simulators & Toolchains](#65-simulators--toolchains)
  - [Acknowledgement](#acknowledgement)
  - [Citation](#citation)

<h2 id="-1-data-perception">📡 1. Data Perception</h2>

Data perception covers the sensor-facing layer: extracting depth, normals, geometry priors, dense maps, and active-imaging signals from 2D images, video, or physical sensors.

<a id="11-depth--normal-estimation"></a>

### 1.1 Depth & Normal Estimation

#### 1.1.1 Monocular High-Fidelity Depth

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-12-09 | Any-View Depth, Metric Geometry, Multi-View | ByteDance | [Depth Anything 3: Recovering the Visual Space from Any Views](https://arxiv.org/abs/2512.08600) | arXiv | [project](https://depth-anything-3.github.io/) |
| 2024-06-14 | Monocular Depth, Foundation Model, Metric Depth | TikTok / HKU | [Depth Anything V2](https://arxiv.org/abs/2406.09414) | NeurIPS 2024 | [project](https://depth-anything-v2.github.io/) / [github](https://github.com/DepthAnything/Depth-Anything-V2) |
| 2024-06-05 | Metric Depth, Zero-Shot, Image Priors | Apple | [Depth Pro: Sharp Monocular Metric Depth in Less Than a Second](https://arxiv.org/abs/2410.02073) | arXiv | [github](https://github.com/apple/ml-depth-pro) |
| 2023-12-22 | Monocular Depth, Relative Depth, Foundation Model | TikTok / HKU | [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891) | CVPR 2024 | [project](https://depth-anything.github.io/) |
| 2023-04-24 | Monocular Depth, Zero-Shot, Affine-Invariant | Intel Labs | [Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](https://arxiv.org/abs/2312.02145) | CVPR 2024 | [project](https://marigoldmonodepth.github.io/) |

#### 1.1.2 Geometric Consistency Prior

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-07-19 | Feed-Forward 3D, Survey, Geometry Priors | NUS | [Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501) | arXiv | [project](https://fnzhan.com/3D-Reconstruction-and-Generation-Survey/) |
| 2025-03-18 | Metric 3D, Multi-Task, Geometry Foundation | Shanghai AI Lab | [Metric3D v2: A Versatile Monocular Geometric Foundation Model](https://arxiv.org/abs/2404.15506) | TPAMI 2025 | [project](https://jugghm.github.io/Metric3Dv2/) |
| 2024-10-02 | Normal Estimation, 3D Priors, Surface Geometry | Nvidia | [StableNormal: Reducing Diffusion Variance for Stable and Sharp Normal](https://arxiv.org/abs/2406.16864) | SIGGRAPH Asia 2024 | [project](https://stable-x.github.io/StableNormal/) |
| 2023-12-08 | Geometry, Normals, Depth, Multi-Task | Apple | [GeoWizard: Unleashing the Diffusion Priors for 3D Geometry Estimation from a Single Image](https://arxiv.org/abs/2403.12013) | ECCV 2024 | [project](https://fuxiao0719.github.io/projects/geowizard/) |

<a id="12-active-imaging--sensors"></a>

### 1.2 Active Imaging & Sensors

#### 1.2.1 Structured Light & Neural Decoding

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-08-05 | Structured Light, Single-Shot, Neural Decoding | ShanghaiTech | [Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding](https://arxiv.org/abs/2408.03029) | arXiv | [paper](https://arxiv.org/abs/2408.03029) |
| 2024-04-29 | Event Camera, Active Stereo, Depth | Tsinghua | [Event-Based Structured Light for Depth Reconstruction](https://arxiv.org/abs/2404.17973) | arXiv | [paper](https://arxiv.org/abs/2404.17973) |
| 2023-06-15 | Structured Light, Phase Unwrapping, Learning | Nanjing University | [Deep Learning-Based Structured Light 3D Imaging: A Survey](https://arxiv.org/abs/2306.10409) | arXiv | [survey](https://arxiv.org/abs/2306.10409) |

#### 1.2.2 Panoramic & Fisheye Perception

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-06-23 | Panoramic Depth, 360 Vision, Foundation Model | Lingbo AI | [Lingbo-Depth](https://github.com/LingboAI/Lingbo-Depth) | GitHub | [github](https://github.com/LingboAI/Lingbo-Depth) |
| 2025-06-23 | Panoramic Mapping, Large-Scale, 3D Map | Lingbo AI | [Lingbo-Map](https://github.com/LingboAI/Lingbo-Map) | GitHub | [github](https://github.com/LingboAI/Lingbo-Map) |
| 2021-09-06 | 360 Depth, Indoor, Panoramic Images | CERTH | [Pano3D: A Holistic Benchmark and a Solid Baseline for 360 Depth Estimation](https://arxiv.org/abs/2109.02749) | CVPRW 2021 | [project](https://vcl3d.github.io/Pano3D/) / [github](https://github.com/VCL3D/Pano3D) |

<a id="13-dense-mapping-systems"></a>

### 1.3 Dense Mapping Systems

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-01-19 | Real-Time Mapping, Open-Vocabulary, 3D Semantics | MIT | [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650) | ICRA 2024 | [project](https://concept-graphs.github.io/) / [github](https://github.com/concept-graphs/concept-graphs) |
| 2024-06-17 | Dense SLAM, Gaussian Splatting, RGB-D | TUM | [Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741) | CVPR 2024 | [github](https://github.com/muskie82/MonoGS) |
| 2023-05-30 | Neural Mapping, Dense RGB-D SLAM, SDF | HKUST | [NICE-SLAM: Neural Implicit Scalable Encoding for SLAM](https://arxiv.org/abs/2112.12130) | CVPR 2022 | [project](https://pengsongyou.github.io/nice-slam) |

<h2 id="-2-3d4d-representation">🧱 2. 3D/4D Representation</h2>

This section focuses on the mathematical and data-structure layer used to represent geometry, appearance, and motion.

<a id="21-explicit--hybrid-representations"></a>

### 2.1 Explicit & Hybrid Representations

#### 2.1.1 Structure-Aware 3D Gaussian Splatting

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-07-10 | 3DGS, Structure, Sparse Views | USTC | [SparseGS: Real-Time 360 Sparse View Synthesis using Gaussian Splatting](https://arxiv.org/abs/2312.00206) | ECCV 2024 | [project](https://formycat.github.io/SparseGS-Real-Time-360-Sparse-View-Synthesis-using-Gaussian-Splatting/) |
| 2024-07-02 | 2DGS, Surface Reconstruction, Geometry | TUM | [2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://arxiv.org/abs/2403.17888) | SIGGRAPH 2024 | [project](https://surfsplatting.github.io/) |
| 2024-04-16 | 3DGS, Mesh Extraction, Surface | ETH Zurich | [SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction](https://arxiv.org/abs/2311.12775) | CVPR 2024 | [project](https://anttwo.github.io/sugar/) |
| 2023-08-08 | 3DGS, Real-Time Rendering, Explicit Radiance | Inria | [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | SIGGRAPH 2023 | [github](https://github.com/graphdeco-inria/gaussian-splatting) |

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
| 2024-02-05 | 4DGS, Dynamic Scenes, Real-Time Rendering | Zhejiang University | [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2310.08528) | CVPR 2024 | [project](https://guanjunwu.github.io/4dgs/) |
| 2023-10-16 | Dynamic 3DGS, Scene Motion, Multi-View Video | Cornell | [Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis](https://dynamic3dgaussians.github.io/) | 3DV 2024 | [github](https://github.com/JonathonLuiten/Dynamic3DGaussians) |
| 2023-08-21 | Dynamic NeRF, Deformation, Canonical Space | Google Research | [HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields](https://arxiv.org/abs/2106.13228) | SIGGRAPH Asia 2021 | [project](https://hypernerf.github.io/) |

#### 2.3.2 Deformation Graphs & Canonical Spaces

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-04-18 | Deformation, Dynamic Radiance Fields, Canonical | ETH Zurich | [SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](https://arxiv.org/abs/2312.14937) | CVPR 2024 | [project](https://yihua7.github.io/SC-GS-web/) |
| 2023-05-17 | Non-Rigid Tracking, Neural Deformation, 4D | Tsinghua | [Neuralangelo: High-Fidelity Neural Surface Reconstruction](https://arxiv.org/abs/2306.03092) | CVPR 2023 | [project](https://research.nvidia.com/labs/dir/neuralangelo/) |

<h2 id="-3-3d-reconstruction">🏗️ 3. 3D Reconstruction</h2>

Reconstruction systems recover objects or scenes from images, video, RGB-D, or multi-sensor streams under offline, online, and dynamic conditions.

<a id="31-offline-high-fidelity-reconstruction"></a>

### 3.1 Offline High-Fidelity Reconstruction

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
| 2025-03-18 | Feed-Forward 3D, Pose-Free, Point Map | Meta AI | [VGGT: Visual Geometry Grounded Transformer](https://vgg-t.github.io/) | CVPR 2025 | [github](https://github.com/facebookresearch/vggt) |
| 2024-12-11 | Feed-Forward, SLAM, DUSt3R, Online | Shanghai AI Lab | [SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos](https://arxiv.org/abs/2412.09401) | arXiv | [project](https://slam3r.github.io/) |
| 2024-08-28 | Spatial Memory, Feed-Forward, Multi-View | HKU | [Spann3R: 3D Reconstruction with Spatial Memory](https://arxiv.org/abs/2408.16061) | arXiv | [project](https://hengyiwang.github.io/projects/spann3r) |
| 2024-06-05 | Multi-View Reconstruction, Matching, MVS | NAVER Labs | [MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion](https://arxiv.org/abs/2409.19152) | 3DV 2025 | [github](https://github.com/naver/mast3r) |

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
| 2026-03-09 | Dynamic VGGT, Autonomous Driving, 4D | Fudan University | [DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving](https://arxiv.org/abs/2603.08254) | arXiv | [paper](https://arxiv.org/abs/2603.08254) |
| 2025-11-23 | Dynamic Geometry, Spatiotemporal, VGGT | Huazhong University of Science and Technology | [4D-VGGT: A General Foundation Model with SpatioTemporal Awareness for Dynamic Scene Geometry Estimation](https://arxiv.org/abs/2511.18416) | arXiv | [paper](https://arxiv.org/abs/2511.18416) |
| 2025-10-20 | VGGT-4D, Pose/Geometry, Dynamic Mask | Harvard | [PAGE-4D: Disentangled Pose and Geometry Estimation for 4D Perception](https://arxiv.org/abs/2510.17568) | ICLR 2026 | [project](https://page4d.github.io/) |
| 2024-10-04 | Monocular Video, Dynamic Reconstruction, 3DGS | University of Oxford | [MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion](https://arxiv.org/abs/2410.03825) | arXiv | [project](https://monst3r-project.github.io/) |

<h2 id="-4-3d-generation">🎛️ 4. 3D Generation</h2>

This section tracks methods that create new 3D assets, parts, articulated objects, scenes, and editable 3D worlds, with emphasis on physical and simulation use.

<a id="41-object-level-generation"></a>

### 4.1 Object-Level Generation

#### 4.1.1 Image/Text to 3D Mesh

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-11-19 | Single Image, Textured Mesh, SAM 3D | Meta AI | [SAM 3D Objects](https://github.com/facebookresearch/sam-3d-objects) | GitHub | [github](https://github.com/facebookresearch/sam-3d-objects) |
| 2025-01-21 | Image-to-3D, Mesh, Texture | Tencent | [Hunyuan3D 2.0: Scaling Diffusion Models for High Resolution Textured 3D Assets Generation](https://arxiv.org/abs/2501.12202) | arXiv | [github](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) |
| 2024-12-02 | Structured Latents, Text/Image-to-3D, Mesh | Microsoft | [TRELLIS: Structured 3D Latents for Scalable and Versatile 3D Generation](https://arxiv.org/abs/2412.01506) | CVPR 2025 | [project](https://trellis3d.github.io/) |
| 2024-03-04 | Single Image, Fast 3D, Mesh | Stability AI | [TripoSR: Fast 3D Object Reconstruction from a Single Image](https://arxiv.org/abs/2403.02151) | arXiv | [github](https://github.com/VAST-AI-Research/TripoSR) |
| 2023-08-28 | Text-to-3D, Diffusion, Mesh | UC Berkeley | [DreamFusion: Text-to-3D using 2D Diffusion](https://arxiv.org/abs/2209.14988) | ICLR 2023 | [project](https://dreamfusion3d.github.io/) |

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
| 2025-11-02 | URDF, 3D MLLM, Articulated Objects | Tsinghua | [URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model](https://openreview.net/forum?id=g3EF5XsapH) | ICLR 2026 | [paper](https://arxiv.org/abs/2511.00940) |
| 2025-02-26 | Articulated Objects, 3DGS, Joint Estimation | Peking University | [ArtGS: Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459) | ICLR 2025 | [project](https://buzz-beater.github.io/artgs/) |
| 2024-09-26 | Open-Vocabulary, URDF, Articulation | Stanford | [Articulate Anything: Open-vocabulary 3D Articulated Object Generation](https://openreview.net/forum?id=6akuzEqP38) | ICLR 2025 | [project](https://articulate-anything.github.io/) |

#### 4.2.2 Part-Aware Assembly & Editing

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-01-20 | Part-Level 3D, Object Decomposition, Generation | University of Waterloo | [PartCrafter: Structured 3D Mesh Generation via Compositional Latent Diffusion Transformers](https://arxiv.org/abs/2501.11015) | arXiv | [project](https://wgsxm.github.io/projects/partcrafter/) |
| 2024-06-13 | Part-Aware, Shape Assembly, 3D Generation | Shanghai AI Lab | [Michelangelo: Conditional 3D Shape Generation based on Shape-Image-Text Aligned Latent Representation](https://arxiv.org/abs/2306.17115) | NeurIPS 2023 | [github](https://github.com/NeuralCarver/Michelangelo) |
| 2023-12-04 | Shape Program, Structure, Editable Assets | MIT | [Shape2Program: Learning to Infer Shape Programs from 3D Shapes](https://arxiv.org/abs/2312.08307) | arXiv | [project](https://shape2prog.csail.mit.edu/) |

<a id="43-scene-level-generation"></a>

### 4.3 Scene-Level Generation

#### 4.3.1 Layout & Procedural Generation

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
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

<h2 id="-5-embodiment--world-models">🌐 5. Embodiment & World Models</h2>

This section focuses on how reconstructed and generated 3D assets become physical, interactive, trackable, and agent-facing.

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
| 2024-02-26 | Interactive Environment, Generative World, Agent | Google DeepMind | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | ICML 2024 | [project](https://sites.google.com/view/genie-2024/) |

<a id="53-robotics-integration--llm-agents"></a>

### 5.3 Robotics Integration & LLM Agents

#### 5.3.1 Sim-to-Real via Generated Assets

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-02-26 | Articulated Objects, URDF, Manipulation | Peking University | [ArtGS: Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459) | ICLR 2025 | [project](https://buzz-beater.github.io/artgs/) |
| 2024-09-26 | Open-Vocabulary, Articulation, URDF | Stanford | [Articulate Anything: Open-vocabulary 3D Articulated Object Generation](https://openreview.net/forum?id=6akuzEqP38) | ICLR 2025 | [project](https://articulate-anything.github.io/) |
| 2023-06-16 | Digital Twin, Synthetic Scenes, Embodied AI | NVIDIA | [ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://arxiv.org/abs/2206.06994) | NeurIPS 2022 | [project](https://procthor.allenai.org/) |

#### 5.3.2 VLMs for 3D Grounding & Planning

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2024-11-11 | 3D Grounding, VLM, Point Cloud | Shanghai AI Lab | [LLaVA-3D: A Simple yet Effective Pathway to Empowering LMMs with 3D Awareness](https://arxiv.org/abs/2410.06250) | arXiv | [github](https://github.com/ZCMax/LLaVA-3D) |
| 2024-07-12 | Spatial VLM, 3D Reasoning, Robotics | Stanford | [SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities](https://arxiv.org/abs/2401.12168) | CVPR 2024 | [project](https://spatial-vlm.github.io/) |
| 2023-11-13 | Embodied Planning, 3D Scene, LLM | MIT | [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](https://arxiv.org/abs/2307.06135) | CoRL 2023 | [project](https://sayplan.github.io/) |

<h2 id="-6-datasets-benchmarks--infrastructure">🧰 6. Datasets, Benchmarks & Infrastructure</h2>

This section is the toolbox and dictionary for quickly choosing datasets, benchmarks, metrics, simulators, and reference surveys.

<a id="61-surveys--taxonomies"></a>

### 6.1 Surveys & Taxonomies

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2025-07-19 | Feed-Forward Reconstruction, View Synthesis, Survey | NUS | [Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501) | arXiv | [project](https://fnzhan.com/3D-Reconstruction-and-Generation-Survey/) |
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
| 2024-01-05 | Dynamic Scenes, Multi-View Video, 4D | University of Oxford | [PanopticSports](https://github.com/JonathonLuiten/Dynamic3DGaussians) | Dataset | [github](https://github.com/JonathonLuiten/Dynamic3DGaussians) |
| 2023-06-06 | Indoor RGB-D, Habitat, 3D Scenes | Meta AI | [Habitat-Matterport 3D Semantics Dataset](https://aihabitat.org/datasets/hm3d/) | Dataset | [dataset](https://aihabitat.org/datasets/hm3d/) |
| 2017-07-26 | Indoor RGB-D, Semantic Labels, Reconstruction | Stanford | [ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes](http://www.scan-net.org/) | CVPR 2017 | [dataset](http://www.scan-net.org/) |
| 2012-06-18 | Indoor RGB-D, NYUv2, Semantics | NYU | [NYU Depth Dataset V2](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html) | ECCV 2012 | [dataset](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html) |

<a id="63-datasets-for-3d-generation"></a>

### 6.3 Datasets for 3D Generation

#### 6.3.1 Object-Level 3D/Text-to-3D

| Date | Keywords | Institute (first) | Paper / Resource | Publication | Others |
| :--: | :------: | :---------------: | :--------------- | :---------: | :----: |
| 2023-07-10 | 3D Objects, Web-Scale, Textured Mesh | Allen Institute for AI | [Objaverse-XL: A Universe of 10M+ 3D Objects](https://arxiv.org/abs/2307.05663) | NeurIPS 2023 | [dataset](https://objaverse.allenai.org/) |
| 2022-12-13 | 3D Objects, LVIS Annotations, Web-Scale | Allen Institute for AI | [Objaverse: A Universe of Annotated 3D Objects](https://arxiv.org/abs/2212.08051) | CVPR 2023 | [dataset](https://objaverse.allenai.org/) |
| 2021-09-16 | Real Scanned Objects, Simulation Assets | Google Research | [Google Scanned Objects](https://app.gazebosim.org/GoogleResearch/fuel/collections/Scanned%20Objects%20by%20Google%20Research) | ICRA 2022 | [dataset](https://app.gazebosim.org/GoogleResearch/fuel/collections/Scanned%20Objects%20by%20Google%20Research) |
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
| 2023-10-04 | Text-to-3D, Benchmark, Multi-View Metrics | Tsinghua | [T3Bench: Benchmarking Current Progress in Text-to-3D Generation](https://arxiv.org/abs/2310.02977) | arXiv | [project](https://t3bench.com/) |
| 2024-12-12 | Image-to-3D, Evaluation, Asset Quality | University of Oxford | [GSO / OmniObject3D Evaluation Protocols](https://omniobject3d.github.io/) | Dataset | [dataset](https://omniobject3d.github.io/) |
| 2024-06-07 | Reconstruction, Geometry, Feed-Forward | NAVER Labs | [DUSt3R Evaluation Suite](https://github.com/naver/dust3r) | GitHub | [github](https://github.com/naver/dust3r) |
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
