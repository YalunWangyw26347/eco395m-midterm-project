import os
import pandas as pd

# Read the CSV file into a DataFrame
IN_PATH = os.path.join("artifacts", "cleaned_placement.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "placement.csv")
df = pd.read_csv(IN_PATH)

# Creating new variales for school tier and placement tier
df["School Tier"] = "Not Assigned"
df["Placement Tier"] = "Not Assigned"

# Creating tier search keys
Tier_1 = [
    "Harvard University",
    "Massachusetts Institute of Technology",
    "Stanford University",
    "Princeton University",
    "University of California, Berkeley",
    "University of Chicago",
    "Yale University",
    "Northwestern University",
    "Columbia University",
    "University of Pennsylvania",
    "New York University",
]
Tier_2 = [
    "University of California, Los Angeles",
    "University of Michigan—​Ann Arbor",
    "CalTech",
    "Cornell University",
    "UCSD",
    "University of Wisconsin – Madison",
    "Duke University",
    "University of Minnesota—​Twin Cities",
    "Brown University",
]
Tier_3 = [
    "Carnegie Mellon",
    "Boston University",
    "Johns Hopkins University",
    "University of Maryland—​College Park",
    "University of Texas—​Austin",
    "UC Davis",
    "Boston College",
    "Pennsylvania State University",
    "​University of Maryland- College Park",
    "University of Rochester",
    "University of North Carolina—​Chapel Hill",
    "University of Virginia",
    "Vanderbilt University",
    "Washington University in St Louis",
    "University of Minnesota",
]
# if the string contains the search key in tier1, then tier 1 school and vice versa.
df.loc[df["School"].isin(Tier_1), "School Tier"] = "Tier 1"
df.loc[df["School"].isin(Tier_2), "School Tier"] = "Tier 2"
df.loc[df["School"].isin(Tier_3), "School Tier"] = "Tier 3"

# Creating the search string keywords for each tier.
df["Placement Tier"] = "Others"
search_strings = [
    "Harvard",
    "MIT",
    "Stanford",
    "Princeton",
    "University of California-Berkeley",
    "University of California—​Berkeley",
    "University of California ​Berkeley",
    "​Berkeley",
    "UCB",
    "Chicago",
    "Yale",
    "Northwestern",
    "Columbia",
    "Pennsylvania",
    "NYU",
    "New York",
    "Stern",
]
search_strings_1 = [
    "Brown",
    "Twin Cities",
    "Duke",
    "UWM",
    "University of Wisconsin—​Madison",
    "Wisconsin ​Madison",
    "UCSD",
    "San Diego",
    "Cornell",
    "Caltech",
    "UCLA",
    "​Los Angeles",
    "Ann Arbor",
    "University of Michigan",
]
search_strings_2 = [
    "Boston",
    "Vanderbilt",
    "WUSTL",
    "Washington University in St. Louis",
    "St. Louis",
    "University of Virginia",
    "Virgnia",
    "Pennsylvania State",
    "PSU",
    "Davis",
    "Austin",
    "College Park",
    "Johns Hopkins",
    "JHU",
    "Carnegie",
    "CMU",
]

# Create a combined pattern for all search strings
pattern1 = "|".join(search_strings)
pattern2 = "|".join(search_strings_1)
pattern3 = "|".join(search_strings_2)
# Assign "Tier 1" to rows where the "Placement" column contains any of the search strings, same for the rest of the tiers.
df.loc[
    df["Placement"].str.contains(pattern1, case=False, na=False), "Placement Tier"
] = "Tier 1"
df.loc[
    df["Placement"].str.contains(pattern2, case=False, na=False), "Placement Tier"
] = "Tier 2"
df.loc[
    df["Placement"].str.contains(pattern3, case=False, na=False), "Placement Tier"
] = "Tier 3"

df.to_csv(IN_PATH, index=False)
