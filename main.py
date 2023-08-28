from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
origins = [
    "https://news-api-vaqm.onrender.com/news",
    "http://localhost",
    "http://localhost:8080",
    "https://monumental-palmier-ac3734.netlify.app/"
]


def scrape_news(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    tags = soup.find_all('h2')
    tit = []
    news = []
    for new in tags:
        title_tag = new.find('a')
        if title_tag:
            title = title_tag.text
            link = title_tag['href']
            tit.append(title)
            news.append(link)
            
    des = soup.find_all('p')
    desc = []
    for des in des:
        desc.append(des.text)

    divlink = soup.find_all(class_='news_Itm-img')
    link = []
    for img in divlink:
        images = img.find('img')
        img_src = images.get('src')
        link.append(img_src)

    news_items = []
    for title, des, link, img_link in zip(tit, desc, news, link):
        news_item = {
            "title": title,
            "description": des,
            "link": link,
            "img_link": img_link
        }
        news_items.append(news_item)
        
    return news_items

@app.get("/")
def root():
    return {"Server is running"}

@app.get("/developer")
def root():
    return {"This news server is made by Pragun Jaswal"}


news_latest = scrape_news('https://www.ndtv.com/latest')
news_india = scrape_news('https://www.ndtv.com/india')
news_education = scrape_news('https://www.ndtv.com/education')
news_world = scrape_news('https://www.ndtv.com/world-news')
news_science = scrape_news('https://www.ndtv.com/science')

# print(news_latest)

@app.get("/news")
def get_news_latest():
    return news_latest

@app.get("/news-india")
def get_news_india():
    return news_india

@app.get("/news-education")
def get_news_education():
    return news_education

@app.get("/news-world")
def get_news_world():
    return news_world

@app.get("/news-science")
def get_news_science():
    return news_science

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)