from playwright.sync_api import sync_playwright

def verify_portfolio():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Aller sur la page portfolio en français
        page.goto("http://localhost:5000/portfolio")
        page.wait_for_selector(".project-card")

        # Prendre un screenshot de la page portfolio en FR
        page.screenshot(path="portfolio_fr.png", full_page=True)

        # Changer la langue en anglais
        page.goto("http://localhost:5000/set-language/en")
        page.goto("http://localhost:5000/portfolio")
        page.wait_for_selector(".project-card")

        # Prendre un screenshot de la page portfolio en EN
        page.screenshot(path="portfolio_en.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_portfolio()
