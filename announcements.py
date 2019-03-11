from flask import Flask, render_template
from flask_ask import Ask, statement, question
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.nitw.ac.in/main/update/Announcements/').read()
soup = bs.BeautifulSoup(source,'lxml')
events = []
for event in soup.find_all('td'):
    events.append(event.text)

print (events)
