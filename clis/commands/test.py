import argparse
import re
import subprocess
from typing import Generator

from ..print import print_green, print_red, print_yellow


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
    for i, (input, expected) in testcase_generator(args.contest, args.problem, args.testcase):
        try:
            # TLE時に途中までの標準出力を取得するために標準出力をバッファしない
            result = subprocess.run(
                ["python3", "-u", f"contests/{args.contest}/{args.problem}.py"],
                input=input,
                capture_output=True,
                text=True,
                timeout=3,
            )
        except subprocess.TimeoutExpired as error:
            print_yellow(f"TLE: Test {i}")
            print_yellow(error.stdout.decode())
            failed = True
            continue

        if result.returncode != 0:
            print_yellow(f"CE: Test {i}")
            print_yellow(result.stdout)
            print_yellow(result.stderr)
            failed = True
            continue

        if not same(result.stdout, expected):
            print_red(f"WA: Test {i}")
            print_red("Expected:")
            print_red(expected)
            print_red("Got:")
            print_red(result.stdout)
            failed = True
            continue

        print_green(f"AC: Test {i}")

    if failed:
        exit(1)


if __name__ == "__main__":
    main()
