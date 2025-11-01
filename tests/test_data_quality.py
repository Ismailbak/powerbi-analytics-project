from etl.utils.helpers import ensure_dir


def test_ensure_dir(tmp_path):
    p = tmp_path / 'a' / 'b'
    assert not p.exists()
    ensure_dir(str(p))
    assert p.exists()
