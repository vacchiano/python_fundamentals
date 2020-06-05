# Selection Sort Practice
# Dom Vacchiano

# Overview of algorithm
# Selection sort works by finding the smalled value and moving it all the way left, and finds the next lowest value, and so on.
# It doesn't need to iterate over the previously found mins since those are already sorted

testList = [4,1,7,3,6,2,5,9,8]

def checkList(myList):
    if (len(myList) == 0):
        return False
    elif (len(myList) == 1):
        return myList

def selectionSort(myList):
    checkList(myList)
    for i in range(len(myList)):
        min = [myList[i], i]
        #print("="*10,"loop", i, "| min:", min[0], "="*10)
        #print ("*"*10, myList, "*"*10)
        for j in range(len(myList)-i):
            if myList[i+j] < min[0]:
                min = [myList[i+j], i+j]
            if j == (len(myList)-i-1):
                myList[min[1]], myList[i] = myList[i], myList[min[1]]
                #print("LAST")
            #print(j, "j loop", myList[i+j], "| min:", min[0])
    #print ("*"*10, "FINAL LIST", myList, "*"*10)
    return myList

print(testList)
print(selectionSort(testList))