import urllib.request
from bs4 import BeautifulSoup
import urllib.parse


def main():
    with open('final_information.txt', 'a') as w:
        with open('finallist_without_appendages.txt', 'r', encoding='utf-8-sig') as r:
            for i in r.readlines():
                #try:
                f = urllib.request.urlopen(i)
                s = f.read().decode('utf-8')
                soup = BeautifulSoup(s)

                #print(soup)
                try:
                    instructions = soup.find("span", itemprop="name").get_text()
                    w.write(instructions + '~')
                except AttributeError:
                    w.write('Cannot find data ~')
                try:
                    instructions = soup.find("span", itemprop="streetAddress").get_text()
                    w.write(instructions + '~')
                except AttributeError:
                    w.write('Cannot find data ~')
                try:
                    instructions = soup.find("span", itemprop="addressLocality").get_text()
                    w.write(instructions + '~')
                except AttributeError:
                    w.write('Cannot find data ~')
                try:
                    instructions = soup.find("span", itemprop="addressRegion").get_text()
                    w.write(instructions + '~')
                except AttributeError:
                    w.write('Cannot find data ~')
                try:
                    instructions = soup.find("span", itemprop="postalCode").get_text()
                    w.write(instructions + '~')
                except AttributeError:
                    w.write('Cannot find data ~')
                try:
                    instructions = soup.find("span", itemprop="telephone").get_text()
                    w.write(instructions + '~')
                except AttributeError:
                    w.write('Cannot find data ~')
                try:
                    instructions = soup.find("span", itemprop="description").get_text()
                    w.write(instructions +'\n')
                except AttributeError:
                    w.write('Cannot find data\n')
                #except urllib.request.HTTPError:
                    #continue

if __name__ == '__main__':
    main()