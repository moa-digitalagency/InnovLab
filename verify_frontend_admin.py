from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Login
        page.goto("http://localhost:5000/admin/login")
        page.fill("input[name='username']", "admin")
        page.fill("input[name='password']", "admin")
        page.click("button[type='submit']")

        # Go to Settings
        page.goto("http://localhost:5000/admin/settings")
        page.screenshot(path="settings_page.png")

        # Test Tabs (Switch to Telegram)
        page.click("#btn-telegram")
        time.sleep(0.5)
        page.screenshot(path="settings_telegram_tab.png")

        # Test Tabs (Switch to Social)
        page.click("#btn-social")
        time.sleep(0.5)
        page.screenshot(path="settings_social_tab.png")

        # Upload Logo (Switch to Identity first)
        page.click("#btn-identity")
        time.sleep(0.5)
        page.set_input_files("input[name='header_logo']", "test_logo.png")
        page.click("button[type='submit']")
        time.sleep(1) # Wait for reload/flash

        # Check Homepage for Logo
        page.goto("http://localhost:5000/")
        page.screenshot(path="home_with_logo.png")

        # Go to SEO
        page.goto("http://localhost:5000/admin/seo")
        page.screenshot(path="seo_page.png")

        # Fill Global SEO
        page.fill("input[name='google_analytics_id']", "G-TEST-PLAYWRIGHT")
        page.click("button[type='submit']")
        time.sleep(1)

        # Verify Source (GA ID)
        page.goto("http://localhost:5000/")
        content = page.content()
        if "G-TEST-PLAYWRIGHT" in content:
            print("GA ID verified in source.")
        else:
            print("GA ID NOT found in source.")

        browser.close()

if __name__ == "__main__":
    run()
