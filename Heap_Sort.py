import numpy as np
import time
from sys import setrecursionlimit
import time
from sys import setrecursionlimit
setrecursionlimit(1000000000)
import matplotlib.pyplot as plt
import pandas as pd

#For calculating average execution time when input is randomly ordered
def calcAvg(s):
    global a
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]

        a=[]
        nArr=[]
        a.append(None)
        tic = time.process_time()

        for i in arr:
            heapsort(i)

        for m in range(1,len(a)):
            elem=removeMin(m)
            nArr.append(elem)


        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    HeapTimeArr.append(time_taken)
    print("The average execution time taken when input is randomly ordered for size {} is {}".format(s,HeapTimeArr))

    return

#For calculating average execution time when input is sorted
def calcAvgSort(s):
    global a
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]

        arr.sort()

        a=[]
        nArr=[]
        a.append(None)
        tic = time.process_time()
        for i in arr:
            heapsort(i)

        for m in range(1,len(a)):
            elem=removeMin(m)
            nArr.append(elem)

        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    HeapTimeArrSort.append(time_taken)
    print("The average execution time taken when input is randomly ordered for size {} is {}".format(s,HeapTimeArrSort))

    return
#For calculating average execution time when input is reversely sorted
def calcAvgSortRev(s):
    global a
    add = 0
    seed = [6,7,8]
    for j in seed:
        np.random.seed(j)
        arr = [np.random.randint(10, 10000000) for i in range(s)]

        arr.sort(reverse = True)

        a=[]
        nArr=[]
        a.append(None)
        tic = time.process_time()
        for i in arr:
            heapsort(i)

        for m in range(1,len(a)):
            elem=removeMin(m)
            nArr.append(elem)

        toc = time.process_time()
        time_taken = 1000*(toc-tic)
        add += time_taken

    time_taken = add/3
    HeapTimeArrRev.append(time_taken)
    print("The average execution time taken when input is randomly ordered for size {} is {}".format(s,HeapTimeArrRev))

    return


def heapsort(x):
    global nArr
    global a
    n = len(a)
    a.append(x)
    i = n

    while i>1 and a[i//2]>a[i]:
        a[i],a[i//2] = a[i//2],a[i]
        i = i//2
    return

def removeMin(m):
    global a
    n = len(a)
    n = n-m
    temp = a[1]
    a[1] = a[n]
    n = n-1
    i=1
    while i<n:

        if ((2*i)+1) <= n:

            if a[i] <= a[(2*i)] and a[i] <= a[((2*i)+1)]:

                return temp
            else:

                if a[((2*i)+1)] < a[(2*i)]:
                    j=((2*i)+1)
                elif a[(2*i)] <= a[((2*i)+1)]:
                    j=(2*i)
                a[i],a[j] = a[j],a[i]
                i=j

        else:

            if (2*i) <= n:
                if a[i] > a[(2*i)]:
                    a[i],a[(2*i)] = a[(2*i)],a[i]

            return temp

    return temp

#Initialize empty array to store average execution time for different input cases
HeapTimeArr = []
HeapTimeArrSort = []
HeapTimeArrRev = []

a=[]
nArr = []
a.append(None)


size = [1000,10000,20000,30000,40000,50000]
#size = [1000,2000,3000,4000,5000]
for n in size:

    calcAvg(n)
    calcAvgSort(n)
    calcAvgSortRev(n)

#for plotting
dict={'Input Size': size, 'Random':HeapTimeArr, 'Sorted': HeapTimeArrSort, 'Reverse Sorted': HeapTimeArrRev}
df = pd.DataFrame(dict)
print(df)
#df.to_csv("Heapsort.csv")
df=df.melt('Input Size', var_name='Input Case', value_name='Average Execution Time (ms)')

import seaborn as sb
sb.set_style("darkgrid", {"axes.facecolor":".9"})
p=(sb.factorplot(x='Input Size', y='Average Execution Time (ms)', data=df, hue='Input Case'))
plt.title('Heap Sort plot (Input: Random-Sorted-Reverse sorted)')

plt.show()
