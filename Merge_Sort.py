
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

        tic = time.process_time()
        MergeSort(arr)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    MergeTimeArr.append(time_taken)
    print("The average execution time taken when input is randomly ordered for size {} is {}".format(s,MergeTimeArr))

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
        MergeSort(arr)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    MergeTimeArrSort.append(time_taken)
    print("The average execution time taken when input is randomly ordered for size {} is {}".format(s,MergeTimeArrSort))

    return

#For calculating average execution time when input is reversely ordered
def calcAvgSortRev(s):
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]
        arr.sort(reverse=True)

        tic = time.process_time()
        MergeSort(arr)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    MergeTimeArrRev.append(time_taken)
    print("The average execution time taken when input is randomly ordered for size {} is {}".format(s,MergeTimeArrRev))

    return

def MergeSort(arr):
    if len(arr)>1:
        n = len(arr)
        mid = n//2
        s1 = arr[:mid]
        s2 = arr[mid:]
        MergeSort(s1)
        MergeSort(s2)

        i = 0
        j = 0
        k = 0
        while i<len(s1) and j<len(s2):
            if s1[i]<=s2[j]:
                arr[k] = s1[i]
                i = i+1
            else:
                arr[k] = s2[j]
                j = j+1
            k = k+1
        while i<len(s1):
            arr[k] = s1[i]
            i = i+1
            k = k+1
        while j<len(s2):
            arr[k] = s2[j]
            j = j+1
            k = k+1

#Initialize empty array to store average execution time for different input cases
MergeTimeArr = []
MergeTimeArrSort = []
MergeTimeArrRev = []


size = [1000,10000,20000,30000,40000,50000]

for n in size:

    calcAvg(n)
    calcAvgSort(n)
    calcAvgSortRev(n)


#for plotting
dict={'Input Size': size, 'Random':MergeTimeArr, 'Sorted': MergeTimeArrSort, 'Reverse Sorted': MergeTimeArrRev}
df = pd.DataFrame(dict)
print(df)
#df.to_csv("Mergesort.csv")
df=df.melt('Input Size', var_name='Input Case', value_name='Average Execution Time (ms)')

import seaborn as sb
sb.set_style("darkgrid", {"axes.facecolor":".9"})
p=(sb.factorplot(x='Input Size', y='Average Execution Time (ms)', data=df, hue='Input Case'))
plt.title('Merge Sort plot (Input: Random-Sorted-Reverse sorted)')

plt.show()
