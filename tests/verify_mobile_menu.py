import sys
import time
import subprocess
import requests
import os
from playwright.sync_api import sync_playwright

def verify_mobile_menu():
    print("Starting verification...")

    # Ensure DB exists
    if not os.path.exists("instance/app.db"):
        print("Database not found. Initializing...")
        subprocess.run([sys.executable, "init_db.py"], check=True)

    # Start the server
    process = subprocess.Popen([sys.executable, "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Server process started with PID", process.pid)

    server_url = "http://127.0.0.1:5000"

    # Wait for server to be ready
    server_ready = False
    for i in range(10):
        try:
            response = requests.get(server_url)
            if response.status_code == 200:
                server_ready = True
                print("Server is ready.")
                break
        except requests.ConnectionError:
            pass
        time.sleep(1)

    if not server_ready:
        print("Server failed to start.")
        outs, errs = process.communicate(timeout=5)
        print("STDOUT:", outs)
        print("STDERR:", errs)
        process.terminate()
        return False

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            # iPhone 8 viewport
            context = browser.new_context(viewport={"width": 375, "height": 667})
            page = context.new_page()

            print(f"Navigating to {server_url}...")
            page.goto(server_url)

            # Check initial state
            menu = page.locator("#mobile-menu")
            btn = page.locator("#mobile-menu-btn")

            # Verify menu is hidden initially
            # In Tailwind, 'hidden' class sets display: none.
            # Playwright's is_hidden() checks if element is not visible.
            if not menu.is_hidden():
                print("FAILURE: Mobile menu should be hidden initially.")
                return False
            print("SUCCESS: Mobile menu is initially hidden.")

            # Click to open
            print("Clicking mobile menu button...")
            btn.click()
            # Wait for transition (though Playwright auto-waits for actionability,
            # we need to wait for the class change/visibility change if it's animated)
            page.wait_for_timeout(500)

            if menu.is_hidden():
                print("FAILURE: Mobile menu should be visible after click.")
                # Debug: check classes
                print("Classes:", menu.get_attribute("class"))
                return False

            # Take a screenshot
            if not os.path.exists("tests/screenshots"):
                os.makedirs("tests/screenshots")
            page.screenshot(path="tests/screenshots/mobile_menu_open.png")
            print("Screenshot saved to tests/screenshots/mobile_menu_open.png")

            print("SUCCESS: Mobile menu is visible after click.")

            # Click to close
            print("Clicking mobile menu button again to close...")
            btn.click()
            page.wait_for_timeout(500)

            if not menu.is_hidden():
                print("FAILURE: Mobile menu should be hidden after second click.")
                return False
            print("SUCCESS: Mobile menu is hidden after second click.")

            return True

    except Exception as e:
        print(f"An error occurred during testing: {e}")
        return False
    finally:
        print("Stopping server...")
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()

if __name__ == "__main__":
    success = verify_mobile_menu()
    if success:
        print("VERIFICATION PASSED")
        sys.exit(0)
    else:
        print("VERIFICATION FAILED")
        sys.exit(1)
