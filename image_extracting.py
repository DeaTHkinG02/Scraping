import requests as rq
from bs4 import BeautifulSoup as bs
import os

url='https://yourlieinaprilmanga.com/manga/your-lie-in-april-chapter-1/'
max_chapter=1 #44
urls=[url[:-2]+str(i)+'/' for i in range(1,max_chapter+1)]

# create folders
!mkdir chapters
for chapter in range(1, max_chapter+1):
    if os.path.exists('/chapters/chapter-'+str(chapter))==False:
        os.mkdir('chapters/chapter-'+str(chapter))

# collect all url-pages
all_url_pages=[]
for chapter in range(max_chapter):
    req=rq.get(urls[chapter])
    soup = bs(req.content, 'html.parser')
    chapter_page_urls=[link.get('src') for link in soup.find_all('img',{'decoding': 'async'})]
    all_url_pages.append(chapter_page_urls)

# collect and download images
for chapter in range(max_chapter):
    for page in range(len(all_url_pages[chapter])):
        img_data= rq.get(all_url_pages[chapter][page]).content
        with open(f'chapters/chapter-{chapter+1}/page-{page+1}.jpg','wb') as handler:
            handler.write(img_data)