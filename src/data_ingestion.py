import os
import pandas as pd

DATA_FOLDER = "data/raw"

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 70)
    print("File:", file)

    file_path = os.path.join(DATA_FOLDER, file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst Five Rows:")
    print(df.head())

    print("=" * 70)
    