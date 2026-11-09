"""Append-only JSON Lines storage. One line = one Sample. Never edit in place."""

from pathlib import Path

from .schema import Sample


def append(path: Path, sample: Sample) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(sample.model_dump_json() + "\n")


def read_all(path: Path) -> list[Sample]:
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    return [Sample.model_validate_json(line) for line in lines if line.strip()]


def done_keys(path: Path) -> set[tuple[str, int]]:
    """(defect_id, sample_id) pairs already saved, so a crashed run can resume."""
    return {(s.defect_id, s.sample_id) for s in read_all(path)}
