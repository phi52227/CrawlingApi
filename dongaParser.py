import time
import requests
import re
from bs4 import BeautifulSoup as bs
import os
import django
import html as hl

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlingNews.settings")

django.setup()
from dongaIlbo.models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    CultureNews,
    EntertainmentsNews,
    SportsNews,
)

total_start = time.time()

sections = {
    "Politics": PoliticsNews,
    "Economy": EconomyNews,
    "Inter": InternationalNews,
    "Society": SocietyNews,
    "Culture": CultureNews,
    "Entertainment": EntertainmentsNews,
    "Sports": SportsNews,
}


# Function to collect news titles
def collect_news_urls(section):
    news_urls = []
    for num in range(1, 40, 10):
        response = requests.get(
            f"https://www.donga.com/news/{section}?p={num}&prod=news&ymd=&m="
        )
        soup = bs(response.text, "html.parser")
        for url in soup.find_all("div", class_="rightList"):
            news_urls.append(url.find("a")["href"])

    return news_urls


def date_to_integer(target_date):
    target_date = target_date.split()
    date = target_date[0].replace("-", "")
    time = target_date[1].split(":")
    result_date = date + time[0] + time[1]

    return result_date


def crawling_article(url, index, News):
    response = requests.get(url)

    html_text = response.text

    html = bs(html_text, "html.parser")

    article_title = html.select_one("#container > div.article_title > h1").get_text()
    article_title = article_title.replace("…", "… ")
    article_title = article_title.replace("…  ", "… ")
    article_title = hl.unescape(article_title)

    article_time_arr = (
        html.select_one(
            "#container > div.article_title > div.title_foot > span:nth-child(1)"
        )
        .get_text()
        .split(" ")
    )
    article_time = article_time_arr[1] + " " + article_time_arr[2]

    article_content = str(html.select_one("#article_txt"))
    article_content = article_content.split("function")[0]
    article_content = article_content.split('<div class="article_issue article_issue02">')[0]
    article_content = article_content.replace("<br/>", "\n")
    article_content = article_content.replace('크게보기', '')
    article_content = article_content.replace('\r\n', '\n')
    article_content = re.sub("<(.|\n|\r)+?>", "\n", article_content).strip()
    article_content = re.sub(" +", " ", article_content)
    article_content = re.sub("\n{2,}", "\n\n", article_content)
    article_content = article_content.replace('\n \n', '')
    # article_content = article_content.replace(" \n", "\n")
    # article_content = article_content.replace("\n", "\n ")
    # article_content = article_content.replace("\n \n", "\n\n")
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

    for index, url in enumerate(all_news_urls):
        crawling_article(url, index, News)

    end = time.time()
    print(f"section({section}) 응답시간 : {end - start : .5f} sec")


total_end = time.time()
print(f"총 응답시간 : {total_end - total_start : .5f} sec")
