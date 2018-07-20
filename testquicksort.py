

# Each time this algorithm is called,
# it's called on a subset of the list every time.

def quicksort(listToSort, lowIndex, highIndex):



    # base case to stop recursion calls

    if ((highIndex - lowIndex) > 0):

# start by keep partitioning

# original listToSort = [1, 0, 2, 3, 4, 6, 5, 8, 9, 7]
# call to function = quicksort(listToSort, 0, 9)


        print listToSort
        print lowIndex
        print highIndex
        print '--------------------------------'

        p = partition(listToSort, lowIndex, highIndex)

#once the partition is complete, this give you two sublists to sort
# Therefore, you need to call quicksort another two times.


#highIndex = p - 1, since we know the pivot is in the correct position
# sort the low sublist, left of pivot
# the left sublist is called recursively, until the left sublist is finished sorted.

        #print listToSort
        #print p - 1
        #print '------------------------------'



        quicksort(listToSort, lowIndex, p - 1)

# lowIndex = p + 1, since we know the pivot is in the correct position
# sort the high sublist, right of pivot
        quicksort(listToSort, p + 1, highIndex)



def partition(listToSort, lowIndex, highIndex):

    divider = lowIndex   #divider = first element in list
    pivot = highIndex    # pivot = last element in list


# compare every element in the list with the pivot

    # loops 8 times
    for i in range(lowIndex, highIndex):

        print '*************'
        print 'i = ', i
        print 'divider =', divider
        print '*************'

        #if i is less than pivot - then swap i with divider
        if (listToSort[i] < listToSort[pivot]):

            #swap i with divider
            listToSort[i], listToSort[divider] = listToSort[divider], listToSort[i]

            #Now increment the divider
            divider += 1

    # When partition is complete swap the pivot with the divider

    listToSort[pivot], listToSort[divider] = listToSort[divider], listToSort[pivot]


# now partition the sublists ?

    # now return the divider index - why?

    return divider


listToSort = [1, 0, 2, 3, 4, 6, 5, 8, 9, 7]

quicksort(listToSort, 0, 9)

print listToSort
