import os
from pathlib import Path
import pandas as pd
from etl.transform import transform_sales


def test_transform_on_sample(tmp_path):
    # Create a small JSON sample
    sample = tmp_path / 'sample.json'
    sample.write_text('[{"date":"2020-01-01","value":1},{"date":"2020-01-02","value":2}]')
    df = transform_sales(str(sample))
    assert not df.empty
    assert 'date' in df.columns

