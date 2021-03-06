#!/usr/bin/python3

# This script analyzes the height of Molly and her friends

inches_in_meter = 39.4 # the number of inches in a meter
inches = 64 # Molly's height in inches
meters = 64/39.4 # Molly's height in meters


heights = [1.65, 1.75, 1.55, 1.78, 1.83] # list of height of Molly's friends
heights.append(meters) # height of height of Molly's friends and Molly


# calculate the mean of all of the heights
total = 0
for height in heights:
    total = total + height

mean = total/len(heights)
print(mean)

sum_diffsq = 0
for height in heights:
    diff = height-mean
    diff_sq = diff**2
    sum_diffsq = sum_diffsq + diff_sq

variance = sum_diffsq/(len(heights)-1)
print(variance)
