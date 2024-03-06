import asyncio
from pyppeteer import launch

async def print_dom():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://www.sportybet.com/ng/games')
    dom = await page.evaluate('document.documentElement.outerHTML')
    print(dom)
    await browser.close()

asyncio.get_event_loop().run_until_complete(print_dom())
