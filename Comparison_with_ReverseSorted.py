import Insertion_Sort as ins
import Merge_Sort as mrg
import Heap_Sort as hp
import Quick_Sort_InPlace as qki
import QuickSortMedian as qkm
import matplotlib.pyplot as plt
import pandas as pd


size=[1000,10000,20000,30000,40000,50000]

dict={'Input Size': size, 'Insertion':ins.InsertionTimeArrRev, 'Heap':hp.HeapTimeArrRev, 'Merge':mrg.MergeTimeArrRev, 'Quicksort In-Place': qki.QuickInPlaceTimeArrRev, 'Modified Quicksort': qkm.QuickMTimeArrRev}
df = pd.DataFrame(dict)
print(df)
#df.to_csv("ComparisonRev.csv")
df=df.melt('Input Size', var_name='Sort Type', value_name='Average Execution Time (ms)')

import seaborn as sb
sb.set_style("darkgrid", {"axes.facecolor":".9"})
p=(sb.factorplot(x='Input Size', y='Average Execution Time (ms)', data=df, hue='Sort Type'))
plt.title('Comparison plot (without Insertion Sort) Input: Reverse sorted')

plt.show()
