from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.investing.com/currencies/streaming-forex-rates-majors'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36',
    'Referer': url,
    # Add any other necessary headers
}
payload = {
    # Include any required payload or parameters
}

response = requests.get(url, headers=headers, params=payload)
ajax_content = response.content  # Assuming the response is in JSON format

# html_content = response.content

soup = BeautifulSoup(ajax_content, 'html.parser')

# print(soup)

tbodies = soup.find_all('tbody')
for tbody in tbodies:
    trs = tbody.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        for td in tds:
            print(td.text)

