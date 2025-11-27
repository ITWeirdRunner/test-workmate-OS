from .performance import PerformanceReport

# register reports
__all_reports__ = {
    PerformanceReport.name: PerformanceReport,
}

def get_report_class():
    return __all_reports__
