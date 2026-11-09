# blindstitch

A measurement study following up on [Patchwork](https://github.com/Abdurrafay19/patchwork).

In Patchwork, the 3B model (Qwen 2.5 Coder 3B) writes both a fix and unit tests to verify itself. But weak tests mean the agent often claims a bug is fixed when it isn't—the model's self-tests said "fixed" 75 times out of 100, while the hidden oracle only passed 58.

This project tests four cheap checks that don't need the oracle to see if we can tell good patches from bad ones:
- **Self-tests (Baseline / V0):** The model's own tests pass on its patch.
- **Discriminating tests (V1):** The tests must also fail on the original buggy code to prove they actually test the bug.
- **Mutation score (V2):** We inject small syntax changes (mutants) into the patch to see if the tests catch them.
- **Cross-sample consensus (V3):** We sample 8 fixes and see if different patches agree on test outcomes.