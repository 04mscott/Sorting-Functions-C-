#include "sort_funcs.h"
#include "time.h"

int main(){
  int len = 10000;
  int range = 1000;
  clock_t start_time;
  int arr[len];
  double bubble_arr[100];
  double selection_arr[100];
  double insertion_arr[100];
  double heap_arr[100];
  double merge_arr[100];
  double quick_arr[100];
  double count_arr[100];
  double radix_arr[100];

  printf("\n\n\n");
  printf("Implemented sorting algorithms:\n");
  printf("Bubble Sort\nSelection Sort\nInsertion Sort\nHeap Sort\nMerge Sort\nQuick Sort\nCount Sort\nRadix Sort\n\n");
  printf("The array of integers to be sorted has a length of %d and \n", len);
  printf("the integers are selected randomly within the range [0, %d]\n\n", range);

  get_array(arr, len, range);
  start_time = clock();
  bubble_sort(arr, len);
  double bubble_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Bubble Sort Benchmark: Done in %f seconds\n", bubble_time);
  printf("Time complexity O(n^2)\n");
  printf("Valid Sort: %s\n\n", check_sort(arr, len) ? "true" : "false");

  get_array(arr, len, range);
  start_time = clock();
  selection_sort(arr, len);
  double selection_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Selection Sort Benchmark: Done in %f seconds\n", selection_time);
  printf("Time complexity O(n^2)\n");
  printf("Valid Sort: %s\n\n", check_sort(arr, len) ? "true" : "false");

  get_array(arr, len, range);
  start_time = clock();
  insertion_sort(arr, len);
  double insertion_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Insertion Sort Benchmark: Done in %f seconds\n", insertion_time);
  printf("Time complexity O(n^2)\n");
  printf("Valid Sort: %s\n\n", check_sort(arr, len) ? "true" : "false");

  get_array(arr, len, range);
  start_time = clock();
  heap_sort(arr, len);
  double heap_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Heap Sort Benchmark: Done in %f seconds\n", heap_time);
  printf("Time complexity O(n log n)\n");
  printf("Valid Sort: %s\n\n", check_sort(arr, len) ? "true" : "false");

  get_array(arr, len, range);
  start_time = clock();
  merge_sort(arr, 0, len - 1);
  double merge_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Merge Sort Benchmark: Done in %f seconds\n", merge_time);
  printf("Time complexity O(n log n)\n");
  printf("Valid Sort: %s\n\n", check_sort(arr, len) ? "true" : "false");

  get_array(arr, len, range);
  start_time = clock();
  quick_sort(arr, 0, len - 1);
  double quick_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Quick Sort Benchmark: Done in %f seconds\n", quick_time);
  printf("Time complexity O(n log n)\n");
  printf("Valid Sort: %s\n\n", check_sort(arr, len) ? "true" : "false");

  get_array(arr, len, range);
  start_time = clock();
  count_sort(arr, len, 0);
  double count_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Count Sort Benchmark: Done in %f seconds\n", count_time);
  printf("Time complexity O(n + k)\n");
  printf("Valid Sort: %s\n\n", check_sort(arr, len) ? "true" : "false");

  get_array(arr, len, range);
  start_time = clock();
  radix_sort(arr, len);
  double radix_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Radix Sort Benchmark: Done in %f seconds\n", radix_time);
  printf("Time complexity O(nd)\n");
  printf("Valid Sort: %s\n\n", check_sort(arr, len) ? "true" : "false");

  return 0;
}