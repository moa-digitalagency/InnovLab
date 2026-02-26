from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    try:
        pages_to_check = [
            "/",
            "/about",
            "/services",
            "/portfolio",
            "/contact-us",
            "/candidature/founder",
            "/candidature/startup",
            "/candidature/investor"
        ]

        for path in pages_to_check:
            url = f"http://localhost:5000{path}"
            print(f"Navigating to {url}...")
            page.goto(url)

            # Check Header (Navigation)
            print(f"  Checking Header on {path}...")
            if not page.is_visible("nav >> text=Nos Services"):
                raise Exception(f"Header missing on {path}")

            # Check Footer
            print(f"  Checking Footer on {path}...")
            if not page.is_visible("footer"):
                raise Exception(f"Footer missing on {path}")

            # Check Footer Content (Copyright)
            if not page.is_visible("text=© 2024 Shabaka InnovLab"):
                 raise Exception(f"Footer content missing on {path}")

        print("Verification complete: Header and Footer present on all pages.")
    except Exception as e:
        print(f"Verification failed: {e}")
        raise e
    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
