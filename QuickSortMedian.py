
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
        quicksortMedianThree(arr,0,len(arr)-1)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    QuickMTimeArr.append(time_taken)
    print("The average execution time taken when input is randomly ordered for size {} is {}".format(s,QuickMTimeArr))
    return
#For calculating average execution time when input is sorted
def calcAvgSort(s):
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]
        arr.sort()
        n = len(arr)

        tic = time.process_time()
        quicksortMedianThree(arr,0,len(arr)-1)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    QuickMTimeArrSort.append(time_taken)
    print("The average execution time taken when input is sorted for size {} is {}".format(s,QuickMTimeArrSort))

    return
#For calculating average execution time when input is reversely sorted
def calcAvgSortRev(s):
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]
        arr.sort(reverse=True)
        tic = time.process_time()
        quicksortMedianThree(arr,0,len(arr)-1)
        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    QuickMTimeArrRev.append(time_taken)
    print("The average execution time taken when input is Reverse sorted for size {} is {}".format(s,QuickMTimeArrRev))

    return


#This function to choose the pivot
def medianofThree(arr,left,right):
    centre = (left+right)//2
    if (arr[left]>arr[centre]):
        arr[left],arr[centre] = arr[centre],arr[left]
    if (arr[centre]>arr[right]):
        arr[centre],arr[right] = arr[right],arr[centre]
    if (arr[left]>arr[right]):
        arr[left],arr[right] = arr[centre],arr[right]
    arr[centre],arr[right-1] = arr[right-1],arr[centre]
    return arr[right-1]

#Quick Sort using the chosen pivot
def quicksortMedianThree(arr,left,right):
    if left+10<=right:
        pivot = medianofThree(arr,left,right)
        i = left
        j = right-2
        while(i<j):
            while arr[i] < pivot:
                i+=1

            while arr[j] > pivot:
                j-=1

            if(i<j):
                arr[i],arr[j] = arr[j],arr[i]
            else:
                break

        arr[i],arr[right-1] = arr[right-1], arr[i]

        quicksortMedianThree(arr, left, i-1)
        quicksortMedianThree(arr, i+1, right)
    else:
        InsertionSort(arr,left,right)

#If the array size is <=10
def InsertionSort(arr,l,r):
    for j in range(l,r+1):
        i = j-1
        key = arr[j]
        while i>=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key

#Initialize empty array to store average execution time for different input cases
QuickMTimeArr = []
QuickMTimeArrSort = []
QuickMTimeArrRev = []


size = [1000,10000,20000,30000,40000,50000]
# size = [1000,2000,3000,4000,5000]

for n in size:

    calcAvg(n)
    calcAvgSort(n)
    calcAvgSortRev(n)



                                                    #For plotting

dict={'Input Size': size, 'Random':QuickMTimeArr, 'Sorted': QuickMTimeArrSort, 'Reverse Sorted': QuickMTimeArrRev}
df = pd.DataFrame(dict)
print(df)
# df.to_csv("ModQuickSort.csv")

df=df.melt('Input Size', var_name='Input Case', value_name='Average Execution Time (ms)')


import seaborn as sb
sb.set_style("darkgrid", {"axes.facecolor":".9"})
p=(sb.factorplot(x='Input Size', y='Average Execution Time (ms)', data=df, hue='Input Case'))

plt.title('Modified Quicksort plot (Input: Random-Sorted-Reverse sorted)')
plt.show()

