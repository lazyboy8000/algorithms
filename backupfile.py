

mylist = [2, 75, 3, 83, 1]


mylist = [2, 75, 3, 83, 1]

def merge(left, right):

    finalList = []
    i = 0 #counter for left index
    j = 0 #counter for right index

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            finalList.append(left[i])
            i += 1
        else:
            finalList.append(right[j])
            j += 1

    finalList += left[i:]
    finalList += right[j:]

    return finalList


def mergesort(mylist):

    if len(mylist) <= 1: #base case
        return mylist    #[1][2][3][4][5][6]

    middleIndex = len(mylist) / 2


    left = mergesort(mylist[:middleIndex])


    right = mergesort(mylist[middleIndex:])

    print 'merge, left = ', left, 'right = ', right

    return merge(left, right)

print mergesort(mylist)
