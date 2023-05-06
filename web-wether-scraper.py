import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Function to scrape the Fox News website and extract desired information
def scrape_fox_news():
    # Send a GET request to the Fox News homepage
    response = requests.get('https://www.foxnews.com/')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element(s) containing the desired information
    # Modify this part based on the structure of the website and the information you want to scrape
    article_titles = soup.find_all('h2', class_='title')

    # Process the scraped information
    titles = [title.text.strip() for title in article_titles]
    return titles

# Create a function to handle the button click event
def scrape_and_display():
    # Call the scrape_fox_news function
    scraped_data = scrape_fox_news()

    # Create a pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Scraped Data")

    # Create a text widget to display the scraped data
    text_widget = tk.Text(popup_window, height=10, width=50)
    text_widget.pack()

    # Insert the scraped data into the text widget
    for data in scraped_data:
        text_widget.insert(tk.END, data + '\n')

# Create the main window
root = tk.Tk()
root.title("Web Scraper")

# Create a button to trigger the scraping and display
scrape_button = tk.Button(root, text="Scrape Fox News", command=scrape_and_display)
scrape_button.pack()

# Start the Tkinter event loop
root.mainloop()

# Things to do later: 
#1.Look more into how to how to give more funcinality to the program, like images and a more scoped out function of the program. 

