import time
import requests
import re
from bs4 import BeautifulSoup as bs
import os
import django
import html as hl
from concurrent.futures import ThreadPoolExecutor

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlingNews.settings")

django.setup()
from ytnNews.models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    NationwideNews,
    SocietyNews,
    CultureNews,
    ScienceNews,
    SportsNews,
    CalamityNews
)

# Define the sections as a dictionary
sections = {
    "0101": PoliticsNews,
    "0102": EconomyNews,
    "0104": InternationalNews,
    "0115": NationwideNews,
    "0103": SocietyNews,
    "0106": CultureNews,
    "0105": ScienceNews,
    "0107": SportsNews,
    'S0018': CalamityNews
}

def create_session():
    # Create an HTTP session for making requests
    session = requests.Session()
    # Set headers, if needed
    session.headers.update({'User-Agent': 'Your User Agent String'})
    return session

def collect_news_urls(session, section):
    news_urls = []
    response = session.get(
        f"https://www.ytn.co.kr/news/list.php?mcd={section}"
    )
    soup = bs(response.text, "html.parser")
    for url in soup.select("#nav_content > div:nth-child(1) > ul > li"):
        news_urls.append(url.find("a")["href"])
    return news_urls

def date_to_integer(target_date):
    target_date = target_date.split()
    result_date = target_date[0][:-1] + target_date[1][:-1] + target_date[2][:-1] + target_date[3][:-1] + target_date[4][:-1]
    return result_date

def cleanup_html(article_content):
    cleanup_items = [
        ('div', {'id': 'hns_mask'}),
        ('div', {'id': 'YTN_Player'}),
        ('div', {'id': 'ad_box txtad'}),
        ('div', {'class': 'imgArea'}),
        ('iframe', None),
        ('style', None),
    ]
    for tag, attrs in cleanup_items:
        try:
            if attrs:
                article_content.find(tag, attrs).decompose()
            else:
                article_content.find(tag).decompose()
        except:
            pass

def process_article_content(article_content):
    article_content = str(article_content)
    article_content = article_content.split("※ '당신의 제보가 뉴스가 됩니다'")[0]
    article_content = article_content.split("[저작권자(c) YTN 무단전재, 재배포 및 AI 데이터 활용 금지]")[0]
    article_content = article_content.replace("<br/>", "\n")
    article_content = article_content.replace('크게보기', '')
    article_content = article_content.replace("<b>", "")
    article_content = article_content.replace("</b>", "")
    article_content = article_content.replace("\r\n", "\n")
    article_content = re.sub("<(.|\n|\r)+?>", "\n", article_content).strip()
    article_content = re.sub(" +", " ", article_content)
    article_content = re.sub("\n {1,}", "\n", article_content)
    article_content = re.sub("\n{2,}", "\n\n", article_content)
    article_content = re.sub(" {1,}", " ", article_content)
    article_content = article_content.replace('\n \n', '')
    article_content = article_content.replace("...", "... ")
    article_content = article_content.replace("...  ", "... ")
    article_content = hl.unescape(article_content)
    return article_content

def crawling_article(session, url, index, News):
    response = session.get(url)
    html_text = response.text
    html = bs(html_text, "html.parser")

    article_title = html.select_one("#nav_content > div:nth-child(1) > h3").get_text()
    article_title = article_title.replace("...", "... ")
    article_title = article_title.replace("...  ", "... ")
    article_title = hl.unescape(article_title)

    article_time = (
        html.select_one(
            '#nav_content > div.wrap > div.li_1 > span.time'
        )
        .get_text()
        .strip()
    )

    article_content = html.select_one("#zone1 > div.content > div > div")
    cleanup_html(article_content)
    article_content = process_article_content(article_content)

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

def process_section(section, News, session):
    start = time.time()
    # Collect news titles before and after clicking the pagination link
    all_news_urls = []
    all_news_urls += collect_news_urls(session, section)

    # Process the first 10 articles
    all_news_urls = all_news_urls[:10]
    for index, url in enumerate(all_news_urls):
        crawling_article(session, url, index, News)

    end = time.time()
    print(f"section({str(News)}) 응답시간 : {end - start : .5f} sec")

if __name__ == "__main__":
    total_start = time.time()
    session = create_session()


    for section, News in sections.items():
        process_section( section, News, session)

    total_end = time.time()
    print(f"총 응답시간 : {total_end - total_start : .5f} sec")
