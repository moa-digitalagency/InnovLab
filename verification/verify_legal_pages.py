from playwright.sync_api import sync_playwright

def verify_legal_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Verify Privacy Policy
        page.goto("http://127.0.0.1:5000/privacy-policy")
        page.screenshot(path="verification/privacy_policy.png", full_page=True)
        print("Privacy Policy screenshot taken.")

        # Verify Terms & Conditions
        page.goto("http://127.0.0.1:5000/terms-conditions")
        page.screenshot(path="verification/terms_conditions.png", full_page=True)
        print("Terms & Conditions screenshot taken.")

        # Verify Footer Links
        page.goto("http://127.0.0.1:5000/")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.screenshot(path="verification/footer_links.png")
        print("Footer links screenshot taken.")

        browser.close()

if __name__ == "__main__":
    verify_legal_pages()
