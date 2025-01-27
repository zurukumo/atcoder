import argparse
import subprocess

import colorama


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", type=str, help="The problem to test")

    args = parser.parse_args()

    for i in range(1, 1000):
        try:
            with open(f"tests/{args.problem}/{i}-in.txt") as f:
                input = f.read()
            with open(f"tests/{args.problem}/{i}-out.txt") as f:
                expected = f.read()

            # inputが空の場合break
            if input == "":
                break
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


if __name__ == "__main__":
    main()
