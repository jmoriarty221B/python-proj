#!/usr/bin/env python3
import webbrowser,bs4,sys,os,requests
for i in range(1525,0,-1):
    data=requests.get("http://www.xkcd.com/"+str(i)+"/")
    try:
        data.raise_for_status()
    except:
        continue
    else:
        page=bs4.BeautifulSoup(data.text)
        comic=page.select("#comic img")
        try:
            img=comic[0].get("src")
        except:
            continue
        print("Downloading " + str(i) + "....")
        try:
            result=requests.get("http:"+img)
        except:
            continue
        try:
            result.raise_for_status()
        except:
            continue
        else:
            image=open(os.path.join('xkcd',str(i)),'wb')
            for bits in result.iter_content(100000):
                image.write(bits)
            image.close()






