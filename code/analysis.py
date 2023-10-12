import os
import pandas as pd

# Define file paths
IN_PATH = os.path.join("artifacts", "cleaned_placement.csv")
OUTPUT_DIR = "analysis"

df = pd.read_csv(IN_PATH)

# Separate data into male and female candidates
male_df = df[df['Gender'] == 'male']
female_df = df[df['Gender'] == 'female']

# Function to calculate and save tier distribution for male and female candidates
def calculate_distribution(data, output_filename):
    result_df = pd.DataFrame(columns=['School Tier', 'Placement Tier', 'Percentage'])

    for school_tier in ['Tier 1', 'Tier 2', 'Tier 3']:
        for placement_tier in ['Tier 1', 'Tier 2', 'Tier 3', 'Others']:
            total_candidates = len(data[data['School Tier'] == school_tier])
            assistant_professors = len(data[(data['School Tier'] == school_tier) & (data['Placement Tier'] == placement_tier)])
            percentage = (assistant_professors / total_candidates) * 100
            result_df = pd.concat([result_df, pd.DataFrame({'School Tier': [school_tier], 'Placement Tier': [placement_tier], 'Percentage': ['{:.2f}%'.format(percentage)]})], ignore_index=True)

    # Save the results to a CSV file in the "artifacts" directory
    result_df.to_csv(os.path.join(OUTPUT_DIR, output_filename), index=False)


#Normal Distribution
calculate_distribution(df, "tier_distribution.csv")

# Tier distribution for Male candidates
calculate_distribution(male_df, "tier_distribution_male.csv")

# Tier distribution for Female candidates
calculate_distribution(female_df, "tier_distribution_female.csv")
