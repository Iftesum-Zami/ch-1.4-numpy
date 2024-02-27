# Import numpy package
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]  # more remaining

updated = [[1, -6],
            [3, 7],
            [-10, 5],
            [8, 2]]  # more remaining

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])  # on ques, there are 3 columns

# Print out product of np_baseball and conversion
print(np_baseball * conversion)