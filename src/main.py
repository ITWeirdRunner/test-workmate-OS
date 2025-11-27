import argparse
import sys
from .utils import read_rows_from_files
from .reports import get_report_class
from tabulate import tabulate

def build_parser():
    parser = argparse.ArgumentParser(
        description='Generate reports from CSV files'
    )
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='paths to CSV files to process'
    )
    parser.add_argument(
        '--report',
        required=True,
        choices=list(get_report_class().keys()) if callable(get_report_class) else [],
        help='report anme'
    )
    return parser

def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        rows = list(read_rows_from_files(args.files))
    except Exception as e:
        print(f"error reading files: {e}", file=sys.stderr)
        sys.exit(2)

    report_cls = get_report_class()[args.report]
    report = report_cls()
    result_rows = report.generate(rows)

    if not result_rows:
        print("No data to show.")
        return

    # normalize: sequence of dicts -> headers from keys
    headers = list(result_rows[0].keys())
    table = [[r.get(h, '') for h in headers] for r in result_rows]
    print(tabulate(table, headers=headers, tablefmt='github'))

if __name__ == '__main__':
    main()
