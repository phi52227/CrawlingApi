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

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlingNews.settings")

django.setup()
from news.models import News

start = time.time()

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)

driver.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100")

wait = WebDriverWait(driver, 3)
time.sleep(0.5)


# Function to collect news titles
def collect_news_urls():
    news_urls = []
    for num1 in range(1, 5):
        for num2 in range(1, 6):
            try:
                element = wait.until(
                    (
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                f'//*[@id="section_body"]/ul[{num1}]/li[{num2}]/dl/dt[2]/a',
                            )
                        )
                    )
                )
                url_element = driver.find_element(
                    By.XPATH,
                    f'//*[@id="section_body"]/ul[{num1}]/li[{num2}]/dl/dt[2]/a',
                )
                url = url_element.get_attribute("href")
                news_urls.append(url)
            except Exception as e:
                # print(f"Error: {e}")
                print(f"{num1} {num2} 불러오기 실패")
    return news_urls


# Collect news titles before and after clicking the pagination link
all_news_urls = []
all_news_urls += collect_news_urls()

driver.find_element(By.CSS_SELECTOR, "#paging > a:nth-child(2)").click()
time.sleep(0.5)

# Collect news titles again after clicking the pagination link
all_news_urls += collect_news_urls()

driver.quit()


def date_to_integer(target_date):
    target_date = target_date.split()
    date = target_date[0][:-1].replace(".", "")
    time = target_date[2].split(":")
    if target_date[1] == "오후":
        if time[0] == "12":
            time[0] = "12"
        else:
            time[0] = str(int(time[0]) + 12)
    time = "".join(time)
    result_date = date + time

    return result_date


def crawling_article(url, index):
    response = requests.get(url)

    html_text = response.text

    html = bs(html_text, "html.parser")

    article_title = html.select_one("#title_area > span").get_text()

    article_time = html.select_one(
        "#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span"
    ).get_text()

    article_content = str(html.select_one("#dic_area"))
    article_content = article_content.replace("<br/>", "\n")
    article_content = re.sub("<.+?>", "", article_content).strip()
    article_content = re.sub(" +", " ", article_content)
    article_content = re.sub("\n{2,}", "\n\n", article_content)
    article_content = article_content.replace("\n ", "\n")

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


article_list = []

for index, url in enumerate(all_news_urls):
    crawling_article(url, index)

end = time.time()
print(f"{end - start : .5f} sec")
