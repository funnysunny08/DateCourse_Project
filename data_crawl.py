import requests
import pprint
import time
from urllib.parse import quote
def data_crawl(keyword):
    client_id = "TGQKHQehJjfRIYcCQ52c"
    client_secret = "0KVrnmVTMy"
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

    url_base = "https://openapi.naver.com/v1/search/local.json?query="

    url_middle = "&display=10&start=1&sort=comment"

    url = url_base + keyword + url_middle

    result = requests.get(url, headers=headers).json()

    place = result['items']

    return place

def data_crawl_recommend():
    client_id = "TGQKHQehJjfRIYcCQ52c"
    client_secret = "0KVrnmVTMy"
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

    url_base = "https://openapi.naver.com/v1/search/local.json?query="
    keyword_recommend = "서울 핫플레이스"
    url_middle = "&display=10&start=1&sort=comment"

    url_recommend = url_base + keyword_recommend + url_middle

    result_recommend = requests.get(url_recommend, headers=headers).json()

    place_recommend = result_recommend['items']

    return place_recommend