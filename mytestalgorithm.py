
# This function merges the left and right lists together
def merge(left, right):

    sortedlist = [] # The final list to hold the sorted list
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

# This function keeps dividing the list in half, until all elements are in 1 list.
def mergesort(mylist):

    #THIS IS THE BASE CASE TO STOP THE RECURSIVE CALLS
    if len(mylist) <= 1: #When the base case is triggered, start returning mylist
        return mylist    #Return [1][2][77][9][66][21]
                         #If the list only contains 1 element, it's already sorted


    midpoint = int(len(mylist) / 2)     #The midpoint is used to divide the list in half.
    left = mergesort(mylist[:midpoint]) #Keep recursively calling the function, dividing the list in half, until base case (above) is triggered.
    right = mergesort(mylist[midpoint:])

    print 'left', left
    print 'right', right
    return merge(left,right) #Pass the left and right elements to the function 'merge'

mylist = [1, 2, 77, 9, 66, 21]

print mergesort(mylist)
