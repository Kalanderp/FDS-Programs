import numpy as np
car_data = np.array([
    [300, 11],
    [450, 15],
    [600, 21],
    [150, 5],
    [500, 18]
])
mpg = car_data[:,0] / car_data[:,1]
avg_mpg = np.mean(mpg)
print("Miles per gallon for each car:", mpg)
print("Average MPG for all cars:", avg_mpg)