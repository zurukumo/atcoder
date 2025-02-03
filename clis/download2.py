import argparse
import os
import time

from playwright.sync_api import sync_playwright
from utils import load_context, print_green, print_red


def main():
    with sync_playwright() as p:
        context = load_context(p)
        page = context.new_page()

        for nnn in range(108, 392):
            contest = f"abc{nnn:03d}"

            PROBLEM_URL = f"https://atcoder.jp/contests/{contest}/submissions/me?f.Task=&f.LanguageName=Python&f.Status=AC&f.User="

            page.goto(PROBLEM_URL)
            page.wait_for_load_state("networkidle")

            # コンテストページが存在するならディレクトリを作成する
            if page.url != PROBLEM_URL:
                print_red(f"Contest {contest} not found")
                exit(1)

            # リンクから各問題のURLを抽出
            # テーブルの行の2列目と10列目のaタグを取得
            col2 = page.query_selector_all("table tr td:nth-child(2) a")
            col10 = page.query_selector_all("table tr td:nth-child(10) a")
            problem_urls = [page.evaluate("(e) => e.href", link) for link in col2]
            submission_urls = [page.evaluate("(e) => e.href", link) for link in col10]

            done = set()
            for i, (problem_url, submission_url) in enumerate(
                zip(problem_urls, submission_urls)
            ):
                if problem_url in done:
                    continue
                done.add(problem_url)

                problem = problem_url.split("_")[-1]
                if problem == "1":
                    problem = "a"
                elif problem == "2":
                    problem = "b"
                elif problem == "3":
                    problem = "c"
                elif problem == "4":
                    problem = "d"

                if "arc" in problem_url:
                    problem = chr(ord(problem) + 2)

                page.goto(submission_url)
                page.wait_for_load_state("networkidle")

                # コピーボタンをクリック
                page.click(".btn-copy")
                time.sleep(1)
                text = page.evaluate("() => navigator.clipboard.readText()")
                print(text)
                try:
                    with open(f"{contest}/{problem}.py", "w") as f:
                        f.write(text)
                except Exception as e:
                    print_red(f"Failed to create samples")
                    print_red(e)
                    exit(1)
                print_green(f"Created {contest}_{problem} code")

                time.sleep(1)


if __name__ == "__main__":
    main()
