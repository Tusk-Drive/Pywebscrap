import requests
from bs4 import BeautifulSoup
#This is a colabrative event to get a web scraper to pull publicly known infroamtion to present in the code. 
# URL of the website to scrape
url = 'https://weather.com/'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the weather information
weather_element = soup.find('div', {'class': 'weather'})

# Extract the text of the weather information
weather_text = weather_element.text.strip()

# Print the weather information
print("Most Recent Weather:", weather_text)


