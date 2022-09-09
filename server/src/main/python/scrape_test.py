from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    DRIVER_PATH = "../../../Include/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    driver.get("https://turo.com/us/en/search?defaultZoomLevel=11&delivery=false&deliveryLocationType=googlePlace&endDate=09%2F14%2F2022&endTime=11%3A00&isMapSearch=false&itemsPerPage=200&latitude=40.78994&location=Salt%20Lake%20City%20International%20Airport%20%28SLC%29%2C%20West%20Terminal%20Drive%2C%20Salt%20Lake%20City%2C%20UT%2C%20USA&locationType=CITY&longitude=-111.97907&pickupType=ALL&placeId=ChIJ6fTXZ4vzUocRGUhZ9SZDH28&sortType=RELEVANCE&startDate=09%2F14%2F2022&startTime=10%3A00&useDefaultMaximumDistance=true")
    with open('page.html', 'wb+') as f:
        f.write(driver.page_source.encode('utf-8'))


    try:
        car_grid = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer-content"]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div'))
        )
        print(car_grid.text)
    finally:
        driver.quit()


    # soup = BeautifulSoup(page.content, "html.parser")
    # results = soup.find(id="content")
    # results = results.find("section", class_="job_list")
    # job_elements = results.find_all("div", class_="job")
    # python_jobs = results.find_all(
    #     "h2",
    #     string=lambda x: "python" in x.lower()
    # )
    # python_job_elements = [
    #     h2_element.parent.parent.parent for h2_element in python_jobs
    # ]
    # for job_element in job_elements:
    #     title_element = job_element.find("h1")
    #     company_element = job_element.find("span", class_="info")
    #     print(title_element.text.strip())
    #     print(company_element.text.strip())
    #     print()
    #
    # print("Number of Jobs: {}".format(len(job_elements)))



if __name__ == "__main__":
    main()
    exit(0)