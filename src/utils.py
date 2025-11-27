"""CSV reading."""
import csv
from pathlib import Path
from typing import Iterator, Dict


def read_rows_from_files(paths: list[Path]) -> Iterator[Dict[str, str]]:
    """
    yield rows (as dict) from given CSV file paths.
    """
    if not paths:
        raise ValueError('no input files')

    for p in paths:
        with open(p, newline='', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                yield row
