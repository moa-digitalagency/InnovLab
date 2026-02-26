import sys
import subprocess
import time
import os
import requests
from playwright.sync_api import sync_playwright

def verify_flash():
    # Start server
    env = os.environ.copy()
    process = subprocess.Popen([sys.executable, "app.py"], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Server started with PID {process.pid}")

    # Wait for server
    url = "http://127.0.0.1:5000"
    started = False
    for _ in range(15):
        try:
            if requests.get(url).status_code == 200:
                started = True
                break
        except:
            time.sleep(1)

    if not started:
        print("Server failed to start")
        out, err = process.communicate()
        print(out)
        print(err)
        return

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1280, "height": 720})

            print("Navigating to home...")
            page.goto(url)

            # Scroll to footer to find form (it's in footer)
            # Actually we can just fill it if it's in the DOM
            print("Filling footer contact form...")
            # The input is in the footer: <input type="email" name="email" ...>
            page.locator("footer input[name='email']").scroll_into_view_if_needed()
            page.locator("footer input[name='email']").fill("test_flash@example.com")
            page.locator("footer button[type='submit']").click()

            # Wait for reload/redirect and flash message
            # The flash message container is fixed top-24 right-4
            # We look for text "Merci pour votre inscription!"
            print("Waiting for flash message...")
            try:
                flash_msg = page.locator("text=Merci pour votre inscription!")
                flash_msg.wait_for(state="visible", timeout=10000)
                print("Flash message found!")
            except Exception as e:
                print(f"Flash message not found: {e}")
                # Save screenshot anyway for debugging
                page.screenshot(path="verification/flash_failure.png")
                raise e

            # Take screenshot
            screenshot_path = "verification/flash_message.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

    finally:
        print("Terminating server...")
        process.terminate()
        process.wait()

if __name__ == "__main__":
    verify_flash()
