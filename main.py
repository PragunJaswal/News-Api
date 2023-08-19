from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI ,Response ,status ,HTTPException, Request
from fastapi.params import Body          #FOR POST RESPONSE
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://news-api-vaqm.onrender.com/news",
    "http://localhost",
    "http://localhost:8080",
]

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

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)
