# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:35:07 2017

@author: aryay
"""

def door_calc(N = 5):
    # calcuate the doors which will be open or closed at the end of the sequence
    array = []
    for ii in range (1, N+1):
        array.append(1)
        for jj in range (1, ii):
            if ii%jj == 0 :
                array[jj-1] = 1 - array[jj-1]
    return array
    

#### Main caller for the functions
num_doors = int(input("Enter number of doors..."));
#print (door_calc(num_doors))
i = 0
array = door_calc(num_doors)
open_doors = 0
closed_doors = 0
while i < len(array):
    if array[i] == 1:
        open_doors = open_doors + 1
    else:
        closed_doors = closed_doors + 1
    i = i+1
print ("Closed doors:", closed_doors, "\nOpen doors:", open_doors)