import tempfile
import os
from pathlib import Path
from src.reports.performance import PerformanceReport
from src.utils import read_rows_from_files

SAMPLE = '''
name,position,completed_tasks,performance,skills,team,experience_years
A,Backend,10,4.5,"a",T,1
B,Backend,12,5.0,"b",T,2
C,Frontend,8,4.0,"c",W,1
'''

def make_temp_csv(content: str) -> Path:
    fd, path = tempfile.mkstemp(suffix='.csv', text=True, dir='tests' )
    os.close(fd)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    return Path(path)

def test_performance_avg_basic():
    path = make_temp_csv(SAMPLE)
    try:
        rows = list(read_rows_from_files([path]))
        rep = PerformanceReport()
        out = rep.generate(rows)
        # Expect Backend average (4.75) then Frontend (4.0)
        assert out[0]['position'] == 'Backend'
        assert abs(out[0]['avg_performance'] - 4.75) < 1e-6
        assert out[1]['position'] == 'Frontend'
    finally:
        os.unlink(path)
