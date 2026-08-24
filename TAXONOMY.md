# Final L0-L4 Controller-Capability Taxonomy

This document is the normative classification standard for this repository and the accompanying survey. It classifies a complete system by the maximum **generation-level action authority** demonstrated by its controller, not by its number of modules, agents, tools, training losses, or pipeline stages.

## Core principle

The levels answer four increasingly strong questions:

```text
What is supplied? -> What visual operation is invoked? -> What follows an outcome? -> What changes across tasks?
       L1                        L2                            L3                         L4
```

L0 is the lower boundary. L1-L4 are assigned to complete systems. A paper is placed at the highest level for which the method provides concrete evidence; lower capabilities are recorded in its `Path`.

## L0: No Generation-Level Control

**Definition.** The method generates, edits, retrieves, renders, evaluates, or optimizes under a fixed invocation rule. It does not contain a controller that chooses among materially different generation-level actions during inference.

**Typical cases.** A fixed generator or editor, a predetermined retrieval-then-generation pipeline, a stand-alone evaluator or benchmark, or generator post-training without an inference-time action policy.

**Decision test.** Given the same goal and state, can the system choose a materially different generation action? If not, it is L0 or a supporting component.

## L1: Conditioning Control

**Definition.** The controller constructs the declarative specification supplied to a predetermined visual executor, while invocation of that executor remains externally specified or fixed.

**Controlled variables.** Prompts, preferences, layouts, scene graphs, storyboards, scripts, references, retrieved knowledge, spatial controls, motion trajectories, camera plans, and other generator-facing conditions.

**What does not raise L1 to L2.** Complex reasoning, search, multiple planning roles, or an internal loop that only improves the condition. A hierarchy of planners can remain L1 if its final product is a specification handed to a fixed generator or renderer.

**Decision test.** If the controller were replaced by a stored specification, would the same predetermined visual operation still be invoked? If yes, the demonstrated authority is L1.

## L2: Execution Control

**Definition.** Before generated outcomes are observed, the controller chooses and invokes actual visual generation, editing, rendering, or artifact-mutating operations. It can select the operation or model, decide whether and when it runs, and determine the number, order, or route of such operations.

**Controlled variables.** Generator or editor identity, generation-versus-editing mode, executable visual tool calls, artifact-mutating programs, model routing, invocation order, and stopping before outcome feedback.

**What does not establish L2.** Agent roles, generic function arguments, retrieval alone, or a fixed multi-stage topology. A declarative SVG, scene, slide, or storyboard specification consumed by a predetermined renderer remains L1. An imperative program whose operations create or mutate the artifact is L2.

**Decision test.** Does the controller choose among materially different visual operations or invocation routes, rather than only changing the input to one predetermined executor? If yes, and no outcome redirects the route, the system is L2.

## L3: Outcome-Adaptive Control

**Definition.** An observation from the current trajectory changes a later generation-level action. The observation can be a generated artifact, rendered or engine state, execution result, verifier diagnosis, or user response.

**Controlled variables.** Revision, localized editing, rerouting, regeneration, rollback, retry, and stopping.

**Required causal link.** The paper must demonstrate `outcome -> updated state or diagnosis -> different later action`. Merely scoring candidates, running a fixed number of iterations, or using a critic only during training is insufficient.

**Boundary cases.** Search results that only enrich a prompt remain L1. Generated-image feedback that triggers a new search, edit, or generation call is L3. Compilation, rendering, simulation, or physics feedback is L3 when failure changes the remaining artifact-construction trajectory.

## L4: Experience-Adaptive Control

**Definition.** Information retained from completed trajectories persistently changes control on later, independent tasks.

**Persistent variables.** Episodic memory, reusable skills, capability profiles, workflow libraries, strategy stores, controller parameters, or other cross-task policy state.

**Required causal link.** The paper must demonstrate `completed trajectory -> persistent update -> changed decision on a later task`. A long context, shared state across shots, or memory used only within one request is not L4.

**Decision test.** After the current task ends, does an update survive and affect a later task? If not, the system is at most L3.

## Classification procedure

Apply the following tests from highest to lowest:

1. **Cross-task test.** Does completed experience persistently alter later control? Classify as L4.
2. **Outcome test.** Does a current outcome alter a later generation action? Classify as L3.
3. **Invocation test.** Does the controller choose and invoke actual visual operations? Classify as L2.
4. **Condition test.** Does it only construct the specification for a predetermined executor? Classify as L1.
5. **Boundary test.** If none applies, treat the method as L0 or a supporting component.

## Evidence policy

- Classify the complete inference-time method, not an isolated module or a term in the title.
- Use the highest capability explicitly implemented and evaluated in the paper. Do not infer authority from words such as “agentic,” “multi-agent,” “self-reflection,” “memory,” or “reinforcement learning.”
- An implementation may contain lower-level capabilities without listing every one. The `Path` records only capabilities that are materially demonstrated.
- When evidence is ambiguous, use the lower level and state the missing causal link needed for promotion.
- Modality and mechanism are orthogonal tags. They never determine the level.

## Canonical boundary examples

- **MovieAgent is L1:** its planning hierarchy constructs script, scene, and shot conditions for a predetermined generation backend; role count does not establish visual-operation routing.
- **Gen-Searcher is L1:** its learned search trajectory constructs grounded context before a predetermined generation call; an internal retrieval loop is not outcome-adaptive generation.
- **Mind-Brush is L2:** it selects search versus reasoning and, critically, generation versus editing mode, which changes the invoked visual operation.
- **RS-Gen is L3:** generated images enter a verify-and-correct loop whose diagnosis triggers local modification or regeneration.
- **BrandFusion is L4:** user feedback from completed outputs is abstracted into a persistent experience pool that informs later brand-integration strategies.

## Short citation-ready definition

> L0 contains fixed supporting components without generation-level action selection. L1 controls the declarative conditions supplied to a predetermined visual executor. L2 controls which visual generation or artifact-mutating operations are invoked and how they are sequenced. L3 uses outcomes from the current trajectory to change later generation actions. L4 retains completed experience so that it changes control on future tasks.
