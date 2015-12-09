
#Filename:quotes.py
#Get Dow Jones Industrial Avarage from Yahoo with quotes_historical_yahoo
#!/bin/python

from matplotlib.finance import quotes_historical_yahoo 
from datetime import date
import pandas as pd



today = date.today()
start = (today.year-1,today.month,today.day)
quotes = quotes_historical_yahoo('IBM',start,today)
date_list=[]
for i in range(0,len(quotes)):
    nomal_time=date.fromordinal(int(quotes[i][0]))
    format_time = date.strftime(nomal_time, '%Y-%m-%d')
    date_list.append(format_time)

df = pd.DataFrame(data=quotes,index=date_list,columns=("date","open","close","high","low","volumn"))
df = df.drop(['date'],axis=1)

print df
