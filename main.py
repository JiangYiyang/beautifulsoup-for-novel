# -*- encoding=UTF-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

fp = open("test.txt","a",encoding='utf-8')
html = urlopen("https://www.mywenxue.com/xiaoshuo/113/113682/45438760.htm").read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, features='lxml')
mydivs = soup.find("div", {"class": "txt"})
txt = mydivs.get_text()
fp.write(txt)
fp.write('\n')
# 一轮已经完了，开始读取下一个网页的地址
nexthref = soup.find("div", {"class": "r"})
for k in nexthref.find_all('a'):
    decide = k['href']
    html = urlopen("https://www.mywenxue.com" + k['href'] + "l").read().decode('utf-8')  # 查a标签的href值
while decide != "/xiaoshuo/113/113682/Index.htm" :
    # print(nexthref)
    soup = BeautifulSoup(html, features='lxml')
    mydivs = soup.find("div", {"class": "txt"})
    txt = mydivs.get_text()
    fp.write(txt)
    fp.write('\n')
    nexthref = soup.find("div", {"class": "r"})
    print(nexthref)
    for k in nexthref.find_all('a'):
        decide = k['href']
        html  =  urlopen("https://www.mywenxue.com"+ k['href']+"l").read().decode('utf-8')#查a标签的href值
        # print(html)

fp.close()
# txt = mydivs.replace("<br/>","")
# print(txt)
# print(mydivs,'\n')
# mydivs.translate(str.maketrans('', '', string.punctuation))
# mydivs.translate(str.maketrans('','','b'))
# print(mydivs.replace('<br/>', ''))
# lis = mydivs.select("a[href*=theater.aspx]")
# for x in lis:
#     theater = x.find('h2', class_='txt')
#     print(theater.text)
# [script.extract() for script in soup.findAll('script')]
# [style.extract() for style in soup.findAll('style')]
# soup.prettify()
# reg1 = soup.compile("<[^>]*>")
# content = reg1.sub('',soup.prettify())

# print(content)
