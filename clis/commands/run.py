import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contest", type=str, help="The contest to test")
    parser.add_argument("problem", type=str, help="The problem to test")

    args = parser.parse_args()

    subprocess.run(
        ["python3", f"contests/{args.contest}/{args.problem}.py"],
    )


if __name__ == "__main__":
    main()
