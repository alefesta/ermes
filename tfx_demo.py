import pandas as pd 
import numpy as np


df = pd.DataFrame(
  np.random.randint(0, 5, size=(100, 4)), 
  columns=[f'column{i}' for i in range(0, 4)]
)

print(df)