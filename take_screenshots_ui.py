import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        langs = ['fr', 'en', 'ar', 'zh']

        # Go to homepage once
        await page.goto('http://127.0.0.1:5000/')
        await page.wait_for_timeout(2000)

        for lang in langs:
            # Hover over the language selector to reveal the dropdown
            await page.hover("div.fixed.bottom-6.left-6.z-50.group")
            await page.wait_for_timeout(1000)

            # Click the language link inside the dropdown
            await page.click(f"a[href*='/set-language/{lang}']")

            # Wait for navigation and dynamic content to load
            await page.wait_for_timeout(2000)

            # Take a screenshot
            await page.screenshot(path=f'screenshot_ui_{lang}.png', full_page=True)
            print(f'Screenshot taken via UI click for {lang}')

        await browser.close()

asyncio.run(run())
