import ctypes
import numpy as np
import subprocess
import sys
from io import StringIO

sort = ctypes.CDLL("/Users/masonscott/C Projects/Sorting-Functions-C-/sort_funcs.so")

py_values = [4, 2, 7, 1, 9, 3]
arr = (ctypes.c_int * len(py_values))(*py_values)
sort.bubble_sort(arr, len(arr))
print(arr)