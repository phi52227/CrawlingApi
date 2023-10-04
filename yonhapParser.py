import time
import requests
import re
from bs4 import BeautifulSoup as bs
import os
import django
import html as hl

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlingNews.settings")

django.setup()
from yonhapNews.models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    CultureNews,
    EntertainmentsNews,
    SportsNews,
    NorthKoreaNews
)

total_start = time.time()

sections = {
    "politics": PoliticsNews,
    "economy": EconomyNews,
    "international": InternationalNews,
    "society": SocietyNews,
    "culture": CultureNews,
    "entertainment": EntertainmentsNews,
    "sports": SportsNews,
    'north-korea':NorthKoreaNews
}

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

# Function to collect news titles
def collect_news_urls(section):
    news_urls = []
    response = requests.get(
        f"https://www.yna.co.kr/{section}/all/1", headers=headers
    )
    soup = bs(response.text, "html.parser")
    for url in soup.select("#container > div > div > div.section01 > section > div.list-type038 > ul > li > div > div.news-con"):
        news_urls.append(url.find("a")["href"])

    return news_urls


def date_to_integer(target_date):
    target_date = target_date.split()
    date = target_date[0].replace("-", "")
    time = target_date[1].split(":")
    result_date = date + time[0] + time[1]

    return result_date


def crawling_article(url, index, News):
    response = requests.get("https:" + url)

    html_text = response.text

    html = bs(html_text, "html.parser")

    article_title = html.select_one("#articleWrap > div.content03 > header > h1").get_text()
    article_title = article_title.replace("…", "… ")
    article_title = article_title.replace("…  ", "… ")
    article_title = hl.unescape(article_title)

    article_time = (
        html.select_one(
            '#newsUpdateTime01'
        )
        .get_text()
        .replace('송고시간', '').strip()
    )

    article_content = html.select_one("#articleWrap > div.content01.scroll-article-zone01 > div > div > article")
    try:
        article_content.find('div', {'id':'newsWriterCarousel01'}).decompose()
    except Exception as e:
        pass
    try:
        article_content.find('div', {'class':'related-zone rel'}).decompose()
    except Exception as e:
        pass
    try:
        article_content.find('p', {'class':'txt-copyright adrs'}).decompose()
    except Exception as e:
        pass
    try:
        article_content.find('span', {'class':'blind'}).decompose()
    except Exception as e:
        pass
    try:
        article_content.find('div', {'class':'comp-box youtube-group'}).decompose()
    except Exception as e:
        pass
    article_content = str(article_content)
    article_content = article_content.split("function")[0]
    article_content = article_content.split('<div class="article_issue article_issue02">')[0]
    article_content = article_content.replace("<br/>", "\n")
    article_content = article_content.replace('크게보기', '')
    article_content = re.sub("<(.|\n|\r)+?>", "\n", article_content).strip()
    article_content = re.sub(" +", " ", article_content)
    article_content = re.sub("\n{2,}", "\n\n", article_content)
    article_content = re.sub("\n {1,}", "\n", article_content)
    # article_content = article_content.replace("\n ", "\n")
    article_content = article_content.replace('\n \n', '')
    article_content = article_content.replace("  ", " ")
    article_content = article_content.replace("...", "... ")
    article_content = article_content.replace("...  ", "... ")
    article_content = hl.unescape(article_content)
    # article_content = article_content.replace("&lt;", "<")
    # article_content = article_content.replace("&gt;", ">")

    try:
        News(
            title=article_title,
            posting_date=article_time,
            content=article_content,
            order=date_to_integer(article_time),
        ).save()
    except Exception as e:
        print(e)
        pass

for section, News in sections.items():
    start = time.time()
    # Collect news titles before and after clicking the pagination link
    all_news_urls = []
    all_news_urls += collect_news_urls(section)

    for index in range(0, 10):
        crawling_article(all_news_urls[index], index, News)

    end = time.time()
    print(f"section({section}) 응답시간 : {end - start : .5f} sec")


total_end = time.time()
print(f"총 응답시간 : {total_end - total_start : .5f} sec")
