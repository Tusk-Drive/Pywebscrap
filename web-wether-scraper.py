from requests import get
from bs4 import BeautifulSoup
#This is a collaborative event to get a web scraper to pull publicly known information to present in the code.
# URL of the website to scrape
URL = 'https://openweathermap.org/city'

# Send a GET request to the URL
response = get(URL)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the weather information
weather_element = soup.find('div', {'class': 'weather__temperature'})

# Extract the text of the weather information
weather_text = weather_element.text.strip()

# Print the weather information
print("Most Recent Weather:", weather_text)
