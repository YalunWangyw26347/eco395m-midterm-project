import os
import pandas as pd

# Read the CSV files
BASE_DIR = "artifacts"
csv_path1 = os.path.join(BASE_DIR, "rawplacement.csv")
csv_path2 = os.path.join(BASE_DIR, "Uchi PSU.csv")

csv1 = pd.read_csv(csv_path1)
csv2 = pd.read_csv(csv_path2)

# Combine the two dataframes
combined_csv = pd.concat([csv1, csv2])

# Save the combined dataframe to a new CSV
combined_csv_path = os.path.join(BASE_DIR, "rawplacement1.csv")
combined_csv.to_csv(combined_csv_path, index=False)

