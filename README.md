# Awesome Agentic Visual Generation

> Paper coming soon.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated and taxonomy-driven collection of papers on agents that plan, execute, evaluate, revise, and improve visual generation. The repository covers image generation and editing, video generation and editing, 3D scene construction, and interactive visual worlds.

The primary organization follows the maximum control authority of the system. Modality and mechanism are secondary tags. This prevents tool use, multi-agent design, memory, or reinforcement learning from being treated as agenticity levels by themselves.

## Contents

- [Scope and inclusion rule](#scope-and-inclusion-rule)
- [Controller-capability taxonomy](#controller-capability-taxonomy)
- [L1: Conditioning Control](#l1-conditioning-control)
- [L2: Execution Control](#l2-execution-control)
- [L3: Outcome-Adaptive Control](#l3-outcome-adaptive-control)
- [L4: Experience-Adaptive Control](#l4-experience-adaptive-control)
- [Evaluation, Benchmarks, and Reward Models](#evaluation-benchmarks-and-reward-models)

## Scope and inclusion rule

An agentic visual generation system contains a visual generator or editor and a controller that makes generation-level decisions. The controller may be external, hybrid, or internalized in a unified model.

We classify a system by the highest controller capability demonstrated by the complete method:

- The action type does not determine the level. A prompt rewrite before generation is L1, while a prompt rewrite caused by inspection of a generated image is L3.
- Tool use describes the action space. Multi-agent design describes the topology. Reinforcement learning describes a training method. None of them alone determines the level.
- A paper appears once in L1-L4 according to its maximum demonstrated level. The `Path` column records the lower-level capabilities that it also contains.
- Fixed generators, fixed pipelines, stand-alone evaluators, reward models, and benchmarks are not generation controllers. They are listed separately.

Official resources are listed in separate `GitHub` and `Website` columns. A dash means that no author-maintained resource could be verified at the time of the latest update. Official datasets are linked from the `Website` column.

**Latest update (August 2026):** added ToolArtist, VideoCoCo, ReCA, Audio-Visual Flamingo, and the IA-Bench and MSVE-Bench evaluation resources; also re-verified Qwen-Image-Agent.

## Controller-capability taxonomy

| Level | Controller capability | Main question | Typical controlled variables |
| :---: | --- | --- | --- |
| **L1** | Conditioning control | What should be provided to the generator? | Prompt, layout, reference, knowledge, motion plan |
| **L2** | Execution control | Which capability should be invoked, how, and when? | Generator, tool, arguments, roles, action order |
| **L3** | Outcome-adaptive control | What should happen after observing the result? | Revision, editing, rerouting, regeneration, stopping |
| **L4** | Experience-adaptive control | How should completed trajectories change future decisions? | Long-term memory, skill, capability profile, policy |

The levels form a capability progression:

```text
conditions  ->  execution  ->  current trajectory  ->  future trajectories
    L1              L2                 L3                      L4
```

Modality tags used below are `Image`, `Editing`, `Video`, `3D`, and `World`.

## L1: Conditioning Control

L1 controllers construct or modify the information supplied to a generator. Generator invocation and the remaining execution procedure are externally specified or fixed.

### Prompt, preference, and intent conditioning

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [Promptist: Optimizing Prompts for Text-to-Image Generation](https://arxiv.org/abs/2212.09611) | [GitHub](https://github.com/microsoft/LMOps/tree/main/promptist) | [Website](https://aka.ms/promptist-demo) | L1 | Image | Learned prompt policy | 2022 |
| [DiffChat: Learning to Chat with Text-to-Image Synthesis Models](https://arxiv.org/abs/2403.04997) | [GitHub](https://github.com/alibaba/EasyNLP) | - | L1 | Image | Instruction-conditioned prompt modification | 2024 |
| [TIPO: Text to Image with Text Presampling for Prompt Optimization](https://arxiv.org/abs/2411.08127) | [GitHub](https://github.com/KohakuBlueleaf/KGen) | - | L1 | Image | Prompt expansion | 2024 |
| [POSI: Universal Prompt Optimizer for Safe Text-to-Image Generation](https://arxiv.org/abs/2402.10882) | - | - | L1 | Image | Safety-aware prompt optimization | 2024 |
| [PASTA: Preference Adaptive and Sequential Text-to-Image Generation](https://arxiv.org/abs/2412.10419) | - | [Dataset](https://www.kaggle.com/datasets/googleai/pasta-data) | L1 | Image | Preference-conditioned prompt policy | 2024 |
| [APE: Agentic Prompt Enhancer for Image Generation and Editing](https://arxiv.org/abs/2606.00204) | - | [Website](https://research.nvidia.com/labs/sil/projects/ape/) | L1 | Image, Editing | Prompt enhancement | 2026 |
| [ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment](https://arxiv.org/abs/2605.27374) | - | - | L1 | Image | Prompting and preference alignment | 2026 |

### Structured and internal conditioning

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [LLM-grounded Diffusion](https://arxiv.org/abs/2305.13655) | [GitHub](https://github.com/TonyLianLong/LLM-groundedDiffusion) | [Website](https://llm-grounded-diffusion.github.io/) | L1 | Image | Bounding-box planning | 2023 |
| [LayoutGPT](https://arxiv.org/abs/2305.15393) | [GitHub](https://github.com/UCSB-AI/LayoutGPT) | [Website](https://layoutgpt.github.io/) | L1 | Image, 3D | Layout planning | 2023 |
| [LLM Blueprint](https://arxiv.org/abs/2310.10640) | [GitHub](https://github.com/hananshafi/llmblueprint) | - | L1 | Image | Structured scene description | 2023 |
| [RPG: Recaptioning, Planning, and Generating with Multimodal LLMs](https://arxiv.org/abs/2401.11708) | [GitHub](https://github.com/YangLing0818/RPG-DiffusionMaster) | - | L1 | Image | Region planning | 2024 |
| [Region-Aware Text-to-Image Generation via Hard Binding and Soft Refinement](https://arxiv.org/abs/2411.06558) | [GitHub](https://github.com/NJU-PCALab/RAG-Diffusion) | - | L1 | Image | Region binding | 2024 |
| [LLMControl](https://arxiv.org/abs/2507.19939) | - | - | L1 | Image | Grounded controls | 2025 |
| [PointT2I](https://arxiv.org/abs/2506.01370) | - | - | L1 | Image | Keypoint conditioning | 2025 |
| [AgentComp](https://arxiv.org/abs/2512.09081) | - | - | L1 | Image | Structured subgoal reasoning | 2025 |
| [DraCo: Draft as CoT for Text-to-Image Preview and Rare Concept Generation](https://arxiv.org/abs/2512.05112) | [GitHub](https://github.com/CaraJ7/DraCo) | - | L1 | Image | Draft conditioning | 2025 |
| [GoT: Reasoning for Visual Generation and Editing](https://arxiv.org/abs/2503.10639) | [GitHub](https://github.com/rongyaofang/GoT) | - | L1 | Image, Editing | Generation-oriented reasoning | 2025 |
| [MetaPoint](https://arxiv.org/abs/2606.05031) | - | - | L1 | Image | Spatial-token planning | 2026 |
| [MGIE: Guiding Instruction-based Image Editing via Multimodal LLMs](https://arxiv.org/abs/2309.17102) | [GitHub](https://github.com/tsujuifu/pytorch_mgie) | [Website](https://mllm-ie.github.io/) | L1 | Editing | Expressive edit instruction | 2023 |

### Retrieval, world knowledge, and motion conditioning

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [RealRAG](https://arxiv.org/abs/2502.00848) | [GitHub](https://github.com/charles-xjy/realrag) | - | L1 | Image | Self-reflective retrieval training | 2025 |
| [ImageRAG](https://arxiv.org/abs/2502.09411) | [GitHub](https://github.com/rotem-shalev/ImageRAG) | [Website](https://rotem-shalev.github.io/ImageRAG/) | L1 | Image | Dynamic reference retrieval | 2025 |
| [Cross-modal RAG](https://arxiv.org/abs/2505.21956) | [GitHub](https://github.com/mengdanzhu/Cross-modal-RAG) | - | L1 | Image | Sub-dimensional retrieval | 2025 |
| [World-to-Image](https://arxiv.org/abs/2510.04201) | [GitHub](https://github.com/mhson-kyle/World-To-Image) | - | L1 | Image, World | Agent-driven knowledge grounding | 2025 |
| [Mind-Brush](https://arxiv.org/abs/2602.01756) | [GitHub](https://github.com/PicoTrex/Mind-Brush) | - | L1 | Image, World | Cognitive search and reasoning | 2026 |
| [Gen-Searcher](https://arxiv.org/abs/2603.28767) | [GitHub](https://github.com/tulerfeng/Gen-Searcher) | [Website](https://gen-searcher.vercel.app/) | L1 | Image, World | Learned search for generation context | 2026 |
| [VideoGen-of-Thought](https://arxiv.org/abs/2412.02259) | [GitHub](https://github.com/DuNGEOnmassster/VideoGen-of-Thought) | [Website](https://cheliosoops.github.io/VGoT/) | L1 | Video | Shot and identity planning | 2024 |
| [MotionAgent](https://arxiv.org/abs/2502.03207) | [GitHub](https://github.com/leoisufa/MotionAgent) | - | L1 | Video | Motion-field planning | 2025 |
| [ShotVerse](https://arxiv.org/abs/2603.11421) | [GitHub](https://github.com/Songlin1998/ShotVerse) | [Website](https://shotverse.github.io/) | L1 | Video | Multi-shot camera planning | 2026 |

[Back to top](#awesome-agentic-visual-generation)

## L2: Execution Control

L2 controllers select and invoke generation-related capabilities. They can choose tools, models, arguments, roles, and action order, but the executed results do not autonomously change the remaining path.

### Tool use, expert routing, and executable programs

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [Visual ChatGPT](https://arxiv.org/abs/2303.04671) | [GitHub](https://github.com/microsoft/visual-chatgpt) | - | L1+L2 | Image, Editing | Visual foundation model orchestration | 2023 |
| [Visual Programming for Text-to-Image Generation and Evaluation](https://arxiv.org/abs/2305.15328) | [GitHub](https://github.com/j-min/VPGen) | [Website](https://vp-t2i.github.io/) | L1+L2 | Image | Executable visual program | 2023 |
| [DiffusionAgent](https://arxiv.org/abs/2401.10061) | [GitHub](https://github.com/DiffusionAgent/DiffusionAgent) | [Website](https://diffusionagent.github.io/) | L1+L2 | Image | Diffusion expert routing | 2024 |
| [Policy Optimized Text-to-Image Pipeline Design](https://arxiv.org/abs/2505.21478) | - | - | L1+L2 | Image | Generator and processing-block selection | 2025 |
| [Collaborative Text-to-Image Generation via Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2510.10633) | - | - | L1+L2 | Image | Learned multi-agent execution | 2025 |
| [LLM-I: LLMs are Naturally Interleaved Multimodal Creators](https://arxiv.org/abs/2509.13642) | [GitHub](https://github.com/ByteDance-BandAI/LLM-I) | - | L1+L2 | Image | Search, generation, code, and editing tools | 2025 |
| [GenClaw: Code-Driven Agentic Image Generation](https://arxiv.org/abs/2605.30248) | [GitHub](https://github.com/yejy53/GenClaw) | - | L1+L2 | Image | Code-driven canvas operations | 2026 |
| [GlyphBanana](https://arxiv.org/abs/2603.12155) | [GitHub](https://github.com/yuriYanZeXuan/GlyphBanana) | - | L1+L2 | Image | Glyph tools and workflow execution | 2026 |

### Multi-agent and long-horizon workflow orchestration

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [Mora](https://arxiv.org/abs/2403.13248) | [GitHub](https://github.com/lichao-sun/Mora) | - | L1+L2 | Video | Multi-agent video modules | 2024 |
| [Kubrick](https://arxiv.org/abs/2408.10453) | - | [Website](https://kubrick9.github.io/) | L1+L2 | Video, 3D | Executable scene workflow | 2024 |
| [DreamFactory](https://arxiv.org/abs/2408.11788) | - | - | L1+L2 | Video | Multi-scene workflow | 2024 |
| [Anim-Director](https://arxiv.org/abs/2408.09787) | [GitHub](https://github.com/HITsz-TMG/Anim-Director) | - | L1+L2 | Video | Controllable animation workflow | 2024 |
| [StoryAgent](https://arxiv.org/abs/2411.04925) | - | - | L1+L2 | Image, Video | Storyboard and character workflow | 2024 |
| [VisAgent](https://arxiv.org/abs/2503.02399) | - | - | L1+L2 | Image | Narrative visualization workflow | 2025 |
| [FilmAgent](https://arxiv.org/abs/2501.12909) | [GitHub](https://github.com/HITsz-TMG/FilmAgent) | [Website](https://filmagent.github.io/) | L1+L2 | Video, 3D | Virtual film crew | 2025 |
| [MovieAgent](https://arxiv.org/abs/2503.07314) | [GitHub](https://github.com/showlab/MovieAgent) | [Website](https://weijiawu.github.io/MovieAgent/) | L1+L2 | Video | Hierarchical script-to-shot workflow | 2025 |
| [MCCD](https://arxiv.org/abs/2505.02648) | - | - | L1+L2 | Image | Multi-agent compositional generation | 2025 |
| [MAViS](https://arxiv.org/abs/2508.08487) | - | - | L1+L2 | Video | Long-sequence story workflow | 2025 |
| [MM-StoryAgent](https://arxiv.org/abs/2503.05242) | [GitHub](https://github.com/X-PLUG/MM_StoryAgent) | - | L1+L2 | Image, Video | Multimodal narrated story workflow | 2025 |
| [AutoMV](https://arxiv.org/abs/2512.12196) | [GitHub](https://github.com/multimodal-art-projection/AutoMV) | [Website](https://m-a-p.ai/AutoMV/) | L1+L2 | Video | Music video workflow | 2025 |
| [Long-Video Audio Synthesis with Multi-Agent Collaboration](https://arxiv.org/abs/2503.10719) | [GitHub](https://github.com/ZYH-Lightyear/LVAS) | [Website](https://lvas-agent.github.io/) | L1+L2 | Video | Audio workflow orchestration | 2025 |
| [UniVA](https://arxiv.org/abs/2511.08521) | [GitHub](https://github.com/univa-agent/univa) | [Website](https://univa.online/) | L1+L2 | Video | Plan-and-Act tool servers | 2025 |
| [BOOKAGENT](https://arxiv.org/abs/2604.16541) | [GitHub](https://github.com/bogao-code/BookAgent) | - | L1+L2 | Image, Video | Safety-aware visual narrative workflow | 2026 |
| [Educational Video Generation with an LLM-Based Multi-Agent System](https://arxiv.org/abs/2602.11790) | [GitHub](https://github.com/RobitsG/LASEV) | [Website](https://robitsg.github.io/LASEV/) | L1+L2 | Video | Educational video workflow | 2026 |
| [Camera Artist](https://arxiv.org/abs/2604.09195) | - | - | L1+L2 | Video | Cinematic role orchestration | 2026 |
| [Co-Director](https://arxiv.org/abs/2604.24842) | [GitHub](https://github.com/GoogleCloudPlatform/genmedia-izumi-agent) | [Website](https://co-director-agent.github.io/) | L1+L2 | Video | Hierarchical video workflow | 2026 |
| [BrandFusion](https://arxiv.org/abs/2603.02816) | - | [Website](https://zihao-ai.github.io/brandfusion/) | L1+L2 | Video | Brand integration workflow | 2026 |

[Back to top](#awesome-agentic-visual-generation)

## L3: Outcome-Adaptive Control

L3 controllers observe a generated artifact, rendered state, tool result, verifier report, reward, or user response and use that observation to choose the next action in the current trajectory.

### Prompt feedback and compositional correction

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [OPT2I: Improving Text-to-Image Consistency via Automatic Prompt Optimization](https://arxiv.org/abs/2403.17804) | - | - | L1+L3 | Image | Rendered-score prompt search | 2024 |
| [Promptify: Interactive Prompt Exploration with Large Language Models](https://arxiv.org/abs/2304.09337) | [GitHub](https://github.com/promptslab/Promptify) | - | L1+L3 | Image | Candidate-driven user feedback | 2023 |
| [MuLan](https://arxiv.org/abs/2402.12741) | [GitHub](https://github.com/measure-infinity/mulan-code) | - | L1+L3 | Image | Progressive construction | 2024 |
| [CompAgent](https://arxiv.org/abs/2401.15688) | - | - | L1+L3 | Image | Visual-feedback correction | 2024 |
| [LayerCraft](https://arxiv.org/abs/2504.00010) | [GitHub](https://github.com/PeterYYZhang/LayerCraft) | - | L1+L3 | Image | Layered integration and revision | 2025 |
| [RATTPO](https://arxiv.org/abs/2506.16853) | [GitHub](https://github.com/seminkim/RATTPO) | - | L1+L3 | Image | Reward-history prompt search | 2025 |
| [Twin Co-Adaptive Dialogue](https://arxiv.org/abs/2504.14868) | - | - | L1+L3 | Image | Progressive dialogue and image updates | 2025 |
| [VisualPrompter](https://arxiv.org/abs/2506.23138) | [GitHub](https://github.com/teheperinko541/VisualPrompter) | - | L1+L3 | Image | Image-grounded prompt repair | 2025 |
| [Test-time Prompt Refinement](https://arxiv.org/abs/2507.22076) | - | - | L1+L3 | Image | Iterative visual diagnosis | 2025 |
| [CountLoop](https://arxiv.org/abs/2508.16644) | - | [Website](https://mondalanindya.github.io/CountLoop/) | L1+L3 | Image | Counting feedback loop | 2025 |
| [PromptSculptor](https://arxiv.org/abs/2509.12446) | - | - | L1+L2+L3 | Image | Multi-agent self-evaluation | 2025 |
| [GenPilot](https://arxiv.org/abs/2510.07217) | [GitHub](https://github.com/27yw/GenPilot) | - | L1+L2+L3 | Image | Error analysis and prompt refinement | 2025 |
| [coDrawAgents](https://arxiv.org/abs/2603.12829) | [GitHub](https://github.com/ChunhanLiii/coDrawAgents) | - | L1+L2+L3 | Image | Multi-round scene construction | 2026 |
| [M3](https://arxiv.org/abs/2602.06166) | [GitHub](https://github.com/LINs-lab/M3) | - | L1+L2+L3 | Image | Multi-agent visual diagnosis | 2026 |

### Tool orchestration, routing, and world grounding with feedback

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [GenArtist](https://arxiv.org/abs/2407.05600) | - | [Website](https://zhenyuw16.github.io/GenArtist_page/) | L1+L2+L3 | Image, Editing | Tool tree, verification, and repair | 2024 |
| [T2I-Copilot](https://arxiv.org/abs/2507.20536) | [GitHub](https://github.com/SHI-Labs/T2I-Copilot) | - | L1+L2+L3 | Image | Evaluator-controlled regeneration | 2025 |
| [Image-POSER](https://arxiv.org/abs/2511.11780) | - | - | L1+L2+L3 | Image, Editing | Reflective expert routing | 2025 |
| [ImAgent](https://arxiv.org/abs/2511.11483) | - | - | L1+L2+L3 | Image | Policy-controlled test-time actions | 2025 |
| [Maestro](https://arxiv.org/abs/2509.10704) | - | - | L1+L2+L3 | Image | Critic-guided orchestration | 2025 |
| [Generation Navigator](https://arxiv.org/abs/2605.17969) | - | - | L1+L2+L3 | Image | State-aware action choice | 2026 |
| [GenAgent](https://arxiv.org/abs/2601.18543) | - | - | L1+L2+L3 | Image | Trained tool use and reflection | 2026 |
| [Unify-Agent](https://arxiv.org/abs/2603.29620) | [GitHub](https://github.com/shawn0728/Unify-Agent) | - | L1+L2+L3 | Image, World | Search-generation workflow | 2026 |
| [Qwen-Image-Agent](https://arxiv.org/abs/2606.26907) | - | - | L1+L2+L3 | Image, World | Search, memory, editing, and feedback | 2026 |
| [ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image Generation](https://arxiv.org/abs/2608.04436) | [GitHub](https://github.com/bubble65/EMU-Agentic-PostTrain) | [Dataset](https://huggingface.co/datasets/bubble65/EMU-Agentic-PostTrain-Data) | L1+L2+L3 | Image, World | Unified search, native drawing, inspection, and revision | 2026 |
| [UniReason 1.0](https://arxiv.org/abs/2602.02437) | [GitHub](https://github.com/AlenjandroWang/UniReason) | - | L1+L3 | Image, Editing, World | Knowledge reasoning and correction | 2026 |

### Unified and latent closed-loop generation

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [Image CoT](https://arxiv.org/abs/2501.13926) | [GitHub](https://github.com/ZiyuGuo99/Image-Generation-CoT) | - | L1+L3 | Image | Stepwise generation and verification | 2025 |
| [FoX](https://arxiv.org/abs/2503.01298) | - | - | L1+L3 | Image | Planning, acting, reflection, correction | 2025 |
| [Uni-CoT](https://arxiv.org/abs/2508.05606) | [GitHub](https://github.com/Fr0zenCrane/UniCoT) | [Website](https://sais-fuxi.github.io/projects/uni-cot/) | L1+L3 | Image | Macro and micro visual reasoning | 2025 |
| [ThinkGen](https://arxiv.org/abs/2512.23568) | [GitHub](https://github.com/jiaosiyuu/ThinkGen) | - | L1+L3 | Image | Alternating reasoner-generator learning | 2025 |
| [MILR](https://arxiv.org/abs/2509.22761) | [GitHub](https://github.com/spatigen/MILR) | [Website](https://spatigen.github.io/milr.io/) | L1+L3 | Image | Test-time latent search | 2025 |
| [UniGen](https://arxiv.org/abs/2505.14682) | - | - | L1+L3 | Image | Candidate verification and selection | 2025 |
| [Large Language Models are Universal Reasoners for Visual Generation](https://arxiv.org/abs/2605.04040) | - | - | L1+L3 | Image | Draft and grounded self-critique | 2026 |
| [UniT](https://arxiv.org/abs/2602.12279) | - | [Website](https://ai.meta.com/research/publications/unit-unified-multimodal-chain-of-thought-test-time-scaling/) | L1+L3 | Image | Sequential generation and refinement | 2026 |
| [Latent Action Control](https://arxiv.org/abs/2605.16961) | - | - | L1+L3 | Image | Latent diagnosis and halting | 2026 |
| [Think in Strokes, Not Pixels](https://arxiv.org/abs/2604.04746) | - | - | L1+L3 | Image | Interleaved draft and reflection | 2026 |
| [Self-Adaptive Interleaved Visual Reasoner](https://arxiv.org/abs/2605.14709) | [GitHub](https://github.com/WeChatCV/Interleaved_Visual_Reasoner) | - | L1+L3 | Image | Adaptive reflection and planning | 2026 |
| [AlphaGRPO](https://arxiv.org/abs/2605.12495) | [GitHub](https://github.com/huangrh99/AlphaGRPO) | [Website](https://huangrh99.github.io/AlphaGRPO/) | L1+L3 | Image | Self-reflective verifiable rewards | 2026 |
| [FiRe](https://arxiv.org/abs/2604.13491) | - | - | L1+L3 | Image | Fine-grained multimodal reflection | 2026 |

### Image and video editing with artifact feedback

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [LAVE](https://arxiv.org/abs/2402.10294) | - | [Website](https://www.dgp.toronto.edu/~bryanw/lave/) | L1+L2+L3 | Video, Editing | Timeline state and user revision | 2024 |
| [Self-correcting LLM-controlled Diffusion Models](https://arxiv.org/abs/2311.16090) | [GitHub](https://github.com/tsunghan-wu/SLD) | [Website](https://self-correcting-llm-diffusion.github.io/) | L1+L3 | Image | Requirement inspection and repair | 2024 |
| [EditDuet](https://arxiv.org/abs/2509.10761) | - | - | L1+L2+L3 | Video, Editing | Proposal and critique | 2025 |
| [Text-Driven Reasoning Video Editing via Reinforcement Learning](https://arxiv.org/abs/2511.14100) | - | - | L1+L2+L3 | Video, Editing | Digital-twin reasoning | 2025 |
| [Image Editing as Programs with Diffusion Models](https://arxiv.org/abs/2506.04158) | [GitHub](https://github.com/YujiaHu1109/IEAP) | [Website](https://yujiahu1109.github.io/IEAP/) | L1+L2+L3 | Editing | Verified sequential edit operations | 2025 |
| [Agentic Retoucher](https://arxiv.org/abs/2601.02046) | [GitHub](https://github.com/MediaX-SJTU/Agentic-Retoucher) | - | L1+L2+L3 | Image, Editing | Defect localization and retouching | 2026 |
| [EditRefiner](https://arxiv.org/abs/2605.07457) | [GitHub](https://github.com/IntMeGroup/EditRefiner) | - | L1+L3 | Editing | Human-aligned iterative refinement | 2026 |
| [Refinement via Regeneration](https://arxiv.org/abs/2604.25636) | [GitHub](https://github.com/LeapLabTHU/RvR) | - | L1+L3 | Image, Editing | Adaptive modification space | 2026 |
| [Agent Banana](https://arxiv.org/abs/2602.09084) | [GitHub](https://github.com/taco-group/agent-banana) | [Website](https://agent-banana.github.io/) | L1+L2+L3 | Editing | Multi-step reasoning and tools | 2026 |
| [PhotoAgent](https://arxiv.org/abs/2602.22809) | - | [Website](https://mdyao.github.io/PhotoAgent/) | L1+L2+L3 | Editing | Long-horizon aesthetic planning | 2026 |
| [CutClaw](https://arxiv.org/abs/2603.29664) | [GitHub](https://github.com/GVCLab/CutClaw) | - | L1+L2+L3 | Video, Editing | Hours-long timeline control | 2026 |
| [Crayotter](https://arxiv.org/abs/2606.07636) | [GitHub](https://github.com/idwts/Crayotter) | - | L1+L2+L3 | Video, Editing | Traceable iterative workflow | 2026 |
| [Aurora](https://arxiv.org/abs/2605.18748) | [GitHub](https://github.com/yeates/Aurora) | [Website](https://yeates.github.io/Aurora-Page/) | L1+L2+L3 | Video, Editing | Tool-using video editor | 2026 |
| [CineAgents](https://arxiv.org/abs/2604.10456) | - | - | L1+L2+L3 | Video, Editing | Iterative cinematic compilation | 2026 |

### Video, 3D, and persistent world-state control

| Paper | GitHub | Website | Path | Modality | Primary mechanism | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [GenMAC](https://arxiv.org/abs/2412.04440) | [GitHub](https://github.com/Karine-Huang/GenMAC) | [Website](https://karine-h.github.io/GenMAC/) | L1+L2+L3 | Video | Verification and correction | 2024 |
| [VideoAgent](https://arxiv.org/abs/2410.10076) | [GitHub](https://github.com/video-as-agent/videoagent) | [Website](https://video-as-agent.github.io/) | L1+L3 | Video | Environment-feedback planning | 2024 |
| [SceneCraft](https://arxiv.org/abs/2403.01248) | - | - | L1+L2+L3 | 3D | Blender execution and revision | 2024 |
| [Scenethesis](https://arxiv.org/abs/2505.02836) | - | [Website](https://research.nvidia.com/labs/dir/scenethesis/) | L1+L2+L3 | 3D | Render-guided scene construction | 2025 |
| [Agentic 3D Scene Generation](https://arxiv.org/abs/2505.20129) | - | [Website](https://spatctxvlm.github.io/project_page/) | L1+L2+L3 | 3D | Spatial reasoning and rendered-view inspection | 2025 |
| [MoReGen](https://arxiv.org/abs/2512.04221) | - | - | L1+L2+L3 | Video, 3D | Simulator code and physical checking | 2025 |
| [Hollywood Town](https://arxiv.org/abs/2510.22431) | - | [Website](https://olpleo.github.io/) | L1+L2+L3 | Video | Adaptive cross-modal workflow | 2025 |
| [AniME](https://arxiv.org/abs/2508.18781) | - | - | L1+L2+L3 | Video | Adaptive animation planning | 2025 |
| [CoAgent](https://arxiv.org/abs/2512.22536) | - | - | L1+L2+L3 | Video | Cross-segment consistency agent | 2025 |
| [ViMax](https://arxiv.org/abs/2606.07649) | [GitHub](https://github.com/HKUDS/ViMax) | - | L1+L2+L3 | Video | Agentic video workflow | 2026 |
| [ReCA: Multi-Shot Long Video Extrapolation via Recursive Context Allocation](https://arxiv.org/abs/2605.26525) | [GitHub (announced)](https://github.com/ali-vilab/ReCA) | [Website](https://reca.vmv.re/) | L1+L2+L3 | Video | Recursive context allocation and state refresh | 2026 |
| [VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System](https://arxiv.org/abs/2607.27380) | [GitHub](https://github.com/micky-li-hd/VideoCoCo) | - | L1+L2+L3 | Video, 3D | Executable simulation, draft inspection, and conditioned editing | 2026 |
| [ShareVerse](https://arxiv.org/abs/2603.02697) | - | - | L1+L2+L3 | Video, World | Shared multi-agent world state | 2026 |
| [SPIRAL](https://arxiv.org/abs/2603.08403) | - | [Website](https://yuyang-cloud.github.io/spiral/) | L1+L2+L3 | Video, World | Think-act-reflect state transitions | 2026 |

[Back to top](#awesome-agentic-visual-generation)

## L4: Experience-Adaptive Control

L4 controllers use completed trajectories to change decisions in future tasks. Parameter updates are not required. Persistent experience must alter later action selection, capability estimates, reusable skills, or the controller policy.

| Paper | GitHub | Website | Path | Modality | Persistent adaptation | Year |
| --- | :---: | :---: | :---: | :---: | --- | :---: |
| [VISTA: A Test-Time Self-Improving Video Generation Agent](https://arxiv.org/abs/2510.15831) | - | [Website](https://g-vista.github.io/) | L1+L3+L4 | Video | Transferable test-time improvement | 2025 |
| [SIDiffAgent](https://arxiv.org/abs/2602.02051) | - | - | L1+L3+L4 | Image | Self-improving generation behavior | 2026 |
| [GEMS](https://arxiv.org/abs/2603.28088) | [GitHub](https://github.com/lcqysl/GEMS) | [Website](https://gems-gen.github.io/) | L1+L2+L3+L4 | Image, Editing | Trajectory memory and reusable skills | 2026 |
| [MemoGen](https://arxiv.org/abs/2606.03243) | [GitHub](https://github.com/Chatonz/MemoGen) | - | L1+L3+L4 | Image | Cross-task episodic experience | 2026 |
| [OctoT2I](https://arxiv.org/abs/2606.01803) | [GitHub](https://github.com/JaxJiang2642081986/OctoT2I) | - | L1+L2+L3+L4 | Image | Evolving generator capability profiles | 2026 |
| [GenEvolve](https://arxiv.org/abs/2605.21605) | [GitHub](https://github.com/MeiGen-AI/GenEvolve) | [Website](https://ephemeral182.github.io/GenEvolve/) | L1+L2+L3+L4 | Image, Editing | Visual experience distillation into skills | 2026 |
| [VideoWeaver](https://arxiv.org/abs/2606.08091) | [GitHub](https://github.com/JianhuiWei7/VideoWeaver) | - | L1+L2+L3+L4 | Video | Evaluation and evolution of workflow skills | 2026 |

[Back to top](#awesome-agentic-visual-generation)

## Evaluation, Benchmarks, and Reward Models

These resources evaluate outputs, trajectories, controllers, or supporting signals. A stand-alone evaluator is not assigned an agenticity level. When an agent uses its feedback to choose a new generation action, the complete system may qualify as L3 or L4.

### Agent and trajectory evaluation

| Resource | GitHub | Website | Scope | Type | Year |
| --- | :---: | :---: | --- | --- | :---: |
| [A Unified Agentic Framework for Evaluating Conditional Image Generation](https://arxiv.org/abs/2504.07046) | [GitHub](https://github.com/HITsz-TMG/Agentic-CIGEval) | - | Image generation | Evaluator orchestration | 2025 |
| [Draw ALL Your Imagine](https://arxiv.org/abs/2505.24787) | [GitHub](https://github.com/yczhou001/LongBench-T2I) | - | Complex image instructions | Benchmark and iterative agent framework | 2025 |
| [AtelierEval](https://arxiv.org/abs/2605.22645) | - | - | Human and LLM prompters | Prompter evaluation | 2026 |
| [IA-Bench](https://arxiv.org/abs/2606.26907) | - | - | Planning, reasoning, search, and memory in image generation | Agent benchmark | 2026 |
| [MSVE-Bench and NB-Q](https://arxiv.org/abs/2605.26525) | [GitHub (announced)](https://github.com/ali-vilab/ReCA) | [Website](https://reca.vmv.re/) | 3–5 minute multi-shot video extrapolation | Benchmark and source-grounded protocol | 2026 |
| [UniVA-Bench](https://arxiv.org/abs/2511.08521) | [GitHub](https://github.com/univa-agent/univa) | [Website](https://univa.online/) | Multi-step video workflows | Agent benchmark | 2025 |
| [ActVideoGen-Bench](https://arxiv.org/abs/2603.08403) | - | [Website](https://yuyang-cloud.github.io/spiral/) | Long-horizon action-conditioned video | Agent benchmark | 2026 |
| [CineBench](https://arxiv.org/abs/2604.10456) | - | - | Cinematic compilation | Agent benchmark | 2026 |
| [SynthSeg-Agents](https://arxiv.org/abs/2512.15310) | - | - | Synthetic data for segmentation | Downstream task evaluation | 2025 |

### Output benchmarks and evaluators

| Resource | GitHub | Website | Modality | Focus | Year |
| --- | :---: | :---: | :---: | --- | :---: |
| [T2I-CompBench](https://arxiv.org/abs/2307.06350) | - | [Website](https://karine-h.github.io/T2I-CompBench-new/) | Image | Compositional text-image alignment | 2023 |
| [GenEval](https://arxiv.org/abs/2310.11513) | [GitHub](https://github.com/djghosh13/geneval) | - | Image | Object, count, color, and position | 2023 |
| [VBench](https://arxiv.org/abs/2311.17982) | [GitHub](https://github.com/Vchitect/VBench) | [Website](https://vchitect.github.io/VBench-project/) | Video | Appearance and temporal quality | 2023 |
| [EvalCrafter](https://arxiv.org/abs/2310.11440) | [GitHub](https://github.com/EvalCrafter/EvalCrafter) | [Website](https://evalcrafter.github.io/) | Video | Human-aligned video evaluation | 2023 |
| [MME-Unify](https://arxiv.org/abs/2504.03641) | [GitHub](https://github.com/MME-Benchmarks/MME-Unify) | [Website](https://mme-unify.github.io/) | Image | Unified understanding and generation | 2025 |
| [Multi-Modal Language Models as Text-to-Image Model Evaluators](https://arxiv.org/abs/2505.00759) | - | - | Image | MLLM-based evaluation | 2025 |
| [AIGVE-MACS](https://arxiv.org/abs/2507.01255) | - | [Website](https://huggingface.co/xiaoliux/AIGVE-MACS) | Video | Multi-aspect comments and scores | 2025 |

### Reward models, verifiers, and preference data

| Resource | GitHub | Website | Scope | Role | Year |
| --- | :---: | :---: | --- | --- | :---: |
| [ImageReward](https://arxiv.org/abs/2304.05977) | [GitHub](https://github.com/THUDM/ImageReward) | - | Text-to-image | General preference reward | 2023 |
| [Pick-a-Pic](https://arxiv.org/abs/2305.01569) | [GitHub](https://github.com/yuvalkirstain/pickscore) | - | Text-to-image | Pairwise preference dataset | 2023 |
| [Unified Multimodal Chain-of-Thought Reward Model](https://arxiv.org/abs/2505.03318) | - | [Website](https://codegoat24.github.io/UnifiedReward/) | Multimodal generation | Reasoning-based reward | 2025 |
| [Generative Universal Verifier](https://arxiv.org/abs/2510.13804) | [GitHub](https://github.com/Cominclip/OmniVerifier) | [Website](https://omniverifier.github.io/) | Multimodal generation | Generative verification | 2025 |
| [Personalized Reward Modeling for Text-to-Image Generation](https://arxiv.org/abs/2511.19458) | - | - | Text-to-image | User-conditioned reward | 2025 |
| [Customized Reward Models for Text-to-Image Generation](https://arxiv.org/abs/2507.21391) | [GitHub](https://github.com/sjz5202/LLaVA-Reward) | - | Text-to-image | Request-specific reward | 2025 |

[Back to top](#awesome-agentic-visual-generation)

## Supporting Components: the L0 Boundary

L0 is an inclusion boundary, not an agent category. The following systems are important generators, editors, retrieval modules, or optimization methods, but their fixed execution rules do not provide generation-level controller authority by themselves.

| Supporting component | GitHub | Website | Modality | Why it is outside L1-L4 |
| --- | :---: | :---: | :---: | --- |
| [GLIDE](https://arxiv.org/abs/2112.10741) | [GitHub](https://github.com/openai/glide-text2im) | - | Image | Fixed conditional generator |
| [DALL-E 2](https://arxiv.org/abs/2204.06125) | - | - | Image | Fixed conditional generator |
| [Imagen](https://arxiv.org/abs/2205.11487) | - | [Website](https://imagen.research.google/) | Image | Fixed conditional generator |
| [Parti](https://arxiv.org/abs/2206.10789) | - | [Website](https://parti.research.google/) | Image | Fixed conditional generator |
| [Latent Diffusion](https://arxiv.org/abs/2112.10752) | [GitHub](https://github.com/CompVis/latent-diffusion) | - | Image | Fixed conditional generator |
| [SDXL](https://arxiv.org/abs/2307.01952) | [GitHub](https://github.com/Stability-AI/generative-models) | - | Image | Fixed conditional generator |
| [DALL-E 3](https://cdn.openai.com/papers/dall-e-3.pdf) | - | - | Image | Fixed conditional generator |
| [Video Diffusion Models](https://arxiv.org/abs/2204.03458) | - | [Website](https://video-diffusion.github.io/) | Video | Fixed conditional generator |
| [Make-A-Video](https://arxiv.org/abs/2209.14792) | - | - | Video | Fixed conditional generator |
| [Imagen Video](https://arxiv.org/abs/2210.02303) | - | [Website](https://imagen.research.google/video/) | Video | Fixed conditional generator |
| [Video LDM](https://arxiv.org/abs/2304.08818) | - | [Website](https://research.nvidia.com/labs/toronto-ai/VideoLDM/) | Video | Fixed conditional generator |
| [ModelScopeT2V](https://arxiv.org/abs/2308.06571) | - | [Website](https://modelscope.cn/models/damo/text-to-video-synthesis/summary) | Video | Fixed conditional generator |
| [Show-1](https://arxiv.org/abs/2309.15818) | [GitHub](https://github.com/showlab/Show-1) | [Website](https://showlab.github.io/Show-1/) | Video | Fixed conditional generator |
| [Lumiere](https://arxiv.org/abs/2401.12945) | - | [Website](https://lumiere-video.github.io/) | Video | Fixed conditional generator |
| [InstructPix2Pix](https://arxiv.org/abs/2211.09800) | [GitHub](https://github.com/timothybrooks/instruct-pix2pix) | [Website](https://www.timothybrooks.com/instruct-pix2pix) | Editing | Fixed single-pass editor |
| [Tune-A-Video](https://arxiv.org/abs/2212.11565) | [GitHub](https://github.com/showlab/Tune-A-Video) | [Website](https://tuneavideo.github.io/) | Editing | Fixed editing pipeline |
| [TokenFlow](https://arxiv.org/abs/2307.10373) | [GitHub](https://github.com/omerbt/TokenFlow) | [Website](https://diffusion-tokenflow.github.io/) | Editing | Fixed editing pipeline |
| [Video-P2P](https://arxiv.org/abs/2303.04761) | - | [Website](https://video-p2p.github.io/) | Editing | Fixed editing pipeline |
| [SmartEdit](https://arxiv.org/abs/2312.06739) | - | [Website](https://yuzhou914.github.io/SmartEdit/) | Editing | Single-pass editor |
| [AVI-Edit](https://arxiv.org/abs/2512.10571) | - | [Website](https://hjzheng.net/projects/AVI-Edit/) | Editing | Fixed editing pipeline |
| [DreamFusion](https://arxiv.org/abs/2209.14988) | - | [Website](https://dreamfusion3d.github.io/) | 3D | Fixed optimization pipeline |
| [Magic3D](https://arxiv.org/abs/2211.10440) | - | [Website](https://research.nvidia.com/labs/dir/magic3d/) | 3D | Fixed optimization pipeline |
| [DreamGaussian](https://arxiv.org/abs/2309.16653) | [GitHub](https://github.com/dreamgaussian/dreamgaussian) | [Website](https://dreamgaussian.github.io/) | 3D | Fixed optimization pipeline |
| [Re-Imagen](https://arxiv.org/abs/2209.14491) | - | - | Image | Fixed retrieval and generation pipeline |
| [DPOK](https://arxiv.org/abs/2305.16381) | [GitHub](https://github.com/google-research/google-research/tree/master/dpok) | - | Image | Optimizes a generator rather than a generation-level controller |
| [Reward-Instruct](https://arxiv.org/abs/2503.13070) | [GitHub](https://github.com/Luo-Yihong/R0) | - | Image | Optimizes a generator rather than a generation-level controller |
| [Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos](https://arxiv.org/abs/2607.16107) | [GitHub](https://github.com/NVIDIA/audio-flamingo) | [Website](https://avflamingo.pages.dev/) | Video | Audio-visual understanding and reasoning model; does not generate or edit visual artifacts |

[Back to top](#awesome-agentic-visual-generation)
