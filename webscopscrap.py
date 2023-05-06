from tkinter import Button, Entry, Label, Tk, Toplevel, messagebox, Listbox, Scrollbar, SINGLE, END, VERTICAL, RIGHT, Y
import requests
from bs4 import BeautifulSoup


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


# Function to display the selected content in a message box
def show_selected_content():
    # Get the selected item from the listbox
    selected_item = Listbox.get(Listbox.curselection())

    # Show the selected content in a message box
    messagebox.showinfo("Selected Content", selected_item)


# Function to handle the button click event
def scrape_and_display():
    # Get the URL from the input field
    url = url_entry.get()

    # Call the scrape_website function with the URL
    scraped_data = scrape_website(url)

    # Create a pop-up window
    popup_window = Toplevel(root)
    popup_window.title("Scraped Data")

    # Create a listbox to display the scraped data
    listbox = Listbox(popup_window, selectmode=SINGLE)
    listbox.pack(side="left", fill="y")

    # Create a scrollbar for the listbox
    scrollbar = Scrollbar(popup_window, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the listbox to use the scrollbar
    listbox.config(yscrollcommand=scrollbar.set)

    # Insert the scraped data into the listbox
    for data in scraped_data:
        listbox.insert(END, data)

    # Create a button to show the selected content
    select_button = Button(popup_window, text="Select", command=show_selected_content)
    select_button.pack()


# Create the main window
root = Tk()
root.title("Web Scraper")

# Create an input field for the URL
url_label = Label(root, text="Enter URL:")
url_label.pack()

url_entry = Entry(root, width=50)
url_entry.pack()

# Create a button to trigger the scraping and display
scrape_button = Button(root, text="Scrape", command=scrape_and_display)
scrape_button.pack()

# Start the Tkinter event loop
root.mainloop()
