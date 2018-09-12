import urllib.request
import re
import urllib3
from bs4 import BeautifulSoup


with open('final_information.txt', 'w') as w:
    with open('finallist_without_appendages.txt', 'r') as r:
        for i in r.readlines():

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
              
                
''' 
                
f = urllib.request.urlopen('https://www.chamberofcommerce.com/stamford-ct/25930829-compu-joy')
s = f.read().decode('utf-8')
soup = BeautifulSoup(s)

#print(soup)
try:
    instructions = soup.find("span", itemprop="name").get_text()
    print(instructions)
except AttributeError:
    print('Cannot find data')
try:
    instructions = soup.find("span", itemprop="streetAddress").get_text()
    print(instructions)
except AttributeError:
    print('Cannot find data')
try:
    instructions = soup.find("span", itemprop="addressLocality").get_text()
    print(instructions)
except AttributeError:
    print('Cannot find data')
try:
    instructions = soup.find("span", itemprop="addressRegion").get_text()
    print(instructions)
except AttributeError:
    print('Cannot find data')
try:
    instructions = soup.find("span", itemprop="postalCode").get_text()
    print(instructions)
except AttributeError:
    print('Cannot find data')
try:
    instructions = soup.find("span", itemprop="telephone").get_text()
    print(instructions)
except AttributeError:
    print('Cannot find data')
try:
    instructions = soup.find("span", itemprop="description").get_text()
    print(instructions)
except AttributeError:
    print('Cannot find data')

''' 