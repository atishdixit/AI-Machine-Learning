import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward', 'Frank'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Score': [85, 78, 92, 88, 76, 95]
}
df = pd.DataFrame(data)
grouped_df = df.groupby('Subject')['Score'].mean()
print(grouped_df)