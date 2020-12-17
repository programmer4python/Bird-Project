# -*- coding: utf-8 -*-plt.
"""
Created on Fri Dec 11 05:44:57 2020
Had difficulty placing these bar graphs in a tkinter window, shows in console only
Implemented button for console
Shows mean and std for 3 sets of data
@author: Michelle Umali
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
#first button
firstBtn=tk.Button(root,text="Submit for Bullock's Orioles mean and std graphs",width=50,height=10,bg="orange",fg="black",command=lambda:LoadFirstGraph())
firstBtn.pack()
#second button
secondBtn=tk.Button(root,text='Submit for Blue grosbeak mean and std',width=50,height=10,bg="blue",fg="white",command=lambda:LoadSecondGraph())
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

x1,x2=dt[mask1].mean()
y1,y2=dt[mask1].std()
x3,x4=dt[mask2].mean()
y3,y4=dt[mask2].std()
x5,x6=dt[mask3].mean()
y5,y6=dt[mask3].std()    
def LoadFirstGraph():
    means=(x1,x3,x5)
    positions=(0,1,2)
    std=(y1,y3,y5)
    bar_tick_label=['2017','2018','2019']
    plt.bar(positions, means, tick_label=bar_tick_label,color="y", yerr=std)
    plt.xlabel("Icterrus bullockii or Bullock's Orioles")
    plt.ylabel('mean and std in latitudes')
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

x7,x8=dt[mask4].mean()
y7,y8=dt[mask4].std()
x9,x10=dt[mask5].mean()
y9,y10=dt[mask5].std()
x11,x12=dt[mask6].mean()
y11,y12=dt[mask6].std()
def LoadSecondGraph():    
    means=(x7,x9,x11)
    positions=(3,4,5)
    std=(y7,y9,y11)
    bar_tick_label=['2017','2018','2019']
    plt.bar(positions, means, tick_label=bar_tick_label,color="b", yerr=std)
    plt.xlabel('Passerina caerula or Blue grosbeak')
    plt.ylabel('mean and std in latitudes')
    plt.title('Nesting seasons')
    #plt.legend()
    plt.show()
   
print(dt[mask1].describe())
print(dt[mask2].describe())
print(dt[mask3].describe())
print(dt[mask4].describe())
print(dt[mask5].describe())
print(dt[mask6].describe())
root.mainloop()