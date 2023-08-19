from bs4 import BeautifulSoup

with open('index.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')

tag1= soup.find('h2')            #find method only search for first element
tag2 = soup.find_all("h2")       #find_all method search for all element
print(tag1)
print(tag2)

for tags in tag2:               #use loop to only print inside content
    print(tags.text)

last = soup.find_all('p')
list =[]
for p in last:
    list.append(p.text)
    stf = str(list[:2:-1])
print(stf)

header = soup.find_all("ul")
for head in header:
    print (head.text)