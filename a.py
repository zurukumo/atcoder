import subprocess

# for i in range(1, 192):
#     process = subprocess.Popen(["pipenv", "run", "download_submission", f"arc{i:03d}"])
#     process.wait()

for i in range(1, 71):
    process = subprocess.Popen(["pipenv", "run", "download_submission", f"agc{i:03d}"])
    process.wait()
