import urllib.request
import re
import urllib3
from bs4 import BeautifulSoup



#x = re.findall(r"\+\d{2}\s?0?\d{10}",s)
        #y = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)


with open('new_list_of_main_html(continue at PA).txt','r') as reading:
    for i in reading.readlines():
        f = urllib.request.urlopen(i)
        s = f.read().decode('utf-8')
        #print(s)
        soup = BeautifulSoup(s)
        #print(soup.prettify())
        with open('list_of_main_html4.txt','a') as writing:
            for link in soup.find_all('a'):
                #print(link.get('href'))
                if len(re.findall(r"(?<!\d)\d{6,10}(?!\d)", link.get('href'))) > 0:
                    writing.write('https://www.chamberofcommerce.com{}\n'.format(link.get('href')))

