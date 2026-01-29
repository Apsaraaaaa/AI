import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print(df)

print("\nDescription:\n", df.describe())

