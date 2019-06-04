def insertionSort1(length, arr):
  l = arr[::-1]
  ref = l[0]

  for number in range(1, length):

    if ref < l[number]:
      l[number-1] = l[number]
      print(l[::-1])
    elif ref >= l[number]:
      l[number-1] = ref
      print(l[::-1])


# def insertionSort1(length, arr):
#   sorted_arr = []
#   l = arr[::-1]
#   ref = l[0]

#   for number in l[1:]:
#     if ref > number:
#       sorted_arr.append(ref)
#       ref = number
#     else:
#       sorted_arr.append(number)
#       sorted_arr.append(ref)

#   return sorted_arr[::-1]
