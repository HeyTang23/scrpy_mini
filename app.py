import requests
from lxml import etree

heades = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

def get_url(url):
    text = requests.get(url, heades)
    text.encoding = 'utf-8'
    return text.text

def get_data(url):
    doc = etree.HTML(get_url(url))
    return doc

# base_url = f'http://www.qszy9.com/index-{1}.html'
# get_data(get_url(base_url))