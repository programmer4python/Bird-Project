# -*- coding: utf-8 -*-plt.
"""
Created on Fri Dec 11 05:44:57 2020

@author: miche
"""

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
def center_window(width=300, height=200):
    s_width = root.winfo_screenwidth()
    s_height = root.winfo_screenheight()
    x = (s_width/2) - (width/2)
    y = (s_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

center_window(700,400)

firstBtn=tk.Button(root,text="Click for Bullock's Orioles count of occurrences",width=50,height=10,bg="orange",fg="black",command=lambda:LoadFirstGraph())
firstBtn.pack()

secondBtn=tk.Button(root,text='Click for Blue grosbeak count of occurrences',width=50,height=10,bg="blue",fg="white",command=lambda:LoadSecondGraph())
secondBtn.pack()


plot1 = ttk.Labelframe(root, text='Plot Area')
fig, ax = plt.subplots()

df = pd.read_csv('Ictterus bullockii.csv',
                   skiprows=0,nrows=428000, encoding='utf-8-sig',
                   parse_dates=['eventDate'])
ds=df.sort_values('eventDate')
dt=ds.dropna(how='any')
#----------------------------------------------------------------------
mask1 = (dt['eventDate']>='2017-5-2')&(dt['eventDate']<='2017-8-27')
mask2 = (dt['eventDate']>='2018-5-8')&(dt['eventDate']<='2018-8-30')
mask3 = (dt['eventDate']>='2019-5-6')&(dt['eventDate']<='2019-8-28')

rows1=dt[mask1].shape[0]
rows2=dt[mask2].shape[0]
rows3=dt[mask3].shape[0]

def LoadFirstGraph():
   
    means=(rows1,rows2,rows3)
    positions=(0,1,2)
    bar_tick_label=['2017','2018','2019']
    plt.bar(positions, means, tick_label=bar_tick_label,color="y")
    plt.xlabel("Icterrus bullockii or Bullock's Orioles")
    plt.ylabel('count of occurrences')
    plt.title('Nesting seasons')
    #plt.legend()
    plt.show()


dg = pd.read_csv('Passerina caerula 2.csv',
                   skiprows=0,nrows=571402, encoding='utf-8-sig',
                   parse_dates=['eventDate'])
du=dg.sort_values('eventDate')
dv=du.dropna(how='any')
#----------------------------------------------------------------------

mask4 = (dt['eventDate']>='2017-4-23')&(dt['eventDate']<='2017-8-27')
mask5 = (dt['eventDate']>='2018-4-17')&(dt['eventDate']<='2018-8-30')
mask6 = (dt['eventDate']>='2019-4-13')&(dt['eventDate']<='2019-8-28')

rows4=dt[mask4].shape[0]
rows5=dt[mask5].shape[0]
rows6=dt[mask6].shape[0]


def LoadSecondGraph():    
    means=(rows4,rows5,rows6)
    positions=(3,4,5)
    
    bar_tick_label=['2017','2018','2019']
    plt.bar(positions, means, tick_label=bar_tick_label,color="b")
    plt.xlabel('Passerina caerula or Blue grosbeak')
    plt.ylabel('count of occurrences')
    plt.title('Nesting seasons')
    #plt.legend()
    plt.show()

root.mainloop()