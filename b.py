import builtins
import os
import subprocess

for i in range(1, 71):
    for file in ["a", "b", "c", "d", "e", "f"]:
        if not os.path.exists(f"agc{i:03d}/{file}.py"):
            continue

        with open(f"agc{i:03d}/{file}.py") as f:
            input = f.read()
        with open("clis/data/template.py") as f:
            template = f.read()

        if input == template:
            continue

        print(f"Testing agc{i:03d}/{file}")
        process = subprocess.Popen(["pipenv", "run", "test", f"agc{i:03d}", f"{file}"])
        process.wait()
        if process.returncode != 0:
            builtins.input()
