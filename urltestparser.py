from bs4 import BeautifulSoup as Soup
import requests


with open('final_information.txt', 'a') as a:
    with open('finallist_without_appendages.txt', 'r', encoding='utf-8-sig') as r:

        for i in r.readlines():
            page = requests.get(i.strip(), headers={'User-Agent':'test'})
            soup = Soup(page.content)

            #print(soup)
            a = soup.find('span', itemprop='name')
            b = soup.find('span', itemprop='streetAddress')
            c = soup.find('span', itemprop='addressLocality')
            d = soup.find('span', itemprop='addressRegion')
            e = soup.find('span', itemprop='postalCode')
            f = soup.find('span', itemprop='telephone')
            g = soup.find('span', itemprop='description')

            if a == None:
                w.write('Cannot find data ~')
            else:
                w.write(a.get_text() + '~')
            if b == None:
                w.write('Cannot find data ~')
            else:
                w.write(b.get_text() + '~')
            if c == None:
                w.write('Cannot find data ~')
            else:
                w.write(c.get_text() + '~')
            if d == None:
                w.write('Cannot find data ~')
            else:
                w.write(d.get_text() + '~')
            if e == None:
                w.write('Cannot find data ~')
            else:
                w.write(e.get_text() + '~')
            if f == None:
                w.write('Cannot find data ~')
            else:
                w.write(f.get_text() + '~')
            if g == None:
                w.write('Cannot find data\n')
            else:
                w.write(g.get_text() + '\n')
