#Biggie Size
def biggieSize(myList):
    for i in range(len(myList)):
        if myList[i] > 0:
            myList[i] = "big"
    return myList
# print(biggieSize([-1,2,-3,4,-5]))

#Count Positives
def countPos(myList):
    count = 0
    for i in range(len(myList)):
        if myList[i] > 0:
            count+=1
    myList[len(myList)-1] = count
    return myList
# print(countPos([1,-2,3,-4,5,-6]))

#Sum Total
def sumTotal(myList):
    sum = 0
    for item in myList:
        sum += item
    return sum
# print(sumTotal([1,2,3,4]))

# Average
def getAvg(myList):
    avg = 0
    for item in myList:
        avg+=item
    avg = avg/len(myList)
    return avg
# print(getAvg([1,2,3,4,5,6]))

# Length
def getLen(myList):
    myLen = 0
    for i in myList:
        myLen+=1
    return myLen
# print(getLen([1,2,3,4,5]))

# Minimum
def getMin(myList):
    if getLen(myList) == 0:
        return False
    min = myList[0]
    for i in myList:
        if i < min:
            min = i
    return min
# print(getMin([1,2,3,-4,5]))

# Maximum
def getMax(myList):
    if getLen(myList) == 0:
        return False
    max = myList[0]
    for i in myList:
        if i > max:
            max = i
    return max
# print(getMax([1,2,3,4,5,5,8,4]))

# Ultimate Analysis
def ultAnalysis(myList):
    listStats = {
        'sumTotal' : sumTotal(myList),
        'average' : getAvg(myList),
        'minimum' : getMin(myList),
        'maximum' : getMax(myList),
        'length' : getLen(myList),
    }
    return listStats
# print(ultAnalysis([1,2,3,4,5,6,7,8,9,10]))

# Reverse List
def revList(myList):
    if len(myList) == 0:
        return False
    elif len(myList) == 1:
        return myList
    for i in range(int(len(myList)/2)):
        temp = myList[i]
        myList[i] = myList[(len(myList) - i - 1)]
        myList[(len(myList) - i - 1)] = temp
    return myList
# print(revList([1,2,3,4,5]))