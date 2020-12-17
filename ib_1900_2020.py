# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:00:42 2020
This as an image takes a long time to run.  Graph 1900 to 2020 - Bullock's Oriole
@author: miche
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
plot = ttk.Labelframe(root, text='Plot Area')
plot.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)
df = pd.read_csv('Ictterus bullockii.csv',
                   skiprows=0,nrows=427897, encoding='utf-8-sig',
                   parse_dates=['eventDate'])
ds=df.sort_values('eventDate')
#getting rid of invalid values
dt=ds.dropna(how='any')
fig = Figure(figsize=(5,4),dpi=100)
ax=fig.add_subplot(111)
dt.plot(x='eventDate',y='decimalLatitude',c='orange',ax=ax,title="Data from 1900 to 2020, source GBIF website")
ax.set_xlabel("Ictterus bullockii or Bullock's Oriole event dates")
ax.set_ylabel("Latitudes based on GBIF records")
canvas = FigureCanvasTkAgg(fig, master = plot)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)

root.mainloop()
