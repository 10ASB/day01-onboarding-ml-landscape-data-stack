import pandas as pd

# Create a sample DataFrame
data = {
    "NAME": ["ASB", "RAI", "VIK", "ARVIND", "ANAND"],
    "AGE": [20, 21, 20, 25, 21],
    "MARKS": [85, 90, 88, 95, 80]
}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nInfo:")
df.info()

print("\nDescribe:")
print(df.describe())

print("\nAge counts:")
print(df["AGE"].value_counts())

# Apply
df["MARKS + 5"] = df["MARKS"].apply(lambda x: x + 5)
print("\nAfter apply:")
print(df)

# Group by
print("\nAverage marks by age:")
print(df.groupby("AGE")["MARKS"].mean())
