from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import re
from bs4 import BeautifulSoup as bs
import os
import django
import html as hl

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlingNews.settings")

django.setup()
from joongangIlbo.models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    CultureNews,
    SportsNews,
    LifeNews
)

total_start = time.time()

sections = {
    "politics": PoliticsNews,  # 정치
    "money": EconomyNews,  # 경제
    "world": InternationalNews,  # 국제
    "society": SocietyNews,  # 사회
    "culture": CultureNews,  #문화
    "sports": SportsNews,  # 스포츠
    'lifestyle':LifeNews  # 재난
}

# Function to collect news titles
def collect_news_urls(section):
    news_urls = []
    response = requests.get(
        f"https://www.joongang.co.kr/{section}"
    )
    soup = bs(response.text, "html.parser")
    for a in soup.select("#story_list > li > div > h2"):
        news_urls.append(a.find("a")["href"])

    return news_urls


def date_to_integer(target_date):
    # target_date = target_date.split()
    # date = target_date[0].replace(".", "")
    # time = target_date[1].split(":")
    # result_date = date + time[0] + time[1]
    result_date = target_date

    return result_date

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def crawling_article(url, News):
    driver = webdriver.Chrome(executable_path="/root/CrawlingApi/chromedriver-linux64/chromedriver", options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    # element = wait.until((EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/section/article/header/div[2]/div/p[1]/time'))))
    time.sleep(10)
    soup = bs(driver.page_source, 'html.parser')
    # response = requests.get(url)

    # html_text = response.text

    # html = bs(html_text, "lxml")

    article_title = soup.select_one("#container > section > article > header > h1").get_text()
    article_title = article_title.replace("...", "... ")
    article_title = article_title.replace("...  ", "... ")
    article_title = hl.unescape(article_title)

    article_time = (
        soup.select_one(
            '#container > section > article > header > div.datetime > div > p:nth-child(1) > time'
        )
        .get_text()
    )
    # print(article_time)

    article_content = soup.select_one("#article_body")

    try:
        article_content.find('a', {'class':'btn_photo_viewer'}).decompose()
    except:
        pass
  
    try:
        article_content.find('div', {'class':'ad_wrap lg_hidden ad_article'}).decompose()
    except:
        pass
  
    try:
        article_content.find('div', {'class':'ad_wrap ad_wide sm_hidden ad_article'}).decompose()
    except:
        pass
  
    try:
        article_content.find('div', {'class':'ad_wrap fixed_right sm_hidden position_fi'}).decompose()
    except:
        pass
  

    article_content = str(article_content)
    article_content = article_content.replace("<br/>", "\n")
    article_content = article_content.replace("<b>", "")
    article_content = article_content.replace("</b>", "")
    article_content = article_content.replace("\r\n", "\n")
    article_content = re.sub("<(.|\n|\r)+?>", "\n", article_content).strip()
    article_content = re.sub(" +", " ", article_content)
    article_content = re.sub("\n {1,}", "\n", article_content)
    article_content = re.sub("\n{2,}", "\n\n", article_content)
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

    driver.quit()

for section, News in sections.items():
    start = time.time()
    all_news_urls = []
    all_news_urls += collect_news_urls(section)

    for url in all_news_urls:
        
        try:
            crawling_article(url, News)
        except Exception:
            print(Exception)

    end = time.time()
    print(f"section({str(News)}) 응답시간 : {end - start : .5f} sec")


total_end = time.time()
print(f"총 응답시간 : {total_end - total_start : .5f} sec")
