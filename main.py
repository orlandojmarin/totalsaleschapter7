"""
Name: Orlando Marin
Date: December 26, 2024

Design a program that asks the user to enter a store’s sales for each day of 
the week. The amounts should be stored in a list. Use a loop to calculate the 
total sales for the week and display the result.
"""

# create a list that has each day of the week
daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# create an empty list that will hold the sales from each day
dailySales = []

# initialize the weekly sales total to 0
weekSalesTotal = 0

# iterate through the daysofweek list and ask the user for the sales each day
# append the sales from each day to the dailySales list 
for day in daysOfWeek:
    daySales = float(input(f"Enter the sales on {day}: "))
    dailySales.append(daySales)

# now iterate through the daily sales list and add them all up to get
# the weekly sales total
for sales in dailySales:
    weekSalesTotal += sales

# print the result and round to 2 decimal places
print(f"Total sales for the week: ${weekSalesTotal:,.2f}")
    
    