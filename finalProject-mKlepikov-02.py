'''
Program: Final Project
Author: Klepikov Mikhail
Purpose: Program is used to visualise the date, wi the use of plotly
Revisions:
    00 - Open csv file and reading the data
    01 - Filter data
    02 - Create bar graph using plotly
'''
import csv # Read csv file
from datetime import datetime # import datetime module
import plotly.offline as py # import plotly.offline to be able create graph offline
import plotly.graph_objs as go # import plotly.graph_objs to be able to plot bar graphs


# there are no literal constants
# there are no class definitions
# there are no functions

# announcement on the next line
print('='*len('Analysis of Commodity Data'))
print('Analysis of Commodity Data')
print('='*len('Analysis of Commodity Data'))

# Read the data table from the file and verify that all records have been accurately read into a list of lists <data>.
with open('produce_csv.csv') as s:
    reader = csv.reader(s)
    data = [ row for row in reader]
    location = data.pop(0)[2:] # pop off the column headings and slice to obtain a list of locations

# initialize new lists to receive data
modData = []
records = []
user_com = []
new_dates = []
new_locations = []
final_dict={}
final_chart = []
   
# Traverse <data> and change all date strings to datetime objects and price strings to float
for row in data: # traverse the rows
    newRow = list() # make an empty row to receive values
    for item in row: # traverse the values in the old row
        if '$' in item: # test for price string and convert
            newRow.append(float(item.replace('$','')))
        elif '/' in item: # test for date and cconvert
            newRow.append(datetime.strptime(item, '%m/%d/%Y'))
        else: # otherwise append item (not a date or a price)
            newRow.append(item)
    modData.append(newRow)


# Traverse <data> and convert the tabular format to individual records <records>
for row in modData: # Each row in data will contain five data records, one for each city
    newRow = row[:2]
    for loc, price in zip(location, row[2:]): # traverse locations and prices
        records.append(newRow +[loc,price]) # add a new data record  

# Extract a list of product strings from the data records without duplicates
# Sort the list and print each product and the index associated with it
commodityLst = list(set([x[0] for x in data])) 
for x,y in enumerate(commodityLst,0):
    if x % 3 != 0 and x != 0: # print 3 data in a line
        print(f'<{x:2}> {y:20}', end = '')
    else:
        print
        print(f'<{x:2}> {y:20}', end = '')

# Ask the user to type indexes instead of product names
while True:
    a = True
    productIndex = input("Enter product numbers separated by spaces: ")
    productIndex = productIndex.split()
    productIndex = [ int(x) for x in productIndex ]
    if max(productIndex) < len(commodityLst):
        break

# Use the index numbers provided by the user to create a list of product strings to select.  
for comIndex in productIndex:
    user_com.append(commodityLst[int(comIndex)])
    
# Verify the interaction (print the chosen product strings)
print(f'Selected products: {", ".join(user_com)}\n')

# Extract a list of dates from the data records without duplicates.
# Sort the list and print each date and the index associated with it.
select = list(filter(lambda x: x[0] in user_com, records))  
dates = list(set([x[1] for x in select])) 
dates.sort() 
select.sort(key= lambda a: a[1])

print("SELECT DATE RANGE BY NUMBER ...")

# Determine the earliest and latest date available in the data and print them out.
for x,y in enumerate(dates,0):
        print(f"<{x:2}> {datetime.strftime(y, '%m/%d/%Y'):<13}",end=' ')

print(f"\nEarliest available date is: {datetime.strftime(dates[0], '%m/%d/%Y')}")
print(f"Latest available date is: {datetime.strftime(dates[-1], '%m/%d/%Y')}")

# Ask the user to specify a start and end date by giving the index numbers.  
while True:
    user_dates = input("Enter start/end date numbers separated by a space: ")
    user_dates = user_dates.split()
    user_dates = [int(x) for x in user_dates]
    if max(user_dates) < len(dates) and len(user_dates) == 2:
        break

# Use the index numbers provided by the user to assign datetime objects to variables representing the start and end times
for x,y in enumerate(dates, 0):
    if int(user_dates[0]) <= x <= int(user_dates[1]):
        new_dates.append(y)
        
# Verify the interaction (print the chosen start/end dates, make sure the start date precedes the end date).
new_data = list(filter(lambda x: x[1] in new_dates, select))
print(f"Dates from {datetime.strftime(new_data[0][1], '%m/%d/%Y')} to {datetime.strftime(new_data[-1][1], '%m/%d/%Y')}\n")

print("SELECT LOCATIONS BY NUMBER ...")
# Sort the list of location strings, print each location along with its index.
for x,y in enumerate(location):
    print(f"<{x:2}> {y}")

# Ask the user to specify the locations of interest by giving index numbers.
while True:
    user_locations = input("Enter location numbers separated by space: ")
    user_locations = user_locations.split()
    user_locations = [ int(x) for x in user_locations ]
    if max(user_locations) < 5:
        break



# Use the index numbers to create a list of desired location strings.
for x in user_locations:
    new_locations.append(location[int(x)])
print(f'Selected locations: {", ".join(new_locations)}')

#Verify the interaction (print the location strings for the user to see).
finalData = list(filter(lambda x: x[2] in new_locations, new_data))
print(f"{len(finalData)} has been selected.")


"""
Select the data records that meet the criteria given: date range, selected products and selected cities
Organize the selected data records in a dictionary with two keys: product and location.
Each product and location will refer to a list of prices that spans the selected dates.
There's no need to include the dates here.
The list of prices is necessary to compute the average price.
Verify each list of prices.
Traverse the dictionary and replace each list with the average of the prices in the list
"""
for x in new_locations:
        final_dict[x] = {}
        
for z in finalData:
    for y in new_locations:
        for x in productIndex:
            if z[0] == commodityLst[int(x)] and z[2] == y: 
                if not commodityLst[int(x)] in final_dict[y]:
                    final_dict[y].update({commodityLst[int(x)]:z[3]})
                else: 
                    final_dict[y].update({ commodityLst[int(x)] : final_dict[y][commodityLst[int(x)]] + z[3]})

for x in final_dict:
    for y in final_dict[x]:
        count = len(list(filter(lambda z: z[0] == y and z[2] == x, new_data)))
        final_dict[x][y] = final_dict[x][y] / count


# Now you've compiled all the data you need to generate the grouped bar graph
for z in new_locations:
    final_chart.append(go.Bar(x = list(final_dict[z].keys()), y = list(final_dict[z].values()), name = z))
"""
# Create a title string for the graph
lay = go.Layout(barmode = 'group', title= f"Produce Prices from {datetime.strftime(new_data[0][1], '%m/%d/%Y')} to {datetime.strftime(new_data[-1][1], '%m/%d/%Y')}")
fig = go.Figure(data=final_chart, layout=lay)
fig.update_layout(legend_title_text = "Locations")
fig.update_xaxes(title_text="Product")
fig.update_layout(yaxis_tickformat = '$')
fig.update_yaxes(title_text="Average Prices")
py.plot(fig, filename = 'Plot bar.html') # creating offline html file of the chart
"""