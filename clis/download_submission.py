import argparse
import time

from playwright.sync_api import sync_playwright
from utils import load_context, print_green, print_red


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contest", type=str, help="The contest to download")
    args = parser.parse_args()

    SUBMISSION_URL = f"https://atcoder.jp/contests/{args.contest}/submissions/me?f.Task=&f.LanguageName=Python&f.Status=AC&f.User="

    with sync_playwright() as p:
        context = load_context(p)

        page = context.new_page()
        page.goto(SUBMISSION_URL)
        page.wait_for_load_state("networkidle")
        time.sleep(1)

        # 提出ページが存在するならディレクトリを作成する
        if page.url != SUBMISSION_URL:
            print_red(f"Contest {args.contest} not found")
            exit(1)

        # 問題URLと提出URLを取得
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
            elif problem == "5":
                problem = "e"
            elif problem == "6":
                problem = "f"

            page.goto(submission_url)
            page.wait_for_load_state("networkidle")

            text = page.query_selector("pre#for_copy0").text_content()
            try:
                with open(f"{args.contest}/{problem}.py", "w") as f:
                    f.write(text)
            except Exception as e:
                print_red(f"Failed to create samples")
                print_red(e)
                exit(1)
            print_green(f"Created {args.contest}_{problem} code")

            time.sleep(1)


if __name__ == "__main__":
    main()
