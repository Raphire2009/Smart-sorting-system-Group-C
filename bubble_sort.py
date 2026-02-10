arr = [64, 34, 25, 12, 22, 11, 90]

def b_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
           
           if arr[j] < arr[j + 1]:
               temp = arr[j]
               arr[j] = arr[j + 1]
               arr[j+1] = temp
               swapped = True
        if not swapped:
            break
    return arr


ar = b_sort(arr)
print(ar)