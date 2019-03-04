def countingInversions(aList, length):
    halfLength = length/2
    if length < 2:
        return 0
    else:
        X = countingInversions(aList[:length/2], half)
        Y = countingInversions(aList[length/2]:)

data = [1, 3, 5, 2, 4, 6] #3

print(countingInversions(data, len(data))
