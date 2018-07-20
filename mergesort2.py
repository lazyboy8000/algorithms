
# **********************************************************************************
# This function merges leftList & rightList together into finalList. These lists are already sorted.
def merge(leftList, rightList):
    finalList = [] # The final list to hold the sorted list, reset to = [] each time this function is called.
    leftIndex = 0 #index counter for leftList
    rightIndex = 0 #index counter for rightList

    # While the index < length of the list, keep appending the listLEFT and listRIGT to the finalList.
    while leftIndex < len(leftList) and rightIndex < len(rightList):

        # If leftList[0] <= rightList[0] - append it to finalList
        if leftList[leftIndex] <= rightList[rightIndex]: # If left index is less than right index
            finalList.append(leftList[leftIndex]) # Append to finalList
            leftIndex += 1  #Increment leftIndex by 1 to look at next value in list.
        else:
            finalList.append(rightList[rightIndex])
            rightIndex += 1

    # If there is any remaining values in leftList or rightList - append it to the finalList
    finalList += leftList[leftIndex:]
    finalList += rightList[rightIndex:]

    return finalList # return the list - [1,2,3,4,5,6]

# **********************************************************************************



# This function keeps dividing the list in half, until all elements are in 1 list.

# This functions does the SORTING.

def mergesort(mylist):



    #THIS IS THE BASE CASE TO STOP THE RECURSIVE CALLS
    if len(mylist) <= 1: #When the base case is triggered, start returning mylist
        print 'mylist,', mylist
        return mylist    #Return [1][2][3][4][5][6]
    else:



        midIndex = int(len(mylist) / 2)      # The midpoint is used to divide the list in half.

        print 'mergesort  for leftList has been called with mylist', mylist[:midIndex]

        leftList = mergesort(mylist[:midIndex])  # Keep recursively calling the itself (the function), -

        print 'mergesort  for rightList has been called with mylist', mylist[midIndex:]

        rightList = mergesort(mylist[midIndex:]) # dividing the list in half, until base case (above) is triggered.


        print '-----------------------------------------------'

    #print 'midIndex = ', midIndex
    #print 'leftlist = ', leftList
    #print 'rightlist = ', rightList
    #print '----------------------------------'

    #eventually : left = [1,2,77]  right = [9,21,66]
    #return merge(leftList, rightList) #Pass the left and right elements to the function 'merge'

mylist = [1, 2, 3, 4, 5, 6]



print mergesort(mylist)
