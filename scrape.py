from bs4 import BeautifulSoup
import requests

# Connect to website and instantiate a response object
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

spans = soup.find_all("span", class_ = "text")

with open('./output-files/quotes.txt', 'w', encoding = 'utf-8', errors = 'replace') as file:
    for span in spans:
        modified_text = span.text.replace("�", '\"')
        file.write(modified_text + '\n')