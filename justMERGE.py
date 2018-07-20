


def merge(leftList, rightLeft):

    finalList = []

    leftIndex = 0
    rightIndex = 0


    while leftIndex < len(leftList) and rightIndex < len(rightList):

        #If leftIndex is higher, append to finalList
        if leftList[leftIndex] < rightList[rightIndex]:

            finalList.append(leftList[leftIndex])
            leftIndex += 1
        else: #Else rightIndex is higher, append to finalList
            finalList.append(rightList[rightIndex])
            rightIndex += 1

    # If there is any remaining values in leftList or rightList - append it to the finalList
    finalList += leftList[leftIndex:]
    finalList += rightList[rightIndex:]

    return finalList


leftList = [1,2,5]
rightList = [3,4,8]

print merge(leftList, rightList)
