import numpy as np
house_data = np.array([
    [3, 2000, 250000],
    [5, 3000, 400000],
    [4, 1800, 220000],
    [6, 3500, 500000]
])
houses_over4 = house_data[house_data[:,0] > 4]
avg_price_4plus = np.mean(houses_over4[:,2])
print("Average price of houses with >4 bedrooms:", avg_price_4plus)