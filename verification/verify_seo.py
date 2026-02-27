from playwright.sync_api import sync_playwright, expect

def verify_seo_admin(page):
    # Login
    page.goto("http://localhost:3000/admin/login")
    page.fill("input[name='username']", "admin")
    page.fill("input[name='password']", "ChangeMeNow!")
    page.click("button[type='submit']")

    # Go to SEO Settings
    page.goto("http://localhost:3000/admin/seo")

    # Verify new fields exist
    expect(page.locator("input[name='og_site_name']")).to_be_visible()
    expect(page.locator("input[name='twitter_handle']")).to_be_visible()
    expect(page.locator("input[name='og_image_default']")).to_be_visible()

    # Verify defaults
    expect(page.locator("input[name='og_site_name']")).to_have_value("Shabaka InnovLab")
    expect(page.locator("input[name='twitter_handle']")).to_have_value("@ShabakaInnov")

    # Update fields
    page.fill("input[name='og_site_name']", "My Updated Site")
    page.fill("input[name='twitter_handle']", "@UpdatedTw")

    # Click save (assuming it's the sticky save button at the bottom right)
    page.click("button[type='submit']")

    # Reload and verify persistence
    page.reload()
    expect(page.locator("input[name='og_site_name']")).to_have_value("My Updated Site")
    expect(page.locator("input[name='twitter_handle']")).to_have_value("@UpdatedTw")

    # Take screenshot
    page.screenshot(path="verification/seo_admin_verified.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_seo_admin(page)
            print("Verification successful!")
        except Exception as e:
            print(f"Verification failed: {e}")
        finally:
            browser.close()
