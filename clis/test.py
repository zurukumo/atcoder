import argparse
import subprocess

import colorama


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", type=str, help="The problem to test")

    args = parser.parse_args()

    i = 1
    while True:
        try:
            with open(f"tests/{args.problem}/in-{i}.txt") as f:
                input = f.read()
            with open(f"tests/{args.problem}/out-{i}.txt") as f:
                expected = f.read()
        except FileNotFoundError:
            break

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

        i += 1


if __name__ == "__main__":
    main()
