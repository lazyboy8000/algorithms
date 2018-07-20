

mylist = [1, 2, 3, 4, 5, 6]


def binarySearch(mylist, item):

    lowIndex = 0
    highIndex = len(mylist) - 1

    while lowIndex <= highIndex:

        middleIndex = (lowIndex + highIndex) / 2
        print middleIndex # 2,

        if item == mylist[middleIndex]:
            return '%d found at position %d' % (item, middleIndex)
        elif item < mylist[middleIndex]:
            highIndex = middleIndex - 1  #Set highIndex to middle element || disregard all elements above mid.
        elif item > mylist[middleIndex]:
            lowIndex = middleIndex + 1  #Set the lowIndex to the middle element || disregard all element below mid.

print binarySearch(mylist, 5)
