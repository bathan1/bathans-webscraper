from bs4 import BeautifulSoup
import requests

# Connect to website and instantiate a response object
url = "https://www.hangmanwords.com/words"
response = requests.get(url)

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

# Put all ul elements in ul_elements list
ul_elements = soup.find_all('ul')

# Check if there is at least a second <ul> element
if len(ul_elements) >= 2:
    second_ul = ul_elements[1]
    
    li_elements = second_ul.find_all('li')

    with open('./output-files/hangman.txt', 'w', encoding = 'utf-8', errors = 'replace') as file:
        for elements in li_elements:
            modified_text = elements.text.replace("�", '\"')
            file.write(modified_text + '\n')