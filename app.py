import asyncio
import urllib.request
from pyppeteer import launch

async def main():
    # WSL2で実行しているのでheadless前提
    browser = await launch(args=['--no-sandbox'])

    print("== Start ==")

    page = await browser.newPage()
    # 気象庁の気象データを取得する
    await page.goto('https://www.data.jma.go.jp/obd/stats/data/mdrr/docs/csv_dl_format_prenh.html')
    element = await page.querySelector('#main>ul>li>a')

    ## 取得したaタグのURLを取りに行く
    link = await page.evaluate('(element) => element.href', element)

    # --download--
    # puppeteerがfile downloadに対応しておらず、リクエストが中途半端に切れてしまう
    # await page._client.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': './'});
    # await page.goto(link)

    # そのためリンクを取得したらurllibを使って別でダウンロードする
    urllib.request.urlretrieve(link, './最新の気象データ.csv')

    print("== End ==")
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
