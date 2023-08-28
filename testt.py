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

html_text = requests.get('https://www.ndtv.com/india').text
soup = BeautifulSoup(html_text,'lxml')
tags = soup.find_all('h2')
# print(tags)
tit = []
news = []
for new in tags:
    title_tag = new.find('a')  # Find the <a> tag
    if title_tag:
        title = title_tag.text  # Extract the title
        link = title_tag['href']  # Extract the link
        tit.append(title)
        news.append(link)
        
        # news.append({"title": title, "link": link})
    

des = soup.find_all('p')
# print(tags)
desc = []
for des in des:
    desc.append(des.text)


link = soup.find('div',{'class':'row s-lmr mt-10'})
divlink = link.find_all(class_='news_Itm-img')

# print (divlink)
link = []
for img in divlink:
    images =img.find('img')
    img_src = images.get('src')
    link.append(img_src)

# Combine all

news_india=[]
for title,des, link, img_link in zip(tit,desc, news, link):
    news_item = {
        "title": title,
        "description":des,
        "link": link,
        "img_link": img_link
    }
    news_india.append(news_item)

print (news_india)
html_text = requests.get('https://www.ndtv.com/education').text
soup = BeautifulSoup(html_text,'lxml')
tags = soup.find_all('h2')
# print(tags)
tit = []
news = []
for new in tags:
    title_tag = new.find('a')  # Find the <a> tag
    if title_tag:
        title = title_tag.text  # Extract the title
        link = title_tag['href']  # Extract the link
        tit.append(title)
        news.append(link)
        
        # news.append({"title": title, "link": link})
    

des = soup.find_all('p')
# print(tags)
desc = []
for des in des:
    desc.append(des.text)


link = soup.find('div',{'class':'row s-lmr mt-10'})
divlink = link.find_all(class_='news_Itm-img')

# print (divlink)
link = []
for img in divlink:
    images =img.find('img')
    img_src = images.get('src')
    link.append(img_src)

# Combine all

news_education=[]
for title,des, link, img_link in zip(tit,desc, news, link):
    news_item = {
        "title": title,
        "description":des,
        "link": link,
        "img_link": img_link
    }
    news_education.append(news_item)

print(news_education)



@app.get("/")
def root():
    return{"Server is running"}

@app.get("/developer")
def root():
    return{"This news server is made by Pragun jaswal"}

@app.get("/news-india")
def root():
    return news_india

@app.get("/news-education")
def root():
    return news_education

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)
