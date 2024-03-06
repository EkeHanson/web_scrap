import asyncio
from pyppeteer import launch
import os

async def print_dom():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chromium_executable_path = os.path.join(current_dir, 'chrome-win', 'chrome.exe')
    browser = await launch(headless=True, executablePath=chromium_executable_path)
    page = await browser.newPage()
    await page.goto('https://www.sportybet.com/ng/games')
    body_content = await page.evaluate('document.body.innerHTML')
    print(body_content)
    await browser.close()

asyncio.get_event_loop().run_until_complete(print_dom())
