import os
import csv
## import data from scrape.py here


def write_data_to_csv(data, path):
    """Write the data to the csv file."""

    headers = ["School", "Year","Name", "Placement"]
    with open(path, "w+", newline="") as out_file:
        write = csv.writer(out_file)
        write.writerow(headers)
        write.writerows(data)


if __name__ == "__main__":
    data = 
    OUTPUT_DIR = "artifacts"
    OUTPUT_PATH = os.path.join(OUTPUT_DIR, "placement.csv")
    write_data_to_csv(data, OUTPUT_PATH)