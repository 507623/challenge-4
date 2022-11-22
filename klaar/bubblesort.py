## BUBBLE SORT ##

def bubbleSort(arr):
    n = len(arr)

    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped : True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
        if not swapped :
            return


arr = [62,11, 12, 73, 34]

bubbleSort(arr)

print("De gesorteerde Array is: ")
for i in range(len(arr)):
    print("% d" % arr[i], end="  ")