import requests
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image

kxanUrl = 'https://www.kxan.com/weather/forecast/todays-forecast/'
kxanPage = requests.get(kxanUrl)
kvueUrl = 'https://www.kvue.com/allergy'
kvuePage = requests.get(kvueUrl)

soup = BeautifulSoup(kxanPage.content, 'html.parser')
weatherHtmlData = soup.find("div", {"class": "article-content rich-text"})
weatherText = weatherHtmlData.get_text()

allergyImage = urllib.request.urlretrieve("http://cdn.tegna-media.com/kvue/weather/allergy16x9.jpg", "allergy_forecast.jpg")
image = Image.open("allergy_forecast.jpg")

