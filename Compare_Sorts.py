import Insertion_Sort as ins
import Merge_Sort as mrg
import Heap_Sort as hp
import Quick_Sort_InPlace as qki
import QuickSortMedian as qkm
import matplotlib.pyplot as plt
import pandas as pd


size=[1000,10000,20000,30000,40000,50000]

dict={'Input Size': size,'Insertion':ins.InsertionTimeArr,'Heap':hp.HeapTimeArr, 'Merge':mrg.MergeTimeArr, 'Quicksort In-Place': qki.QuickInPlaceTimeArr, 'Modified Quicksort': qkm.QuickMTimeArr}
df = pd.DataFrame(dict)
print(df)
#df.to_csv("ComparisonR.csv")
df=df.melt('Input Size', var_name='Sort Type', value_name='Average Execution Time (ms)')

import seaborn as sb
sb.set_style("darkgrid", {"axes.facecolor":".9"})
p=(sb.factorplot(x='Input Size', y='Average Execution Time (ms)', data=df, hue='Sort Type'))
plt.title('Comparison plot(without Insertion sort) Input: Random')

plt.show()

