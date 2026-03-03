import sys
from playwright.sync_api import sync_playwright

def verify_footer_logo():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to index
        page.goto("http://127.0.0.1:5000/")

        # Scroll down to footer
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # Wait for footer to be visible
        page.wait_for_selector("footer#contact")

        # Take screenshot of the entire footer area
        footer = page.locator("footer#contact")
        footer.screenshot(path="verification.png")

        print("Screenshot saved to verification.png")
        browser.close()

if __name__ == "__main__":
    verify_footer_logo()
