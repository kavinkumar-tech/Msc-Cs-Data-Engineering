import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# ------------------------------------------------
# Load Dataset
# ------------------------------------------------

file_path = r"E:\26mcs03\archive\student_performance.csv"

df = pd.read_csv(file_path)

print("Original Dataset:")
print(df.head())

# ------------------------------------------------
# 1. Handle Missing Values
# ------------------------------------------------

# Numerical columns
numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

# Fill numerical missing values with median
for column in numeric_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].median())

# Categorical columns
categorical_columns = df.select_dtypes(exclude=np.number).columns.tolist()

# Fill categorical missing values with mode
for column in categorical_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# ------------------------------------------------
# 2. Remove Duplicate Records
# ------------------------------------------------

df = df.drop_duplicates()

print("\nNumber of Duplicate Records Removed:", df.duplicated().sum())

# ------------------------------------------------
# 3. Detect Outliers using IQR
# ------------------------------------------------

print("\nOutliers:")

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(column, ":", len(outliers), "outliers")

# ------------------------------------------------
# 4. Normalize Numerical Data
# ------------------------------------------------

scaler = MinMaxScaler()

if len(numeric_columns) > 0:
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# ------------------------------------------------
# 5. Display Preprocessed Dataset
# ------------------------------------------------

print("\nPreprocessed Dataset:")
print(df.head())

# ------------------------------------------------
# 6. Display Final Dataset Information
# ------------------------------------------------

print("\nFinal Shape:")
print(df.shape)

print("\nFinal Data Types:")
print(df.dtypes)

