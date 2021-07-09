## insertion sort

### algorithm is ->
#  1. for i = 1 to n
#  2.   key = A[i]
#  3.   j = i-1
#  4.   while j >0 and A[j] > key:
#  5.         A[j+1] = A[j]
#  6.         j = j-1
#  7.   A[j+1] = key


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        print(key)
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr



arr = [31,22,73,44,6,33]
print(insertion_sort(arr))