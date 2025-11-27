import subprocess
import sys
import os
import tempfile

def test_runs_and_outputs_table():
    # create a test CSV
    content = 'name,position,completed_tasks,performance,skills,team,experience_years\nX,Dev,1,5.0,sk,Team,1\n'
    t = tempfile.NamedTemporaryFile('w', delete=False, suffix='.csv')
    t.write(content)
    t.close()
    try:
        # Run the module as a script
        cmd = [sys.executable, '-m', 'src.main', '--files', t.name, '--report', 'performance']
        proc = subprocess.run(cmd, capture_output=True, text=True)
        assert proc.returncode == 0
        assert 'position' in proc.stdout
        assert 'avg_performance' in proc.stdout
    finally:
        os.unlink(t.name)
