"""One row of raw data = one sample (one patch + tests for one defect)."""

from pydantic import BaseModel


class Sample(BaseModel):
    defect_id: str
    dataset: str  # "d1" or "d2"
    category: str
    sample_id: int
    patch: str
    tests: str
    generation_failed: bool  # schema/timeout failure: patch is the original code
    oracle_pass: bool  # hidden oracle says the patch is correct
    self_pass: bool  # the model's own tests pass on the patch  (signal V0)
    fails_on_original: bool | None = None  # >=1 own test fails on buggy file (for V1)
    mutants_total: int | None = None  # valid mutants of the patch (for V2)
    mutants_killed: int | None = None
