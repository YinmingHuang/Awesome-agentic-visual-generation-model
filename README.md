# Awesome-agentic-visual-generation-model
# A Survey on Visual Generation Agents

A curated list of research papers and open-source resources for Agentic and LLM-driven/guided Text-to-Image (T2I) generation and editing.

---

## 📅 News
* **[2026/06]** Updated newly released papers from mid-2026 (e.g., APE, GenClaw, MetaPoint).
* **[2025/12]** Structured the repository to categorize prompt engineering, planning, verification, and orchestration.

---



## Part 1 : Image Gen Agents & LLM-Driven Image Gen

### Mind Map：

```mermaid
mindmap
  root((Image-Gen-Agent &<br/>LLM-Driven-Image-Gen))
    
    Module 1: Semantic Understanding & Prompt Enhancement<br/>_Enhance prompts using LLMs for richer semantics_
      ::icon(fa fa-magic)
      [RL / Preference / Test-time Opt]
        Optimizing Prompts; Promptify; Improving T2I Consistency; PromptSculptor; GenPilot; APE; Preference-Guided Opt; TIPO; Universal Optimizer; Reward-Agnostic Opt
      [LLM-Enhanced Diffusion]
        LLM-grounded Diffusion; ELLA; LLM4GEN; Exploring LLMs in Prompt Encoding
      [MLLMs for Direct Generation]
        DiffusionGPT; Mastering T2I Diffusion; LLM Blueprint; Generating Images with MLLMs; Paragraph-to-Image

    Module 2: Planning & Compositional Control<br/>_Layout, spatial, sequence planning for precise control_
      [Layout / Spatial Planning]
        LayoutGPT; Visual Programming; Divide and Conquer; PointT2I; Two-Stage Layout Control
      [Multi-Object Composition]
        MuLan; GenArtist; LayerCraft; MCCD; CountLoop; MetaPoint
      [Code / Tool / Reasoning-Driven]
        GenClaw; GlyphBanana; LLMControl; DraCo; GoT; MetaCanvas
      [Unified / In-Context]
        UNIMO-G; Multi-Subject In-Context

    Module 3: Feedback Verification & Iterative Refinement<br/>_Evaluate, correct, and refine via closed-loop learning_
      [Self-Correction / Self-Improvement]
        Self-correcting LLM Diffusion; Maestro; SIDiffAgent; MemoGen; Agentic Retoucher; EditRefiner
      [Reward Modeling & Preference]
        Preference Adaptive T2I; Image-POSER; MLLMs as Customized Reward; Personalized Reward; Rewards Are Enough
      [Verification & Test-time]
        MLLMs as Evaluators; Test-time Prompt Refine; Can We Generate with CoT?; M3
      [Iterative Refinement]
        Multi-Agent Iterative Refine; Generation Navigator; MLLM-Guided Correction

    Module 4: Interactive Collaboration<br/>_Multi-turn dialogue, user-agent co-creation_
      [Multi-Turn Dialogue Systems]
        Visual ChatGPT; DiffChat; DialogGen; Talk2Image; coDrawAgents
      [Story Visualization]
        VisAgent; AgentStory; DreamStory
      [User-Guided / Proactive]
        Anywhere; Proactive Agents; T2I-Copilot
      [Retrieval-Augmented]
        Diffusion Augmented Retrieval

    Module 5: System Integration & Orchestration<br/>_Integrate experts, tools, knowledge for complex tasks_
      [Multi-Agent Orchestration]
        DiffusionAgent; CREA; Mac-Tiger; AgentComp; Crafter; ICG
      [World Knowledge & Retrieval Grounding]
        WORLD-TO-IMAGE; Mind-Brush; Gen-Searcher; Unify-Agent
      [Self-Evolving & Routing]
        GenEvolve; OctoT2I; GEMS
      [Unified Reasoning & Generation]
        ImAgent; GenAgent; Think-Then-Generate; UniReason 1.0

    Other Related Works<br/>_3D generation, evaluation, RAG, editing, etc._
      [3D / Novel View]
        MUSES; MVLLaVA
      [Evaluation & Benchmarks]
        Unified Agentic Eval; Draw ALL Your Imagine; AtelierEval
      [Retrieval-Augmented Gen]
        Re-Imagen; RealRAG; ImageRAG; Cross-modal RAG
      [Image Editing]
        Image Editing As Programs; Plug-and-Play Editing
      [Miscellaneous]
        Region-Aware T2I; VisualPrompter; Collaborative MARL; Policy Optimized Pipeline; Show, Don't Tell; Unleashing LLMs via AR Alignment; Bifrost-1; LLMs as Universal Reasoners
```

### 📌 Table of Contents

* [Module 1: Semantic Understanding and Prompt Enhancement](#module-1-semantic-understanding-and-prompt-enhancement)
* [Module 2: Planning and Compositional Control](#module-2-planning-and-compositional-control)
* [Module 3: Feedback Verification and Iterative Refinement](#module-3-feedback-verification-and-iterative-refinement)
* [Module 4: Interactive Collaboration](#module-4-interactive-collaboration)
* [Module 5: System Integration and Orchestration](#module-5-system-integration-and-orchestration)
* [Other Related Works](#other-related-works)

---

### Module 1: Semantic Understanding and Prompt Enhancement

This module covers works utilizing Large Language Models (LLMs) to expand, optimize, and enhance input prompts for richer semantic understanding.

| Title & Authors | Paper | Github | Website | Venue & Date |
| :--- | :---: | :---: | :---: | :---: |
| **[Optimizing Prompts for Text-to-Image Generation](https://arxiv.org/abs/2212.09681)** <br> *Y. Hao, Z. Chi, L. Dong, F. Wei* | [![arXiv](https://img.shields.io/badge/arXiv-2212.09681-b31b1b.svg)](https://arxiv.org/abs/2212.09681) | [![Star](https://img.shields.io/github/stars/microsoft/Promptist.svg?style=social&label=Star)](https://github.com/microsoft/Promptist) | - | NeurIPS, 2023 |
| **[Promptify: Text-to-Image Generation through Interactive Prompt Exploration with LLMs](https://arxiv.org/abs/2304.09337)** <br> *S. Brade, B. Wang, M. Sousa, S. Oore, T. Grossman* | [![arXiv](https://img.shields.io/badge/arXiv-2304.09337-b31b1b.svg)](https://arxiv.org/abs/2304.09337) | [![Star](https://img.shields.io/github/stars/promptslab/Promptify.svg?style=social&label=Star)](https://github.com/promptslab/Promptify) | - | arXiv, 2023 |
| **[LLM-grounded Diffusion: Enhancing Prompt Understanding of Text-to-Image Diffusion Models with LLMs](https://arxiv.org/abs/2305.13655)** <br> *L. Lian, B. Li, A. Yala, T. Darrell* | [![arXiv](https://img.shields.io/badge/arXiv-2305.13655-b31b1b.svg)](https://arxiv.org/abs/2305.13655) | [![Star](https://img.shields.io/github/stars/TonyLianLong/LLM-groundedDiffusion.svg?style=social&label=Star)](https://github.com/TonyLianLong/LLM-groundedDiffusion) | - | arXiv, 2023 |
| **[Improving Text-to-Image Consistency via Automatic Prompt Optimization](https://arxiv.org/abs/2403.17804)** <br> *O. Manas et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2403.17804-b31b1b.svg)](https://arxiv.org/abs/2403.17804) | - | - | arXiv, 2024 |
| **[DiffusionGPT: LLM-Driven Text-to-Image Generation System](https://arxiv.org/abs/2401.10061v1)** <br> *J. Qin et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2401.10061v1-b31b1b.svg)](https://arxiv.org/abs/2401.10061v1) | [![Star](https://img.shields.io/github/stars/DiffusionGPT/DiffusionGPT.svg?style=social&label=Star)](https://github.com/DiffusionGPT/DiffusionGPT) | - | arXiv, 2024 |
| **[Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs](https://arxiv.org/abs/2401.11708)** <br> *L. Yang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2401.11708-b31b1b.svg)](https://arxiv.org/abs/2401.11708) | - | - | arXiv, 2024 |
| **[LLM Blueprint: Enabling Text-to-Image Generation with Complex and Detailed Prompts](https://arxiv.org/abs/2310.10640)** <br> *H. Gani et al.* | [![Paper](https://img.shields.io/badge/Paper-OpenReview-blue.svg)](https://openreview.net/forum?id=uNWe5bXv8p) | - | - | ICLR, 2024 |
| **[PromptSculptor: Multi-Agent Based Text-to-Image Prompt Optimization](https://arxiv.org/abs/2509.12446)** <br> *D. Xiang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2509.12446-b31b1b.svg)](https://arxiv.org/abs/2509.12446) | - | - | EMNLP Demo, 2025 |
| **[GenPilot: A Multi-Agent System for Test-Time Prompt Optimization in Image Generation](https://arxiv.org/abs/2510.07217)** <br> *W. Ye et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2510.07217-b31b1b.svg)](https://arxiv.org/abs/2510.07217) | - | - | arXiv, 2025 |
| **[APE: Agentic Prompt Enhancer for Image Generation and Editing](https://arxiv.org/abs/2606.00204)** <br> *Z. Huang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2606.00204-b31b1b.svg)](https://arxiv.org/abs/2606.00204) | - | - | arXiv, 2026 |
| **[Preference-Guided Prompt Optimization for Text-to-Image Generation](https://arxiv.org/abs/2602.13131)** <br> *Z. Li, Y.-C. Liao, C. Holz* | [![arXiv](https://img.shields.io/badge/arXiv-2602.13131-b31b1b.svg)](https://arxiv.org/abs/2602.13131) | [![Star](https://img.shields.io/github/stars/siplab-gt/APPO.svg?style=social&label=Star)](https://github.com/siplab-gt/APPO) | - | CHI, 2026 |
| **[TIPO: Text to Image with Text Pre-sampling for Prompt Optimization](https://openreview.net/forum?id=dDnw3Pp70x)** <br> *S.-Y. Yeh et al.* | [![Paper](https://img.shields.io/badge/Paper-OpenReview-blue.svg)](https://openreview.net/forum?id=dDnw3Pp70x) | - | - | ICLR, 2026 |
| **[Generating Images with Multimodal Language Models](https://arxiv.org/abs/2305.17216)** <br> *J. Y. Koh, D. Fried, R. Salakhutdinov* | [![arXiv](https://img.shields.io/badge/arXiv-2305.17216-b31b1b.svg)](https://arxiv.org/abs/2305.17216) | - | - | arXiv, 2023 |
| **[ELLA: Equip Diffusion Models with LLM for Enhanced Semantic Alignment](https://arxiv.org/abs/2403.05135)** <br> *X. Hu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2403.05135-b31b1b.svg)](https://arxiv.org/abs/2403.05135) | [![Star](https://img.shields.io/github/stars/TencentQQGYLab/ELLA.svg?style=social&label=Star)](https://github.com/TencentQQGYLab/ELLA) | - | NeurIPS, 2024 |
| **[Exploring the Role of Large Language Models in Prompt Encoding for Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d68c1d10957c8d21ed9dea209533c5a4-Abstract-Conference.html)** <br> *B. Ma et al.* | [![Paper](https://img.shields.io/badge/Paper-NeurIPS-blue.svg)](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d68c1d10957c8d21ed9dea209533c5a4-Abstract-Conference.html) | - | - | NeurIPS, 2024 |
| **[LLM4GEN: Leveraging Semantic Representation of LLMs for Text-to-Image Generation](https://arxiv.org/abs/2407.00737)** <br> *M. Liu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2407.00737-b31b1b.svg)](https://arxiv.org/abs/2407.00737) | - | - | arXiv, 2024 |
| **[Paragraph-to-Image Generation with Information-Enriched Diffusion Model](https://arxiv.org/abs/2311.14284)** <br> *W. Wu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2311.14284-b31b1b.svg)](https://arxiv.org/abs/2311.14284) | - | - | arXiv, 2023 |
| **[Universal Prompt Optimizer for Safe Text-to-Image Generation](https://arxiv.org/abs/2412.03541)** <br> *X. Zhang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2412.03541-b31b1b.svg)](https://arxiv.org/abs/2412.03541) | - | - | arXiv, 2024 |
| **[Reward-Agnostic Prompt Optimization for Text-to-Image Diffusion Models](https://arxiv.org/abs/2506.16853)** <br> *S. Kim, Y. Cha, J. Yoo, S. Hong* | [![arXiv](https://img.shields.io/badge/arXiv-2506.16853-b31b1b.svg)](https://arxiv.org/abs/2506.16853) | - | - | arXiv, 2025 |

[⬆ Back to Top](#-table-of-contents)

---

### Module 2: Planning and Compositional Control

Focuses on using agents and LLMs to perform spatial, layout, and sequence planning, achieving precise semantic and regional control over image composition.

| Title & Authors | Paper | Github | Website | Venue & Date |
| :--- | :---: | :---: | :---: | :---: |
| **[LayoutGPT: Compositional Visual Planning and Generation with Large Language Models](https://arxiv.org/abs/2305.15393)** <br> *W. Feng et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2305.15393-b31b1b.svg)](https://arxiv.org/abs/2305.15393) | [![Star](https://img.shields.io/github/stars/weixi-feng/LayoutGPT.svg?style=social&label=Star)](https://github.com/weixi-feng/LayoutGPT) | [![Website](https://img.shields.io/badge/Website-9cf)](https://weixi-feng.github.io/LayoutGPT/) | NeurIPS, 2023 |
| **[Visual Programming for Text-to-Image Generation and Evaluation](https://arxiv.org/abs/2305.15328)** <br> *J. Cho and A. Kembhavi* | [![arXiv](https://img.shields.io/badge/arXiv-2305.15328-b31b1b.svg)](https://arxiv.org/abs/2305.15328) | [![Star](https://img.shields.io/github/stars/j-min/VPGen.svg?style=social&label=Star)](https://github.com/j-min/VPGen) | [![Website](https://img.shields.io/badge/Website-9cf)](https://vp-t2i.github.io/) | NeurIPS, 2023 |
| **[Divide and Conquer: Language Models can Plan and Self-Correct for Compositional Text-to-Image Generation](https://arxiv.org/abs/2401.15688)** <br> *Z. Wang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2401.15688-b31b1b.svg)](https://arxiv.org/abs/2401.15688) | - | - | arXiv, 2024 |
| **[MuLan: Multimodal-LLM Agent for Progressive and Interactive Multi-Object Diffusion](https://arxiv.org/abs/2402.12741)** <br> *S. Li et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2402.12741-b31b1b.svg)](https://arxiv.org/abs/2402.12741) | [![Star](https://img.shields.io/github/stars/measure-infinity/mulan-code.svg?style=social&label=Star)](https://github.com/measure-infinity/mulan-code) | [![Website](https://img.shields.io/badge/Website-9cf)](https://measure-infinity.github.io/mulan-page/) | arXiv, 2024 |
| **[GenArtist: Multimodal LLM as an Agent for Unified Image Generation and Editing](https://arxiv.org/abs/2407.05600)** <br> *Z. Wang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2407.05600-b31b1b.svg)](https://arxiv.org/abs/2407.05600) | - | [![Website](https://img.shields.io/badge/Website-9cf)](https://zhenyuw16.github.io/GenArtist_page/) | arXiv, 2024 |
| **[LayerCraft: Enhancing Text-to-Image Generation with CoT Reasoning and Layered Object Integration](https://arxiv.org/abs/2504.00010)** <br> *Y. Zhang, J. Li, and Y.-W. Tai* | [![arXiv](https://img.shields.io/badge/arXiv-2504.00010-b31b1b.svg)](https://arxiv.org/abs/2504.00010) | [![Star](https://img.shields.io/github/stars/PeterYYZhang/LayerCraft.svg?style=social&label=Star)](https://github.com/PeterYYZhang/LayerCraft) | - | arXiv, 2025 |
| **[MCCD: Multi-Agent Collaboration-based Compositional Diffusion for Complex Text-to-Image Generation](https://arxiv.org/abs/2505.02648)** <br> *M. Li et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2505.02648-b31b1b.svg)](https://arxiv.org/abs/2505.02648) | - | - | arXiv, 2025 |
| **[LLMControl: Grounded Control of Text-to-Image Diffusion-based Synthesis with Multimodal LLMs](https://arxiv.org/abs/2507.19939)** <br> *J. Wang, R. Chen, and H. Cui* | [![arXiv](https://img.shields.io/badge/arXiv-2507.19939-b31b1b.svg)](https://arxiv.org/abs/2507.19939) | - | - | arXiv, 2025 |
| **[CountLoop: Training-Free High-Instance Image Generation via Iterative Agent Guidance](https://arxiv.org/abs/2508.16644)** <br> *A. Mondal et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2508.16644-b31b1b.svg)](https://arxiv.org/abs/2508.16644) | - | [![Website](https://img.shields.io/badge/Website-9cf)](https://mondalanindya.github.io/CountLoop/) | arXiv, 2025 |
| **[GenClaw: Code-Driven Agentic Image Generation](https://arxiv.org/abs/2605.30248)** <br> *J. Ye et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2605.30248-b31b1b.svg)](https://arxiv.org/abs/2605.30248) | [![Star](https://img.shields.io/github/stars/yejy53/GenClaw.svg?style=social&label=Star)](https://github.com/yejy53/GenClaw) | - | arXiv, 2026 |
| **[GlyphBanana: Advancing Precise Text Rendering Through Agentic Workflows](https://arxiv.org/abs/2603.12155)** <br> *Z. Yan et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2603.12155-b31b1b.svg)](https://arxiv.org/abs/2603.12155) | [![Star](https://img.shields.io/github/stars/yuriYanZeXuan/GlyphBanana.svg?style=social&label=Star)](https://github.com/yuriYanZeXuan/GlyphBanana) | - | arXiv, 2026 |
| **[MetaPoint: Unlocking Precise Spatial Control in Agentic Visual Generation](https://arxiv.org/abs/2606.05031)** <br> *D. Zhou et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2606.05031-b31b1b.svg)](https://arxiv.org/abs/2606.05031) | - | - | arXiv, 2026 |
| **[UNIMO-G: Unified Image Generation through Multimodal Conditional Diffusion](https://arxiv.org/abs/2401.13388)** <br> *W. Li, X. Xu, J. Liu, and X. Xiao* | [![arXiv](https://img.shields.io/badge/arXiv-2401.13388-b31b1b.svg)](https://arxiv.org/abs/2401.13388) | - | - | ACL, 2024 |
| **[PointT2I: LLM-based Text-to-Image Generation via Keypoints](https://arxiv.org/abs/2506.01370)** <br> *T. Lee, D. Lee, and M. Kang* | [![arXiv](https://img.shields.io/badge/arXiv-2506.01370-b31b1b.svg)](https://arxiv.org/abs/2506.01370) | - | - | arXiv, 2025 |
| **[A Two-Stage System for Layout-Controlled Image Generation using Large Language Models and Diffusion Models](https://arxiv.org/abs/2511.06888)** <br> *J.-H. Koch, J. Krumme, and K. Gadzicki* | [![arXiv](https://img.shields.io/badge/arXiv-2511.06888-b31b1b.svg)](https://arxiv.org/abs/2511.06888) | - | - | arXiv, 2025 |
| **[Multimodal Large Language Models for Multi-Subject In-Context Image Generation](https://arxiv.org/abs/2604.07422)** <br> *Y. Zhou, D. Chen, H. Zheng, and J. Shen* | [![arXiv](https://img.shields.io/badge/arXiv-2604.07422-b31b1b.svg)](https://arxiv.org/abs/2604.07422) | - | - | arXiv, 2026 |
| **[DraCo: Draft as CoT for Text-to-Image Preview and Rare Concept Generation](https://arxiv.org/abs/2512.05112)** <br> *D. Jiang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2512.05112-b31b1b.svg)](https://arxiv.org/abs/2512.05112) | [![Star](https://img.shields.io/github/stars/CaraJ7/DraCo.svg?style=social&label=Star)](https://github.com/CaraJ7/DraCo) | - | arXiv, 2025 |
| **[Exploring MLLM-Diffusion Information Transfer with MetaCanvas](https://arxiv.org/abs/2512.11464)** <br> *H. Lin et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2512.11464-b31b1b.svg)](https://arxiv.org/abs/2512.11464) | - | [![Website](https://img.shields.io/badge/Website-9cf)](https://metacanvas.github.io) | arXiv, 2025 |
| **[GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing](https://arxiv.org/abs/2503.10639)** <br> *R. Fang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2503.10639-b31b1b.svg)](https://arxiv.org/abs/2503.10639) | [![Star](https://img.shields.io/github/stars/rongyaofang/GoT.svg?style=social&label=Star)](https://github.com/rongyaofang/GoT) | - | NeurIPS, 2025 |

[⬆ Back to Top](#-table-of-contents)

---

### Module 3: Feedback Verification and Iterative Refinement

Explores methodologies for evaluating generated images (using reward models or VLM evaluators) and applying closed-loop correction or reinforcement learning to iteratively refine generations.

| Title & Authors | Paper | Github | Website | Venue & Date |
| :--- | :---: | :---: | :---: | :---: |
| **[Self-correcting LLM-controlled Diffusion Models](https://arxiv.org/abs/2311.16090)** <br> *T.-H. Wu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2311.16090-b31b1b.svg)](https://arxiv.org/abs/2311.16090) | [![Star](https://img.shields.io/github/stars/tsunghan-wu/SLD.svg?style=social&label=Star)](https://github.com/tsunghan-wu/SLD) | [![Website](https://img.shields.io/badge/Website-9cf)](https://self-correcting-llm-diffusion.github.io) | CVPR, 2024 |
| **[Preference Adaptive and Sequential Text-to-Image Generation](https://arxiv.org/abs/2412.10419)** <br> *O. Nabati et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2412.10419-b31b1b.svg)](https://arxiv.org/abs/2412.10419) | - | - | ICML, 2025 |
| **[A Multi-Agent Approach for Iterative Refinement in Visual Content Generation](https://multiagents.org/2025_artifacts/a_multi_agent_approach_for_iterative_refinement_in_visual_content_generation.pdf)** <br> *A. Nayak et al.* | [![Paper](https://img.shields.io/badge/Paper-WMAC-blue.svg)](https://multiagents.org/2025_artifacts/a_multi_agent_approach_for_iterative_refinement_in_visual_content_generation.pdf) | - | - | AAAI WMAC, 2025 |
| **[Maestro: Self-Improving Text-to-Image Generation via Agent Orchestration](https://arxiv.org/abs/2509.10704)** <br> *X. Wan et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2509.10704-b31b1b.svg)](https://arxiv.org/abs/2509.10704) | - | - | arXiv, 2025 |
| **[Image-POSER: Reflective RL for Multi-Expert Image Generation and Editing](https://arxiv.org/abs/2511.11780)** <br> *H. Mohebbi et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2511.11780-b31b1b.svg)](https://arxiv.org/abs/2511.11780) | - | - | arXiv, 2025 |
| **[Generation Navigator: A State-Aware Agentic Framework for Image Generation](https://arxiv.org/abs/2605.17969)** <br> *J. Liu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2605.17969-b31b1b.svg)](https://arxiv.org/abs/2605.17969) | - | - | arXiv, 2026 |
| **[M3: High-fidelity Text-to-Image Generation via Multi-Modal, Multi-Agent and Multi-Round Visual Reasoning](https://arxiv.org/abs/2602.06166)** <br> *B. Yang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2602.06166-b31b1b.svg)](https://arxiv.org/abs/2602.06166) | [![Star](https://img.shields.io/github/stars/LINs-lab/M3.svg?style=social&label=Star)](https://github.com/LINs-lab/M3) | - | arXiv, 2026 |
| **[Agentic Retoucher for Text-To-Image Generation](https://arxiv.org/abs/2601.02046)** <br> *S. Shen et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2601.02046-b31b1b.svg)](https://arxiv.org/abs/2601.02046) | [![Star](https://img.shields.io/github/stars/MediaX-SJTU/Agentic-Retoucher.svg?style=social&label=Star)](https://github.com/MediaX-SJTU/Agentic-Retoucher) | - | CVPR, 2026 |
| **[EditRefiner: A Human-Aligned Agentic Framework for Image Editing Refinement](https://arxiv.org/abs/2605.07457)** <br> *Z. Xu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2605.07457-b31b1b.svg)](https://arxiv.org/abs/2605.07457) | [![Star](https://img.shields.io/github/stars/IntMeGroup/EditRefiner.svg?style=social&label=Star)](https://github.com/IntMeGroup/EditRefiner) | - | arXiv, 2026 |
| **[SIDiffAgent: Self-Improving Diffusion Agent](https://arxiv.org/abs/2602.02051)** <br> *S. Garg, A. Singh, and G. K. Nayak* | [![arXiv](https://img.shields.io/badge/arXiv-2602.02051-b31b1b.svg)](https://arxiv.org/abs/2602.02051) | - | - | arXiv, 2026 |
| **[MemoGen: Can Past Experience Improve Future Text-to-Image Generation?](https://arxiv.org/abs/2606.03243)** <br> *W. Chen et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2606.03243-b31b1b.svg)](https://arxiv.org/abs/2606.03243) | [![Star](https://img.shields.io/github/stars/Chatonz/MemoGen.svg?style=social&label=Star)](https://github.com/Chatonz/MemoGen) | - | arXiv, 2026 |
| **[Multimodal LLM-Guided Semantic Correction in Text-to-Image Diffusion](https://arxiv.org/abs/2505.20053)** <br> *Z. Lv et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2505.20053-b31b1b.svg)](https://arxiv.org/abs/2505.20053) | [![Star](https://img.shields.io/github/stars/HelloZicky/PPAD.svg?style=social&label=Star)](https://github.com/HelloZicky/PPAD) | - | arXiv, 2025 |
| **[Test-time Prompt Refinement for Text-to-Image Models](https://arxiv.org/abs/2507.22076)** <br> *M. A. H. Khan et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2507.22076-b31b1b.svg)](https://arxiv.org/abs/2507.22076) | - | - | ICCV Workshop, 2025 |
| **[Multi-Modal Language Models as Text-to-Image Model Evaluators](https://arxiv.org/abs/2505.00759)** <br> *J. Chen et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2505.00759-b31b1b.svg)](https://arxiv.org/abs/2505.00759) | - | - | arXiv, 2025 |
| **[Multimodal LLMs as Customized Reward Models for Text-to-Image Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Multimodal_LLMs_as_Customized_Reward_Models_for_Text-to-Image_Generation_ICCV_2025_paper.html)** <br> *S. Zhou et al.* | [![Paper](https://img.shields.io/badge/Paper-ICCV_OpenAccess-blue.svg)](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Multimodal_LLMs_as_Customized_Reward_Models_for_Text-to-Image_Generation_ICCV_2025_paper.html) | [![Star](https://img.shields.io/github/stars/sjz5202/LLaVA-Reward.svg?style=social&label=Star)](https://github.com/sjz5202/LLaVA-Reward) | - | ICCV, 2025 |
| **[Personalized Reward Modeling for Text-to-Image Generation](https://arxiv.org/abs/2511.19458)** <br> *J. Lee, R. Heo, and D. Lee* | [![arXiv](https://img.shields.io/badge/arXiv-2511.19458-b31b1b.svg)](https://arxiv.org/abs/2511.19458) | - | - | arXiv, 2025 |
| **[Rewards Are Enough for Fast Photo-Realistic Text-to-image Generation](https://arxiv.org/abs/2503.13070)** <br> *Y. Luo, T. Hu, W. Luo, K. Kawaguchi, and J. Tang* | [![arXiv](https://img.shields.io/badge/arXiv-2503.13070-b31b1b.svg)](https://arxiv.org/abs/2503.13070) | [![Star](https://img.shields.io/github/stars/Luo-Yihong/R0.svg?style=social&label=Star)](https://github.com/Luo-Yihong/R0) | - | arXiv, 2025 |
| **[Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step](https://arxiv.org/abs/2501.13926)** <br> *Z. Guo et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2501.13926-b31b1b.svg)](https://arxiv.org/abs/2501.13926) | [![Star](https://img.shields.io/github/stars/ZiyuGuo99/Image-Generation-CoT.svg?style=social&label=Star)](https://github.com/ZiyuGuo99/Image-Generation-CoT) | - | CVPR, 2025 |

[⬆ Back to Top](#-table-of-contents)

---

### Module 4: Interactive Collaboration

Focuses on multi-turn dialogue systems and interactive collaboration frameworks, enabling users to direct, edit, and visualize complex narratives or retrieve images progressively through natural conversation with agents.

| Title & Authors | Paper | Github | Website | Venue & Date |
| :--- | :---: | :---: | :---: | :---: |
| **[Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models](https://arxiv.org/abs/2303.04671)** <br> *C. Wu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2303.04671-b31b1b.svg)](https://arxiv.org/abs/2303.04671) | [![Star](https://img.shields.io/github/stars/microsoft/visual-chatgpt.svg?style=social&label=Star)](https://github.com/microsoft/visual-chatgpt) | - | arXiv, 2023 |
| **[DiffChat: Learning to Chat with Text-to-Image Synthesis Models for Interactive Image Creation](https://aclanthology.org/2024.findings-acl.522/)** <br> *J. Wang et al.* | [![Paper](https://img.shields.io/badge/Paper-ACL_Findings-blue.svg)](https://aclanthology.org/2024.findings-acl.522/) | [![Star](https://img.shields.io/github/stars/alibaba/EasyNLP.svg?style=social&label=Star)](https://github.com/alibaba/EasyNLP) | - | ACL Findings, 2024 |
| **[DialogGen: Multi-modal Interactive Dialogue System for Multi-turn Text-to-Image Generation](https://aclanthology.org/2025.findings-naacl.25/)** <br> *M. Huang et al.* | [![Paper](https://img.shields.io/badge/Paper-NAACL_Findings-blue.svg)](https://aclanthology.org/2025.findings-naacl.25/) | [![Star](https://img.shields.io/github/stars/Centaurusalpha/DialogGen.svg?style=social&label=Star)](https://github.com/Centaurusalpha/DialogGen) | [![Website](https://img.shields.io/badge/Website-9cf)](https://centaurusalpha.github.io/DialogGen/) | NAACL Findings, 2025 |
| **[Anywhere: A Multi-Agent Framework for User-Guided, Reliable, and Diverse Foreground-Conditioned Image Generation](https://ojs.aaai.org/index.php/AAAI/article/view/32797)** <br> *T. Xie et al.* | [![Paper](https://img.shields.io/badge/Paper-AAAI-blue.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/32797) | [![Star](https://img.shields.io/github/stars/Sealical/anywhere-multi-agent.svg?style=social&label=Star)](https://github.com/Sealical/anywhere-multi-agent) | [![Website](https://img.shields.io/badge/Website-9cf)](https://anywheremultiagent.github.io/) | AAAI, 2025 |
| **[Proactive Agents for Multi-Turn Text-to-Image Generation Under Uncertainty](https://arxiv.org/abs/2412.06771)** <br> *M. Hahn et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2412.06771-b31b1b.svg)](https://arxiv.org/abs/2412.06771) | [![Star](https://img.shields.io/github/stars/google-deepmind/proactive_t2i_agents.svg?style=social&label=Star)](https://github.com/google-deepmind/proactive_t2i_agents) | - | ICML, 2025 |
| **[VisAgent: Narrative-Preserving Story Visualization Framework](https://arxiv.org/abs/2503.02399)** <br> *S. Kim et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2503.02399-b31b1b.svg)](https://arxiv.org/abs/2503.02399) | - | - | ICASSP, 2025 |
| **[AgentStory: A Multi-Agent System for Story Visualization with Multi-Subject Consistent Text-to-Image Generation](https://dl.acm.org/doi/10.1145/3731715.3733271)** <br> *T. Zhou et al.* | [![Paper](https://img.shields.io/badge/Paper-ACM_ICMR-blue.svg)](https://dl.acm.org/doi/10.1145/3731715.3733271) | [![Star](https://img.shields.io/github/stars/tc2000731/AgentStory.svg?style=social&label=Star)](https://github.com/tc2000731/AgentStory) | - | ICMR, 2025 |
| **[T2I-Copilot: A Training-Free Multi-Agent Text-to-Image System for Enhanced Prompt Interpretation and Interactive Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_T2I-Copilot_A_Training-Free_Multi-Agent_Text-to-Image_System_for_Enhanced_Prompt_Interpretation_ICCV_2025_paper.html)** <br> *C.-Y. Chen et al.* | [![Paper](https://img.shields.io/badge/Paper-ICCV_OpenAccess-blue.svg)](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_T2I-Copilot_A_Training-Free_Multi-Agent_Text-to-Image_System_for_Enhanced_Prompt_Interpretation_ICCV_2025_paper.html) | [![Star](https://img.shields.io/github/stars/SHI-Labs/T2I-Copilot.svg?style=social&label=Star)](https://github.com/SHI-Labs/T2I-Copilot) | - | ICCV, 2025 |
| **[Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing](https://ojs.aaai.org/index.php/AAAI/article/view/40519)** <br> *S. Ma et al.* | [![Paper](https://img.shields.io/badge/Paper-AAAI-blue.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/40519) | - | - | AAAI, 2026 |
| **[coDrawAgents: A Multi-Agent Dialogue Framework for Compositional Image Generation](https://arxiv.org/abs/2603.12829)** <br> *C. Li et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2603.12829-b31b1b.svg)](https://arxiv.org/abs/2603.12829) | [![Star](https://img.shields.io/github/stars/ChunhanLiii/coDrawAgents.svg?style=social&label=Star)](https://github.com/ChunhanLiii/coDrawAgents) | - | arXiv, 2026 |
| **[Diffusion Augmented Retrieval: A Training-Free Approach to Interactive Text-to-Image Retrieval](https://arxiv.org/abs/2501.15379v2)** <br> *Z. Long et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2501.15379v2-b31b1b.svg)](https://arxiv.org/abs/2501.15379v2) | [![Star](https://img.shields.io/github/stars/longkukuhi/Diffusion-Augmented-Retrieval.svg?style=social&label=Star)](https://github.com/longkukuhi/Diffusion-Augmented-Retrieval) | - | SIGIR, 2025 |
| **[DreamStory: Open-Domain Story Visualization by LLM-Guided Multi-Subject Consistent Diffusion](https://ieeexplore.ieee.org/document/10.1109/TPAMI.2025.3600149)** <br> *H. He et al.* | [![Paper](https://img.shields.io/badge/Paper-IEEE_T--PAMI-blue.svg)](https://ieeexplore.ieee.org/document/10.1109/TPAMI.2025.3600149) | [![Star](https://img.shields.io/github/stars/hehuiguo/DreamStory.svg?style=social&label=Star)](https://github.com/hehuiguo/DreamStory) | [![Website](https://img.shields.io/badge/Website-9cf)](https://dream-xyz.github.io/dreamstory) | IEEE T-PAMI, 2025 |

[⬆ Back to Top](#-table-of-contents)

---

### Module 5: System Integration and Orchestration

Covers system-level frameworks and routers that integrate multiple specialized experts, tools, cognitive reasoning mechanisms, or knowledge bases to solve complex, open-domain text-to-image tasks.

| Title & Authors | Paper | Github | Website | Venue & Date |
| :--- | :---: | :---: | :---: | :---: |
| **[DiffusionAgent: Navigating Expert Models for Agentic Image Generation](https://arxiv.org/abs/2401.10061v2)** <br> *J. Qin et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2401.10061v2-b31b1b.svg)](https://arxiv.org/abs/2401.10061v2) | [![Star](https://img.shields.io/github/stars/DiffusionAgent/DiffusionAgent.svg?style=social&label=Star)](https://github.com/DiffusionAgent/DiffusionAgent) | [![Website](https://img.shields.io/badge/Website-9cf)](https://DiffusionAgent.github.io) | arXiv, 2024 |
| **[CREA: A Collaborative Multi-Agent Framework for Creative Content Generation with Diffusion Models](https://arxiv.org/abs/2504.05306)** <br> *K. Venkatesh, C. Dunlop, and P. Yanardag* | [![arXiv](https://img.shields.io/badge/arXiv-2504.05306-b31b1b.svg)](https://arxiv.org/abs/2504.05306) | - | - | arXiv, 2025 |
| **[Mac-Tiger: Multi-Agent Cooperation for Enhanced Text-to-Image Generation](https://openreview.net/forum?id=e7Zsc3oRer)** <br> *Y. Luo and M. Cheng* | [![Paper](https://img.shields.io/badge/Paper-OpenReview-blue.svg)](https://openreview.net/forum?id=e7Zsc3oRer) | - | - | ICLR Submission, 2026 |
| **[ImAgent: A Unified Multimodal Agent Framework for Test-Time Scalable Image Generation](https://arxiv.org/abs/2511.11483)** <br> *K. Wang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2511.11483-b31b1b.svg)](https://arxiv.org/abs/2511.11483) | - | - | arXiv, 2025 |
| **[WORLD-TO-IMAGE: Grounding Text-to-Image Generation with Agent-Driven World Knowledge](https://arxiv.org/abs/2510.04201)** <br> *M. H. Son et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2510.04201-b31b1b.svg)](https://arxiv.org/abs/2510.04201) | [![Star](https://img.shields.io/github/stars/mhson-kyle/World-To-Image.svg?style=social&label=Star)](https://github.com/mhson-kyle/World-To-Image) | - | arXiv, 2025 |
| **[AgentComp: From Agentic Reasoning to Compositional Mastery in Text-to-Image Models](https://arxiv.org/abs/2512.09081)** <br> *A. Zarei et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2512.09081-b31b1b.svg)](https://arxiv.org/abs/2512.09081) | - | - | arXiv, 2025 |
| **[Mind-Brush: Integrating Agentic Cognitive Search and Reasoning into Image Generation](https://arxiv.org/abs/2602.01756)** <br> *J. He et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2602.01756-b31b1b.svg)](https://arxiv.org/abs/2602.01756) | - | - | arXiv, 2026 |
| **[Gen-Searcher: Reinforcing Agentic Search for Image Generation](https://arxiv.org/abs/2603.28767)** <br> *K. Feng et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2603.28767-b31b1b.svg)](https://arxiv.org/abs/2603.28767) | - | - | arXiv, 2026 |
| **[Unify-Agent: A Unified Multimodal Agent for World-Grounded Image Synthesis](https://arxiv.org/abs/2603.29620)** <br> *S. Chen et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2603.29620-b31b1b.svg)](https://arxiv.org/abs/2603.29620) | - | - | arXiv, 2026 |
| **[GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning](https://arxiv.org/abs/2601.18543)** <br> *K. Jiang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2601.18543-b31b1b.svg)](https://arxiv.org/abs/2601.18543) | [![Star](https://img.shields.io/github/stars/deep-kaixun/GenAgent.svg?style=social&label=Star)](https://github.com/deep-kaixun/GenAgent) | - | arXiv, 2026 |
| **[Think-Then-Generate: Reasoning-Aware Text-to-Image Diffusion with LLM Encoders](https://arxiv.org/abs/2601.10332)** <br> *S. Kou et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2601.10332-b31b1b.svg)](https://arxiv.org/abs/2601.10332) | - | - | arXiv, 2026 |
| **[UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing](https://arxiv.org/abs/2602.02437)** <br> *D. Wang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2602.02437-b31b1b.svg)](https://arxiv.org/abs/2602.02437) | - | - | arXiv, 2026 |
| **[GEMS: Agent-Native Multimodal Generation with Memory and Skills](https://arxiv.org/abs/2603.28088)** <br> *Z. He et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2603.28088-b31b1b.svg)](https://arxiv.org/abs/2603.28088) | - | - | arXiv, 2026 |
| **[GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation](https://arxiv.org/abs/2605.21605)** <br> *S. Chen et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2605.21605-b31b1b.svg)](https://arxiv.org/abs/2605.21605) | - | [![Website](https://img.shields.io/badge/Website-9cf)](https://ephemeral182.github.io/GenEvolve/) | arXiv, 2026 |
| **[OctoT2I: A Self-Evolving Agentic Text-to-Image Router](https://arxiv.org/abs/2606.01803)** <br> *X. Jiang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2606.01803-b31b1b.svg)](https://arxiv.org/abs/2606.01803) | [![Star](https://img.shields.io/github/stars/JaxJiang2642081986/OctoT2I.svg?style=social&label=Star)](https://github.com/JaxJiang2642081986/OctoT2I) | - | CVPR, 2026 |
| **[Crafter: A Multi-Agent Harness for Editable Scientific Figure Generation from Diverse Inputs](https://arxiv.org/abs/2605.30611)** <br> *H. Zhao et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2605.30611-b31b1b.svg)](https://arxiv.org/abs/2605.30611) | [![Star](https://img.shields.io/github/stars/HaozheZhao/Crafter.svg?style=social&label=Star)](https://github.com/HaozheZhao/Crafter) | - | arXiv, 2026 |
| **[ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment](https://aclanthology.org/2025.emnlp-main.617/)** <br> *Z. Bian et al.* | [![Paper](https://img.shields.io/badge/Paper-EMNLP-blue.svg)](https://aclanthology.org/2025.emnlp-main.617/) <br> [![arXiv](https://img.shields.io/badge/arXiv-2605.27374-b31b1b.svg)](https://arxiv.org/abs/2605.27374) | - | - | EMNLP, 2025 |

[⬆ Back to Top](#-table-of-contents)

---

### Other Related Works

A curated collection of broader related works, including 3D-controllable generation, novel view synthesis, evaluation benchmarks, and retrieval-augmented generation (RAG) paradigms.

| Title & Authors | Paper | Github | Website | Venue & Date |
| :--- | :---: | :---: | :---: | :---: |
| **[Re-Imagen: Retrieval-Augmented Text-to-Image Generator](https://arxiv.org/abs/2209.14491)** <br> *W. Chen et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2209.14491-b31b1b.svg)](https://arxiv.org/abs/2209.14491) | - | - | ICLR, 2023 |
| **[MUSES: 3D-Controllable Image Generation via Multi-Modal Agent Collaboration](https://arxiv.org/abs/2408.10605)** <br> *Y. Ding et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2408.10605-b31b1b.svg)](https://arxiv.org/abs/2408.10605) <br> [![Paper](https://img.shields.io/badge/Paper-AAAI-blue.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/32280) | [![Star](https://img.shields.io/github/stars/DINGYANB/MUSES.svg?style=social&label=Star)](https://github.com/DINGYANB/MUSES) | - | AAAI, 2025 |
| **[MVLLaVA: An Intelligent Agent for Unified and Flexible Novel View Synthesis](https://arxiv.org/abs/2409.07129)** <br> *H. Jiang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2409.07129-b31b1b.svg)](https://arxiv.org/abs/2409.07129) | - | [![Website](https://img.shields.io/badge/Website-9cf)](https://jamesjg.github.io/MVLLaVA_homepage/) | ICMEW, 2025 |
| **[Region-Aware Text-to-Image Generation via Hard Binding and Soft Refinement](https://arxiv.org/abs/2411.06558)** <br> *Z. Chen et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2411.06558-b31b1b.svg)](https://arxiv.org/abs/2411.06558) <br> [![Paper](https://img.shields.io/badge/Paper-ICCV_OpenAccess-blue.svg)](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_RAGD_Regional-Aware_Diffusion_Model_for_Text-to-Image_Generation_ICCV_2025_paper.html) | [![Star](https://img.shields.io/github/stars/NJU-PCALab/RAG-Diffusion.svg?style=social&label=Star)](https://github.com/NJU-PCALab/RAG-Diffusion) | - | ICCV, 2025 |
| **[Twin Co-Adaptive Dialogue for Progressive Image Generation](https://arxiv.org/abs/2504.14868)** <br> *J. Wang et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2504.14868-b31b1b.svg)](https://arxiv.org/abs/2504.14868) | - | - | arXiv, 2025 |
| **[Image Editing As Programs with Diffusion Models](https://arxiv.org/abs/2506.04158)** <br> *Y. Hu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2506.04158-b31b1b.svg)](https://arxiv.org/abs/2506.04158) | [![Star](https://img.shields.io/github/stars/Cicici1109/IEAP.svg?style=social&label=Star)](https://github.com/Cicici1109/IEAP) | [![Website](https://img.shields.io/badge/Website-9cf)](https://yujiahu.github.io/IEAP/) | NeurIPS, 2025 |
| **[VisualPrompter: Semantic-Aware Prompt Optimization with Visual Feedback for Text-to-Image Synthesis](https://arxiv.org/abs/2506.23138)** <br> *S. Wu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2506.23138-b31b1b.svg)](https://arxiv.org/abs/2506.23138) <br> [![Paper](https://img.shields.io/badge/Paper-OpenReview-blue.svg)](https://openreview.net/forum?id=hIwVFRLaFy) | [![Star](https://img.shields.io/github/stars/teheperinko541/VisualPrompter.svg?style=social&label=Star)](https://github.com/teheperinko541/VisualPrompter) | - | ICLR, 2026 |
| **[Collaborative Text-to-Image Generation via Multi-Agent Reinforcement Learning and Semantic Fusion](https://arxiv.org/abs/2510.10633)** <br> *J. Shi et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2510.10633-b31b1b.svg)](https://arxiv.org/abs/2510.10633) | - | - | arXiv, 2025 |
| **[Policy Optimized Text-to-Image Pipeline Design](https://arxiv.org/abs/2505.21478)** <br> *U. Gadot et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2505.21478-b31b1b.svg)](https://arxiv.org/abs/2505.21478) | - | - | NeurIPS, 2025 |
| **[A Unified Agentic Framework for Evaluating Conditional Image Generation](https://aclanthology.org/2025.acl-long.620/)** <br> *J. Wang et al.* | [![Paper](https://img.shields.io/badge/Paper-ACL-blue.svg)](https://aclanthology.org/2025.acl-long.620/) <br> [![arXiv](https://img.shields.io/badge/arXiv-2504.07046-b31b1b.svg)](https://arxiv.org/abs/2504.07046) | [![Star](https://img.shields.io/github/stars/HITsz-TMG/Agentic-CIGEval.svg?style=social&label=Star)](https://github.com/HITsz-TMG/Agentic-CIGEval) | - | ACL, 2025 |
| **[Draw ALL Your Imagine: A Holistic Benchmark and Agent Framework for Complex Instruction-based Image Generation](https://arxiv.org/abs/2505.24787)** <br> *Y. Zhou, J. Yuan, and Q. Wang* | [![arXiv](https://img.shields.io/badge/arXiv-2505.24787-b31b1b.svg)](https://arxiv.org/abs/2505.24787) | [![Star](https://img.shields.io/github/stars/yczhou001/LongBench-T2I.svg?style=social&label=Star)](https://github.com/yczhou001/LongBench-T2I) | - | arXiv, 2025 |
| **[SynthSeg-Agents: Multi-Agent Synthetic Data Generation for Zero-Shot Weakly Supervised Semantic Segmentation](https://arxiv.org/abs/2512.15310)** <br> *W. Wu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2512.15310-b31b1b.svg)](https://arxiv.org/abs/2512.15310) | - | - | arXiv, 2025 |
| **[RealRAG: Retrieval-augmented Realistic Image Generation via Self-reflective Contrastive Learning](https://arxiv.org/abs/2502.00848)** <br> *Y. Lyu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2502.00848-b31b1b.svg)](https://arxiv.org/abs/2502.00848) | - | - | ICML, 2025 |
| **[ImageRAG: Dynamic Image Retrieval for Reference-Guided Image Generation](https://arxiv.org/abs/2502.09411)** <br> *R. Shalev-Arkushin et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2502.09411-b31b1b.svg)](https://arxiv.org/abs/2502.09411) | - | [![Website](https://img.shields.io/badge/Website-9cf)](https://imagerag.github.io/) | ICLR, 2026 |
| **[Cross-modal RAG: Sub-dimensional Retrieval-Augmented Text-to-Image Generation](https://arxiv.org/abs/2505.21956)** <br> *M. Zhu et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2505.21956-b31b1b.svg)](https://arxiv.org/abs/2505.21956) | [![Star](https://img.shields.io/github/stars/mndzhu/Cross-modal-RAG-Official.svg?style=social&label=Star)](https://github.com/mndzhu/Cross-modal-RAG-Official) | - | arXiv, 2025 |
| **[Show, Don't Tell: Morphing Latent Reasoning into Image Generation](https://arxiv.org/abs/2602.02227)** <br> *H. H. Chen et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2602.02227-b31b1b.svg)](https://arxiv.org/abs/2602.02227) | [![Star](https://img.shields.io/github/stars/HKUST-KnowLab/LatentMorph.svg?style=social&label=Star)](https://github.com/HKUST-KnowLab/LatentMorph) | - | ICML, 2026 |
| **[A Plug-and-Play Agentic Framework for Text Guided Image Editing](https://openreview.net/forum?id=EPAuWPVcZQ)** <br> *D. Bandyopadhyay et al.* | [![Paper](https://img.shields.io/badge/Paper-OpenReview-blue.svg)](https://openreview.net/forum?id=EPAuWPVcZQ) | - | - | ICLR Submission, 2026 |
| **[AtelierEval: Agentic Evaluation of Humans & LLMs as Text-to-Image Prompters](https://arxiv.org/abs/2605.22645)** <br> *H. Luo et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2605.22645-b31b1b.svg)](https://arxiv.org/abs/2605.22645) | - | - | ICML, 2026 |
| **[Unleashing the Potential of Large Language Models for Text-to-Image Generation through Autoregressive Representation Alignment](https://arxiv.org/abs/2503.07334)** <br> *X. Xie et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2503.07334-b31b1b.svg)](https://arxiv.org/abs/2503.07334) <br> [![Paper](https://img.shields.io/badge/Paper-AAAI-blue.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/38089) | - | - | AAAI, 2026 |
| **[Bifrost-1: Bridging Multimodal LLMs and Diffusion Models with Patch-level CLIP Latents](https://arxiv.org/abs/2508.05954)** <br> *H. Lin et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2508.05954-b31b1b.svg)](https://arxiv.org/abs/2508.05954) | [![Star](https://img.shields.io/github/stars/hanlincs/Bifrost-1.svg?style=social&label=Star)](https://github.com/hanlincs/Bifrost-1) | - | NeurIPS, 2025 |
| **[Large Language Models are Universal Reasoners for Visual Generation](https://arxiv.org/abs/2605.04040)** <br> *S. Ren et al.* | [![arXiv](https://img.shields.io/badge/arXiv-2605.04040-b31b1b.svg)](https://arxiv.org/abs/2605.04040) | - | - | arXiv, 2026 |

[⬆Back to Top](#-table-of-contents)
# Awesome-agentic-visual-generation-model
