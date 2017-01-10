
'''
bubble sort

compare indexes that are next to each other and if the index on the left is larger than the one on the right
switch those indexes
once it is sorted, repeat the process, but stop at the index before the last sorted index

need to check if items are already sorted at the end
'''

import random
random_list = []
for i in range(0,10):
    random_list.append(random.randrange(0,10000))
print "Array is: \n",random_list,"\n"
''' 8,7,6,5,4,9,10,1
#0 1 2 3 4 5 6  7
[2,1] #lenght is 2 indexes 0,1

 3,1,2 -> 1,3,2 -> 1,2,3
#0 1 2    0 1 2    0 1 2
 3,2,1 -> 2,3,1 -> 2,1,3 -> 1,2,3
#0 1 2    0 1 2    0 1 2    0 1 2
[4,3,5,6,7]

 1,2,3,4,5
#0 1 2 3 4'''
def bubble(arr):
    temp = 0
    count = 1
    lastIndex = len(arr)
    while count > 0:
        print "while loop is running, count is ",count,"lastIndex is ",lastIndex,"\n"
        count = 0
        length = lastIndex
        for i in range(0,length):
            if arr[i] > arr[i+1]:
                print "if loop is running. i is: ",i,"  length is ",length,"count is ",count,"arr[i] is: ",arr[i],"arr[i+1] is: ",arr[i+1]," \n"
                temp = arr[i]
                print "temp switched to arr[i]"
                arr[i] = arr[i+1]
                print "arr[i] switched to arr[i+1]"
                arr[i+1] = temp
                print "arr[i+1] switched to temp"
                lastIndex = i
                print "lastIndex saved"
                count += 1
                print "count is ",count
                print arr,"\n"

print bubble(random_list)
