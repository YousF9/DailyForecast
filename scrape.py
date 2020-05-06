import webbrowser

import requests
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image
import webbrowser, os

kxanUrl = 'https://www.kxan.com/weather/forecast/todays-forecast/'
kxanPage = requests.get(kxanUrl)
kvueUrl = 'https://www.kvue.com/allergy'
kvuePage = requests.get(kvueUrl)

soup = BeautifulSoup(kxanPage.content, 'html.parser')
weatherHtmlData = soup.find("div", {"class": "article-content rich-text"})
weatherText = weatherHtmlData.get_text()

tempHighHtml = soup.find('span', {"class": "high"})
tempHigh = tempHighHtml.get_text()

tempLowHtml = soup.find('span', {"class": "low"})
tempLow = tempLowHtml.get_text()

allergyImage = urllib.request.urlretrieve("http://cdn.tegna-media.com/kvue/weather/allergy16x9.jpg", "allergy_forecast.jpg")
image = Image.open("allergy_forecast.jpg")

template = """<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="styles.css">
    <title>Daily Austin Forecast</title>
</head>
<body>

<h1>Weather <span class="text-primary">Forecast</span></h1>
<div>
    Today's High: tempHigh    | Today's Low: tempLow
    <br>
    <br>
    FORECAST_INFORMATION
</div>
<h1>Allergy <span class="text-primary">Forecast</span></h1>
<img src="allergy_forecast.jpg"></img>

</body>
</html>"""
template = template.replace("FORECAST_INFORMATION", str(weatherText))
template = template.replace("tempHigh", str(tempHigh))
template = template.replace("tempLow", str(tempLow))

with open("forecast.html", "w") as file:
    file.write(template)

webbrowser.open('file://' + os.path.realpath("forecast.html"))

