

mylist = [1, 2, 3, 4, 5, 6]

def merge(left, right):
    print left, right
    #pass

def mergesort(mylist):

    if len(mylist) < 2: # base case
        return mylist   # stores the values [1][2][77][9][66][21]
    else:


        middleIndex = len(mylist) / 2


        print 'mylist = ', mylist
        print 'middleIndex = ', middleIndex
        print 'mylist after left', mylist[:middleIndex]
        print '--------------------------------------------'

        left = mergesort(mylist[:middleIndex])
        right = mergesort(mylist[middleIndex:])

        #When the right recursion call is finished, merge left and right.
        #return merge(left, right)
        #print left, right
        return merge(left, right)

mergesort(mylist)







"""def merge(left,right):

    #print 'START MERGE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    sortedlist = [] # The final list to hold the sorted list, reset to = [] each time this function is called.
    i = 0 #index counter for left
    j = 0 #index counter for right

    # While this is true, keep appending right and left to the sortlised.
    #'i' will eventually have an index value higher than the len(mylist)
    # therefore break the loop.
    while i < len(left) and j < len(right):

        if left[i] <= right[j]: # If left index is less than right index
            sortedlist.append(left[i]) # Append to sortedlist
            i += 1
        else:
            sortedlist.append(right[j])
            j += 1

    # If all elements from right have been appended :
    # append the rest of elements from left to sortlisted.
    sortedlist += left[i:]
    sortedlist += right[j:]

    return sortedlist # return the sortedList





def mergesort(mylist):

    if len(mylist) < 2:
        return mylist #base cases, stores the values [1][2][77][9][66][21]
    else:
        middleIndex = len(mylist) / 2
        left = mergesort(mylist[:middleIndex])
        right = mergesort(mylist[middleIndex:])

        #When the right recursion call is finished, merge left and right.
        return merge(left, right)
        #print left, right

print mergesort(mylist)"""





"""
def mergesort(mylist):

    if len(mylist) < 2:
        return mylist #base cases, stores the values [1][2][77][9][66][21]
    else:
        middleIndex = len(mylist) / 2
        left = mergesort(mylist[:middleIndex])
        right = mergesort(mylist[middleIndex:])

        #When the right recursion call is finished, merge left and right.
        #return merge(left, right)
        print left, right

mergesort(mylist)"""




"""mylist = [1,77,3,9,5,6]

def mergesort(mylist, first, last):

    print 'mylist = ', mylist

    if first < last:

        middle = (first + last) // 2
        print middle

        mergesort(mylist, first, middle)
        mergesort(mylist, middle + 1, last)

        print mylist



mergesort(mylist, 0, len(mylist) - 1)"""
