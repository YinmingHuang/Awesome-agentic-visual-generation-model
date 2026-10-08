# AutoRef classification review

Reviewed on 2026-10-08 against [arXiv:2609.35530v1](https://arxiv.org/html/2609.35530v1).

- Primary level: L4, Experience-Adaptive Control.
- Capability path: L1+L2+L3+L4; modality: Image.
- Catalog subsection: Executable Workflows and Harnesses.
- Classify the complete AutoRef optimization system, not only its returned AutoRef-Harness.

## Evidence and boundary tests

Sections 3 and 4 describe an accumulated search history containing completed generation-task images, evaluation feedback, harness implementations, and execution trajectories. A coding-agent proposer reads this evidence to rewrite executable harnesses, which govern subsequent generation tasks. The retained update is executable control code, rather than model weights or a user-profile memory. Sections 6.1 and 6.3 evaluate the resulting harness on held-out tasks and its transfer without re-optimization. Together these establish completed-task evidence -> persistent harness update -> changed control on independent tasks, supporting L4.

Reference-grounded prompt construction establishes L1. The complete optimization system changes executable model invocations and control flow, establishing L2. Section 5.3 describes complaints about generated drafts driving revised prompts and a new draft, establishing L3.

The returned AutoRef-Harness, considered alone, retains no completed-task update during deployment and is at most L3. Its fixed invocation topology and complaint-directed prompt repair explain the previous L1+L3 catalog record. Moving the unique record to L4 reflects the complete method's highest demonstrated causal reach; it does not treat fixed offline training or transfer performance alone as L4 evidence.

PR #2 adds an L4 record for a paper already present under L3. Remove the previous L3 row and retain one L4 row with a specific harness-evolution mechanism, preserving the catalog's unique-placement rule and total count.
