from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI ,Response ,status ,HTTPException, Request
from fastapi.params import Body          #FOR POST RESPONSE
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

def scrape_news(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    tags = soup.find_all('h2')
    
    news_list = []
    for tag in tags:
        title_tag = tag.find('a')
        if title_tag:
            title = title_tag.text
            link = title_tag['href']
            
            description_tag = tag.find_next('p')
            if description_tag:
                description = description_tag.text
            else:
                description = ""
            
            image_container = tag.find_next(class_='news_Itm-img')
            img_link = ""
            if image_container:
                image_tag = image_container.find('img')
                if image_tag:
                    img_link = image_tag.get('src')
            
            news_item = {
                "title": title,
                "description": description,
                "link": link,
                "img_link": img_link
            }
            news_list.append(news_item)
    
    return news_list

news_latest = scrape_news('https://www.ndtv.com/latest')
news_india = scrape_news('https://www.ndtv.com/india')
news_education = scrape_news('https://www.ndtv.com/education')
news_world = scrape_news('https://www.ndtv.com/world-news')
news_science = scrape_news('https://www.ndtv.com/science')

@app.get("/")
def root():
    return {"Server is running"}

@app.get("/developer")
def developer_info():
    return {"developer": "This news server is made by Pragun Jaswal"}


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
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)
