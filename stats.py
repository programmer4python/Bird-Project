# -*- coding: utf-8 -*-
"""

This is the program which displays like a slide show.
It takes around 5 minutes to run the program.
@author: Michelle Umali
"""
import tkinter as tk
root = tk.Tk()
pic = tk.PhotoImage(file="two_birds.gif")
pic_lbl=tk.Label(root, image=pic).pack()
message = '''Welcome to the Blue Grosbeak and Bullock's Oriole Study!'''
pic_msg=tk.Label(root,text=message).pack()
root.mainloop()

import ib_1900_2020
import pc_1900_2020
import ib_amf
import ib_bmf
import pc_amf
import pc_bmf
import describestats_an
import describestats_ns
import count_an
import count_ns
import ib_pc_fp_values


#this graph takes a few minutes to run, the next 6 files display in tkinter window
ib_1900_2020();
pc_1900_2020();
#the next graph takes a few minutes to run
ib_amf();
ib_bmf();
pc_amf();
pc_bmf();
#the 2 graphs show in the Panes, plot area with tkinter button, the stats show in the console 
describestats_an();
describestats_ns();
count_an();
count_ns();
#these stats show in the console window
ib_pc_fp_values();

