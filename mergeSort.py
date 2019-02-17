def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",alist)


while True:
    print("Sort the list using merge sort.  Give a list of numbers inside [] 'q' to quit, hit 'Enter' to see \n")
    #list = input()

    str_arr = input().split(' ')
    arr = [int(num) for num in str_arr]

    # make this into an array
    if str_arr == 'q':
        print("Thank you \n")
        break
    else:
        answer = mergeSort(arr)
        print("Your answer is", answer, "\n")
