
'''
bubble sort

compare indexes that are next to each other and if the index on the left is larger than the one on the right
switch those indexes
once it is sorted, repeat the process, but stop at the index before the last sorted index

need to check if items are already sorted at the end
'''

import random
import time
from datetime import datetime
a = datetime.now()

random_list = []

for i in range(0,101):
    random_list.append(random.randrange(0,10000))

def bubble(arr):



    temp = 0
    count = 1
    lastIndex = (len(arr)-1)

    while count > 0:

        count = 0
        length = lastIndex

        for i in range(0,length):

            if arr[i] > arr[i+1]:

                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                lastIndex = i
                count += 1
    return "sorted arr is ",arr

print bubble(random_list)
b = datetime.now()
c = b-a
print "runtime is ",c
