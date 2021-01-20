# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

result = []
url = []


# 获得目录下的所有文件
def get_all(cwd):
    get_dir = os.listdir(cwd)
    for i in get_dir:
        sub_dir = os.path.join(cwd, i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            result.append(i)


# 获得文件的所有链接并存入新的文件
def getUrl():
    for file in result:
        with open('/Users/taozehua/PycharmProjects/数据科学/venv/data/' + file, 'r', encoding='GBK') as f:
            for i in f:
                a = i.split('|')[1]
                if a[0] == 'h':
                    url.append(a)
    with open('sina_news.txt', 'a') as f:
        f.writelines(url)


def readAndWrite(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find(attrs={'class': 'main-title'})
    date = soup.find(attrs={'class': 'date'})
    article = soup.find(attrs={'class': 'article'})
    try:
        titleStr = title.text
        dateStr = date.text
        articleStr = article.text.replace("\n", "")
        ret = titleStr + " " + dateStr + " " + articleStr + "\n"
    except:
        return

    with open('sina新冠_news.txt', 'a') as f:
        f.writelines(ret)  # 最后写入的文件


if __name__ == "__main__":
    # get_all('/Users/taozehua/PycharmProjects/数据科学/venv/data')
    # getUrl()
    # readAndWrite('https://news.sina.com.cn/c/2020-03-13/doc-iimxxstf8750983.shtml')
    f = open('sina_news.txt')  # 链接所在文件
    for i in f:
        a = i.replace("\n", "")
        readAndWrite(a)