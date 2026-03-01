from playwright.sync_api import Page, expect, sync_playwright
import os

languages = ["fr", "en", "es", "pt", "it", "de", "ar", "zh", "ja", "ko"]

def test_hero_title_langs(page: Page):
    os.makedirs("tests/screenshots", exist_ok=True)
    for lang in languages:
        page.goto(f"http://127.0.0.1:5000/set-language/{lang}")
        page.goto("http://127.0.0.1:5000/")

        # Wait for the hero section to load
        page.wait_for_selector(".hero-container")

        # Capture a screenshot
        page.screenshot(path=f"tests/screenshots/hero_{lang}.png")
        print(f"Captured screenshot for {lang}")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_hero_title_langs(page)
        finally:
            browser.close()
