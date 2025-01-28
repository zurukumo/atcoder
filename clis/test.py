import argparse
import subprocess
from typing import Generator

import colorama


def read_testcase_file(problem, testcase) -> tuple[str, str]:
    with open(f"tests/{problem}/{testcase}-in.txt") as f:
        input = f.read()
    with open(f"tests/{problem}/{testcase}-out.txt") as f:
        expected = f.read()

    if input == "":
        raise FileNotFoundError

    return input, expected


def testcase_generator(
    problem, testcase: int | None = None
) -> Generator[tuple[int, tuple[str, str]], None, None]:
    if testcase is not None:
        yield testcase, read_testcase_file(problem, testcase)
    else:
        for i in range(1, 1000):
            try:
                yield i, read_testcase_file(problem, i)
            except FileNotFoundError:
                break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", type=str, help="The problem to test")
    parser.add_argument("--testcase", type=int, help="The testcase to run")

    args = parser.parse_args()

    for i, (input, expected) in testcase_generator(args.problem, args.testcase):
        result = subprocess.run(
            ["python3", f"problems/{args.problem}.py"],
            input=input.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if result.returncode != 0:
            print(f"Test {i} failed: {result.stderr.decode()}")
            exit()

        if result.stdout.decode() != expected:
            print(colorama.Fore.RED + f"Test {i} failed")
            print("Expected:")
            print(expected)
            print("Got:")
            print(result.stdout.decode())
        else:
            print(colorama.Fore.GREEN + f"Test {i} passed")
        print(colorama.Style.RESET_ALL)


if __name__ == "__main__":
    main()
