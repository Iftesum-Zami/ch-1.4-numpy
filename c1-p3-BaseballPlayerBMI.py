# Import numpy
import numpy as np

height_in = [71, 79, 70, 72, 73, 74, 76, 75, 78, 73]
weight_lb = [171, 179, 170, 172, 173, 174, 176, 175, 178, 173]

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / (np_height_m ** 2)

# Print out bmi
print(bmi)