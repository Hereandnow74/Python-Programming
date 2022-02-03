# -*- coding: utf-8 -*-
"""
Program: Commodity Data Visualization Project
Author: Mikhail Klepikov
Description: CSV Data visualization project
    Revisions:
    00 - open csv file
    01 - create textgraph
    02 - create visualization 
"""
# import all modules that we need for work
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import csv
from datetime import datetime
# there are no literal constants
# there are no class definitions
# there are no functions 

# announcement on the next line
with open('produce_csv.csv', 'r') as csvfile: # read csv file
    reader = csv.reader(csvfile)
    data = [row for row in reader]

    modData = [] # initialize new list to receive data
    for row in data: # traverse the rows
        newRow = list() # make an empty row to receive values
        for item in row: # traverse the values in the old row
            if "$" in item: # test for price string and convert
                newRow.append(float(item.replace("$", "")))
            elif "/" in item: # test for date and cconvert
                newRow.append(datetime.strptime(item, '%m/%d/%Y'))
            else: # otherwise append item (not a date or a price)
                newRow.append(item)
        modData.append(newRow)

    locations = modData.pop(0) [2:] # remove header and slice
    records = list() # create new empty list for data records
    for row in modData: # traverse each row
        newRow = row[:2] # first two values are common for all five locations
        for loc, price in zip(locations, row[2:]): # traverse locations and prices
            records.append(newRow + [loc, price]) # add a new data record
            
#   # filter data by creating a list to contain prices recorded for Oranges in Chicago
    select = list(filter(lambda x: x[0]=="Oranges" and x[2]=="Chicago", records))
#   ###! dates and prices to plot
    dates = [ x[1] for x in select ]
    prices = [ x[3] for x in select ]
    dpMerge = [ [d,p] for d,p in zip(dates, prices) ]
    dpMerge.sort(key = lambda a: a[0])
    
    ###! Create textgraph 
    for x in dpMerge:
        print(f'{datetime.strftime(x[0], "%m-%d-%Y")} {int(25*x[1])*"="}')

    # establish the figure and the subplot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # plot the data
    ax.plot(dates,prices,label="Oranges in Chicago")
    # create a font for title
    font1 = {'weight':'bold', 'size':14}
    # create a title
    plt.title("The Cost of Oranges in Chicago", fontdict = font1)
    # set the axis labels
    ax.set_xlabel('Date')
    ax.set_xlabel('Price in Dollars')
    # add legend in best location
    leg = plt.legend(loc='best')
    # format the y-axis to show dollsrs and cents
    fmt = '${x:,.2f}' # format for dollars w/ 2 decimal places
    tick = mtick.StrMethodFormatter(fmt) # define the format
    ax.yaxis.set_major_formatter(tick)
    # plot the legend and show the graph
    plt.legend()
    plt.show()
    # open and output file
    resultfile = open('result.csv', 'w')
    # initiate a csv wrier for the output file
    # change EOL defaults to prevent blank lines
    writer = csv.writer(resultfile,lineterminator='\n')
    writer.writerows(data) # write the organized data to the file
    resultfile.close() # close the output file
