[Return to Home](https://04mscott.github.io/)

# C Sorting Algorithms With Python Visualizations

## Overview

![All sort funcs bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/All%20(10).png)

In this project, I implemented 8 common sorting algorithms in C. Each algorithm takes in a list of integers, along with an end position (in most cases this means the length of the list), and, in some cases, a starting position.

The above graph shows the time taken for each sorting algorithm to sort a list of 2^n random integers, where 0 <= n <= 10. The following documentation will go into further detail visualizing and comparing each algorithm for larger data sets. The graph was created using the Python plotting libraries and the benchmark function writtin in C below:
```c
// Output is the time elapseed between function call and end of sort function
int benchmark(int sort, int num_elements, int range);
The input variables are:
```
- `int sort` An int between 0 and 7, each representing one of the sorting functions below
- `int num_elements` An int representing the desired number of elements in the list to run the benchmark on
- `int range` An int representing the range of numbers to be sorted. For example 100 would be numbers \[0-99]

An important note about benchmark: Each time the function is called it uses a new list of random ints within the submitted range. The function is used in the Python code later in the documentation to visualize and compare the performence of each algorithm.

## C Code

---

## Miscellaneous Helper Functions

There have been multiple additional functions to help with each of the algorithms. There are some specific helper functions meant for particular sorting algorithms, which will be covered in their respective part; However, there are also some general helper functions used throughout. The general helper functions implemented are as follows:
```c
// Prints an array in the form '0, 1, 2, 3, 4, ..., n'
void print_arr(char string[], int arr[], int len);

// Returns an array of size len with random elements in range [0-range]
void get_array(int *arr, int len, int range);

// Returns the index of the maximum element in the array within the bounds start and end
int max(int arr[], int start, int end);

// Returns the index of the minimum element in the array within the bounds start and end
int min(int arr[], int start, int end);

// Returns the number of digits there are in the integer x
int digits(int x);

// Swaps the values each pointer refers to
void swap(int *x, int *y);

// Verifies that the given array is sorted
bool check_sort(int arr[], int len);
```
## Part I - Bubble Sort

![bubble sort bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/Bubble.png)

Bubble sort is stable, meaning if two elements are of equal value, the one that originally appears earlier in the unsorted list willl also appear earlier in the sorted list, and in place, meaning it moves the elements around within the input list rather than creating new lists to store them. Bubble sort is the most straightforward algorithm, and likely one that most programmers discover on their own. It is implemented using nested loops and the `swap` helper function. The outer loop loops over each element in the list, with the inner loop comparing each subsequent element to the element selected by the outer loop. This means that Bubble sort is O(n^2) in all cases. The code for my implementation of Bubble sort is below.
```c
void bubble_sort(int arr[], int len){
  // Loops over list n^2 times
  for(int i = len - 1; i >= 0; i--){
    for(int j = 0; j < i; j++){
      // Compares elements, swapping if necessary
      if(arr[j] > arr[j + 1]){
        swap(&arr[j], &arr[j + 1]);
      }
    }
  }
}
```
An example call to bubble_sort would look like the following:
```c
int arr[] = {4, 1, 2, 5, 3};
bubble_sort(arr, 5);
print_arr(arr);
Result:
```
```c
1, 2, 3, 4, 5
```
The remaining documentation will not contain the full source code for the sorting algorithms, although it can be found in the projects GitHub repository [here](https://github.com/04mscott/Sorting-Functions-C-)

## Part II - Selection Sort
![selection sort bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/Select.png)

Selection sort is not stable, but is in place. It 'selects' the smallest element of the unsorted sub list and swaps it with the first element of said sublist. This is implemented using a loop, the `min` and `swap` helper functions, swapping the minimum element and the first element in the unsorted sublist. This results in a O(n^2) time complexity in all cases, similar to Bubble Sort. Selection sort takes in two parameters, the list to be sorted and the size of said list. An example call is below:
```c
int arr[] = {4, 1, 2, 5, 3};
selection_sort(arr, 5);
```

## Part III - Insertion Sort
![insertion sort bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/Insert.png)

Insertion Sort is stable and is in place. It focuses on one element at a time, comparing it to the previously sorted elements in the list. As the function progresses, a sorted sublist forms at the beginning of the list, although, it is only sorted relative to itself, the values may not be in the correct sorted order pertaining to the overall list. Insertion sort is implemented using a set of nested loops and the `swap` helper function. The first loop loops over each element in the list, with the inner loop increasing the size of the sorted sublist, swapping the minimum element in the unsorted list with the first element in said list.
```c
int arr[] = {4, 1, 2, 5, 3};
selection_sort(arr, 5);
```
## Part IV - Heap Sort
![heap sort bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/Heap.png)

Heap sort is not stable, but is in place. It converts the list into a max-heap, meaning the root node is the largest element in the sub-tree, going all the way down to the leaf nodes. 
This done using the `build_max_heap` and `heapify` helper functions. `build_max_heap`reorders the elements in the list such that each row appears in order from left to right in the array. 

For example, the array `[4, 1, 2, 5, 3]` would be converted to the max-heap `[5, 4, 2, 1, 3]`, which would look like this: ![maxheap1](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/maxheap1.png)
Next, the root node is swapped with the last element of the list, or the rightmost node. So the heap will become `[4, 2, 1, 3, 5]` or ![maxheap2](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/maxheap2.png)

The 5 is now considered sorted and removed from the max-heap. This remaining sub list is converted back into a max-heap using the `heapify` helper function. In this case, there is no work for `heapify` to do, and the heap becomes `[4, 2, 1, 3]` or ![maxheap3](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/maxheap3.png)

Following this, the process repeats until the list is sorted. The root node is swapped with the last element in the unsorted sub list, becoming `[3, 2, 1, 4, 5]`, and then removed from the heap. After conversion back to a max heap it will become `[3, 2, 1]` or ![maxheap4](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/maxheap5.png)

Once the list is sorted, heap sort has a best case time complexity of O(n) and worst case of O(n log n)

## Part V - Merge Sort
![merge sort bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/Merge.png)
## Part VI - Quick Sort
![quick sort bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/Quick.png)
## Part VII - Count Sort
![count sort bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/Count.png)
## Part VIII - Radix Sort
![radix sort bm](https://raw.githubusercontent.com/04mscott/Sorting-Functions-C-/refs/heads/main/assets/img/Radix.png)

## Python Code

---


## Visualizations

---
[Return to Home](https://04mscott.github.io/)
