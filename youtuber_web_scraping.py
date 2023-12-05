from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from datetime import datetime

options = Options()
options.chrome_executable_path = (
    "/Users/chenxingchun/Python_彭彭/web crawler/chromedriver.exe"
)

driver = webdriver.Chrome(options=options)

# 想爬取的youtuber
youtuber = [
    # "@classychoice94",
    # "@thisgroupofpeople",
    # "@crowd1111",
    # "@STRNetworkasia",
    # "@fumeancats",
    # "@crowndu",
    # "@WawaKu",
    # "@ding-ding9707",
    # "@ChefgodFred",
    # "@HowHowEat",
    # "@walkerdad",
    # "@daddy.iam.9999",
    # "@2UncleTsaiPoPo",
    # "@chuchushoeTW",
    # "@liketaitai",
    # "@cheapaoe",
    # "@bluepigeon0810",
    # "@Notorious_3cm",
    # "@laogao",
    # "@alisasa_official",
    # "@ATienDai",
    # "@howfunofficial"
    "@bailingguo",
    "@onion_man",
    "@dannybeeech",
    "@ggukim",
    "@goldfishbrain",
    "@lioumonn",
    "@tessereq",
    "@huzi1989",
    "@BIGSNAKEBALL",
    "@aottergirls",
    "@beautywu",
    "@miihuang711",
    "@theLiuPei",
    "@GinnyDailyTV",
    "@illyandlean",
    "@SanyuanJAPAN2015",
    "@peetagege",
    "@ironbulltingting",
    "@kuan_kuan",
]

# 準備容器
name = []
pageurl = []
intotime = []
looking = []
subscription = []
location = []
otherlink = []
videolink = []

# 開始一個一個爬蟲
for yChannel in youtuber:
    # --- 簡介 部分
    driver.get("https://www.youtube.com/" + str(yChannel) + "/about")
    time.sleep(5)
    # 基本資料
    name.append(driver.find_element(By.ID, "text-container").text)
    pageurl.append("https://www.youtube.com/" + str(yChannel))
    # 訂閱數量
    getSubscription = driver.find_element(By.ID, "subscriber-count").text
    getSubscription = getSubscription.replace(" subscribers", "")
    subscription.append(getSubscription)
    # 開始經營時間
    gettime = driver.find_element(
        By.XPATH, '//div[@id="right-column"]/yt-formatted-string[2]/span[2]'
    ).text
    intotime.append(datetime.strptime(gettime, "%b %d, %Y"))
    # 總觀看次數
    getlooking = driver.find_element(
        By.XPATH, '//div[@id="right-column"]/yt-formatted-string[3]'
    ).text
    getlooking = getlooking.replace(",", "")
    getlooking = getlooking.replace(" views", "")
    looking.append(int(getlooking))
    # description.append(driver.find_element_by_id('description').text)  # 存文案
    location.append(
        driver.find_element(
            By.XPATH, '//div[@id="details-container"]/table/tbody/tr[2]/td[2]'
        ).text
    )  # 存國家位置

    # 其他連結，使用更具體的XPath以獲取每個外部鏈接的容器
    link_containers = driver.find_elements(
        By.XPATH,
        '//div[@id="link-list-container"]//yt-channel-external-link-view-model',
    )

    containar = {}  # 結果整理成dict

    for container in link_containers:
        # 在每個容器中，獲取標題和鏈接
        title = container.find_element(
            By.XPATH, './/span[contains(@class, "yt-core-attributed-string")]'
        ).text
        link_url = container.find_element(By.XPATH, ".//a").get_attribute("href")
        containar[title] = link_url

    otherlink.append(containar)

    # 影片
    driver.get("https://www.youtube.com/" + str(yChannel) + "/videos")
    time.sleep(10)
    # 滾動頁面
    for scroll in range(10):
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(2)
    containar = []
    for link in driver.find_elements(By.ID, "video-title-link"):
        containar.append(link.get_attribute("href"))
    videolink.append(containar)

    dic = {
        "Youtuber頻道名稱": name,
        "頻道網址": pageurl,
        "開始經營時間": intotime,
        "總觀看數": looking,
        "總訂閱數": subscription,
        "國家位置": location,
        "其他連結": otherlink,
        "所有影片連結": videolink,
    }

pd.DataFrame(dic).to_csv("Youtuber_頻道資料_4.csv", encoding="utf-8-sig", index=False)
