import argparse
import sys
from diagnostic_analyzer import analyze_diagnostic_log

def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to analyze diagnostic log file of an automated test equipment system (ATE)."
    )

    parser.add_argument(
        "-file_path",
        type=str,
        help="path/to/diagnostic.log"
    )
    args = parser.parse_args()

    try:
        analyze_diagnostic_log(args.file_path)
            
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()