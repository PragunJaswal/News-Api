from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI ,Response ,status ,HTTPException, Request
from fastapi.params import Body          #FOR POST RESPONSE

app = FastAPI()


html_text = requests.get('https://timesofindia.indiatimes.com/?from=mdr').text
soup = BeautifulSoup(html_text,'lxml')
tags = soup.find_all('figcaption')
news=[]
for new in tags:
    news.append(new.text)


@app.get("/")
def root():
    return{"Server is running"}

@app.get("/news")
def root():
    return{f"Latest NEWS are {news}"}