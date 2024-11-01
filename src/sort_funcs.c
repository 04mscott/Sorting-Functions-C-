#include "sort_funcs.h"
#include "time.h"

// Benchmark Function
double benchmark(int sort, int num_elements, int range){
  clock_t start_time;
  int arr[num_elements];
  get_array(arr, num_elements, range);

  get_array(arr, num_elements, range);
  start_time = clock();
  switch(sort){
    case 0:
      bubble_sort(arr, num_elements);
      break;
    case 1:
      selection_sort(arr, num_elements);
      break;
    case 2:
      insertion_sort(arr, num_elements);
      break;
    case 3:
      heap_sort(arr, num_elements);
      break;
    case 4:
      merge_sort(arr, 0, num_elements);
      break;
    case 5:
      quick_sort(arr, 0, num_elements);
      break;
    case 6:
      count_sort(arr, num_elements, 0);
      break;
    case 7:
      radix_sort(arr, num_elements);
      break;
  }
  double time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  bool sorted = check_sort(arr, num_elements);
  if(!sorted){
    return -1;
  }
  return time;
}

// General Helper Functions
/*----------------------------------------------*/
// Prints all elements of an array in addition to an input string
void print_arr(char string[], int arr[], int len){
  printf("%s", string);
  for(int i = 0; i < len; i++){
    if(i == len - 1){
      printf("%d\n", arr[i]);
    } else{
      printf("%d, ", arr[i]);
    }
  }
}

// Creates an array of length len, filled with random integers
// from 0 - range
void get_array(int *arr, int len, int range){
  for(int i = 0; i < len; i++){
    arr[i] = rand() % range;
  }
}

// Checks that an array is sorted
bool check_sort(int arr[], int len){
  for(int i = 1; i < len; i++){
    if(arr[i - 1] > arr[i]){
      return false;
    }
  }
  return true;
}

// Returns index of maximum value in an array
int max(int arr[], int start, int end){
  int m = arr[start];
  int index = start;
  for(int i = start + 1; i < end; i++){
    if(arr[i] > m){
      m = arr[i];
      index = i;
    }
  }
  return index;
}

// Returns index of minimum value in an array
int min(int arr[], int start, int end){
  int m = arr[start];
  int index = start;
  for(int i = start + 1; i < end; i++){
    if(arr[i] < m){
      m = arr[i];
      index = i;
    }
  }
  return index;
}

// Swaps two pointers
void swap(int *x, int *y){
  int temp = *x;
  *x = *y;
  *y = temp;
}

// Sorting Helper Functions
/*----------------------------------------------*/
// Converts a sorted tree into a max heap
void heapify(int arr[], int len, int parent){
  int max_node = parent;
  // Indices of children
  int left = 2 * parent + 1;
  int right = left + 1;

  // Set the max_node to the index of the maximum element
  // of the three: parent, left child, or right child
  if(left < len && arr[max_node] < arr[left]){
    max_node = left;
  }
  if(right < len && arr[max_node] < arr[right]){
    max_node = right;
  }

  // Swaps child and parent elements if necessary
  // Calls heapify on the parent node to check any effected sub trees
  if(max_node != parent){
    swap(&arr[parent], &arr[max_node]);
    heapify(arr, len, max_node);
  }
}

// Builds a max heap from a list by placing them in correct order
void build_max_heap(int arr[], int len){
  // Find index of last non-leaf node
  int last_node = (len / 2) - 1;
  // Loop backwards over list, working from the bottom up of the heap
  for(int i = last_node; i >= 0; i--){
    heapify(arr, len, i);
  }
}

// Merges two sublists of a given list in sorted order
void merge(int arr[], int start, int mid, int end) {
  int r, l, c;
  int l_len = mid - start + 1;
  int r_len = end - mid;
  int l_arr[l_len], r_arr[r_len];
  // Copy each sub array into temp arrays
  for(l = 0; l < l_len; l++){
    l_arr[l] = arr[start + l];
  }
  for(r = 0; r < r_len; r++){
    r_arr[r] = arr[mid + 1 + r];
  }
  // Add elements back to original array in order
  l = 0;
  r = 0;
  c = start;
  while(l < l_len && r < r_len){
    if(l_arr[l] <= r_arr[r]){
      arr[c] = l_arr[l];
      l++;
    } else{
      arr[c] = r_arr[r];
      r++;
    }
    c++;
  }
  // Copy Any remaining elements
  while(l < l_len){
    arr[c] = l_arr[l];
    l++;
    c++;
  }
  while(r < r_len){
    arr[c] = r_arr[r];
    r++;
    c++;
  }
}

// Partitions a list using the last element as the pivot
// Places all elements < pivot to the left, all elements > pivot to the right
// Returns new index of the pivot
int partition(int arr[],  int left, int right) {
  // Select the rightmost element as pivot
  int pivot = arr[right];
  int next = left - 1;
  // Compare each element with the pivot
  for (int i = left; i < right; i++) {
    if (arr[i] <= pivot) {
      // Swap smaller element with the element in the next position
      next++;
      swap(&arr[next], &arr[i]);
    }
  }
  // swap the pivot element with the greater element at i
  swap(&arr[next + 1], &arr[right]);
  return next + 1;
}

// Sorting functions
/*----------------------------------------------*/
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

void selection_sort(int arr[], int len){
  // Finds the minimum index using helper fxn and swaps it with 
  // the first element of the unsorted sub-array
  for(int i = 0; i < len - 1; i++){
    int min_idx = min(arr, i, len);
    swap(&arr[i], &arr[min_idx]);
  }
}

void insertion_sort(int arr[], int len){
  for(int i = 1; i < len; i++){
    int j = i;
    // Increases size of sub-arrray, moving new elements 
    // into sorted position with each growth
    while(j > 0 && arr[j] < arr[j - 1]){
      swap(&arr[j], &arr[j - 1]);
      j--;
    }
  }
}

void heap_sort(int arr[], int len){
  // Converts array to a max heap
  build_max_heap(arr, len);
  for(int i = len - 1; i >= 0; i--){
    // Swaps root with last index, sorting it
    // After swapping, converts back into max heap without the sorted element(s)
    swap(&arr[0], &arr[i]);
    heapify(arr, i, 0);
  }
}

void merge_sort(int arr[], int start, int end) {
  if(start < end){
    // Splits array in half and recurses down to base case
    int mid = start + (end - start) / 2;
    merge_sort(arr, start, mid);
    merge_sort(arr, mid + 1, end);
    // Merges smaller arrays back together
    merge(arr, start, mid, end);
    //print_arr("Step: ", arr, len);
  }
}

void quick_sort(int arr[], int left, int right){
  if(left < right){
    // Find the pivot and partition the array
    int pivot = partition(arr, left, right);
    // Recurse down into each half of the array, partitioning until sorted
    quick_sort(arr, left, pivot - 1);
    quick_sort(arr, pivot + 1, right);
  }
}

void count_sort(int arr[], int len, int place) {
  int output[len];
  int k;
  if(place == 0){
    k = arr[max(arr, 0, len)] + 1;
  } else{
    k = 10;
  }
  int *count = calloc(k, sizeof(int));
  // Calculate count of elements
  int index;
  for (int i = 0; i < len; i++) {
    if(place == 0){
      index = arr[i];
    } else{
      index = (arr[i] / place) % 10;
    }
    count[index]++;
  }
  // Calculate cumulative count
  for (int i = 1; i < k; i++) {
    count[i] += count[i - 1];
  }
  // Place the elements in sorted order
  for (int i = len - 1; i >= 0; i--) {
    if(place == 0){
      index = arr[i];
    } else{
      index = (arr[i] / place) % 10;
    }
    output[count[index] - 1] = arr[i];
    count[index]--;
  }
  // Copy the sorted elements into original array
  for (int i = 0; i < len; i++) {
    arr[i] = output[i];
  }
  free(count);
}

void radix_sort(int arr[], int len){
  // Find max element in the array
  int m = arr[max(arr, 0, len)];
  // Call count_sort once for each digit, passing the exponent as a power of ten
  for(int place = 1; m / place > 0; place *= 10){
    count_sort(arr, len, place);
  }
}