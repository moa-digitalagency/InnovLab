from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Homepage
    print("Navigating to Homepage...")
    page.goto("http://localhost:5000/")
    page.screenshot(path="tests/homepage.png")

    # Check "Solutions Startups" in nav
    print("Checking 'Solutions Startups' link...")
    # Wait for the element to be visible
    page.wait_for_selector("nav >> text=Solutions Startups")
    assert page.is_visible("nav >> text=Solutions Startups")

    # Founder Page
    print("Navigating to Founder Page...")
    page.goto("http://localhost:5000/candidature/founder")
    page.screenshot(path="tests/founder.png")
    assert page.is_visible("h1 >> text=Candidature Fondateur")

    # Startup Page
    print("Navigating to Startup Page...")
    page.goto("http://localhost:5000/candidature/startup")
    page.screenshot(path="tests/startup.png")
    assert page.is_visible("h1 >> text=Candidature Startup")

    # Investor Page
    print("Navigating to Investor Page...")
    page.goto("http://localhost:5000/candidature/investor")
    page.screenshot(path="tests/investor.png")
    assert page.is_visible("h1 >> text=Espace Investisseur")

    browser.close()
    print("Verification complete.")

with sync_playwright() as playwright:
    run(playwright)
