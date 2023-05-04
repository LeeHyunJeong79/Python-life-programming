import os,re
import urllib.request as ur
from bs4 import BeautifulSoup as bs
url='https://news.daum.net/'
soup=bs(ur.urlopen(url).read(),'html.parser')
f=open('article_total2.txt','w',encoding='utf8')
#print(soup)
for i in soup.find_all('div',{'class':'item_issue'}):
    try:
        f.write(i.text+'\n') #제목을 추출해 파일에 기록
        f.write(i.find_all('a')[0].get('href')+'\n') #url주소를 추출해 파일에 기록

        soup2=bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')
        #url 주소에 해당하는 웹문서를 열어 새 뷰티불수프 객체로 저장
        
        for j in soup2.find_all('p'):
            f.write(j.text+'\n')
    except :
        pass
    
f.close()
    