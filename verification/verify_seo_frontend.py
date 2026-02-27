from playwright.sync_api import sync_playwright
import time
import os

# Ensure the upload directory exists for the test to prevent 500 error
os.makedirs('statics/uploads/logos', exist_ok=True)

def verify_seo_render():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the home page (assuming Flask is running on port 5000)
        # Note: In a real CI environment, we would start the server here.
        # For this interactive session, we assume the user/environment handles it
        # or we rely on the previous unit tests for logic verification.
        # However, to be thorough, we will try to connect.
        try:
            page.goto("http://localhost:5000/")

            # Wait for content to load
            page.wait_for_load_state("networkidle")

            # Take a screenshot of the home page to verify visual rendering hasn't broken
            page.screenshot(path="verification/home_seo_render.png")
            print("Screenshot taken: verification/home_seo_render.png")

            # Verify the title programmatically (Mock data should be active if DB is empty)
            title = page.title()
            print(f"Page Title: {title}")

            # Check for meta description
            meta_desc = page.locator('meta[name="description"]').get_attribute("content")
            print(f"Meta Description: {meta_desc}")

            # Check for Open Graph Title
            og_title = page.locator('meta[property="og:title"]').get_attribute("content")
            print(f"OG Title: {og_title}")

        except Exception as e:
            print(f"Error connecting to server or verifying: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_seo_render()
