from numpy import random
import numpy as np


def generateRandomNumbers():
    """Function to understand how to generate single random int or float"""
    print("Random int: ", random.randint(0, 10))
    print("Random float between 0 and 1: ", random.rand())
    print("Random float between 10 and 20: ", random.uniform(10, 20))
    print("-" * 25)


def generateRandomArrays():
    """Function to understand how to generate 1-d array of random int or float"""

    print("One Dimensional array")
    print("Random int array: ", random.randint(low=5, high=12, size=5))
    print("Random float array: ", random.rand(3))
    print("Random float array of 5 elements between 10 and 20: ", random.uniform(10, 20, 5))
    print("-" * 25)


def generateRandomArrays2():
    """Function to understand how to generate 1-d array of random int or float"""

    print("Two Dimensional array")
    print("Random int array: ", random.randint(low=5, high=12, size=(2, 3)))
    print("Random float array: ", random.rand(3, 2))
    print("Random float array of 5 elements between 10 and 20: ", random.uniform(10, 20, (2, 2)))
    print("-" * 25)


def generateRandomArraysWithChoice():
    """Function to understand how to generate 1-d array of random int or float with choice function"""

    print("generateRandomArraysWithChoice")
    print("Random int array with choice : ", random.choice([10, 20, 30, 40, 11], 3))
    print("Random int array with choice and probability: ", random.choice([10, 20, 30], 6, p=[0.25, 0.45, 0.30]))
    print("Random float array with choice : ", random.choice([10.5, 12.0, 11.25, 31.5], 3))
    print("-" * 25)


def shuffle_and_permutation_demo():
    """Function to understand shuffle and permutation functions from random module"""

    arr = np.array([1, 2, 3, 4, 5])
    print("Array before shuffling: ", arr)
    random.shuffle(arr)
    print("Array post shuffling: ", arr)

    arr = np.array([6, 7, 8, 9])
    print("Input Array before permutation: ", arr)
    permutation_arr = random.permutation(arr)
    print("Input Array post permutation: ", arr)
    print("Permutation Array post permutation: ", permutation_arr)
    print("-" * 25)


def main():
    print("Version of numpy", np.__version__)
    generateRandomNumbers()
    generateRandomArrays()
    generateRandomArrays2()
    generateRandomArraysWithChoice()
    shuffle_and_permutation_demo()


if __name__ == "__main__":
    main()
