import os
import csv
import pandas as pd
import gender_guesser.detector as gender

### Combining data:
# Read the CSV files
BASE_DIR = "artifacts"
CSV_PATH = os.path.join(BASE_DIR, "cleaned_placement.csv")
os.makedirs(BASE_DIR, exist_ok=True)
csv_path1 = os.path.join(BASE_DIR, "rawplacement.csv")
csv_path2 = os.path.join(BASE_DIR, "Uchi PSU.csv")
csv1 = pd.read_csv(csv_path1)
csv2 = pd.read_csv(csv_path2)

# Combine the two dataframes(one from scrape and another one contain data that are not scrappable
combined_csv = pd.concat([csv1, csv2])

# Save the combined dataframe to a new CSV
combined_csv_path = os.path.join(BASE_DIR, "rawplacement_combined.csv")
combined_csv.to_csv(combined_csv_path, index=False)

### Clean the data, gender detector:
INPUT_DIR = os.path.join("artifacts", "rawplacement_combined.csv")


def load_and_clean_file():
    """load the combined raw data, and clean the data by making years 
    to form we want, only including data working as professor, 
    and adding gender column by prediction."""
    d = gender.Detector()
    with open(INPUT_DIR) as f:
        reader = csv.reader(f)
        data_list = []
        data_clean = []
        for row in reader:
            data_list.append(row)
        for data in data_list:
            if "23" not in str(data[1]):
                data[1] = 2022
            if "21" not in str(data[1]):
                data[1] = 2023
        for data in data_list:
            my_list = [
                "university",
                "Uni",
                "institu",
                "Insti",
                "college",
                "Coll",
                "Professor",
                "professor",
            ]
            not_list = ["Pos", "pos"]
            contains_keyword = any(keyword in data[3] for keyword in my_list)
            contains_not_keyword = any(keyword in data[3] for keyword in not_list)
            if contains_keyword == True and contains_not_keyword == False:
                data_clean.append(data)

        for data in data_clean:
            name = data[2]
            first_name = name.split(" ")[0]
            guess = d.get_gender(first_name)
            data.append(guess)
        for data in data_clean:
            sex = data[4]
            if "male" in sex:
                data[4] = "male"
            if "female" in sex:
                data[4] = "female"
            if "female" and "male" not in sex:
                data[4] = "N/A"

        return data_clean


def write_data_to_csv(rawdata, path):
    """wirte the cleandata"""
    with open(path, "w", newline="") as csvfile:
        fieldnames = ["School", "Year", "Name", "Placement", "Gender"]
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for row in rawdata:
            writer.writerow(row)
    return


if __name__ == "__main__":
    rawdata = load_and_clean_file()

    write_data_to_csv(rawdata, CSV_PATH)
