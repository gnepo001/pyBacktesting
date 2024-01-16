
from tkinter import *

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import pandas as pd

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

window = Tk()
window.geometry("700x700")
window.title("Backtester")

data = pd.read_csv("ETH-USD.csv")
closes = data['AdjClose']
dates = pd.to_datetime(data['Date'])
dates = dates.dt.strftime('%m/%d/%Y')
opens = data["Open"]

fig = Figure(figsize = (6, 6), 
                 dpi = 100) 
ax = fig.add_subplot(111) 


sma = closes.rolling(30).mean()
lines = [(dates,closes),(dates,opens),(dates,sma)]

for line in lines:
    ax.plot(line[0],line[1])
    
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
for tick in ax.get_xticklabels():
    tick.set_rotation(35)


#creates tkinter canvas holing the matplotlib graph
canvas = FigureCanvasTkAgg(fig, master = window)   
canvas.draw()

#place canvas in tk window
canvas.get_tk_widget().pack() 

#place toolbar in tk window
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update() 

#Run tk GUI
window.mainloop() 
