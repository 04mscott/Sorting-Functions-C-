[Return to Home](https://04mscott.github.io/)

# C Sorting Algorithms With Python Visualizations

![All sort funcs bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/All%20(10).png)

This project demonstrates the implementation of eight classic sorting algorithms in C, coupled with Python-based visualizations to analyze and compare their performance.

## C Implementation
The following sorting algorithms were implemented in C, utilizing efficient memory management and function-based modularity:
+ Bubble Sort
+ Selection Sort
+ Insertion Sort
+ Heap Sort
+ Merge Sort
+ Quick Sort
+ Count Sort
+ Radix Sort
  
Each algorithm is benchmarked for runtime performance on datasets of varying sizes and ranges, leveraging a custom benchmarking function written in C. The implementation includes utility functions to generate randomized input arrays, validate sorting correctness, and handle edge cases. Memory-efficient techniques such as in-place operations and heap-based structures were used to optimize performance.

## Python Visualization
A Python script leverages the shared library ```(sort_funcs.so)``` generated from the C implementation. Using ```ctypes```, the benchmarking function is integrated into Python, allowing runtime measurements for each algorithm across varying input sizes. Libraries such as Matplotlib, Pandas, and Seaborn are used to create detailed visualizations.
+ Runtime Comparisons: Line plots compare the runtime of all eight algorithms under identical conditions.
+ Algorithm-Specific Performance: Dedicated graphs for individual algorithms reveal scaling behavior and highlight strengths and weaknesses.
+ Special Focus on Non-Comparison Sorts: Visualizations for Count Sort and Radix Sort include a breakdown of performance across datasets with varying digit lengths.
## Technical Highlights
+ Benchmarking Framework: A clock-based benchmarking function in C measures and verifies the performance of each algorithm.
+ Python-C Interfacing: ```ctypes``` enables seamless integration of the C backend with Python's visualization ecosystem.
+ Scalability Testing: The project tests algorithms on datasets ranging from a few elements to millions, providing insights into their theoretical time complexities in practice.

---
[Return to Home](https://04mscott.github.io/)
