#!/usr/bin/env python2
import webbrowser,requests,bs4,os,subprocess,time
block=''
while(1):
    
    time.sleep(1)
    try:
        response=requests.get("http://timesofindia.indiatimes.com/")
    except:
	print("exception")
        continue
# print dir(requests)
    data=bs4.BeautifulSoup(response.text,"lxml")
    featured=data.select("#featuredstory h2 a")
    news=featured[0].getText()
    link=featured[0].get("href")
    if block==0:
        a=5
    else:
        block=news
        subprocess.Popen(['notify-send',news])
	print(news)
