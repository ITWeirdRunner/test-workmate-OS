"""performance report: average performance"""
from collections import defaultdict
from typing import Iterable, Dict, List
from .base import BaseReport

class PerformanceReport(BaseReport):
    name = 'performance'

    def generate(self, rows: Iterable[Dict]) -> List[Dict]:
        totals = defaultdict(float)
        counts = defaultdict(int)

        for r in rows:
            pos = (r.get('position') or '').strip()
            perf_val = r.get('performance')
            try:
                perf = float(perf_val)
            except Exception:
                # skip invalid
                continue
            totals[pos] += perf
            counts[pos] += 1

        result = []
        for pos, tot in totals.items():
            cnt = counts[pos]
            if cnt == 0:
                continue
            avg = tot / cnt
            result.append({'position': pos, 'avg_performance': round(avg, 3)})

        # sort by avg_performance desc
        result.sort(key=lambda x: x['avg_performance'], reverse=True)
        return result
