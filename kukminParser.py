import time
import requests
import re
from bs4 import BeautifulSoup as bs
import os
import django
import html as hl

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlingNews.settings")

django.setup()
from kukminIlbo.models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    IssueNews,
    EntertainmentsNews,
    SportsNews,
    LifeNews,
)

# Define the sections as a dictionary
sections = {
    "pol": PoliticsNews,  # 정치
    "eco": EconomyNews,  # 국민경제
    "int": InternationalNews,  # 국제
    "soc": SocietyNews,  # 사회
    "prj&sid2=0086&st=all": IssueNews,  # 이슈&탐사
    "ent": EntertainmentsNews,  # 연예
    "spo": SportsNews,  # 스포츠
    "lif": LifeNews,  # 라이프
}


def create_session():
    # Create an HTTP session for making requests
    session = requests.Session()
    # Set headers, if needed
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
    )
    return session


def collect_news_urls(session, section):
    news_urls = []
    response = session.get(f"https://news.kmib.co.kr/article/list.asp?sid1={section}")
    soup = bs(response.text, "html.parser")
    for url in soup.select(
        "#sub > div > div.NwsCon > div.nws_list > div.nws > dl > dt"
    ):
        news_urls.append(url.find("a")["href"])
    return news_urls


def date_to_integer(target_date):
    target_date = target_date.split()
    date = target_date[0].replace("-", "")
    time = target_date[1].split(":")
    result_date = date + time[0] + time[1]
    return result_date


def crawling_articles(session, section, News):
    all_news_urls = collect_news_urls(session, section)
    for index in range(0, min(10, len(all_news_urls))):  # Process the first 10 articles
        url = all_news_urls[index]
        response = session.get("https://news.kmib.co.kr/article/" + url)
        html_text = response.content.decode("euc-kr", "replace").encode(
            "utf-8", "replace"
        )
        html = bs(html_text, "html.parser")
        article_title = html.select_one(
            "#sub > div.sub_header > div > div.nwsti > h3"
        ).get_text()
        article_title = article_title.replace("…", "… ")
        article_title = article_title.replace("…  ", "… ")
        article_title = hl.unescape(article_title)
        article_time = (
            html.select_one(
                "#sub > div.sub_header > div > div.nwsti > div > div.date > span"
            )
            .get_text()
            .strip()
        )
        article_content = str(html.select_one("#articleBody"))
        article_content = article_content.split('<div class="view_reporter">')[0]
        article_content = article_content.split("GoodNews paper ⓒ")[0]
        article_content = article_content.replace("<br/>", "\n")
        article_content = article_content.replace("<b>", "")
        article_content = article_content.replace("</b>", "")
        article_content = re.sub("<(.|\n|\r)+?>", "\n", article_content).strip()
        article_content = re.sub(" +", " ", article_content)
        article_content = re.sub("\n{2,}", "\n\n", article_content)
        article_content = re.sub("\n {1,}", "\n", article_content)
        article_content = article_content.replace("\n \n", "")
        article_content = article_content.replace("  ", " ")
        article_content = article_content.replace("...", "... ")
        article_content = article_content.replace("...  ", "... ")
        article_content = hl.unescape(article_content)
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


if __name__ == "__main__":
    total_start = time.time()
    session = create_session()
    for section, News in sections.items():
        start = time.time()
        crawling_articles(session, section, News)
        end = time.time()
        print(f"section({section}) 응답시간 : {end - start : .5f} sec")
    total_end = time.time()
    print(f"총 응답시간 : {total_end - total_start : .5f} sec")
