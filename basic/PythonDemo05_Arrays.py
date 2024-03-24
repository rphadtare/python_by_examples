# This file gives demo about array
from array import *

# creating array of integers and empty array of float
i_arr = array('i', [10, 20, 30])
f_arr = array('f')

# Traverse array
for i in range(len(i_arr)):
    print("arr[", i, "]", " - ", i_arr[i])

# insert elements using append and insert method
f_arr.append(11)  # no need of index in append method as it will append at end position
print("11 is appeneded in f_arr")
f_arr.insert(0, 22)  # insert will need index to insert value at that position and adjust old values post insertion
print("22 is inserted in f_arr at 0 index")
f_arr.insert(5, 33)  # if index is not present then it will add at current last_index + 1 position
print("33 is inserted in f_arr at 5 index")

# update element at last position in arr1
print("f_arr - ", f_arr)
f_arr[-1] = 55
print("Post update of element at last position f_arr is - ", f_arr)

# delete element from array
print("Deleting element from i_arr - ", i_arr[0])
del i_arr[0]
print("i_arr post deletion - ", i_arr)

# search element in array
ele = input("enter number to search")
cnt = 0

for i in range(len(i_arr)):
    if i_arr[i] == int(ele):
        print("Number {} found at {} position in i_arr".format(ele, i))
        cnt += 1

if cnt == 0:
    print("number {} is not present in i_arr ".format(ele))

# using in operator
print("Number {} is present in i_arr : ".format(ele), int(ele) in i_arr)
