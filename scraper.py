import asyncio
from playwright.async_api import async_playwright

async def run():
    seeds = range(53, 63)
    total_sum = 0
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_api_context().new_page()
        
        for seed in seeds:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}" # Replace with the actual URL provided in your prompt
            await page.goto(url)
            # Logic to find tables and sum numbers
            # example: cells = await page.query_selector_all('td')
            # for cell in cells: total_sum += float(await cell.inner_text())
            
        print(f"FINAL_TOTAL_SUM: {total_sum}")
        await browser.close()

asyncio.run(run())
