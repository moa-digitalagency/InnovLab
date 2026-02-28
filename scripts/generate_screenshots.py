from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://127.0.0.1/")
    page.screenshot(path="docs/screenshots/nginx_homepage_screenshot.png", full_page=True)

    page.goto("http://127.0.0.1/admin/login")
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'ChangeMeNow!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(2000)
    page.screenshot(path="docs/screenshots/nginx_admin_dashboard_screenshot.png", full_page=True)

    browser.close()