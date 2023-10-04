import time
import requests
import re
from bs4 import BeautifulSoup as bs
import os
import django
import html as hl

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

total_start = time.time()

sections = {
    "0101": PoliticsNews,  # 정치
    "0102": EconomyNews,  # 경제
    "0104": InternationalNews,  # 국제
    "0115": NationwideNews,  # 전국
    "0103": SocietyNews,  # 사회
    "0106": CultureNews,  #문화
    "0105": ScienceNews,  # 과학
    "0107": SportsNews,  # 스포츠
    'S0018':CalamityNews  # 재난
}

# Function to collect news titles
def collect_news_urls(section):
    news_urls = []
    response = requests.get(
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


def crawling_article(url, index, News):
    response = requests.get(url)

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

    try:
        article_content.find('div', {'id':'hns_mask'}).decompose()
    except:
        pass
    try:
        article_content.find('div', {'id':'YTN_Player'}).decompose()
    except:
        pass
    try:
        article_content.find('div', {'id':'ad_box txtad'}).decompose()
    except:
        pass
    try:
        article_content.find('iframe').decompose()
    except:
        pass
    try:
        article_content.find('style').decompose()
    except:
        pass

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
    # article_content = article_content.replace("\n ", "\n")
    article_content = article_content.replace('\n \n', '')
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
    print(f"section({str(News)}) 응답시간 : {end - start : .5f} sec")


total_end = time.time()
print(f"총 응답시간 : {total_end - total_start : .5f} sec")
