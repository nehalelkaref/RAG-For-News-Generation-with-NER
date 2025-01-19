from bs4 import BeautifulSoup
import requests

def scrape_url(url_list):
    articles = []
    for url in url_list:
        response = requests.get(url=url)
        parsed_content = BeautifulSoup(response.content,"lxml")
        articles.append(parsed_content.get_text().strip().strip('\n'))

    return articles