from playwright.sync_api import sync_playwright

def verify_hero_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            # Navigate to the home page (assuming app runs on port 5000)
            page.goto("http://localhost:5000")

            # Wait for the H1 title to be visible
            # The exact text might be tricky due to <br/> and spans, so we'll locate by h1
            h1 = page.locator("h1.text-5xl")
            h1.wait_for()

            # Take a screenshot
            page.screenshot(path="verification_screenshot.png")
            print("Screenshot taken: verification_screenshot.png")

            # Optional: Print the inner HTML to verify structure if needed
            print(h1.inner_html())

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_hero_title()
