from bs4 import BeautifulSoup as Soup
import requests


with open('naatp_urlsfinal.txt', 'a') as w:
    with open('naatp_urls.txt', 'r', encoding='utf-8-sig') as r:
        for i in r.readlines():
            page = requests.get(i, headers={'User-Agent':'test'})
            soup = Soup(page.content)

            a = soup.find_all('a', {'class': ['accredited-', 'accredited-Yes', 'accredited-No']})
            for x in a:
                if x.has_attr('href'):
                    w.write('https://www.naatp.org'+x['href']+'\n')