mylist = [4, 8, 17, 3, 6]

#the list will have to be iterated through multiple times, till fully sorted.
for j in range(len(mylist)):

    #nested loop causes O(n ^ 2)
    for i in range(len(mylist) - 1): # - 1 is used to stop 'out of index'
        print 'range = ', i

        #if adjacent value is higher,
        #then swap adjacent elements with simultaneous assignment
        if mylist[i] > mylist[i + 1]:
            mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]

print mylist
