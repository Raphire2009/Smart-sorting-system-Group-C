arr = [29, 10, 14, 37, 13]

def s_sort(arr):
    for i in range(len(arr)):
        min_idk = i
        for j in range(i + 1, len(arr)):
            if arr[min_idk] > arr[j]:
                min_idk = j
        arr[min_idk], arr[i] = arr[i], arr[min_idk]
    return arr

sort = s_sort(arr)
print(sort)

"""
Pass 1 (i = 0)
i = 0, min_idx = 0 (initially points to 29)


Inner loop searches for minimum:

j = 1: arr[0] = 29 > arr[1] = 10? Yes - min_idx = 1
j = 2: arr[1] = 10 > arr[2] = 14? No  - min_idx = 1
j = 3: arr[1] = 10 > arr[3] = 37? No  - min_idx = 1
j = 4: arr[1] = 10 > arr[4] = 13? No  - min_idx = 1


Result: Minimum is 10 at index 1

Swap:

Before: [29, 10, 14, 37, 13]
        i=0      min_idx=1

After:  [10, 29, 14, 37, 13]
        sorted

Pass 2 (i = 1)
i = 1, min_idx = 1 (initially points to 29)


Inner loop searches for minimum:

j = 2: arr[1] = 29 > arr[2] = 14? Yes - min_idx = 2
j = 3: arr[2] = 14 > arr[3] = 37? No  - min_idx = 2
j = 4: arr[2] = 14 > arr[4] = 13? Yes - min_idx = 4


Result: Minimum is 13 at index 4

Swap:

Before: [10, 29, 14, 37, 13]
            i=1        min_idx=4

After:  [10, 13, 14, 37, 29]
            sorted

Pass 3 (i = 2)
i = 2, min_idx = 2 (initially points to 14)


Inner loop searches for minimum:

j = 3: arr[2] = 14 > arr[3] = 37? No  - min_idx = 2
j = 4: arr[2] = 14 > arr[4] = 29? No  - min_idx = 2


Result: Minimum is 14 at index 2

Swap:

Before: [10, 13, 14, 37, 29]
                i=2 min_idx=2

After:  [10, 13, 14, 37, 29]
                sorted

Pass 4 (i = 3)
i = 3, min_idx = 3 (initially points to 37)


Inner loop searches for minimum:

j = 4: arr[3] = 37 > arr[4] = 29? Yes - min_idx = 4


Result: Minimum is 29 at index 4

Swap:

Before: [10, 13, 14, 37, 29]
                    i=3 min_idx=4

After:  [10, 13, 14, 29, 37]
                    sorted

Pass 5 (i = 4)
i = 4, min_idx = 4 (initially points to 37)


Inner loop searches for minimum:

(No comparisons left)


Result: Minimum is 37 at index 4

Swap:

Before: [10, 13, 14, 29, 37]
                        i=4 min_idx=4

After:  [10, 13, 14, 29, 37]
                        sorted

Final Sorted Array
[10, 13, 14, 29, 37]
"""