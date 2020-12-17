# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 04:40:48 2020
After nesting season 3 graphs of Bullock's Oriole
@author: Michelle Umali
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk
from tkinter import ttk
from scipy import stats

def center_window(width=300, height=200):
    s_width = root.winfo_screenwidth()
    s_height = root.winfo_screenheight()
    x = (s_width/2) - (width/2)
    y = (s_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = tk.Tk()
#making the window large to fit 3 graphs
center_window(1400,800)
plot1 = ttk.Labelframe(root, text='Plot Area')
plot1.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)

df = pd.read_csv('Ictterus bullockii.csv',
                   skiprows=0,nrows=428000, encoding='utf-8-sig',
                   parse_dates=['eventDate'])
ds=df.sort_values('eventDate')
dt=ds.dropna(how='any')
#----------------------------------------------------------------------
#plotting first latitude graph
mask1 = (dt['eventDate']>='2016-9-10')&(dt['eventDate']<='2017-4-14')
fig1 = Figure(figsize=(7,4),dpi=100)
ax1=fig1.add_subplot(111)
dt.loc[mask1].plot(x='eventDate',y='decimalLatitude',color='orange',ax=ax1,title="Data from September 2016 to April 2017 after nesting season")
ax1.set_ylabel("Latitudes based on GBIF records")
ax1.set_xlabel("Ictterus bullocki or Bullock's Oriole event dates")
canvas = FigureCanvasTkAgg(fig1, master=plot1) 
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)

#plotting second latitude graph
mask2 = (dt['eventDate']>='2017-9-15')&(dt['eventDate']<='2018-3-16')
fig2 = Figure(figsize=(7,4),dpi=100)
ax2=fig2.add_subplot(111)
dt.loc[mask2].plot(x='eventDate',y='decimalLatitude',color="orange",ax=ax2,title="Data from September 2017 to March 2018 after nesting season")
ax2.set_ylabel("Latitudes based on GBIF records")
ax2.set_xlabel("Ictterus bullocki or Bullock's Oriole event dates")
canvas = FigureCanvasTkAgg(fig2, master=plot1) 
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=1)

#plotting third latitude graph
mask3 = (dt['eventDate']>='2018-9-22')&(dt['eventDate']<='2019-3-14')
fig3 = Figure(figsize=(7,4),dpi=100)
ax3=fig3.add_subplot(111)
dt.loc[mask3].plot(x='eventDate',y='decimalLatitude',color="orange",ax=ax3,title="Data from September 2018 to March 2019 after nesting season")
ax3.set_ylabel("Latitudes based on GBIF records")
ax3.set_xlabel("Ictterus bullocki or Bullock's Oriole event dates")
canvas = FigureCanvasTkAgg(fig3, master=plot1) 
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0)

f,p=stats.f_oneway(mask1,mask2,mask3)
print(stats.f_oneway(mask1,mask2,mask3))
print("{0:1.3g}".format(p))
if p < 0.05:
    print("The null hypothesis has been rejected.")
else:
    print("The null hypothesis has been accepted.")
root.mainloop()
