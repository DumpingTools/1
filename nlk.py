import os
import requests
import re
import time
from Colors import colors
import subprocess
from bs4 import BeautifulSoup
os.system("clear")
name = input("Insert name: ")
print("Checking name: \033[1;31;40m{}\033[0;37;40m on Twitter..".format(name))
colors.red("\nAll URLs relating to the name will have 'url' in front of it.")
time.sleep(3)
r = requests.get("https://www.google.com/search?sxsrf=ACYBGNRWIXf790eaUorvYtTl35Ry5y8Kgw%3A1579863195288&ei=m8wqXtWREenl_Qbi07bQBw&q=inurl%3ATwitter+intitle%3A" + name + "&oq=inurl%3ATwitter+intitle%3A" +name+"&gs_l=mobile-gws-wiz-serp.12..0i71l5.0.0..24745...0.2..0.0.0.......0.iPKuh55BZWE")
soup = BeautifulSoup(r.content, 'html5lib')
f = open("URL.txt", "w+")
for site in soup.find_all('a'):
    f.write(str("\n" + site['href']))
with open("URL.txt", "r") as f:
    for search in f:
        colors.green(f.readline())
        time.sleep(2)
colors.red("\nURLs are stored in URL.txt")
time.sleep(4)
os.system("clear")
print("Checking name: \033[1;31;40m{}\033[0;37;40m on Facebook..".format(name))
r = requests.get("https://www.google.com/search?sxsrf=ACYBGNRWIXf790eaUorvYtTl35Ry5y8Kgw%3A1579863195288&ei=m8wqXtWREenl_Qbi07bQBw&q=inurl%3AFacebook+intitle%3A" + name + "&oq=inurl%3AFacebook+intitle%3A" +name+"&gs_l=mobile-gws-wiz-serp.12..0i71l5.0.0..24745...0.2..0.0.0.......0.iPKuh55BZWE")
soup = BeautifulSoup(r.content, 'html5lib')
f = open("URL.txt", "w+")
for site in soup.find_all('a'):
    f.write(str("\n" + site['href']))
with open("URL.txt", "r") as f:
    for search in f:
        colors.green(f.readline())
        time.sleep(2)
colors.red("\nURLs are stored in URL.txt")
time.sleep(4)
os.system("clear")

