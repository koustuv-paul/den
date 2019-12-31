import pandas as pd
import matplotlib as mpl
from matplotlib import style
from matplotlib import pyplot as plt

series = pd.read_csv('D:/Data/stocks/options/snapshot/BANKNIFTY/strike_data/2019-12-12/31800.00.csv')
mpl.rc('figure', figsize=(20, 7))
mpl.__version__
style.use('ggplot')
top10 = series
ema3 = top10["Put Price"].ewm(span=3,adjust=False).mean()
ema5 = top10["Put Price"].ewm(span=5,adjust=False).mean()
top10["Put Price"].plot(label="Put Price")
ema3.plot(label="EMA3" , color="black")
ema5.plot(label="EMA5")

count = 0
bought = False
buy_price = 0.0;
pl=0.0
times_bought =0
buy_list=[]
sold_list=[]
profit=[]
column = "Put Price"
lema3=ema3[count]
lema5=ema5[count]
count +=1
while count < len(top10):
    #and lema3 >=ema3[count] and lema5 >= ema5[count]
    diff = ema3[count]-ema5[count]
    val1= lema3 > lema5
    val2= diff < -0.5
    val3 = not bought
    a = [val1,val2,val3]
    print(a)
    break;
    if all(a):
        print(diff)
        bought = True
        buy_price=top10[column][count]
        times_bought = times_bought + 1
        buy_list.append(str(buy_price) +":"+ str(count))

    elif diff >= 0 and bought:
        bought = False
        pl = pl + (buy_price - top10[column][count])
        buy_price=0.0
        sold_list.append(str(top10[column][count])+":"+ str(count))
    count = count+1
    lema3=ema3
    lema5=ema5

if bought and buy_price != 0.0: 
    sold_list.append(top10[column][count - 1])
    pl = pl + (buy_price - top10[column][count-1])
    
        
print("Trades taken : "+ str(times_bought) +" Profi/Loss : "+ str(pl * 20 - times_bought*40 ) )

count = 0
print(buy_list)
print(sold_list)

plt.legend()
