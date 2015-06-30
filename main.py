__author__ = "Shreymanik"
import requests
from bs4 import BeautifulSoup
def find_pages(k):
    maxpages=1
    url='http://codeforces.com/submissions/'+k
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text)
    for link in soup.findAll('span',{'class' : 'page-index'}):
            maxpages=max(maxpages,int(link.string))
    return maxpages
def crawl(max_page,k):
    page=1
    x=[]
    ct1=0
    ct2=0
    ct3=0
    ct4=0
    ct5=0
    ct6=0
    ct7=0
    while page<= max_page:
        url='http://codeforces.com/submissions/'+k+'/page/'+ str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        for link in soup.findAll('span',{'submissionverdict' : 'OK'}):
            ct1+=1
        for link in soup.findAll('span',{'submissionverdict' : 'WRONG_ANSWER'}):
            ct2+=1
        for link in soup.findAll('span',{'submissionverdict' : 'TIME_LIMIT_EXCEEDED'}):
            ct3+=1
        for link in soup.findAll('span',{'submissionverdict' : 'RUNTIME_ERROR'}):
            ct4+=1
        for link in soup.findAll('span',{'submissionverdict' : 'CHALLENGED'}):
            ct5+=1
        for link in soup.findAll('span',{'submissionverdict' : 'COMPILATION_ERROR'}):
            ct6+=1
        for link in soup.findAll('span',{'submissionverdict' : 'MEMORY_LIMIT_EXCEEDED'}):
            ct7+=1
        page+=1
    x.append(ct1)
    x.append(ct2)
    x.append(ct3)
    x.append(ct4)
    x.append(ct5)
    x.append(ct6)
    x.append(ct7)
    return x
c='Y'
while c=='Y':
    s=input()
    page=find_pages(s)
    list=crawl(page,s)
    print('CODEFORCES DATABASE')
    print('\n')
    print('User Name : ',s)
    print('Total Submissions : ' , sum(list))
    print('Number Of Accepted Solutions : ' , list[0])
    print('Number Of Wrong Answers : ' , list[1])
    print('Number Of TLEs : ' , list[2])
    print('Number Of Run Time Errors : ' , list[3])
    print('Number Of Hacked Solution : ' , list[4])
    print('Number Of Compilation Errors : ',list[5])
    print('Number Of Memory Limit Exceeded Solution : ' ,list[6])
    c=input()



