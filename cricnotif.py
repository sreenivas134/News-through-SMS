#!/usr/bin/env python2

import requests
from bs4 import BeautifulSoup
import pynotify
from getpass import getpass
from time import sleep
from sendsms import sendsms
"""def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return"""

url = "https://news.google.co.in/"
username = raw_input("Enter Username: ")
password = getpass()
number = raw_input("Enter Mobile number: ")
while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)

    soup = BeautifulSoup(r.text)
    data = soup.find_all("div", class_='esc-lead-snippet-wrapper')
    for head in data[0:10]:
    	score = head.text[:128]
    	score=score+'...\n -sreenu'
    	#sendmessage('News', score)
    	sendsms(username, password, score, number)
    	sleep(8)
