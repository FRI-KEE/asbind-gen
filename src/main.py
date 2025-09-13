import argparse
import analyzer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze C++ source files.")
    parser.add_argument("files", metavar="F", type=str, nargs="+", help="C++ source files to analyze")
    args = parser.parse_args()

    for file in args.files:
        print(f"Analyzing {file}...")
