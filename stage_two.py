from bs4 import BeautifulSoup, SoupStrainer
import requests
from fake_useragent import UserAgent
ua = UserAgent()
chr = ua.opera

with open('links.txt', 'r') as f:
    array = []
    for line in f:
        array.append(line)
        req = requests.get(line)
        cookie = req.cookies
        print(cookie)
        print(line)
        get_html = requests.get(line, cookies=cookie, headers={"User-Agent": chr})
        print(get_html)
        soup = BeautifulSoup(get_html.content, 'html.parser')
        doc_link = open('stage_2.txt', 'a')
        for link in soup.findAll("a", class_="link-no-decals block brand-link brand-link-padded", href=True):
            doc_link.write("https://www.laptopscreen.com" + link.get('href') + '\n')
            print(link)
        for link in soup.findAll("a", class_="brand-link link-no-decals text-center", href=True):
            doc_link.write("https://www.laptopscreen.com" + link.get('href') + '\n')

            #brand-link link-no-decals text-center

        doc_2_link = open('apple.txt', 'a')
        for link in soup.findAll("a", class_="brand-link link-no-decals block-inline", href=True):
            doc_2_link.write("https://www.laptopscreen.com" + link.get('href') + '\n')
        for link in soup.findAll("a", class_="block brand-link link-no-decals", href=True):
            doc_2_link.write("https://www.laptopscreen.com" + link.get('href') + '\n')

        doc_link.close()
        doc_2_link.close()

        #print(line)

#
#     req = requests.get(lines)
# cookie = req.cookies
# print(cookie)
# get_html = requests.get(url, cookies = cookie, headers = {"User-Agent": chr})
# soup = BeautifulSoup(get_html.content, 'html.parser')
# html_data = soup.prettify
# doc = open("doc2.html", 'w')
# doc.write(soup.prettify())
# doc.close()
# parse_only = SoupStrainer('b')
# local_doc = '/root/PycharmProjects/parser/doc2.html'
# contents = open(local_doc , 'r')
# contents = contents.read()
# soup2 = BeautifulSoup(contents, 'html5lib')
#
# doc_link = open('links_dell.txt', 'a')
# for link in soup.findAll('a', class_="list-item link-no-decals block", href=True):
#     doc_link.write(("https://www.laptopscreen.com"+ link.get('href') + '\n'))
#
