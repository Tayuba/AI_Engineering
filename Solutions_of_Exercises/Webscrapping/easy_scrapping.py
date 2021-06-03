from bs4 import BeautifulSoup
import requests

weather = "https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YLdcqPkzY2w"
response = requests.get(weather)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
