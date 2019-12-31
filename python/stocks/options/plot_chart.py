import pandas as pd
from matplotlib import pyplot as plt
series = pd.read_csv('D:/Data/stocks/options/snapshot/BANKNIFTY/strike_data/2019-12-12/31400.00.csv')
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(series["Hour.Min"] , series["Call Price"],color='red')
ax1.set_ylabel("Call Price")
ax2 = ax1.twinx()
ax2.plot(series["Hour.Min"] , series["Call IV"])
ax2.set_ylabel("Call IV")
for each in ax2.get_yticklabels():
    each.set_color('red')
