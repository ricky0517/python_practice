import requests
from bs4 import BeautifulSoup

URL = "https://dallas.craigslist.org/search/ats#search=1~list~0~0"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="search-results-page-1")
result_element = results.find_all("li", class_="cl-search-result cl-search-view-mode-list")

for result in result_element:
    title = result.find("span", class_="label")
    print(title.text.strip)