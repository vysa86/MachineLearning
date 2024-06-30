import pandas as pd
import numpy as np
# Original dataset
data = {
    'Size (sq ft)': [1500, 1800, 2400, 3000, 1200, 2000, 2100, 3500, 4000, 1400],
    'Number of Bedrooms': [3, 4, 3, 5, 2, 4, 3, 5, 6, 2],
    'Age of House (years)': [10, 5, 20, 15, 25, 8, 12, 6, 4, 30],
    'Price ($)': [300000, 400000, 350000, 500000, 250000, 450000, 420000, 600000, 750000, 220000]
}

df = pd.DataFrame(data)
print(df)
