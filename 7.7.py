# TODO 7.7 Processing lists
# total the values in list3 and print the results
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(len(list3))
# get the average of values in list 3 and print the results
total = 0.0

for value in list3:
    total += value

average = total / len(list3)
print(average)
# open the file states in read mode, read the contents of the file into the list states_list and print the
# contents of states_list on screen
states = open('states.txt', 'r')

for n in states:
    print(n)
