import os
import pandas as pd
import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use(['seaborn-v0_8-muted'])
# Define file paths
IN_PATH = os.path.join("artifacts", "cleaned_placement.csv")
OUTPUT_DIR = "analysis"

df = pd.read_csv(IN_PATH)

# Separate data into male and female candidates
male_df = df[df['Gender'] == 'male']
female_df = df[df['Gender'] == 'female']

def calculate_distribution(data):
    """Calculate the proportion that people from which School Tier will work for which School Tier."""
    result_df = pd.DataFrame(columns=['School Tier', 'Placement Tier', 'Percentage'])

    for school_tier in ['Tier 1', 'Tier 2', 'Tier 3']:
        for placement_tier in ['Tier 1', 'Tier 2', 'Tier 3', 'Others']:
            total_candidates = len(data[data['School Tier'] == school_tier])
            assistant_professors = len(data[(data['School Tier'] == school_tier) & (data['Placement Tier'] == placement_tier)])
            percentage = (assistant_professors / total_candidates) * 100
            result_df = pd.concat([result_df, pd.DataFrame({'School Tier': [school_tier], 'Placement Tier': [placement_tier], 'Percentage': [percentage]})], ignore_index=True)

    return result_df

def plot_pie_chart(data, title):
    """Plot pie chart for the given data and title."""
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    for index, school_tier in enumerate(['Tier 1', 'Tier 2', 'Tier 3']):
        sub_data = data[data['School Tier'] == school_tier]
        labels = sub_data['Placement Tier']
        values = sub_data['Percentage']
        
        axes[index].pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        axes[index].set_title(school_tier)
        
    fig.suptitle(title, fontsize=16)
    output_filename = os.path.join(OUTPUT_DIR, f"{title.replace(' ', '_').lower()}.png")
    plt.savefig(output_filename)
    plt.close()

# Plotting pie charts
plot_pie_chart(calculate_distribution(df), "Overall Tier Distribution")
plot_pie_chart(calculate_distribution(male_df), "Male Tier Distribution")
plot_pie_chart(calculate_distribution(female_df), "Female Tier Distribution")
