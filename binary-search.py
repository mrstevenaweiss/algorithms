def makeList(number_string):
    numberList = [int(s) for s in number_string.split(',')]
    return numberList

def binary_search(item, numbers):
    arr = makeList(numbers)

    def _binary_search(item, first, last, arr):
        item = int(item)
        if last < first:
            return False
        if last == first:
            return arr[last] == item
        mid = (first + last) // 2
        if arr[mid] > item:
            last = mid
            return _binary_search(item, first, last, arr)
        elif arr[mid] < item:
            first = mid + 1
            return _binary_search(item, first, last, arr)
        else:
            return arr[mid] == item
    return _binary_search(item, 0, len(arr) - 1, arr)

while True:
    print("Find the position of a number in sequence. 'q' to quit, hit 'Enter' to see \n")

    print('Type a number sequence: i.e. 12, 1, 5')
    a = input()
    print('Type the number you want to find in sequence: ')
    b = input()

    if a == 'q' or b == 'q':
        break
    else:
        answer = binary_search(a, b)
        print("Your answer is", answer, "\n")
