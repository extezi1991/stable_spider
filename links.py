from bs4 import BeautifulSoup, SoupStrainer
import requests
from fake_useragent import UserAgent
url = input('Put your url here:   ')
ua = UserAgent()
chr = ua.chrome
req = requests.get(url)
cookie = req.cookies
print(cookie)
get_html = requests.get(url, cookies = cookie, headers = {"User-Agent": chr})
soup = BeautifulSoup(get_html.content, 'html.parser')
html_data = soup.prettify
doc = open("doc2.html", 'w')
doc.write(soup.prettify())
doc.close()
parse_only = SoupStrainer('b')
local_doc = 'doc2.html'
contents = open(local_doc , 'r')
contents = contents.read()
soup2 = BeautifulSoup(contents, 'html5lib')

doc_link = open('links.txt', 'a')
for link in soup.findAll('a', class_="list-item link-no-decals block", href=True):
    doc_link.write(("https://www.laptopscreen.com"+ link.get('href') + '\n'))
for link in soup.findAll('a', class_="list-item link-no-decals block", href=True):
    doc_link.write(("https://www.laptopscreen.com"+ link.get('href') + '\n'))



# image_links = soup2.find_all('a', class_='block brand-link link-no-decals', href=True)
# for link in soup2.findAll('a', class_='block brand-link link-no-decals'):
#     doc_link.write("https://www.laptopscreen.com/" + link.get('href') + '\n')
#
#
# for link2 in soup2.findAll('a', class_="brand-link link-no-decals block-inline"):
#     doc_link.write("https://www.laptopscreen.com/" + link2.get('href') + '\n')
#
#
#
# for link2 in soup2.findAll('a', class_="link-no-decals block brand-link brand-link-padded"):
#     doc_link.write("https://www.laptopscreen.com/" + link2.get('href') + '\n')


