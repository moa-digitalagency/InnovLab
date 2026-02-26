from playwright.sync_api import sync_playwright

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Create a new page
        page = browser.new_page()

        # Navigate to the home page (assuming the app is running on localhost:5000)
        page.goto("http://localhost:5000")

        # 1. Verify Header Height and Logo
        # The header should now be h-24 (96px) instead of h-20 (80px)
        header_container = page.locator("#main-header > div").first
        class_attr = header_container.get_attribute("class")
        print(f"Header container classes: {class_attr}")

        if class_attr and "h-24" in class_attr:
            print("SUCCESS: Header container height is h-24")
        else:
            print("FAILURE: Header container height is not h-24")

        # 2. Verify Hero Padding
        # The hero section should now have pt-24
        hero = page.locator(".hero-container")
        hero_class = hero.get_attribute("class")
        print(f"Hero classes: {hero_class}")
        if hero_class and "pt-24" in hero_class:
            print("SUCCESS: Hero padding is pt-24")
        else:
            print("FAILURE: Hero padding is not pt-24")

        # 3. Verify Hero Text Change
        # Should be "Construire le" instead of "Co-construisez le"
        # Be more specific with the selector
        hero_heading = page.locator(".hero-container h1")
        heading_text = hero_heading.inner_text()
        print(f"Hero Heading Text: {heading_text}")
        if "Construire le" in heading_text:
            print("SUCCESS: Hero text updated correctly")
        else:
            print("FAILURE: Hero text not updated")

        # Take a screenshot
        page.screenshot(path="verification/verification.png")
        print("Screenshot saved to verification/verification.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()
