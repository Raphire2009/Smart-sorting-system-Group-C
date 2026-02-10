my_list = [43 ,41 ,23 ,57 ,45 ,12]

def selection_sort(my_list):
    for i in range(len(my_list)):
        min_idk = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_idk] > my_list[j]:
                min_idk = j
            my_list[min_idk], my_list[i] = my_list[i], my_list[min_idk]
    return my_list

sort = selection_sort(my_list)
print(sort)


"""
Pass 1 (i = 0):

i = 0, m_idx = 0 (initially points to 43)
```
**Inner loop searches for minimum:**
```
j = 1: my_list[0] = 43 > arr[1] = 41? Yes - min_idx = 1
j = 2: my_list[1] = 41 > arr[2] = 23? Yes - min_idx = 2
j = 3: my_list[2] = 23 > arr[3] = 57? No  - min_idx = 2
j = 4: my_list[3] = 23 > arr[4] = 45? No  - min_idx = 2
j = 5: my_list[4] = 23 > arr[5] = 12? Yes - min_idx = 5 Correct
```

**Result:** Minimum is 12 at index 5

**Swap:**
```
Before: [43, 41, 23, 57, 45, 12]
        i=0              min_idx=5

After: [12, 41, 23, 57, 45, 43]
        sorted

Pass 2 (i = 1)

i = 1, min_idx = 1 (initially points to 41)


**Inner loop searches for minimum:**

j = 2: my_list[1] = 41 > arr[2] = 23? Yes - min_idx = 2
j = 3: my_list[2] = 23 > arr[3] = 57? No  - min_idx = 2
j = 4: my_list[2] = 23 > arr[4] = 45? No  - min_idx = 2
j = 5: my_list[2] = 23 > arr[5] = 43? No  - min_idx = 2


Result: Minimum is 23 at index 2

Swap:

Before: [12, 41, 23, 57, 45, 43]
            i=1   min_idx=2

After:  [12, 23, 41, 57, 45, 43]
            sorted

Pass 3 (i = 2)

i = 2, min_idx = 2 (initially points to 41)


Inner loop searches for minimum:

j = 3: my_list[2] = 41 > arr[3] = 57? No  - min_idx = 2
j = 4: my_list[2] = 41 > arr[4] = 45? No  - min_idx = 2
j = 5: my_list[2] = 41 > arr[5] = 43? No  - min_idx = 2


Result: Minimum is 41 at index 2

Swap:

Before: [12, 23, 41, 57, 45, 43]
                i=2 min_idx=2

After:  [12, 23, 41, 57, 45, 43]
                sorted

Pass 4 (i = 3)
i = 3, min_idx = 3 (initially points to 57)


Inner loop searches for minimum:

j = 4: my_list[3] = 57 > arr[4] = 45? Yes - min_idx = 4
j = 5: my_list[4] = 45 > arr[5] = 43? Yes - min_idx = 5


Result: Minimum is 43 at index 5

Swap:

Before: [12, 23, 41, 57, 45, 43]
                    i=3      min_idx=5

After:  [12, 23, 41, 43, 45, 57]
                    sorted

Pass 5 (i = 4)
i = 4, min_idx = 4 (initially points to 45)


Inner loop searches for minimum:

j = 5: my_list[4] = 45 > arr[5] = 57? No - min_idx = 4


Result: Minimum is 45 at index 4

Swap:

Before: [12, 23, 41, 43, 45, 57]
                        i=4 min_idx=4

After:  [12, 23, 41, 43, 45, 57]
                        sorted

 Final Sorted Array
[12, 23, 41, 43, 45, 57]

"""