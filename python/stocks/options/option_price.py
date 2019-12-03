import sys
import requests
from bs4 import BeautifulSoup

stock=sys.argv[1]


if 1 == sys.argv[2]:
	type = "OPTSTK"
else:
	type = "OPTIDX"
	
expiry = sys.argv[3]


	
Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?segmentLink=17&instrument="+ type +"&symbol="+ sys.argv[1]+"&date="+expiry

print(Base_url)
page = requests.get(Base_url)
soup = BeautifulSoup(page.content, 'html.parser')
table_cls_2 = soup.find(id="octable")
req_row = table_cls_2.find_all('tr')
call_strike_put = []
for row_number, tr_nos in enumerate(req_row):
        # This ensures that we use only the rows with values
        if row_number <= 1 or row_number == len(req_row) - 1:
            continue
        td_columns = tr_nos.find_all('td')
        strike_price = BeautifulSoup(str(td_columns[11]), 'html.parser').get_text()
        call_price = BeautifulSoup(str(td_columns[9]), 'html.parser').get_text()
        put_price = BeautifulSoup(str(td_columns[14]), 'html.parser').get_text()
        call_strike_put.append(call_price + " : " +strike_price+ " : " + put_price)
        
print("Call : Strike : Put")
for each in enumerate(call_strike_put):
    print(each)
