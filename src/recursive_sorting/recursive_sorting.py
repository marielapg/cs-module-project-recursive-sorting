# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    current_index = 0 
    while i < len(arrA) and j < len(arrB):
            if arrA[i] < arrB[j]:
                merged_arr[current_index] = arrA[i]
                current_index += 1
                i += 1
            else:
                merged_arr[current_index] = arrB[j]
                j += 1
                current_index += 1

    while i < len(arrA):
        merged_arr[current_index] = arrA[i]
        i += 1
        current_index += 1

    while j < len(arrB):
        merged_arr[current_index] = arrB[j]
        j += 1
        current_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]
     # base case
    if len(left) < 2 and len(right) < 2:
         return merge(left, right)  
    else:
         return merge(merge_sort(left), merge_sort(right))

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
