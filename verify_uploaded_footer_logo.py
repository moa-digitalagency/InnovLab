import sys
import time
from playwright.sync_api import sync_playwright

def verify_logos():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to index
        page.goto("http://127.0.0.1:5000/")

        # Scroll down to footer gradually to trigger animations
        page.evaluate("""
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        """)

        # Wait for the animation to complete
        time.sleep(2)

        # Take screenshot
        page.wait_for_selector("footer#contact")
        footer = page.locator("footer#contact")
        footer.screenshot(path="footer_logo_uploaded.png")
        print("Footer screenshot saved to footer_logo_uploaded.png")

        browser.close()

if __name__ == "__main__":
    verify_logos()
