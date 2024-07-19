from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from time import sleep
from tqdm import tqdm

from .config import DRIVER

firefox_options = Options()
firefox_options.add_argument('--headless')
service = Service(f'{DRIVER}')
driver = webdriver.Firefox(options=firefox_options, service=service)

tqdm_params = {
    "unit_scale": True,
    "miniters": 1,
    "total": 4,
}

def get_yandex_track(url):

    with tqdm(**tqdm_params) as pb:
        driver.get(url)

        ele = driver.find_element(By.XPATH, "/html/body/div[1]/div[22]/div/span")
        ele.click() 
        pb.update()

        sleep(3)

        #get img
        img = driver.find_element(By.CSS_SELECTOR, "img.entity-cover__image.deco-pane")
        imgSrc = img.get_attribute('src')
        pb.update()

        #get track name
        name = driver.find_element(By.XPATH, "/html/body/div[1]/div[16]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/a")
        trackName = name.text
        pb.update()

        #get author 
        author = driver.find_element(By.XPATH, "/html/body/div[1]/div[16]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/span/a")
        authorName = author.text
        pb.update()

        driver.quit()

    return [authorName, trackName, imgSrc]
