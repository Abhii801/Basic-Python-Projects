import random
import time
#Searches from center to either left or right
#proving binary search is faster than normal search

def normal_search(l,target):
    #example l is a list and target is element
    for i in range(len(l)):
        if(l[i]==target):
            return i
    return -1

def binary_search(l,target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    
    #if target is not in list
    if high < low:
        return -1

    midpoint = (low + high)//2

    if l[midpoint]==target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target,low,midpoint-1) #recursion
    else:
        return binary_search(l,target,midpoint+1,high)

if __name__ == '__main__':
    # l = [1,2,3,4,5,6,7,8]
    # target = 2
    # print(normal_search(l,target))
    # print(binary_search(l, target))

    length = 10000
    #building a random sorted list
    sorted_list = set()
    while len(sorted_list)<length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
       normal_search(sorted_list,target)
    end = time.time()
    print("Normal search time: ",(end-start)/length,"seconds")

    start = time.time()
    for target in sorted_list:
       binary_search(sorted_list,target)
    end = time.time()
    print("Binary search time: ",(end-start)/length,"seconds")