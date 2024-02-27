# Import numpy
import numpy as np

height_in = [71, 79, 70, 72, 73, 74, 76, 75, 78, 73]
weight_lb = [171, 179, 170, 172, 173, 174, 176, 175, 178, 173]

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])