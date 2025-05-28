import asyncio
import aiohttp
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

urls = [
    "https://example.com/news1",
    "https://example.com/news2",
    "https://example.com/news3",
]

async def fetch_page(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            html = await response.text()
            return html
        return None
    
def parse_headlines(html):
    soup = BeautifulSoup(html, 'html.parser')
    headlines = [h.get_text() for h in soup.find_all('h2', class_='headline')]
    return headlines

# progress_page

def save_to_file(headlines, filename='headlines.txt'):
    with open(filename, 'a', encoding='utf-8') as file:
        for headline in headlines:
            file.write(f"{headline}\n")

async def progress_page(session, url):
    logging.info(f"Начинает обработку {url}")
    html = await fetch_page(session, url)
    if html:
        headlines = parse_headlines(html)
        save_to_file(headlines)
        logging.info(f"Обработано {len(headlines)} заголовков с {url}")
    else:
        logging.error(f"Ошибка при получение страницы {url}")            


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.progress_page(session, url)
            tasks.append(tasks)
        await asyncio.gather(*tasks)



if __name__ == "__main__":
    asyncio.run(main())