#csv형 리스트에서 숫자형으로 변환할 수 있는 자료만 숫자형으로 변환할 수 있는 프로그램

import csv,re
#파일 읽어오기
def opencsv(filename):
    f=open(filename,'r')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output

#파일 쓰기
def writecsv(filename,the_list):
    with open(filename,'w',newline='') as f:
        a=csv.writer(f,delimiter=',')
        a.writerows(the_list)
#숫자형 변환하기        
def switch(listName):
    for i  in listName:
        for j in i:
            try:
                i[i.index(j)]=float(re.sub(',','',j))
            except:
                pass
    return listName

#함수 호출해서 숫자형으로 변환하기
#writecsv('age2.csv',switch(opencsv('age.csv')))
