#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

// Helper Functions
void print_arr(char string[], int arr[], int len);
void get_array(int *arr, int len, int range);
int max(int arr[], int start, int end);
int min(int arr[], int start, int end);
int digits(int x);
void swap(int *x, int *y);
void heapify(int arr[], int len, int parent);
void build_max_heap(int arr[], int len);
bool check_sort(int arr[], int len);
void merge(int arr[], int left, int mid, int right);
int partition(int arr[], int left, int pivot);

// Sorting Functions
void bubble_sort(int arr[], int len);
void selection_sort(int arr[], int len);
void insertion_sort(int arr[], int len);
void heap_sort(int arr[], int len);
void merge_sort(int arr[], int start, int end);
void quick_sort(int arr[], int left, int right);
void count_sort(int arr[], int len, int place);
void radix_sort(int arr[], int len);