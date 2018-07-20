

mylist = [3, 1, 10, 99, 77, 2]

for index in range(1, len(mylist)): #start at 1, finish at 6


    print 'collection = ', mylist

    # while 0 is less than index, adjacent value is less than it's next value
    #then swap adjacent elements with simultaneous assignment

    #
    while index > 0 and mylist[index] < mylist[index - 1]:
        print  'while loop called at index = ', index
        mylist[index], mylist[index - 1] = mylist[index - 1], mylist[index]
        index -= 1
        #print 'INDEXXXX = ', index

print mylist
