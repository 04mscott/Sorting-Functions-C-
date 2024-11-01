[Return to Home](https://04mscott.github.io/)

# C Sorting Algorithms With Python Visualizations

## Overview

In this project, I implemented 8 common sorting algorithms in C. Each algorithm takes in a list of integers, along with an end position (in most cases this means the length of the list), and, in some cases, a starting position.

There is an additional function writtin in C that is used to benchmark each of the algorithms and compare them:
```c
// Output is the time elapseed between function call and end of sort function
int benchmark(int sort, int num_elements, int range);
The input variables are:
```
- `int sort` An int between 0 and 7, each representing one of the sorting functions below
- `int num_elements` An int representing the desired number of elements in the list to run the benchmark on
- `int range` An int representing the range of numbers to be sorted. For example 100 would be numbers \[0-99]

The benchmark function is used in the Python code later in the documentation to visualize and compare the performence of each algorithm.

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

The first algorithm is Bubble Sort. Bubble sort is a stable, in place, and comparative sorting algorithm. Bubble sort is the most straightforward algorithm, and likely one that most programmers discover on their own. It is made up of a set of nested loops. The outer loop loops over each element in the list, with the inner loop comparing each subsequent element to the element selected by the outer loop. This means that Bubble sort is O(n^2). The code for my implementation of Bubble sort is below.
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

The next algorithm, Selection Sort, is also in place, although it is not stable. Selection sort focuses on one element at a time, comparing it to the previously sorted elements in the list. As the function progresses, a sorted sublist forms at the beginning of the list, although it is only sorted relative to itself, the values are not in the correct sorted order pertaining to the overall list.
```c
int arr[] = {4, 1, 2, 5, 3};
selection_sort(arr, 5);
```
```c
// Steps of selection sort
i.   4, 1, 2, 5, 3
ii.  1, 4, 2, 5, 3
iii. 1, 2, 4, 5, 3
iv.  1, 2, 4, 5, 3
v.   1, 2, 3, 4, 5
```
## Part III - Insertion Sort
## Part IV - Heap Sort
## Part V - Merge Sort
## Part VI - Quick Sort
## Part VII - Count Sort
## Part VIII - Radix Sort

[Return to Home](https://04mscott.github.io/)