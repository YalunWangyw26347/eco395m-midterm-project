import os
import csv
import gender_guesser.detector as gender
INPUT_DIR = os.path.join("artifacts", "rawplacement.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "cleanplacement.csv")

def load_file():
    with open(INPUT_DIR) as f:
        reader = csv.reader(f)
        data_list=[]
        data_clean=[]
        for row in reader:
            data_list.append(row)
        for data in data_list:
            if "23" not in str(data[1]):
                data[1]= 2022
            if "21" not in str(data[1]):
                data[1]=2023
        for data in data_list:
            if (("university" in data[3]) or("Uni" in data[3])or ("institu" in data[3])or("Insti" in data[3]) or ("college" in data[3])or("Coll" in data[3]) or("Prof" in data[3])or("prof" in data[3])) and (("post" not in data[3])or ("Post" not in data[3])):
                data_clean.append(data)
    
    d = gender.Detector()
    for data in data_list:
        print(data)
        name = data[2]
        first_name = name.split(" ")[0]
        print(name)
        print(first_name)
        guess = d.get_gender(first_name)
        print(guess)
        data.append(guess)
    print(data_list)
    return


load= load_file()


