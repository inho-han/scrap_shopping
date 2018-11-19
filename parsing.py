import time
import urllib.request
import requests
from bs4 import BeautifulSoup

from translation import Translation_Module
from path_file import product_image_path

def Aliexpress(URL) :
    count = 1

    source_code = requests.get(URL)
    soup = BeautifulSoup(source_code.content, 'html.parser')
    product_contents = soup.find_all('div', {'class': 'item'})

    for li in product_contents:
        product_image_search = li.find('img')
        # src 또는 image-src에 있는 내용을 표기
        product_image = product_image_search.get('image-src') or product_image_search.get('src')
        image_name = (product_image_search.get('image-src') or product_image_search.get('src')).split('/')[5].strip()
        print('==' * 20, count,"번째",  '==' * 20 )
        name = li.find('h3').text.strip()
        price = li.select('span')[1].text

        Translation_Module('en','ko',name)
        print(price)

        print('이미지 : ',(product_image_search.get('image-src') or product_image_search.get('src')).split('/')[5].strip())
#   print문으로 찍을 내용을 정리하여 엑셀 형식에 맞게 넣어주는 작업 필요
        download_img(product_image, image_name)

        time.sleep(0.1)
        count += 1


def download_img(url, name) :
    full_name = str(name)
    # urllib.request.urlretrieve(이미지 주소 / 경로 + 이미지 이름) 형태로 넘겨주면 이미지 다운로드 진행 함
    urllib.request.urlretrieve("http:"+ url, product_image_path + full_name)