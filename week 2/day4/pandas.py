import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Displaying the first few rows of the DataFrame
print("First 5 rows:")
print(df.head())

# Writing DataFrame to a CSV file
df.to_csv('output.csv', index=False)


# Basic operations
print("Average age:", df['Age'].mean())

# Aggregating data
city_counts = df['City'].value_counts()
print("\nCity counts:")
print(city_counts)

# Creating two DataFrames
data1 = {'A': ['A0', 'A1', 'A2'],
         'B': ['B0', 'B1', 'B2']}
data2 = {'C': ['C0', 'C1', 'C2'],
         'D': ['D0', 'D1', 'D2']}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Concatenating DataFrames along rows
result_concat = pd.concat([df1, df2], axis=1)
print("Concatenated DataFrame:")
print(result_concat)

# Merging DataFrames based on a common column
data3 = {'A': ['A0', 'A1', 'A2'],
         'key': ['K0', 'K1', 'K2']}
data4 = {'B': ['B0', 'B1', 'B2'],
         'key': ['K0', 'K1', 'K2']}
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)
merged_df = pd.merge(df3, df4, on='key')
print("\nMerged DataFrame:")
print(merged_df)
