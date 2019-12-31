import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import dateutil.parser
import os
import time
class FetchOtion():
    def getFileName(self):
        local=datetime.now()
        time = str(dateutil.parser.parse(str(local)).date())
        local = local.strftime("%H-%M")
        name = time+"."+local
        return name
    
    def getOption(self,Type,symbol,expiry):
        url="https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?segmentLink=17&instrument="+str(Type)+"&symbol="+str(symbol)+"&date="+expiry
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        print(url)
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        table_cls_2 = soup.find(id="octable")
        req_row = table_cls_2.find_all('tr')
        each_line=[]
        each_line.append("Call OI,Call IV,Call Price,Strike Price,Put Price,Put_IV,Put OI" )
        print(each_line[0])
        for row_number, tr_nos in enumerate(req_row):
            if row_number <= 1 or row_number == len(req_row) - 1:
                continue
            td_columns = tr_nos.find_all('td')
            call_oi=BeautifulSoup(str(td_columns[1]), 'html.parser').get_text().replace(",","")
            call_iv=BeautifulSoup(str(td_columns[4]), 'html.parser').get_text().replace(",","")
            call_price = BeautifulSoup(str(td_columns[9]), 'html.parser').get_text().replace(",","")
            strike_price = BeautifulSoup(str(td_columns[11]), 'html.parser').get_text().replace(",","")
            put_oi=BeautifulSoup(str(td_columns[18]), 'html.parser').get_text().replace(",","")
            put_iv=BeautifulSoup(str(td_columns[21]), 'html.parser').get_text().replace(",","")
            put_price = BeautifulSoup(str(td_columns[14]), 'html.parser').get_text().replace(",","")
            line = str(call_oi)+","+str(call_iv)+","+str(call_price)+","+str(strike_price)+","+str(put_price)+","+str(put_iv)+","+str(put_oi)
            print(line)
            each_line.append(line)
        name = self.getFileName()
        name="D:/Data/stocks/options/snapshot/"+symbol+"/"
        print(os.path.exists(name))
        if not os.path.exists(name):
            os.makedirs(name)
        name = name+""+self.getFileName()+".csv"
        f = open(name,"w")
        for each in each_line:
            f.write(each)
            f.write("\n")
options = FetchOtion()
while 1==1:
	options.getOption("OPTIDX","BANKNIFTY","26DEC2019")
	time.sleep(60)
    