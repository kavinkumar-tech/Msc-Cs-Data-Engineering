import pandas as pd

# Load dataset
df = pd.read_csv(r"E:\26mcs03\archive\student_performance.csv")

# Display dataset
print("Dataset:")
print(df.head())

# Display shape
print("\nShape of Dataset:")
print(df.shape)

# Display number of rows and columns
print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# Display feature names
print("\nFeature Names:")
print(list(df.columns))

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))
