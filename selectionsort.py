
mylist = [4, 8, 17, 3, 2]

for i in range(len(mylist)): #0,1,2,3,4 - the nested loop below is called 5 times.

    minValue = i #0


    #print 'mylist = ', mylist

    #element = i + 1    range(1, 5) - 1,2,3,4
    for element in range(i + 1, len(mylist)):

        print 'element = ', mylist[element]

        #if element is < than minValue in list
        #element now = minValue.
        if mylist[element] < mylist[minValue]:
            print 'swap', mylist[minValue], 'with', mylist[element]
            minValue = element


    #Loop has finished one iteration through the list:
    #swap minValue with mylist[i]
    mylist[minValue], mylist[i] = mylist[i], mylist[minValue]

print 'Final Sorted List : ', mylist
