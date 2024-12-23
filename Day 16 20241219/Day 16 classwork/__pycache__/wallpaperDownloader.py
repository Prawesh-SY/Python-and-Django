import requests
from bs4 import BeautifulSoup

import threading

def download(image_url):
    try:
        # print(f"Downloading {image_url}")
        image_name= "images/"+image_url.split('/')[-1]
        with open(image_name,'wb') as file:
            file.write(requests.get(image_url).content)
    except:
        pass

url= "https://4kwallpapers.com/"
data = requests.get(url)

soup= BeautifulSoup(data.text, 'html.parser')
# print(soup.prettify())
print(soup.title)
images = soup.find_all('img')
for image in images:
    imageLink=image.get('src')
    t1 = threading.Thread(target=download,arg=[imageLink])
    t1.start()
    download(imageLink)