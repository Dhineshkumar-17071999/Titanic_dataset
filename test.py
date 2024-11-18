import numpy as np
import pandas as pd

# Sample dataset
df = pd.DataFrame({'Age': [25, 30, 35, 40, 120, 28, 32, 150]})

# Sample dataset
df['Z_Score'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()

# Find outliers with Z-score above 3 or below -3
outliers = df[np.abs(df['Z_Score']) > 1]
print(outliers)