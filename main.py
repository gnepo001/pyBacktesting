import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import pandas as pd

data = pd.read_csv("ETH-USD.csv")
closes = data['AdjClose']
dates = pd.to_datetime(data['Date'])
dates = dates.dt.strftime('%m/%d/%Y')
opens = data["Open"]

fig = plt.figure()
ax = plt.subplot(1,1,1)

lines = [(dates,closes),(dates,opens)]

for line in lines:
    ax.plot(line[0],line[1])
    
# ax.plot(dates,closes)
# ax.plot(dates,opens)

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
for tick in ax.get_xticklabels():
    tick.set_rotation(35)


plt.show()
