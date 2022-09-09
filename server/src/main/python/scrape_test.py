import requests
from bs4 import BeautifulSoup

def main():
    URL = "https://pythonjobs.github.io/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content")
    results = results.find("section", class_="job_list")
    job_elements = results.find_all("div", class_="job")
    # python_jobs = results.find_all(
    #     "h2",
    #     string=lambda x: "python" in x.lower()
    # )
    # python_job_elements = [
    #     h2_element.parent.parent.parent for h2_element in python_jobs
    # ]
    for job_element in job_elements:
        title_element = job_element.find("h1")
        company_element = job_element.find("span", class_="info")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print()

    print("Number of Jobs: {}".format(len(job_elements)))



if __name__ == "__main__":
    main()
    exit(0)