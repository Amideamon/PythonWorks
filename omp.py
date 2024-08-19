from numba import njit
import numpy as np
from numba.openmp import openmp_context as openmp
from numba.openmp import omp_get_wtime, omp_get_thread_num, omp_get_num_threads,omp_set_num_threads
import random

@njit
def BubbleSort(arr, size, num_threads):
    omp_set_num_threads(num_threads)
    for i in range(0, size):
        tmp = 0.
        if i % 2 == 0:
            with openmp ("parallel for private(tmp)"):
                for j in range(0, size, 2):
                    if j < size - 1 and arr[j] > arr[j+1]:
                        tmp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = tmp
        else:
            with openmp ("parallel for private(tmp)"):
                for j in range(1, size, 2):
                    if j < size - 1 and arr[j] > arr[j+1]:
                        tmp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = tmp


N = int(input())

ar = np.random.sample(N)

# print(ar)
t = omp_get_wtime()

BubbleSort(ar, n, num_threads)
    
print("Time: ", omp_get_wtime() - t)
print("N = ", N)
# print(ar)
