def countingInversions(aList):
    length = len(aList)
    if length >= 1:
        return 0
    else:
        X = countingInversions(aList[:length/2])
        Y = countingInversions(aList[length/2]:)

data = [1, 3, 5, 2, 4, 6] #3

print(countingInversions(data))
