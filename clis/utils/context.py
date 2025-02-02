import os

from playwright.sync_api import BrowserContext, Playwright


def session_file():
    return os.path.join(os.path.dirname(__file__), "../session.json")


def load_context(p: Playwright):
    browser = p.chromium.launch()

    if os.path.exists(session_file()):
        context = browser.new_context(storage_state=session_file())
    else:
        context = browser.new_context()

    return context


def save_context(context: BrowserContext):
    context.storage_state(path=session_file())
