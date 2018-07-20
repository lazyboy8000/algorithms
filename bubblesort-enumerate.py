mylist = [4, 8, 17, 3, 6]


for t in range(len(mylist)):

    #nested loop causese O(n ^ 2)
    for i, j in enumerate(mylist[:-1]): #Slice last element to stop 'out of range'

        #swap adjacent elements with simultaneous assignement
        if mylist[i] > mylist[i + 1]:
            mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]

print 'mylist = ', mylist
