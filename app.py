import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://example.com')
    element = await page.querySelector('h1')
    title = await page.evaluate('(element) => element.textContent', element)
    await page.screenshot({'path': 'example.png'})
    print("====")
    print(title)
    print("====")
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
