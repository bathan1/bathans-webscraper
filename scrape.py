from bs4 import BeautifulSoup
import requests

# Connect to website and instantiate a response object
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all("a")
for link in links:
    print(link.get("href"))