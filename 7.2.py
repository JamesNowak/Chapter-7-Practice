# TODO 7.2 Lists
# Create a list of days of the week, assign it to the variable days, remove """ """ to test

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
numbers = [0] * 5


# print the contents of your days list using the for operator
for n in days:
    print(n)

# print the list item that holds the value Saturday from the days list by using it's index
print(days[5])

# set the size variable to hold the length of the list days using the len function
size = len(days)
print(size)
# concatenate the two following lists together, storing the value in list3 - remove the """ """ to test


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)

