# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 04:40:48 2020
Plot of data from 1900 to 2020 - Blue grosbeak
@author: Michelle Umali
"""
#import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
plot1 = ttk.Labelframe(root, text='Plot Area')
plot1.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)
df = pd.read_csv('Passerina caerula 2.csv',
                   skiprows=0,nrows=571402, encoding='utf-8-sig',
                   parse_dates=['eventDate'])
ds=df.sort_values('eventDate')
#removing invalid values
dt=ds.dropna(how='any')
fig = Figure(figsize=(5,4),dpi=100)
ax=fig.add_subplot(111)
dt.plot(x='eventDate',y='decimalLatitude',ax=ax,title="Data from 1900 to 2020, source GBIF website")
ax.set_ylabel("Latitudes based on GBIF records")
ax.set_xlabel('Passerina caerula or Blue grosbeak event dates')
canvas = FigureCanvasTkAgg(fig, master = plot1)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)

root.mainloop()
