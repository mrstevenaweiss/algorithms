li = ["hellomore", "hello", "hedgehog"]
# // => "he"
#
# li = ["dog", "fox", "outfox"]
# // => ""


def longestCommon(li):
    newWord = ""
    firstWordLen = 1
    for letter in range(len(li[0])):
        if li[0][letter] == li[1][letter]:
            newWord += li[0][letter]
    return newWord

def longestCommon(li):
    newWord = ""
    firstWordLen = 1
    for letter in range(len(li[0])):
        if li[0][letter] == li[1][letter]:
            newWord += li[0][letter]
    return newWord

print(longestCommon(li))
#
# while True:
#     print("Sort the list using merge sort.  Give a list of numbers inside [] 'q' to quit, hit 'Enter' to see \n")
#     list = input()
#
#     # str_arr = input().split(' ')
#     # arr = [int(num) for num in str_arr]
#     # print(arr)
#
#     # make this into an array
#     if list == 'q':
#         print("Thank you \n")
#         break
#     else:
#         answer = longestCommon(list)
#         print("Your answer is", answer, "\n")
