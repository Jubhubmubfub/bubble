
'''
bubble sort

compare indexes that are next to each other and if the index on the left is larger than the one on the right
switch those indexes
once it is sorted, repeat the process, but stop at the index before the last sorted index

need to check if items are already sorted at the end
'''
8,7,6,5,4,9,10,1

[2,1] #lenght is 2 indexes 0,1

 3,1,2 -> 1,3,2 -> 1,2,3
#0 1 2    0 1 2    0 1 2
 3,2,1 -> 2,3,1 -> 2,1,3 -> 1,2,3
#0 1 2    0 1 2    0 1 2    0 1 2
[4,3,5,6,7]

def bubble(arr):
    temp = 0
    lastIndex = 0
    for i in range(start,len(arr)-lastIndex):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            lastIndex = i
    i = 0
    while i < len(arr)-lastIndex:
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            lastIndex = i
        i+=1
