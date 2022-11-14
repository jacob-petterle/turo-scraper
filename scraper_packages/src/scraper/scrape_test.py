import re
import time
from typing import Type

from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

def main():
    driver = build_driver()

    attempts = 0
    while True:
        driver.get("https://turo.com/us/en/search?defaultZoomLevel=11&delivery=false&deliveryLocationType=googlePlace&endDate=09%2F14%2F2022&endTime=11%3A00&isMapSearch=false&itemsPerPage=200&latitude=40.78994&location=Salt%20Lake%20City%20International%20Airport%20%28SLC%29%2C%20West%20Terminal%20Drive%2C%20Salt%20Lake%20City%2C%20UT%2C%20USA&locationType=CITY&longitude=-111.97907&pickupType=ALL&placeId=ChIJ6fTXZ4vzUocRGUhZ9SZDH28&sortType=RELEVANCE&startDate=09%2F14%2F2022&startTime=10%3A00&useDefaultMaximumDistance=true")
        car_text_list: Type["Driver"] = scroll_element_search(driver)
        if car_text_list:
            break
        if attempts >= 3:
            print("Failed to load page")
            return
        attempts += 1

    car_set = set()
    count = 0
    for car_text in car_text_list:
        car_text_lines = car_text.splitlines()
        if re.match(r'.*total', car_text_lines[-1]):
            car_text_lines = car_text_lines[:-1]
        car_text = "".join(car_text_lines)
        if car_text not in car_set:
            car_set.add(car_text)
            print(car_text, end="\n\n")
        else:
            count += 1

    print("Done")
    print("Number of Listings: {}".format(len(car_set)))
    print("Duplicate elements: {}".format(count))
    time.sleep(1000)
    driver.quit()

def build_driver():
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    return uc.Chrome(options=options)


def scroll_element_search(driver, scroll_count=10000):
    car_text_list = []
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")


    while True:
        # Scroll down to bottom
        curr_element = find_element_xpath(driver, '//*[@id="pageContainer-content"]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div')
        if not curr_element:
            print("Page Load error")
            return None


        car_element_list = curr_element.find_elements(By.CLASS_NAME, 'searchResult-gridItem')
        for car_element in car_element_list:
            car_text_list.append(car_element.text)

        if scroll_count == 0:
            break
        page = find_element_xpath(driver, "/html/body")
        page.send_keys(Keys.PAGE_DOWN)

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

        last_height = new_height
        scroll_count -= 1

    return car_text_list

def focus_element_xpath(driver, xpath):
    element = find_element_xpath(driver, xpath)
    element.click()
    return None

def find_element_xpath(driver, xpath):
    try:
        car_grid = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except:
        return None
    return car_grid



if __name__ == "__main__":
    main()
    exit(0)