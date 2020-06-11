import random
import matplotlib as matplotlib
import numpy as np
import time
from sys import setrecursionlimit
setrecursionlimit(1000000000)
import matplotlib.pyplot as plt
import pandas as pd

#For calculating average execution time when input is randomly ordered
def calcAvg(s):
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]

        n = len(arr)
        tic = time.process_time()
        QuickSortInplace(arr,0,len(arr)-1)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    QuickInPlaceTimeArr.append(time_taken)
    print("The average execution time taken when input is randomly ordered for size {} is {}".format(s,QuickInPlaceTimeArr))

    return
#For calculating average execution time when input is sorted
def calcAvgSort(s):
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]
        arr.sort()
        tic = time.process_time()
        QuickSortInplace(arr,0,len(arr)-1)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    QuickInPlaceTimeArrSort.append(time_taken)
    print("The average execution time taken when input is sorted for size {} is {}".format(s,QuickInPlaceTimeArrSort))

    return

#For calculating average execution time when input is Reversely sorted
def calcAvgSortRev(s):
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]
        arr.sort(reverse=True)
        tic = time.process_time()
        QuickSortInplace(arr,0,len(arr)-1)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    QuickInPlaceTimeArrRev.append(time_taken)
    print("The average execution time taken when input is reversely sorted for size {} is {}".format(s,QuickInPlaceTimeArrRev))

    return

#This function partitions the array
def QuickSortInplace(arr,low,high):
    if low<high:
        part = partition(arr,low,high)

        QuickSortInplace(arr,low,part-1)
        QuickSortInplace(arr,part+1,high)


def partition(arr,low,high):
    i = low-1
    p_ind = random.choice((range(low,high+1)))
    pivot = arr[p_ind]
    arr[p_ind],arr[high] = arr[high],arr[p_ind]


    for j in range(low,high):
        if arr[j]<=pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


#Initialize empty array to store average execution time for different input cases
QuickInPlaceTimeArr = []
QuickInPlaceTimeArrSort = []
QuickInPlaceTimeArrRev = []


size = [1000,10000,20000,30000,40000,50000]
#size = [1000,2000,3000,4000,5000]

for n in size:

    calcAvg(n)
    calcAvgSort(n)
    calcAvgSortRev(n)





#for plotting
dict={'Input Size': size, 'Random':QuickInPlaceTimeArr, 'Sorted': QuickInPlaceTimeArrSort, 'Reverse Sorted': QuickInPlaceTimeArrRev}
df = pd.DataFrame(dict)
print(df)
#df.to_csv("QuickInPlace.csv")

df=df.melt('Input Size', var_name='Input Case', value_name='Average Execution Time (ms)')

import seaborn as sb
sb.set_style("darkgrid", {"axes.facecolor":".9"})
p=(sb.factorplot(x='Input Size', y='Average Execution Time (ms)', data=df, hue='Input Case'))
plt.title('Quicksort In-Place plot (Input: Random-Sorted-Reverse sorted)')

plt.show()


