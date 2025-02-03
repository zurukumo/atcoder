# for i in range(1, 192):
#     process = subprocess.Popen(["pipenv", "run", "download_submission", f"arc{i:03d}"])
#     process.wait()
# for i in range(1, 71):
#     process = subprocess.Popen(["pipenv", "run", "download_submission", f"agc{i:03d}"])
#     process.wait()

# abc, agc, arcで始まるディレクトリを探索
import collections
import os
import re

ret = collections.defaultdict(lambda: [])

for root, dirs, files in os.walk("."):
    for dir in dirs:
        if re.match(r"^(abc|agc|arc)\d{3}$", dir):
            # dirの中の{任意の文字}.pyをリストアップし、かつdir/samplesの中に対応する{任意の一文字}-1-in.txtが存在する場合にprintをする
            for root, dirs, files in os.walk(dir):
                for file in files:
                    if re.match(r".+\.py", file):
                        # .pyがtemplateと同じ場合はスキップ
                        with open(f"{dir}/{file}") as f:
                            with open("clis/data/template.py") as g:
                                if f.read() == g.read():
                                    continue
                        if os.path.exists(f"{dir}/samples/{file[0]}-1-in.txt"):
                            ret[dir].append(file.replace(".py", ""))
                            # print(f"{dir}/{file}")

keys = sorted(ret.keys())
for key in keys:
    ret[key].sort()
    print(key, *ret[key])
