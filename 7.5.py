# TODO 7.5 List Methods and Useful Built-in Functions
# Complete the following code to append the last three months of the year to the list months. Remove
# the """   """ to test, and print the contents of months

months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])

# get the index of "May" from the months list and print it on screen

print(months[4])

# sort list3 from the 7.2 exercise and print the results on screen

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
list3.sort()
print(list3)

# reverse the order of list 3

list3.reverse()
print(list3)

# delete the number 5 from list 3 and print the list(remeber we reversed the list)

del list3[5]
print(list3)

# print the maximum item from list 3

print(max(list3))
