import argparse
import re
import subprocess
from typing import Generator

from ..print import print_green, print_red


def read_testcase_file(contest, problem, testcase) -> tuple[str, str]:
    with open(f"contests/{contest}/samples/{problem}-{testcase}-in.txt") as f:
        input = f.read()
    with open(f"contests/{contest}/samples/{problem}-{testcase}-out.txt") as f:
        expected = f.read()

    if input == "":
        raise FileNotFoundError

    return input, expected


def is_decimal_string(s: str) -> bool:
    decimal_pattern = re.compile(r"^-?\d*\.\d+$")
    return decimal_pattern.match(s) is not None


def same(output: str, expected: str) -> bool:
    output = output.strip().split()
    expected = expected.strip().split()

    if len(output) != len(expected):
        return False

    for o, e in zip(output, expected):
        # 小数の場合は誤差を許容する
        if is_decimal_string(o) or is_decimal_string(e):
            if abs(float(o) - float(e)) >= 1e-6:
                return False
        else:
            if o != e:
                return False

    return True


def testcase_generator(
    contest, problem, testcase: int | None = None
) -> Generator[tuple[int, tuple[str, str]], None, None]:
    if testcase is not None:
        yield testcase, read_testcase_file(contest, problem, testcase)
    else:
        for i in range(1, 1000):
            try:
                yield i, read_testcase_file(contest, problem, i)
            except FileNotFoundError:
                break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contest", type=str, help="The contest to test")
    parser.add_argument("problem", type=str, help="The problem to test")
    parser.add_argument("--testcase", type=int, help="The testcase to run")

    args = parser.parse_args()

    failed = False
    for i, (input, expected) in testcase_generator(
        args.contest, args.problem, args.testcase
    ):
        result = subprocess.run(
            ["python3", f"contests/{args.contest}/{args.problem}.py"],
            input=input.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if result.returncode != 0:
            print_red(f"Test {i} failed")
            print_red(result.stdout.decode())
            print_red(result.stderr.decode())
            failed = True
            continue

        if not same(result.stdout.decode(), expected):
            print_red(f"Test {i} failed")
            print_red("Expected:")
            print_red(expected)
            print_red("Got:")
            print_red(result.stdout.decode())
            failed = True
            continue

        print_green(f"Test {i} passed")

    if failed:
        exit(1)


if __name__ == "__main__":
    main()
