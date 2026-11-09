"""All settings live here. Change a number here, not inside other files."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


DATA_D1 = ROOT / "data" / "d1"
DATA_D2 = ROOT / "data" / "d2"
SPLIT_FILE = ROOT / "data" / "d1_split.json"
RESULTS = ROOT / "results"
SAMPLES_FILE = RESULTS / "samples.jsonl"  # raw output, never edited

SEED = 42
K_SAMPLES = 8  # samples per defect
TEMPERATURE = 0.8  # sampling temperature for the k samples
N_DEV = 30  # D1 defects used to build and tune things

TEST_TIMEOUT_SEC = 10
MAX_MUTANTS = 30
MIN_MUTANTS_FOR_V2 = 3  # fewer valid mutants than this: mutation score not used


def signals_path(split_name: str) -> Path:
    """results/signals_<d1dev|d1test|d2>.jsonl: samples plus computed signals."""
    return RESULTS / f"signals_{split_name}.jsonl"
