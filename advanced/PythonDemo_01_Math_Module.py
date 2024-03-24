# This file provides demo of math module
import math

n1, n2 = 5, 144
n3, n4, n5 = 5.02, 5.72, 5.50
n6, n7, n8 = -0.13, 39, -23

print(f"Square of {n1}: {math.pow(n1, 2)}")
print(f"Square root of {n2}: {math.sqrt(n2)}")
print(f"Factorial of {n1}: {math.factorial(n1)}")

print(f"ceil of {n3}: {math.ceil(n3)}")
print(f"ceil of {n4}: {math.ceil(n4)}")
print(f"ceil of {n5}: {math.ceil(n5)}")
print(f"ceil of {n6}: {math.ceil(n6)}")


print(f"floor of {n3}: {math.floor(n3)}")
print(f"floor of {n4}: {math.floor(n4)}")
print(f"floor of {n5}: {math.floor(n5)}")
print(f"floor of {n6}: {math.floor(n6)}")


print(f"absolute value of {n6}: {math.fabs(n6)}")
print(f"absolute value of {n7}: {math.fabs(n7)}")
print(f"absolute value of {n8}: {math.fabs(n8)}")

print("value of pi: ", math.pi)