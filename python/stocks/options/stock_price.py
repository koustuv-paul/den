import requests
import json
from bs4 import BeautifulSoup
Base_url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=RELIANCE"
page = requests.get(Base_url)
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(id="responseDiv")
data = content.text.split("\",\"")
last_price = "";
print(content)
for el in data:
    if "lastPrice" in el:
        print(el)
        break
