
def mergeSort(mylist):

    print("Splitting ",mylist)

    if len(mylist) > 1: #base case

        midIndex = len(mylist) / 2

        leftList = mylist[:midIndex]
        rightList = mylist[midIndex:]

        mergeSort(leftList)
        mergeSort(rightList)

        leftIndex = 0
        rightIndex = 0
        mylistIndex = 0

        while leftIndex < len(leftList) and rightIndex < len(rightList):

            if leftList[leftIndex] < rightList[rightIndex]:

                mylist[mylistIndex] = leftList[leftIndex]
                leftIndex += 1

            else:

                mylist[mylistIndex] = rightList[rightIndex]
                rightIndex += 1

            mylistIndex += 1



        while leftIndex < len(leftList):
            mylist[mylistIndex] = leftList[leftIndex]

            leftIndex += 1
            mylistIndex += 1

        while rightIndex < len(rightList):
            mylist[mylistIndex] = rightList[rightIndex]

            rightIndex += 1
            mylistIndex += 1

    print 'merging', mylist



mylist = [54,26,93,17,77,31,44,55,20]


mergeSort(mylist)
