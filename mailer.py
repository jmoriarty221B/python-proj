#!/usr/bin/env python2
import smtplib
body=''
obj=smtplib.SMTP('mmtp.iitk.ac.in',25)
obj.starttls()
print("Enter your user name")
user=raw_input()
print("Enter your password")
password=raw_input()
obj.login(user,password)
print("enter email address of recipient")
recipient=raw_input()
print("enter the subject of mail")
subject=raw_input()
print("enter the body(enter :: wherever u want a new line)")
raw_body=raw_input()
lines=raw_body.split('::')
count=len(lines)
for i in range(0,count,1):
    body=body+lines[i]+'\n'
obj.sendmail(user+'@iitk.ac.in',recipient,'Subject:'+subject+'\n'+body)
obj.quit()


