from playwright.sync_api import sync_playwright

def test_contact_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the contact page
        page.goto("http://localhost:3000/contact-us")

        # Verify the map iframe
        iframe = page.locator("iframe[src*='maps.google.com']")
        if iframe.count() > 0:
            print("Map iframe found with correct source pattern.")
        else:
            print("Map iframe NOT found or has incorrect source.")

        # Verify the subject options
        subject_select = page.locator("select[name='subject']")
        options = subject_select.locator("option").all_inner_texts()

        expected_options = [
            "Choisir un sujet...",
            "Renseignement général",
            "Demande de partenariat",
            "Relation Presse / Médias",
            "Opportunité d'investissement",
            "Opportunité d'emploi",
            "Stage",
            "Candidature Spontanée",
            "Support Technique",
            "Autre"
        ]

        missing_options = [opt for opt in expected_options if opt not in options]

        if not missing_options:
            print("All expected subject options are present.")
        else:
            print(f"Missing options: {missing_options}")
            print(f"Found options: {options}")

        # Take a screenshot
        page.screenshot(path="contact_page_verification.png", full_page=True)
        print("Screenshot saved to contact_page_verification.png")

        browser.close()

if __name__ == "__main__":
    test_contact_page()
