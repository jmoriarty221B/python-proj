#!/usr/bin/env python2
import pprint,bs4,sys,os,requests,time
while(1):
    time.sleep(1)
    try:
        data=requests.get("http://apod.nasa.gov/apod/astropix.html")
    except:
        print("Network Error")
        continue
    page=bs4.BeautifulSoup(data.text,"lxml")
    content=page.select("body p a img")
    des=page.select("body p")
    explanation=des[2].getText()
    explanation=explanation.replace("\n", " ")
    link=content[0].get('src')
    # print(link)
    if len(sys.argv)==2:
        description=sys.argv[1]
        if(description=="describe" or description=="-d"):
            pprint.pprint(explanation)
            break
    try:
        result=requests.get("http://apod.nasa.gov/apod/"+link)
    except:
        continue
    image=open(os.path.join('/home','abhinav','python_proj','apod','apod'),'wb')
    for bits in result.iter_content(100000):
        image.write(bits)
    image.close()
    break

        
