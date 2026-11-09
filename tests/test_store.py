from blindstitch.schema import Sample
from blindstitch.store import append, done_keys, read_all


def _s(defect, sid):
    return Sample(defect_id=defect, dataset="d1", category="c", sample_id=sid, patch="p", tests="t",
                  generation_failed=False, oracle_pass=True, self_pass=True)


def test_missing_file_reads_as_empty(tmp_path):
    assert read_all(tmp_path / "nope.jsonl") == []
    assert done_keys(tmp_path / "nope.jsonl") == set()


def test_append_creates_folders_and_roundtrips(tmp_path):
    path = tmp_path / "deep" / "folder" / "samples.jsonl"
    append(path, _s("a", 0))
    append(path, _s("a", 1))
    assert [s.sample_id for s in read_all(path)] == [0, 1]
    assert path.read_text(encoding="utf-8").count("\n") == 2  # one line per sample


def test_done_keys_lets_a_crashed_run_resume(tmp_path):
    path = tmp_path / "s.jsonl"
    append(path, _s("a", 0))
    append(path, _s("b", 3))
    assert done_keys(path) == {("a", 0), ("b", 3)}

def test_read_all_skips_blank_and_whitespace_lines(tmp_path):
    path = tmp_path / "whitespace.jsonl"
    append(path, _s("a", 0))
    # Inject blank lines and whitespace characters
    with path.open("a", encoding="utf-8") as f:
        f.write("\n   \n\t\n")
    append(path, _s("a", 1))

    samples = read_all(path)
    assert [s.sample_id for s in samples] == [0, 1]
    assert done_keys(path) == {("a", 0), ("a", 1)}