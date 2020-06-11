
import random
import matplotlib as matplotlib
import numpy as np
import time
from sys import setrecursionlimit
setrecursionlimit(1000000000)
import matplotlib.pyplot as plt
import pandas as pd

#For calculating average execution time when input is random number
def calcAvg(s):
    add = 0
    seed=[6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]

        tic = time.process_time()
        InsertionSort(arr)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    InsertionTimeArr.append(time_taken)
    print("Random input: ", InsertionTimeArr)
    return
#For calculating average execution time when input is sorted
def calcAvgSort(s):
    add = 0
    seed=[6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]
        arr.sort()

        tic = time.process_time()
        InsertionSort(arr)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    InsertionTimeArrSort.append(time_taken)
    print("Sorted input: ", InsertionTimeArrSort)
    return
#For calculating average execution time when input is reversely ordered
def calcAvgSortRev(s):
    add = 0
    seed=[6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]
        arr.sort(reverse=True)

        tic = time.process_time()
        InsertionSort(arr)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    InsertionTimeArrRev.append(time_taken)
    print("Reverse sorted input: ", InsertionTimeArrRev)
    return

def InsertionSort(arr):

    for j in range(1,len(arr)):
        i = j-1
        key = arr[j]
        while i>=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key

#Initialize empty array to store average execution time for different input cases
InsertionTimeArr = []
InsertionTimeArrSort = []
InsertionTimeArrRev = []


size = [1000,10000,20000,30000,40000,50000]
# size = [10,20,30,40,50,60]
for n in size:

    calcAvg(n)
    calcAvgSort(n)
    calcAvgSortRev(n)


#for plotting
dict={'Input Size': size, 'Random':InsertionTimeArr, 'Sorted': InsertionTimeArrSort, 'Reverse Sorted': InsertionTimeArrRev}
df = pd.DataFrame(dict)
print(df)
#df.to_csv("InsertionSort.csv")

df=df.melt('Input Size', var_name='Input Case', value_name='Average Execution Time (ms)')

import seaborn as sb
sb.set_style("darkgrid", {"axes.facecolor":".9"})
p=(sb.factorplot(x='Input Size', y='Average Execution Time (ms)', data=df, hue='Input Case'))
plt.title('Insertion Sort plot (Input: Random-Sorted-Reverse sorted)')

plt.show()
