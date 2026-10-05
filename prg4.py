import pandas as pd

# Load dataset
df = pd.read_csv(r"E:\26mcs03\archive\student_performance.csv")

print("Dataset:")
print(df.head())

# Count missing values in each column
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Calculate percentage of missing values
missing_percentage = (df.isnull().sum() / len(df)) * 100

print("\nPercentage of Missing Values:")
print(missing_percentage)

# Total number of missing values
total_missing = df.isnull().sum().sum()

print("\nTotal Missing Values:", total_missing)

# Check duplicate records
duplicates = df.duplicated().sum()

print("Number of Duplicate Records:", duplicates)

# Display data quality information
print("\nData Quality Report:")

quality_report = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Missing Percentage": missing_percentage,
    "Data Type": df.dtypes.astype(str),
    "Unique Values": df.nunique()
})

print(quality_report)
