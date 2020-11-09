import os
import pandas as pd 
import numpy as np
# np is essentially a math and data library 
import matplotlib.pyplot as plt

# matplotlib is all the plotting tools
# we create a function that plots a scatter as a timeseries 
# this is one of way to visualize data
# it is just a scatter plot and then we represent time with color 
# in the book, we represent the color as multiple variables 

def plot_ts_scatter(df, s = 75, figsize = (40, 20), 
                    save_fig = False, pp = None):
    
# we pass the dataframe and choose the size of the pints in the scatter plot 
# we choose whether or not we save the figure in a PDF
# pass the file for the pdf 
# the key there is not just that we are using Python to create visualizations, 
# which is really powerful to begin with, but we are actually using python 
# to automate the whole process and so we can have 10 varriables and create 
#200 visualizations in a skestroke

# gather variables from dateframe 
 plot_vars = list(df.keys())
 # we have our plot variables which are just the keys we are passing 
 # a whole data frame or a slice of the dataframe 

# cycle through each variable for x value 
 for x in plot_vars:
 # we cycle through the plot variables 
 # cycle again for y value 
       for y in plot_vars:
# make sure that  x does not equal y 
           if x != y:
 # we check that x and y variables are not the same 
 
 
# we create a new image which is the fiture zie we create earlier 
# this is saying subplots has an options called figsize 
# and it happens that you passed a variable called figsize
# it happens that you passed a variable called fig size
# so the option is eual to the variable  
# option os equal 
                fig, ax = plt.subplots(figsize = figsize)
                # Create list of years from index
                # Year will be represented by color
                # years are the color value 
                # we are going to draw the years from the index, but we can 
                # just create a year value in the dateframe to say if you are not 
                # in the data, not in the keys 
                
                # Var3 also called Z means year 
                # replace in python using Control R 
                
                # this is to check if we have made a column called year 
                if "Year" not in df.keys():
                    # create list from index
                    # convert each index value to string 
                    # only include first 4 characters, which is the year 
# this says we create data for the year and draw that data from a list 
# the list is composed of elemments from the index,so create the lists from index 
# the lists also include time, turn that index data into a string 
# from that string, we take the first 4 chacters which is the year 
# create an integer from those chacters, in another word, convert it back to 
# a numeric, the reason why we have to do becuase index is a special format 

# this is the most complicated part of this section is getting the year 
# to format correctly 

# if we have not made a column called year, we have to make a column 
# if we did, we can skip 
                    df["Year"] = [int(str(ind)[:4]) for ind in df.index] 
                
                
# choose our variables 
# our x values in the scatter plot is going to be the first variable
# plot from the dataframe and it is a scatter 
# the x value or the horizontal value on the horizontal axis is to be variable one 
# values on the Y axis is going to be the variable until we already chose the size 
# which is 75 
# we could show four dimensions in this plot 
# ax tells us plots on this visualization
# c means color here showing the year because we are plotting from the dataframe 
# what we need to do is to tell python about what we want to use the year column 
# to color the data

                df.plot.scatter(x = x, y = y, s = s, ax = ax, 
                                c = "Year", cmap = "viridis")
                
                # Turn the text on the x-axis so that it reads vertically
                # we do not want them to be horizontal and rotate them 90 degrees 
                ax.tick_params(axis='x', rotation=90)
                # Get rid of tick lines perpendicular to the axis for aesthetic
# this says on both x and y both make the length as 0 and the line disappear 
                ax.tick_params('both', length=0, which='both')
                # save image if PdfPages object was passed
                if save_fig:
                    # try to create a new folder 
                    try:
                        os.mkdir("plots")
                        # if it does not exist, we just move on 
                    except:
                        pass
                    # save the figure in the folder 
                    # identify directory to save fiture 
                    
                    directory = "plots/" + x[:12] + " " + y[:12] + " c=Year"
                    plot.savefig()
                    plt.savefig(directory + ".png")
# we save the figure in a PDF
# this says you pass the pdf which means pp here, if it does not equal none
# if you pass someting do it and then save the figure in the PDF 
# it says if you pass the pdf file which is pp here and if it does not equal to none 
# if you pass something and then save the figure in the pdf 
# the reason why save as a pdf instead of png is that it holds all of the files 
# if want to view different files, it is just a matter of pressing left or right 
# and then we can view the change over time, this is nice way to navigate and understand the data 
# when we relate to the reaserch, before we do the regression, plot the data first to show the correlation 
                    if pp != None: pp.savefig(fig, bbox_inches = "tigh)

