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

template = """<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="styles.css">
    <title>Daily Austin Forecast</title>
</head>
<body>

<h1>Forecast</h1>
<div>
    FORECAST_INFORMATION
</div>
<img src="allergy_forecast.jpg"></img>

</body>
</html>"""
template = template.replace("FORECAST_INFORMATION", str(weatherText))

with open("forecast.html", "w") as file:
    file.write(template)