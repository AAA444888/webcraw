import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

def submit():
    x=[]
    y=[]
    date=[]
    a1=onthchoosenx.get()
    a2=onthchooseny.get()
    a3=sd
    a4=onthchoosen1.get()
    a5=onthchoosen2.get()
    a6=onthchoosen3.get()
    for i in range(len(a1)):
        x.append(a1[i])
    for i in range(len(a2)):
        y.append(a2[i])
    
    a="https://www.railway.gov.tw/tra-tip-web/tip"
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(options=option)
    driver.get(a)
    time.sleep(5)
    strr ="/html/body/div[6]/div[4]/div/div[1]/form/div[1]/div[2]/input"
    driver.find_element(By.XPATH,strr).send_keys(x)
    time.sleep(1)
    strr ="/html/body/div[6]/div[4]/div/div[1]/form/div[3]/div[2]/input"
    driver.find_element(By.XPATH,strr).send_keys(y)
    time.sleep(1)
    if a3!="":
        for i in range(len(a3)):
            date.append(a3[i])
        strr ="/html/body/div[6]/div[4]/div/div[1]/form/div[4]/div[2]/input"
        element=driver.find_element(By.XPATH,strr)
        element.clear()
        driver.find_element(By.XPATH,strr).send_keys(date)
        time.sleep(1)
    if a4!="":
        a4a=20*int(a4[0])+2*int(a4[1])
        if a4[3]=='0':
            a4a+=1
        else:
            a4a+=2
        strr =f"/html/body/div[6]/div[4]/div/div[1]/form/div[5]/div[3]/select/option[{a4a}]"
        driver.find_element(By.XPATH,strr).click()
        time.sleep(1)
    if a5!="":
        a5a=20*int(a5[0])+2*int(a5[1])
        if a5[3]=='0':
            a5a+=1
        else:
            a5a+=2
        strr =f"/html/body/div[6]/div[4]/div/div[1]/form/div[5]/div[4]/select/option[{a5a}]"
        driver.find_element(By.XPATH,strr).click()
        time.sleep(1)
    strr ="/html/body/div[6]/div[4]/div/div[1]/form/div[6]/input"
    driver.find_element(By.XPATH,strr).click()
    time.sleep(1)
    if a6=="騰雲座艙":
        strr ="/html/body/div[3]/div[3]/div/div/ul/li[2]/a"
        driver.find_element(By.XPATH,strr).click()
        time.sleep(1)
    elif a6=="自由座":
        strr ="/html/body/div[3]/div[3]/div/div/ul/li[3]/a"
        driver.find_element(By.XPATH,strr).click()
        time.sleep(1)
        
    table=driver.find_element(By.TAG_NAME,"table")
    rows=table.find_elements(By.CLASS_NAME,"trip-column")
    z=[]
    for row in rows:
        t=row.find_elements(By.TAG_NAME,"td")
        z.append(tuple([t[0].text,t[1].text,t[2].text,t[3].text,t[4].text,t[6].text,t[7].text,t[8].text]))
    columns = ("車種車次","出發時間", "抵達時間",'行駛時間','經由','全票','孩童票','敬老票')
    headers =("車種車次","出發時間", "抵達時間",'行駛時間','經由','全票','孩童票','敬老票')
    widthes = (300,80,80,80,80,80,80,80)
    tv = ttk.Treeview(wnd, show="headings",height=14 ,columns=columns)
    for (column, header, width) in zip(columns, headers, widthes):
        tv.column(column, width=width, anchor="w")
        tv.heading(column, text=header, anchor="w")
    tv.place(relx=0.5,rely=0.1,anchor= 'n')
    for i, v in enumerate(z):
            print(i,v)
            tv.insert('', i,values=v)

wnd = tk.Tk()
wnd.geometry("900x400")
wnd.title("台鐵時刻表查詢器")

xt = tk.Label(wnd,text='請輸入或選擇出發站站名:')
xt.place(relx=0.3,rely=0.1,anchor='n')
xx = tk.StringVar()
onthchoosenx = ttk.Combobox(wnd, width = 17, textvariable = xx)
onthchoosenx['values'] = ('基隆', '七堵','板橋','樹林','瑞芳','南港','松山','臺北','萬華','桃園','中壢','新竹','竹南','苗栗','豐原','臺中','彰化','員林','斗六','嘉義','新營','臺南','岡山','新左營','高雄','屏東','潮州','臺東','玉里','花蓮','蘇澳新','宜蘭')
onthchoosenx.place(relx=0.7,rely=0.1,anchor='n')

yt = tk.Label(wnd,text='請輸入或選擇目的站站名:')
yt.place(relx=0.3,rely=0.2,anchor='n')
yy = tk.StringVar()
onthchooseny = ttk.Combobox(wnd, width = 17, textvariable = yy)
onthchooseny['values'] = ('基隆', '七堵','板橋','樹林','瑞芳','南港','松山','臺北','萬華','桃園','中壢','新竹','竹南','苗栗','豐原','臺中','彰化','員林','斗六','嘉義','新營','臺南','岡山','新左營','高雄','屏東','潮州','臺東','玉里','花蓮','蘇澳新','宜蘭')
onthchooseny.place(relx=0.7,rely=0.2,anchor='n')

wt = tk.Label(wnd,text='*無法查詢已經過的時間段*')
wt.place(relx=0.3,rely=0.3,anchor='n')

tt = tk.Label(wnd,text='請選擇欲查詢的日期:')
tt.place(relx=0.3,rely=0.35,anchor='n')

now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
date_entry = DateEntry(wnd, width=12, year=int(now.strftime('%Y')), month=int(now.strftime('%m')), day=int(now.strftime('%d')), background='darkblue',foreground='white', borderwidth=2)
date_entry.place(relx=0.7,rely=0.35,anchor='n')
selected_date = str(date_entry.get_date())
sd=""
for i in range(len(selected_date)):
    if selected_date[i]!='-':
        sd+=selected_date[i]

tst = tk.Label(wnd,text='請輸入欲出發的起始時間段:')
tst.place(relx=0.3,rely=0.45,anchor='n')
ts = tk.StringVar()
onthchoosen1 = ttk.Combobox(wnd, width = 17, textvariable = ts)
onthchoosen1['values'] = ('00:00', '00:30','01:00','01:30','02:00','02:30','03:00','03:30','04:00','04:30','05:00','05:30','06:00','06:30','07:00','07:30','08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00','22:30','23:00','23:30','23:59')
onthchoosen1.place(relx=0.7,rely=0.45,anchor='n')

tet = tk.Label(wnd,text='請輸入欲出發的最晚時間段:')
tet.place(relx=0.3,rely=0.55,anchor='n')
te = tk.StringVar()
onthchoosen2 = ttk.Combobox(wnd, width = 17, textvariable = te)
onthchoosen2['values'] = ('00:00', '00:30','01:00','01:30','02:00','02:30','03:00','03:30','04:00','04:30','05:00','05:30','06:00','06:30','07:00','07:30','08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00','22:30','23:00','23:30','23:59')
onthchoosen2.place(relx=0.7,rely=0.55,anchor='n')

st = tk.Label(wnd,text='請輸入欲搭乘的座位種類:')
st.place(relx=0.3,rely=0.65,anchor='n')
n = tk.StringVar()
onthchoosen3 = ttk.Combobox(wnd, width = 17, textvariable = n)
onthchoosen3['values'] = ('一般', '騰雲座艙','自由座')
onthchoosen3.place(relx=0.7,rely=0.65,anchor='n')

button = tk.Button(wnd,text="submit",underline=-1,command=submit)
button.place(relx=0.5,rely=0.75,anchor='n')
button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
button.place(relx=0.5,rely=0.9,anchor='n')

wnd.mainloop()

