import ctypes
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Assign file
sort_funcs = ctypes.CDLL('/Users/masonscott/C Projects/Sorting-Functions-C-/src/sort_funcs.so')
# Assign Benchmark funciton
benchmark = sort_funcs.benchmark
# Assign Result types
benchmark.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
benchmark.restype = ctypes.c_double

colors = ['#900c3f', '#182b55', '#5f4e94', '#a291c7', '#82cbec', '#d94f21', '#febd2b', '#9aab4b']
sorts = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Heap Sort', 'Merge Sort', 'Quick Sort', 'Count Sort', 'Radix Sort', ]
exp = 20
r = 100000
numEls = [2] * exp
numEls = np.power(numEls, list(range(1, exp + 1)))
ranges = [10, 100, 1000, 10000, 100000]
y_bubble = []
y_selection = []
y_insertion = []
y_heap = []
y_merge = []
y_quick = []
y_count = []
y_radix = []

for i, num in enumerate(numEls):
  bm = benchmark(0, num, 100000)
  y_bubble.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Bubble")

  bm = benchmark(1, num, 100000)
  y_selection.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Selection")

  bm = benchmark(2, num, 100000)
  y_insertion.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Insertion")

  bm = benchmark(3, num, 100000)
  y_heap.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Heap")

  bm = benchmark(4, num, 100000)
  y_merge.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Merge")

  bm = benchmark(5, num, 100000)
  y_quick.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Quick")

  bm = benchmark(6, num, 100000)
  y_count.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Count")

  bm = benchmark(7, num, 100000)
  y_radix.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Radix")

df = pd.DataFrame({
  'Bubble' : y_bubble, 
  'Selection' : y_selection, 
  'Insertion' : y_insertion, 
  'Heap' : y_heap, 
  'Merge' : y_merge, 
  'Quick' : y_quick, 
  'Count' : y_count, 
  'Radix' : y_radix
  })

sns.lineplot(data=df[['Bubble', 'Selection', 'Insertion', 'Heap', 'Merge', 'Quick', 'Count', 'Radix']], palette=colors)
plt.show()
sns.lineplot(data=df[['Bubble']], palette=[colors[0]])
plt.show()
sns.lineplot(data=df[['Selection']], palette=[colors[1]])
plt.show()
sns.lineplot(data=df[['Insertion']], palette=[colors[2]])
plt.show()
sns.lineplot(data=df[['Heap']], palette=[colors[3]])
plt.show()
sns.lineplot(data=df[['Merge']], palette=[colors[4]])
plt.show()
sns.lineplot(data=df[['Quick']], palette=[colors[5]])
plt.show()
sns.lineplot(data=df[['Count']], palette=[colors[6]])
plt.show()
sns.lineplot(data=df[['Radix']], palette=[colors[7]])
plt.show()
