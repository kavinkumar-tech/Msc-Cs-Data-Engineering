
import pandas as pd
df = pd.read_csv(r"E:\26mcs03\archive\student_performance.csv")
print("========== DATASET ==========")
print(df)
print("\n========== DATASET INFORMATION ==========")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])
print("\n========== MISSING VALUES BY COLUMN ==========")
missing_count = df.isnull().sum()
print(missing_count)
print("\n========== MISSING VALUE PERCENTAGE ==========")
missing_percentage = (df.isnull().sum() / len(df)) * 100

for column in df.columns:
    print(column, ":", round(missing_percentage[column], 2), "%")
total_missing = df.isnull().sum().sum()

print("\nTotal Missing Values :", total_missing)
duplicates = df.duplicated().sum()
print("Duplicate Records   :", duplicates)
total_cells = df.shape[0] * df.shape[1]
missing_ratio = (total_missing / total_cells) * 100
print("\n========== DATA QUALITY ==========")
if missing_ratio == 0 and duplicates == 0:
    print("Data Quality : Excellent")
elif missing_ratio <= 5 and duplicates <= 2:
    print("Data Quality : Good")
elif missing_ratio <= 20:
    print("Data Quality : Moderate")
else:
    print("Data Quality : Poor")

print("Missing Data Ratio :", round(missing_ratio, 2), "%")


