# -*- coding: utf-8 -*-
"""
showing f and p values - rejecting null hypotheses
@author: Michelle Umali
"""
import pandas as pd
from scipy import stats

df = pd.read_csv('Ictterus bullockii.csv',
                   skiprows=0,nrows=428000, encoding='utf-8-sig',
                   parse_dates=['eventDate'])
ds=df.sort_values('eventDate')
dt=ds.dropna(how='any')
#----------------------------------------------------------------------
mask1 = (dt['eventDate']>='2017-5-2')&(dt['eventDate']<='2017-8-27')
mask2 = (dt['eventDate']>='2018-5-8')&(dt['eventDate']<='2018-8-30')
mask3 = (dt['eventDate']>='2019-5-6')&(dt['eventDate']<='2019-8-28')

f,p=stats.f_oneway(mask1,mask2,mask3)
print(stats.f_oneway(mask1,mask2,mask3))
print("{0:1.3g}".format(p))
if p < 0.05:
    print("The null hypothesis has been rejected.")
else:
    print("The null hypothesis has been accepted.")

mask4 = (dt['eventDate']>='2016-9-10')&(dt['eventDate']<='2017-4-14')
mask5 = (dt['eventDate']>='2017-9-15')&(dt['eventDate']<='2018-3-16')
mask6 = (dt['eventDate']>='2018-9-22')&(dt['eventDate']<='2019-3-14')
f2,p2=stats.f_oneway(mask4,mask5,mask6)
print(stats.f_oneway(mask4,mask5,mask6))
print("{0:1.3g}".format(p))
if p2 < 0.05:
    print("The null hypothesis has been rejected.")
else:
    print("The null hypothesis has been accepted.")
#---------------------------------------------------------------------    
df = pd.read_csv('Passerina caerula 2.csv',
                   skiprows=0,nrows=571402, encoding='utf-8-sig',
                   parse_dates=['eventDate'])
ds=df.sort_values('eventDate')
dt=ds.dropna(how='any')
mask7= (dt['eventDate']>='2017-4-23')&(dt['eventDate']<='2017-8-27')
mask8 = (dt['eventDate']>='2018-4-17')&(dt['eventDate']<='2018-8-30')
mask9 = (dt['eventDate']>='2019-4-13')&(dt['eventDate']<='2019-8-28')
f3,p3=stats.f_oneway(mask7,mask8,mask9)
print(stats.f_oneway(mask7,mask8,mask9))
print("{0:1.3g}".format(p))
if p3 < 0.05:
    print("The null hypothesis has been rejected.")
else:
    print("The null hypothesis has been accepted.")

mask10 = (dt['eventDate']>='2016-11-5')&(dt['eventDate']<='2017-3-29')
mask11 = (dt['eventDate']>='2017-11-13')&(dt['eventDate']<='2018-3-28')
mask12 = (dt['eventDate']>='2018-11-12')&(dt['eventDate']<='2019-3-14')
f4,p4=stats.f_oneway(mask10,mask11,mask12)
print(stats.f_oneway(mask10,mask11,mask12))
print("{0:1.3g}".format(p))
if p3 < 0.05:
    print("The null hypothesis has been rejected.")
else:
    print("The null hypothesis has been accepted.")