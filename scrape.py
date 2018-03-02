import requests
from bs4 import BeautifulSoup

# question answer pairs are such that even indices contain questions and odd indices contain answers
def scrape_data_evenq_odda(url):
    data = dict()

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list = soup.find_all(class_="TermText")

    index = 0
    while index < len(list):
        data[list[index].text] = list[index + 1].text
        index += 2

    return data

# question answer pairs are such that odd indices contain questions and even indices contain answers
def scrape_data_oddq_evena(url):
    data = dict()

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list = soup.find_all(class_="TermText")

    index = 0
    while index < len(list):
        data[list[index + 1].text] = list[index].text
        index += 2

    return data