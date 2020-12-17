# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 04:40:48 2020
3 graphs for nesting season - Blue grosbeak
@author: Michelle Umali
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk
from tkinter import ttk

def center_window(width=300, height=200):
    s_width = root.winfo_screenwidth()
    s_height = root.winfo_screenheight()
    x = (s_width/2) - (width/2)
    y = (s_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = tk.Tk()
center_window(1400,800)
plot1 = ttk.Labelframe(root, text='Plot Area')
plot1.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)
#File had to be sorted to get rid of rows filled with hashtags because of old dates in excel.
#Could not convert in pandas.
#Hence the file is numbered with 2
df = pd.read_csv('Passerina caerula 2.csv',
                   skiprows=0,nrows=571402, encoding='utf-8-sig',
                   parse_dates=['eventDate'])
ds=df.sort_values('eventDate')
dt=ds.dropna(how='any')
#----------------------------------------------------------------------
mask1 = (dt['eventDate']>='2017-4-23')&(dt['eventDate']<='2017-8-27')
fig1 = Figure(figsize=(7,4),dpi=100)
ax1=fig1.add_subplot(111)
dt.loc[mask1].plot(x='eventDate',y='decimalLatitude',ax=ax1,title="Data from April 2017 to November 2017 nesting season")
ax1.set_ylabel("Latitudes based on GBIF records")
ax1.set_xlabel("Passerina caerula or Blue grosbeak event dates")
canvas = FigureCanvasTkAgg(fig1, master=plot1) 
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)


mask2 = (dt['eventDate']>='2018-4-17')&(dt['eventDate']<='2018-8-30')
fig2 = Figure(figsize=(7,4),dpi=100)
ax2=fig2.add_subplot(111)
dt.loc[mask2].plot(x='eventDate',y='decimalLatitude',ax=ax2,title="Data from April 2018 to October 2018 nesting season")
ax2.set_ylabel("Latitudes based on GBIF records")
ax2.set_xlabel("Passerina caerula or Blue grosbeak event dates")
canvas = FigureCanvasTkAgg(fig2, master=plot1) 
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=1)

mask3 = (dt['eventDate']>='2019-4-13')&(dt['eventDate']<='2019-8-28')
fig3 = Figure(figsize=(7,4),dpi=100)
ax3=fig3.add_subplot(111)
dt.loc[mask3].plot(x='eventDate',y='decimalLatitude',ax=ax3,title="Data from April 2018 to November 2019 nesting season")
ax3.set_ylabel("Latitudes based on GBIF records")
ax3.set_xlabel("Passerina caerula or Blue grosbeak event dates")
canvas = FigureCanvasTkAgg(fig3, master=plot1) 
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0)

print(dt[mask1].describe())
print(dt[mask2].describe())
print(dt[mask3].describe())
root.mainloop()
