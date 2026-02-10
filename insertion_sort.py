arr = [5, 1, 4, 2, 8]

def i_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

ar = i_sort(arr)
print("Sorted list is", ar)