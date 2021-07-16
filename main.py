import requests
from bs4 import BeautifulSoup


def getarticle():
    base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    source = requests.get(base_url)
    soup = BeautifulSoup(source.text, 'html.parser')
    all = soup.find_all("p", {"class": "has-dropcap"}) + soup.find_all("p", {"class": "paywall"})
    t = ""
    for elem in all:
        t = t + (elem.text) + "\n"
    return t


if __name__ == '__main__':
    uf = input("Name of file to save the article: ")
    f = open(uf + ".txt", "a")
    f.write(getarticle())
    f.close()
