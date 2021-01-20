import requests
from bs4 import BeautifulSoup
import  re
import time
url=[]
for line in open(r"E:\Desktop\spider\urls.txt"):
    url.append(line)
n=0
#url=['https://tech.sina.com.cn/d/f/2019-12-20/doc-iihnzhfz7124619.shtml','https://news.sina.com.cn/w/2019-12-03/doc-iihnzhfz3227337.shtml']
#def do(line):
p = re.compile('[\u4e00-\u9fa5]')
for i in range(len(url)):
    try:
        html = requests.get(url[i].replace('\n',''))
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.content, "html.parser")
        date=soup.find_all('span',{'class':{'date'}})
        title=soup.find_all('h1',{'class':{'main-title'}})
        text=soup.find_all('p')
        if len(date) > 0 and len(title) > 0 and len(text) > 0:
            n = n + 1
            res = re.findall(p, str(text))
            hanzi = ''.join(res).replace('\n','')
            # print(date[0].string)
            # print(title[0].string)
            # print(hanzi)
            with open(r'E:\Desktop\spider\news.txt', 'a') as ff:
                ff.write(date[0].string+' ')
                ff.write(title[0].string + ' ')
                ff.write(hanzi + '\n')
    except:
        None
    print(n)



# if __name__ == '__main__':
#     for line in open(r"E:\Desktop\spider\urls.txt"):
#         print(line)
#         do(url)