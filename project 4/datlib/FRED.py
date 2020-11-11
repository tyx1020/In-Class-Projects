#FRED.py
import pandas as pd
import pandas_datareader.data as web
# datatime is important and will let us work with index 
import datetime

# we gather the data and call this gather data 
# we have a disctionary of data codes and data names 
# each code is linked to a name 
# we default the end data to be today 
# frequency is to default by A as annual, W as weekly, M as monthly, 
# Q as quarterly and D as daily 
# you can acually add a number next to each of those to increase the length of frequency 
# for example, 2d means every two days and 3m means a quater 

def gather_data(data_codes, start, end = datetime.datetime.today(), freq = "A"):
 
# check if new column is first column of data, 
# if true, then create a new df, if not,add to existing dataframe 
    i = 0
 # dct.items() calls key and value that key points to
   
    for key, code in data_codes.items():
# check if it's our first column of data        
        if i == 0:
# Create dataframe for first variable, then rename column
            # The key is our column name and the val is going  to be set 
            # we pass the code which refers the val, use Fred because Fred is one option and pandas data reader 
            # if we smaple by weekly, we will take the weekly mean 
            df = web.DataReader(code, "fred", start, end).resample(freq).mean()
            # to rename the first column
            #df.rename(columns = {val:key}, inplace = True) 
            # we have the key which is the name of the variable,
            # Val is actually a code and just call val code 

            df.rename(columns = {code:key}, inplace = True) 

# we have the key which is the name of the variable,
            # Val is actually a code and just call val code 
            i = None
        else:
            
 # If i is no longer zero and dataframe already exists, tell python to add new column
            df[key] = web.DataReader(code, "fred", start, end).resample(freq).mean()

    return df

#  pass a column of data to this function to convert the values from billion to million
def bil_to_mil(series):
# convert, multiply the value in the series by a thousand    
    return series * 10**3