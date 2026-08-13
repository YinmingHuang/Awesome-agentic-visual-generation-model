# Contributing

Thank you for helping maintain Awesome Agentic Visual Generation.

## Inclusion criteria

A paper belongs in L1-L4 only when the complete system contains a visual generator or editor and a controller that makes generation-level decisions.

Before submitting a paper, identify:

1. The controller and the visual generator or editor.
2. The variables controlled by the controller.
3. The observations available before each decision.
4. Whether execution results can change the next action.
5. Whether completed trajectories change behavior in future tasks.

Fixed generators, fixed retrieval-generation pipelines, stand-alone reward models, and benchmarks should be proposed for the supporting or evaluation sections instead of L1-L4.

## Level assignment

Assign the paper to its highest demonstrated controller level:

- **L1, Conditioning Control:** the controller constructs prompts, layouts, references, knowledge, or other generator inputs.
- **L2, Execution Control:** the controller selects generators, tools, arguments, roles, or action order.
- **L3, Outcome-Adaptive Control:** generated artifacts, execution results, verifier reports, rewards, or user feedback change the next action in the current task.
- **L4, Experience-Adaptive Control:** completed trajectories update persistent memory, skills, capability profiles, or policies that change future tasks.

Tool use, multi-agent architecture, memory, loops, and reinforcement learning do not determine the level by themselves.

## Pull request format

Please add one row to the appropriate table and include:

```markdown
| [Paper title](paper-url) | [GitHub](official-code-url) | [Website](official-project-url) | L1+L2+L3 | Image | Short mechanism description | 2026 |
```

In the pull request description, provide:

- Paper title and canonical paper URL
- Maximum level and capability path
- Modality tags
- A short evidence-based classification rationale
- Official code or project page, if available

Use the canonical paper title. Prefer an arXiv abstract page, official proceedings page, or publisher page. Put verified author-maintained code and project links in the separate `GitHub` and `Website` columns. Use `-` when an official URL is unavailable. Do not link to an unofficial PDF mirror or a third-party paper summary.

## Classification changes

For a proposed reclassification, quote or point to the method, algorithm, or system description that establishes the additional controller capability. A title containing “agentic,” “self-improving,” or “multi-agent” is not sufficient evidence.
