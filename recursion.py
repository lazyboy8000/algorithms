
"""def countdown(number):


    if number <= 0:
        print 'Base case trigered'
        #return number
        return number
    else:
        print number
        return countdown(number - 1)


print countdown(4)"""


def printMerge(ok):

    print 'printint', ok

def mergesort(mylist):

    #THIS IS THE BASE CASE TO STOP THE RECURSIVE CALLS
    if len(mylist) <= 1: #When the base case is triggered, start returning mylist
        #print mylist
        return mylist    #Return [1][2][77][9][66][21]
                         #If the list only contains 1 element, it's already sorted


    midpoint = len(mylist) / 2     # The midpoint is used to divide the list in half.
    print 'midpoint', midpoint

    ok = mergesort(mylist[midpoint:])

    return printMerge(ok)

    #left = mergesort(mylist[:midpoint])  # Keep recursively calling the itself (the function), -
    #right = mergesort(mylist[midpoint:]) # dividing the list in half, until base case (above) is triggered.

    #eventually : left = [1,2,77]  right = [9,21,66]
    #return merge(left,right) #Pass the left and right elements to the function 'merge'

mylist = [1, 2, 77, 9, 66, 21]

print mergesort(mylist)










# This function keeps dividing the list in half, until all elements are in 1 list.
"""def mergesort(mylist):

    #THIS IS THE BASE CASE TO STOP THE RECURSIVE CALLS
    if len(mylist) <= 1: #When the base case is triggered, start returning mylist
        #print mylist
        return mylist    #Return [1][2][77][9][66][21]
                         #If the list only contains 1 element, it's already sorted


    midpoint = len(mylist) / 2     # The midpoint is used to divide the list in half.
    print 'midpoint', midpoint

    left = mergesort(mylist[:midpoint])  # Keep recursively calling the itself (the function), -
    right = mergesort(mylist[midpoint:]) # dividing the list in half, until base case (above) is triggered.

    #eventually : left = [1,2,77]  right = [9,21,66]
    #return merge(left,right) #Pass the left and right elements to the function 'merge'

mylist = [1, 2, 77, 9, 66, 21]

print mergesort(mylist)
"""








"""mylist = [1,2,3,4,5,6]
midIndex = len(mylist) / 2

def splitList(mylist, midIndex):

    leftList = mylist[:midIndex]
    rightList = mylist[midIndex:]

    if len(leftList) > 1 and len(rightList) > 1:


        print splitList()

    #sreturn splitList()



print splitList(mylist, midIndex)"""





"""
def mycountdown(number):

    if number <= 0:
        print 'Completed'
    else:


        countdown(number - 1)

        print 'number = ', number


        #print 'noob = ', noob
        return number



print mycountdown(5)

"""

"""

    if number == 0:
        print 'Completed'
    else:
        print number
        countdown(number - 1)
        return 'shit'


"""

"""

    while number >= 0:
        print 'Completed'
    #else:
        print number
        countdown(number - 1)
        return 100

"""
