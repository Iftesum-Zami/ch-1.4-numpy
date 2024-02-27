# Import numpy
import numpy as np

heights = [71, 79, 70, 72, 73, 74, 76, 75, 78, 73]
positions = [171, 179, 170, 172, 173, 174, 176, 175, 178, 173]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
med1 = np.median(gk_heights)
print("Median height of goalkeepers: " + str(med1))

# Print out the median height of other players. Replace 'None'
med2 = np.median(other_heights)
print("Median height of other players: " + str(med2))