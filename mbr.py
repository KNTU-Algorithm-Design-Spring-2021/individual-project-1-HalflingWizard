"""
Minimum Bounding Rectangle Finder:
this script takes a list of n points as input and then outputs four corners of the smallest rectangle that covers all points. 
I hope it will work with time complexity of O(n)
- Mohammad Namvarpour (Halfling Wizard)
Student number: 9920354 
"""

# import necessary libraries
from time import time 
import random
from util_functions import efficent_minmax_finder

# I ask the user to give the number of points
n_points = int(input('How many points?'))

# Let's start the timer!
start_time = time()

# now I create a list of random X and Y coordinates
# random number is between -1000 and 1000
x_list = []
y_list = []
for point in range(n_points):
    x_list.append(random.random() * 2000 - 1000)
    y_list.append(random.random() * 2000 - 1000)

# this is the main part of code: find min and max of X and Y Coordinates
# I used a function that I wrote in 'util_functions.py' that finds min and max numbers in an array with 3n/2 comparisons.
min_y, max_y = efficent_minmax_finder(y_list)
min_x, max_x = efficent_minmax_finder(x_list)

# now I find four corners of rectangle
top_right = (max_x, max_y)
top_left = (min_x, max_y)
bottom_right = (max_x, min_y)
bottom_left = (min_x, min_y)

# stop the timer!
end_time = time()
elapsed = end_time - start_time

# print the outcome
print("Done!")
print("{} points processed in {} seconds".format(len(x_list),elapsed))
print("Rectangle Corners:\n top left:{} \n top right:{} \n bottom left:{} \n bottom right:{}".format(top_left, top_right, bottom_left, bottom_right))