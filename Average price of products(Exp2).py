import numpy as np
sales_data = np.array([
    [220,240,260],
    [150, 140,170],
    [300, 310, 320]
])
avg_price = np.mean(sales_data)
print("Average product price:", avg_price)