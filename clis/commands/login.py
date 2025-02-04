import os

from playwright.sync_api import sync_playwright

from ..context import load_context, save_context
from ..print import print_green, print_red


def login():
    LOGIN_URL = "https://atcoder.jp/login"

    try:
        USERNAME = os.environ["USERNAME"]
        PASSWORD = os.environ["PASSWORD"]
    except KeyError:
        print_red("Set USERNAME and PASSWORD environment variables")
        exit(1)

    with sync_playwright() as p:
        context = load_context(p)

        page = context.new_page()
        page.goto(LOGIN_URL)
        page.wait_for_load_state("networkidle")

        # ヘッダーにログインボタンがあるかどうかでログイン済みかどうかを判定する
        login_button = page.query_selector("#header a[href='/login']")
        if login_button is None:
            print_green("Already logged in.")
            exit()

        # ログイン処理
        page.fill("#username", USERNAME)
        page.fill("#password", PASSWORD)
        page.click("#submit")
        page.wait_for_load_state("networkidle")

        # ログイン成功時にセッション情報を保存
        save_context(context)
        print_green("Login successful. Session saved.")


if __name__ == "__main__":
    login()
