# Import the necessary packages
from bs4 import BeautifulSoup
import requests
import time

# Define the number dictionary
numbers = {}

# Define the function to scrape the website
def scrape_website():

    # Define the URL
    url = 'https://www.investing.com/currencies/streaming-forex-rates-majors'

    # Define the headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36',
        'Referer': url,
        # Add any other necessary headers
    }
    # Define the payload
    payload = {
        # Include any required payload or parameters
    }

    # Make the request
    response = requests.get(url, headers=headers, params=payload)
    ajax_content = response.content  # Assuming the response is in JSON format

    # Parse the response
    soup = BeautifulSoup(ajax_content, 'html.parser')

    # Find the table body and the necessary data
    tbodies = soup.find_all('tbody')
    for tbody in tbodies:
        trs = tbody.find_all('tr')
        for tr in trs:
            try:
                numbers[tr.find('span').text] = tr.find_all('td')[1].text
            except:
                pass
    print(numbers)

    return numbers

def get_number(currency):
    numbers = scrape_website()
    return numbers[currency]

