import sys
from bs4 import BeautifulSoup
import requests
import urllib3
import re
import pymysql

baseurl = "https://baseball-reference.com/players/#/##.shtml"
db = pymysql.connect("localhost", "root", "", "Baseball")

cur = db.cursor()
cur.execute("SELECT count(DISTINCT playerid) FROM Appearances")
lines = cur.fetchall()[0][0]
line = 0
cur.execute("SELECT DISTINCT playerid FROM Appearances")
data = cur.fetchall()
cur.close()

def scrapePlayerImg(playerid):
    url = re.sub(r"##", playerid, baseurl)
    url = re.sub(r"#", playerid[0], url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html5lib")

    for item in soup.find_all("div", class_="media-item", limit=1):
        for img in item.find_all("img", limit=1):
            return img["src"]

def printProgress(iteration, total, prefix='', suffix='', decimals=1, length=64, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    if iteration == total:
        print()

try:
    out = open("resources/playerImages.csv", 'w')

    for pid in data:
        pid = pid[0].strip()
        s = pid + ','
        i = scrapePlayerImg(pid)
        s += i if i != None else ''
        s += '\n'
        out.write(s)
        line += 1
        sfx = '(' + str(line) + '/' + str(lines) + ')'
        printProgress(line, lines, prefix="Searching players...", suffix=sfx)
except KeyboardInterrupt:
    print("program interrupted: aborting")
    sys.exit(0)
except:
    print("failed to open file...")
    sys.exit(-1)
finally:
    out.close()
