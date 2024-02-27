# Import numpy
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]   # be carefull with multi dim array

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))