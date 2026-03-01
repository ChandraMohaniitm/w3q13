import asyncio
from playwright.async_api import async_playwright

async def run():
    seeds = range(53, 63)
    total_sum = 0
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        # Fix: use new_page() directly or new_context().new_page()
        page = await browser.new_page()
        
        for seed in seeds:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            print(f"Scraping: {url}")
            
            await page.goto(url)
            
            # Wait for the table to actually render (since it's a JS table)
            await page.wait_for_selector("td")
            
            # Extract all table cell values
            cells = await page.query_selector_all('td')
            for cell in cells:
                text = await cell.inner_text()
                try:
                    # Convert text to float and add to sum
                    total_sum += float(text.strip())
                except ValueError:
                    # Skip cells that aren't numbers (like headers or empty cells)
                    continue
            
        print(f"FINAL_TOTAL_SUM: {total_sum}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
