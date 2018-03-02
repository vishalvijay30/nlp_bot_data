import requests
from bs4 import BeautifulSoup

# page = requests.get("https://quizlet.com/142680213/high-school-science-bowl-energy-flash-cards/")
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# print(soup.find_all(class_="TermText")[0].text)
# print(soup.find_all(class_="TermText")[1].text)
# # print(soup.find_all(class_="TermText")[1352].text)
# # print(soup.find_all(class_="TermText")[1353].text)
# print(len(soup.find_all(class_="TermText")))

# def scrape_hs_biology_data():
#     biology_url = "https://quizlet.com/138817444/high-school-science-bowl-biology-flash-cards/"
#     biology_data = dict()
#
#     page = requests.get(biology_url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     list = soup.find_all(class_="TermText") # all question answer pairs, even indices are questions, odd indices are answers
#
#     index = 0
#     while index < len(list):
#         biology_data[list[index].text] = list[index + 1].text
#         index += 2
#
#     return biology_data
#
# def scrape_hs_energy_data():
#     energy_url = "https://quizlet.com/142680213/high-school-science-bowl-energy-flash-cards/"
#     energy_data = dict()
#
#     page = requests.get(energy_url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     list = soup.find_all(class_="TermText") # all question answer pairs, even indices are questions, odd indices are answers
#
#     index = 0
#     while index < len(list):
#         energy_data[list[index].text] = list[index + 1].text
#         index += 2
#
#     return energy_data

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