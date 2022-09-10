import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

def main():
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1200")
    driver = uc.Chrome(options=options)


    driver.get("https://turo.com/us/en/search?defaultZoomLevel=11&delivery=false&deliveryLocationType=googlePlace&endDate=09%2F14%2F2022&endTime=11%3A00&isMapSearch=false&itemsPerPage=200&latitude=40.78994&location=Salt%20Lake%20City%20International%20Airport%20%28SLC%29%2C%20West%20Terminal%20Drive%2C%20Salt%20Lake%20City%2C%20UT%2C%20USA&locationType=CITY&longitude=-111.97907&pickupType=ALL&placeId=ChIJ6fTXZ4vzUocRGUhZ9SZDH28&sortType=RELEVANCE&startDate=09%2F14%2F2022&startTime=10%3A00&useDefaultMaximumDistance=true")
    grid_element = scroll_element_search(driver)
    attempts = 1
    while grid_element is None and attempts < 3:
        driver.get("https://turo.com/us/en/search?defaultZoomLevel=11&delivery=false&deliveryLocationType=googlePlace&endDate=09%2F14%2F2022&endTime=11%3A00&isMapSearch=false&itemsPerPage=200&latitude=40.78994&location=Salt%20Lake%20City%20International%20Airport%20%28SLC%29%2C%20West%20Terminal%20Drive%2C%20Salt%20Lake%20City%2C%20UT%2C%20USA&locationType=CITY&longitude=-111.97907&pickupType=ALL&placeId=ChIJ6fTXZ4vzUocRGUhZ9SZDH28&sortType=RELEVANCE&startDate=09%2F14%2F2022&startTime=10%3A00&useDefaultMaximumDistance=true")
        grid_element = scroll_element_search(driver)
        attempts += 1

    elements = [element.find_elements(By.CLASS_NAME, 'searchResult-gridItem') for element in grid_element]
    print(elements)
    car_set = set()
    vehicles = []
    for item in elements:
        for car in item:
            if car.text not in car_set:
                car_set.add(car.text)
                vehicles.append(car)
                print(car.text, end="\n"*4)
    print("Done")
    driver.quit()


def scroll_element_search(driver):
    element_list = []
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        element_list.append(find_element(driver))
        print(element_list[0].text, end="\n"*4)
        if not element_list[-1]:
            print("Page Load error")
            return None
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            return element_list
        last_height = new_height

def find_element(driver):
    try:
        car_grid = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer-content"]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div'))
        )
    except:
        return None
    return car_grid


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