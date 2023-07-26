import requests
from bs4 import BeautifulSoup

x=[]
y=[]
n=0
url = 'https://invoice.etax.nat.gov.tw/index.html'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
reservoir = soup.select('.font-weight-bold')     # 取得所有 class 為 reservoir 的 tag
for i in reservoir:
    a=""
    if n==8:
        break
    else:
        a+=str(i.get_text())
        x.append(a)
        n+=1
for i in range(len(x)):
    if len(x[i])==8:
        y.append(x[i])
    if len(x[i])==5:
        y.append(x[i]+x[i+1])
print(y)
        
while True:
    f=False
    num=input("發票:")
    if num==y[0]:
        print(num)
        print("中獎!!!!!!!! $1000w")
        f=True
    if num==y[1]:
        print(num)
        print("中獎!!!!!!! $200w")
        f=True
    for i in range(2,5,1):
        nn=0
        for j in range(7,-1,-1):
            if num[j]==y[i][j]:
                nn+=1
            else:
                break
        if nn==3:
            print(num)
            print("中獎! $200")
            f=True
        elif nn==4:
            print(num)
            print("中獎!! $1000")
            f=True
        elif nn==5:
            print(num)
            print("中獎!!! $4000")
            f=True
        elif nn==6:
            print(num)
            print("中獎!!!! $1w")
            f=True
        elif nn==7:
            print(num)
            print("中獎!!!!! $4w")
            f=True
        elif nn==8:
            print(num)
            print("中獎!!!!!! $20w")
            f=True
    if f==False:
        print("沒中獎")