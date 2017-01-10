
'''
bubble sort

compare indexes that are next to each other and if the index on the left is larger than the one on the right
switch those indexes
once it is sorted, repeat the process, but stop at the index before the last sorted index

need to check if items are already sorted at the end
'''

import random
random_list = []
for i in range(0,25):
    random_list.append(random.randrange(0,10000))
def bubble(arr):
    temp = 0
    count = 1
    lastIndex = (len(arr)-1)
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
    return "sorted arr is ",arr

print bubble(random_list)
