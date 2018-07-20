
userInput = input('Please enter a number from 1 - 10: ')

mylist = [1,2,3,4,5,6,7,8,9,10]




lowIndex = 0
highIndex = len(mylist) - 1

middleIndex = (lowIndex + highIndex) / 2


while userInput != mylist[middleIndex]:

    if userInput < mylist[middleIndex]:
        highIndex = middleIndex - 1
    elif userInput > mylist[middleIndex]:
        lowIndex = middleIndex + 1


    print 'middleIndex = ', middleIndex
    print 'lowindex = ', lowIndex, 'highIndex = ', highIndex

    userInput = input('Please enter a number from 1 - 10: ')


if userInput == mylist[middleIndex]:
    print '%d found at index position %d' % (userInput, middleIndex)
