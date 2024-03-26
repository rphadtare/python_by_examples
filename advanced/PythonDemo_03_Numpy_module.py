# This file provides demo for numpy module
import numpy as np
import random


def initialisation_demo():
    # To create empty array
    arr = np.zeros(5, 'i')
    print("Empty arr: ", arr, " dtype:", arr.dtype, " dimension: ", arr.ndim)

    str_arr = np.zeros(5, "O")
    print("Empty string arr: ", str_arr, " dtype:", str_arr.dtype, " dimension: ", str_arr.ndim)

    arr = np.ones(5, 'i')
    print("Array with ones : ", arr, " dtype:", arr.dtype, " dimension: ", arr.ndim)

    str_arr = np.full(5, "Test", object)
    print("String arr with default values: ", str_arr, " dtype:", str_arr.dtype, " dimension: ", str_arr.ndim)

    zero_like_arr = np.zeros_like(arr)
    print("zero_like_arr: ", zero_like_arr, " dtype:",
          zero_like_arr.dtype, " dimension: ", zero_like_arr.ndim)

    one_like_arr = np.ones_like(str_arr, dtype='f', shape=2)
    print("one_like_arr: ", one_like_arr, " dtype:", one_like_arr.dtype,
          " dimension: ", one_like_arr.ndim)

    full_like_arr = np.full_like(one_like_arr, fill_value="Hi", dtype=object, shape=[1, 2])
    print("full_like_arr: ", full_like_arr, " dtype:", full_like_arr.dtype,
          " dimension: ", full_like_arr.ndim)


def one_dimensional_array():
    num_list = random.sample(range(0, 100), 7)
    arr = np.array(num_list, 'i')
    print("Accessing elements using indexing of one dimensional array")
    for i in range(arr.size):
        print(f"arr[{i}]: {arr[i]}", end="\t")

    print("")
    print("Updating value at 2nd position to 39")
    arr[1] = 39
    print("Post updating value at 2nd position: ", arr)

    print("Updating values at more than one position using slicing "
          " i.e. position 6 and 7 ")
    arr[5:7] = 29
    print("Post updating value at 6th and 7th position: ", arr)

    print("Array from 2nd element till 7th element "
          "with skip = 2 "
          "using slicing: ", arr[1:6:2])

    print("To access array using negative indexing ", arr[-3:])

    print("To reverse array ", arr[::-1])


def two_dimensional_arr():
    # empty array with zero values
    arr = np.zeros((2, 2), dtype='i')
    print("2-D array with zero values ", arr)

    # initialising array with values
    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, -1]], dtype='i')
    print("2-D array with initial values ", arr, " dimension: ", arr.ndim,
          " Data type: ", arr.dtype, " size of array: ", arr.size,
          "shape: ", arr.shape)

    # accessing elements using index
    print("element at 1st row and 2nd column: ", arr[1, 1])

    # updating value at particular position
    print("update value at 1st row and 2nd column to 9")
    arr[1, 1] = 9
    print("Array post updating element at 1st row and 2nd column")
    print(arr)

    # updating value at multiple position
    print("update value at 2nd row: 7")
    arr[2:3] = 7
    print("Array post updating element at 3rd row")
    print(arr)

    new_arr = arr[1:4:2]
    # get 2-D array from existing one
    print("Getting new 2-D array from existing one using"
          "slicing", new_arr, " shape: ", new_arr.shape)

    new_arr = arr[1:4:2, 0:1]
    # get 2-D array from existing one with one column
    print("Getting new 2-D array with one column "
          "from existing one using"
          "slicing", new_arr, " shape: ", new_arr.shape)

    # reverse 2-D array
    print("Reverse 2-D array ", arr[::-1])


def copy_and_view_demo():
    arr = np.array([1, 2, 3, 4], dtype=int)
    print("Original arr : ", arr, " base: ", arr.base)
    arr1 = arr.copy()
    print("Copied arr : ", arr1, " base: ", arr1.base)
    arr2 = arr.view()
    print("Viewed arr : ", arr2, " base: ", arr2.base)

    print("updating element at 1st index "
          "in copied array with value 5 and"
          "view with value 7")

    arr1[1] = 5
    arr2[2] = 7

    print("post update")
    print(f"original array: {arr}")
    print(f"Copied array: {arr1}")
    print(f"view: {arr2}")


def shapeDemo():
    arr = np.full((3, 2), 1, dtype='i')
    for i in arr:
        for j in i:
            print(j, end="\t")
        print("")


def reShapeDemo():

    num_list = random.sample(range(1, 100), 7)
    arr = np.array(num_list, dtype='i')
    print(f"Input array before resize: {arr} with shape: {arr.shape} and base: {arr.base}")

    try:
        reshaped_arr = np.reshape(arr, newshape=(2, 4))

    except ValueError as v:
        print("Error received : ", v)
        print("Need to resize now input array !!!")

        arr = np.resize(arr, 8)
        print(f"Input array post resize: {arr} with shape: {arr.shape} and base: {arr.base}")

        reshaped_arr = np.reshape(arr, newshape=(2, 4))
        print(f"Reshaped array with new shape: {reshaped_arr.shape} and base: {reshaped_arr.base}")
        for i in reshaped_arr:
            for j in i:
                print(j, end="\t")
            print("")

    finally:
        print("-"*50)

def reShapeDemo2():
    arr = np.array([[1, 2, 3], [4, 5, 6]], dtype='i')
    print(f"Input array before reshape: {arr} with shape: {arr.shape} and base: {arr.base}")
    arr1 = arr.flatten()
    arr2 = arr.ravel()
    print("Flatten existing array: ", arr1, " with base: ", arr1.base)
    print("ravel existing array: ", arr2, " with base: ", arr2.base)


def itrDemo():
    arr = np.array([[1, 2, 3], [4, 5, 6]], dtype='i')
    for x in np.nditer(arr[::, :2], flags=['buffered'], op_dtypes='S'):
        print(x)

def joinDemo():
    arr1 = np.array([1, 2, 3, 4, 5], dtype='i')
    arr2 = np.array([7, 8, 9, 10, 11], dtype='i')

    # using concatenate
    print(np.concatenate((arr1, arr2)))

    # using stack
    print(np.stack((arr1, arr2), axis=1))

    # using hstack
    print(np.hstack((arr1, arr2)))

    # using vstack
    print(np.vstack((arr1, arr2)))

def main():
    print("Version of numpy", np.__version__)
    reShapeDemo()


if __name__ == "__main__":
    main()
