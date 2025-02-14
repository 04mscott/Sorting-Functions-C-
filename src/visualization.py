import ctypes
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Assign file
base_dir = os.path.dirname(__file__)
sort_funcs = ctypes.CDLL(os.path.join(base_dir, 'sort_funcs.so'))
# Assign Benchmark funciton
benchmark = sort_funcs.benchmark
# Assign Result types
benchmark.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
benchmark.restype = ctypes.c_double

colors = ['#900c3f', '#182b55', '#5f4e94', '#a291c7', '#82cbec', '#d94f21', '#febd2b', '#9aab4b']
digit_colors = ['#3c6c88', '#44838e', '#4d9994', '#66ae9c', '#8ac1a8', '#add4b4',
                '#f9e74e', '#f9c54e', '#f9a64e', '#f98c4e', '#f9734e', '#f9594e']
sorts = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Heap Sort', 'Merge Sort', 'Quick Sort', 'Count Sort', 'Radix Sort', ]
exp = 10
r = 100000
numEls = [2] * exp
numEls = np.power(numEls, list(range(1, exp + 1)))
ranges = [10, 100, 1000, 10000, 100000, 1000000]
y_bubble = []
y_selection = []
y_insertion = []
y_heap = []
y_merge = []
y_quick = []
y_count = []
y_radix = []
y_count_dig = [[], [], [], [], [], []]
y_radix_dig = [[], [], [], [], [], []]

for i, num in enumerate(numEls):
  bm = benchmark(0, num, ranges[4])
  y_bubble.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Bubble")

  bm = benchmark(1, num, ranges[4])
  y_selection.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Selection")

  bm = benchmark(2, num, ranges[4])
  y_insertion.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Insertion")

  bm = benchmark(3, num, ranges[4])
  y_heap.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Heap")

  bm = benchmark(4, num, ranges[4])
  y_merge.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Merge")

  bm = benchmark(5, num, ranges[4])
  y_quick.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Quick")

  bm = benchmark(6, num, ranges[4])
  y_count.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Count")

  bm = benchmark(7, num, ranges[4])
  y_radix.append(bm)
  print(str(num) + " elements sorted in " + str(bm) + " seconds - Radix")

for i, range in enumerate(ranges):
  for num in numEls:
    bm = benchmark(6, num, range)
    y_count_dig[i].append(bm)
    print(str(num) + " elements, 0 - " + str(range - 1) + ", sorted in " + str(bm) + " seconds - Count")

    bm = benchmark(7, num, range)
    y_radix_dig[i].append(bm)
    print(str(num) + " elements, 0 - " + str(range - 1) + ", sorted in " + str(bm) + " seconds - Radix")

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

df2 = pd.DataFrame({
  'Count: 1' : y_count_dig[0], 
  'Count: 2' : y_count_dig[1], 
  'Count: 3' : y_count_dig[2], 
  'Count: 4' : y_count_dig[3], 
  'Count: 5' : y_count_dig[4], 
  'Count: 6' : y_count_dig[5], 
  'Radix: 1' : y_radix_dig[0], 
  'Radix: 2' : y_radix_dig[1], 
  'Radix: 3' : y_radix_dig[2], 
  'Radix: 4' : y_radix_dig[3], 
  'Radix: 5' : y_radix_dig[4], 
  'Radix: 6' : y_radix_dig[5], 
  })

ax = sns.lineplot(
  data=df2[['Count: 1', 'Count: 2', 'Count: 3', 'Count: 4', 'Count: 5', 'Count: 6',
            'Radix: 1', 'Radix: 2', 'Radix: 3', 'Radix: 4', 'Radix: 5', 'Radix: 6']], 
  palette=digit_colors)
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Non-Comparison Sorting Algorithms Benchmark (Number of Digits)')
ax.legend(loc='upper left', bbox_to_anchor=(1.00, 0.75), ncol=1)
plt.show()

ax = sns.lineplot(
  data=df2[['Count: 1', 'Count: 2', 'Count: 3', 'Count: 4', 'Count: 5', 'Count: 6']], 
  palette=digit_colors)
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Counting Sort Algorithm Benchmark (Number of Digits)')
ax.legend(loc='upper left', bbox_to_anchor=(1.00, 0.75), ncol=1)
plt.show()

ax = sns.lineplot(
  data=df2[['Count: 1', 'Count: 2', 'Count: 3']], 
  palette=digit_colors)
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Counting Sort Algorithm Benchmark (Number of Digits 1-3)')
ax.legend(loc='upper left', bbox_to_anchor=(1.00, 0.75), ncol=1)
plt.show()

ax = sns.lineplot(
  data=df2[['Radix: 1', 'Radix: 2', 'Radix: 3', 'Radix: 4', 'Radix: 5', 'Radix: 6']], 
  palette=digit_colors[6:])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Radix Sort Algorithm Benchmark (Number of Digits)')
ax.legend(loc='upper left', bbox_to_anchor=(1.00, 0.75), ncol=1)
plt.show()


ax = sns.lineplot(data=df[['Bubble', 'Selection', 'Insertion', 'Heap', 'Merge', 'Quick', 'Count', 'Radix']], palette=colors)
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('All Sorting Algorithms Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Bubble', 'Selection', 'Insertion', 'Heap', 'Merge', 'Quick']], palette=colors)
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Comparison Sorting Algorithms Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Bubble']], palette=[colors[0]])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Bubble Sort Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Selection']], palette=[colors[1]])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Selection Sort Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Insertion']], palette=[colors[2]])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Insertion Sort Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Heap']], palette=[colors[3]])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Heap Sort Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Merge']], palette=[colors[4]])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Merge Sort Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Quick']], palette=[colors[5]])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Quick Sort Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Count']], palette=[colors[6]])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Count Sort Benchmark')
plt.show()

ax = sns.lineplot(data=df[['Radix']], palette=[colors[7]])
ax.set_xlabel('Number of Elements in List (2^n)')
ax.set_ylabel('Time (Seconds)')
ax.set_title('Radix Sort Benchmark')
plt.show()

