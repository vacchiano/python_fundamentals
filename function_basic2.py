#countdown
def countdown(num):
    downList = []
    for i in range(num, -1, -1):
        downList.append(i)
    return downList
# a = countdown(10)
# print(a)

#Print and Return
def printReturn(myList):
    print(myList[0])
    return myList[1]
# print(printReturn([1,2]))

#First Plus Length
def firstPlusLen(myList):
    return myList[0] + len(myList)
# print (firstPlusLen([1,2,3]))

#values greater than second
def valGreater(myList):
    max = myList[1]
    newList = []
    if len(myList) < 3:
        return False
    for item in myList:
        if item > max:
            newList.append(item)
    print (len(newList))
    return newList
# print(valGreater([3,2,3,1,3,4]))

#This Length, That Value
def lenValue(theLen, theVal):
    myList = []
    for i in range(theLen):
        myList.append(theVal)
        i+=1
    return myList

# print(lenValue(5,3))