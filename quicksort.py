
from random import randint


#This function applies quicksort to an unsorted list.
#And returns a sorted list.
def quicksort(mylist):


    if len(mylist) <= 1:
        return mylist #If the list is 1 element, it is already sorted.

    #These lists hold the elements smaller, equal and larger than the pivot.
    smaller, equal, larger = [], [], []

    #pivot = mylist[len(mylist) - 1] #Choose the last element as the pivot
    pivot = mylist[len(mylist) - 1]


    # Each iteration will compare each element with the pivot
    # And place it in the approriate list.
    for i in mylist:

        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)

    return quicksort(smaller) + equal + quicksort(larger)



mylist = [6, 4, 7, 3, 2]

sortedList = quicksort(mylist)

print sortedList
