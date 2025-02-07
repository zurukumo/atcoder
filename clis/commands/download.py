import argparse
import os
import time

from playwright.sync_api import sync_playwright

from ..context import load_context
from ..print import print_green, print_red


def copy_template(contest: str, problem: str) -> None:
    if os.path.exists(f"contests/{contest}/{problem}.py"):
        print_green(f"contests/{contest}/{problem}.py already exists")
        return

    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, "../data/template.py")
    with open(template_path) as f:
        template = f.read()
    with open(f"contests/{contest}/{problem}.py", "w") as f:
        f.write(template)


def create_samples(contest: str, problem: str, id: int, text: str) -> None:
    inout = "in" if id % 2 == 0 else "out"
    num = id // 2 + 1
    with open(f"contests/{contest}/samples/{problem}-{num}-{inout}.txt", "w") as f:
        f.write(text)


def download_submission(contest: str, problem: str) -> None:
    SUBMISSION_URL = f"https://atcoder.jp/contests/{contest}/submissions/me?f.Task=&f.LanguageName=Python&f.Status=AC&f.User="

    with sync_playwright() as p:
        context = load_context(p)

        page = context.new_page()
        page.goto(SUBMISSION_URL)
        page.wait_for_load_state("networkidle")
        time.sleep(1)

        # 提出ページが存在するならディレクトリを作成する
        if page.url != SUBMISSION_URL:
            print_red(f"Contest {contest} not found")
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
                with open(f"contests/{contest}/{problem}.py", "w") as f:
                    f.write(text)
            except Exception as e:
                print_red(f"Failed to create samples")
                print_red(e)
                exit(1)
            print_green(f"Created {contest}_{problem} code")

            time.sleep(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contest", type=str, help="The contest to download")
    parser.add_argument("--submission", action="store_true", help="Download submission")
    args = parser.parse_args()

    PROBLEM_URL = f"https://atcoder.jp/contests/{args.contest}/tasks"

    with sync_playwright() as p:
        context = load_context(p)

        page = context.new_page()
        page.goto(PROBLEM_URL)
        page.wait_for_load_state("networkidle")

        # コンテストページが存在するならディレクトリを作成する
        if page.url != PROBLEM_URL:
            print_red(f"Contest {args.contest} not found")
            exit(1)

        try:
            os.makedirs(f"contests/{args.contest}", exist_ok=True)
            os.makedirs(f"contests/{args.contest}/samples", exist_ok=True)
            print_green(f"Created {args.contest} directory")
        except Exception:
            print_red(f"Failed to create {args.contest} directory")
            exit(1)

        # リンクから各問題のURLを抽出
        problem_links = page.query_selector_all("tr td:first-child a")
        urls = [page.evaluate("(e) => e.href", link) for link in problem_links]

        for i, url in enumerate(urls):
            page.goto(url)
            page.wait_for_load_state("networkidle")

            # 問題番号を生成
            problem = chr(ord("a") + i)

            # テンプレートの作成
            try:
                copy_template(args.contest, problem)
                print_green(f"Created {args.contest}_{problem} template")
            except Exception:
                print_red(f"Failed to create {args.contest}_{problem} template")

            # サンプルの作成
            # サンプルが重複するのでまず.lang-enを削除
            page.evaluate("document.querySelector('span.lang-en').remove()")
            samples = page.query_selector_all("pre[id^=pre-sample]")
            if len(samples) == 0:
                samples = page.query_selector_all("pre[id^=for_copy]")

            for sample in samples:
                # preのidはpre-sample(数字)の形式になっているので数字だけ取り出す
                id = int(
                    sample.get_attribute("id")
                    .replace("pre-sample", "")
                    .replace("for_copy", "")
                )
                text = sample.text_content()
                try:
                    create_samples(args.contest, problem, id, text)
                except Exception:
                    print_red(f"Failed to create samples")
                    exit(1)
            print_green(f"Created {args.contest}_{problem} samples")

            time.sleep(2)

    if args.submission:
        download_submission(args.contest, problem)


if __name__ == "__main__":
    main()
