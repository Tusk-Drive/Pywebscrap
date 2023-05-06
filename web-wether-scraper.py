import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Function to scrape website and extract desired information
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element(s) containing the desired information
    # Modify this part based on the structure of the website and the information you want to scrape
    # Example: Extracting the titles of articles from a news website
    article_titles = soup.find_all('h2', class_='article-title')

    # Process the scraped information
    titles = [title.text.strip() for title in article_titles]
    return titles

# URL of the website to scrape
url = 'https://www.example.com'

# Call the scrape_website function with the URL
scraped_data = scrape_website(url)

# Create a pop-up window
root = tk.Tk()
root.title("Scraped Data")

# Create a text widget to display the scraped data
text_widget = tk.Text(root, height=10, width=50)
text_widget.pack()

# Insert the scraped data into the text widget
for data in scraped_data:
    text_widget.insert(tk.END, data + '\n')

# Start the Tkinter event loop
root.mainloop()
