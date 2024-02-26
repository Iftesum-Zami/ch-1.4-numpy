# height = [1.73, 1.68, 1.71, 1.89, 1.79]
# weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# bmi = weight/(height ** 2)

# ^^^^^^^^^^ above code wont work ^^^^^^^^^^^^^

import numpy as np 
# you can give any name. The benifit is u dont have to use "numpy.()" each time. Will use "np.()"

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

npHeight = np.array(height)  # to convert our height list as numpy array
npWeight = np.array(weight)

bmi = npWeight/(npHeight ** 2)
print("\n1st case>>")
print(bmi)

print("\n2nd case>>")
print(bmi > 23)  # it will give boolean result i.e. True(1) 
print(bmi[bmi > 23])

# numpy array operation goes through each element whereas normal list can't do element wise calculation
# caution: numpy arrays contain only one type
# numpy array is also another kind of data type

print("\n3rd case>>")
pythonList = [1, 2, 3]
numpyArray = np.array(pythonList)

print(pythonList + pythonList)
print(numpyArray + numpyArray)
# check the difference here
