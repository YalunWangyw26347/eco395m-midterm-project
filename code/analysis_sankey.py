import os
import pandas as pd
import plotly.graph_objects as go
from IPython.display import display
# Define file paths
IN_PATH = os.path.join("artifacts", "cleaned_placement.csv")
OUTPUT_DIR = "analysis"

df = pd.read_csv(IN_PATH)

# Separate data into male and female candidates
male_df = df[df['Gender'] == 'male']
female_df = df[df['Gender'] == 'female']


def calculate_distribution(data, output_filename):
    """calculate the proportion that people from which School Tier will work for which School Tier, and write them into a csv file"""
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


OUTPUT_DIR = "analysis"

#Visualization Sankey Diagram : 
csv_file_path = "analysis"

import plotly.graph_objects as go
def create_sankey_diagram(csv_file_path, title):
    df = pd.read_csv(csv_file_path)

    # Create a unique list of tiers
    tiers = sorted(set(df['School Tier'].unique()) | set(df['Placement Tier'].unique()))

    # Create a dictionary to map tiers to unique numbers
    tier_to_num = {tier: i for i, tier in enumerate(tiers)}

    # Map the tiers in the DataFrame to unique numbers
    df['Source'] = df['School Tier'].map(tier_to_num)
    df['Target'] = df['Placement Tier'].map(tier_to_num)
    df['Percentage'] = df['Percentage'].str.rstrip('%').astype(float)

    # Group by source and target tiers and sum the percentages
    links = df.groupby(['Source', 'Target'])['Percentage'].sum().reset_index()

    # Create a Sankey diagram figure with a custom title
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=tiers
        ),
        link=dict(
            source=links['Source'],
            target=links['Target'],
            value=links['Percentage']
        )
    ))

    # Customize the figure layout and set the title
    fig.update_layout(
        title_text=title,
        font_size=10
    )

    #return fig
    display(fig)


create_sankey_diagram(os.path.join("analysis", "tier_distribution.csv"), title="All Tier Distribution")
create_sankey_diagram(os.path.join("analysis", "tier_distribution_male.csv"), title="Male Tier Distribution")
create_sankey_diagram(os.path.join("analysis", "tier_distribution_female.csv"), title="Female Tier Distribution")



# def save_sankey_diagram(csv_file_path, title, output_filename):
#     fig = create_sankey_diagram(csv_file_path, title)
#     # Save the figure as an HTML file
#     fig.write_html(os.path.join(OUTPUT_DIR, output_filename))

# # Save the Sankey diagrams to HTML files
# save_sankey_diagram(os.path.join("analysis", "tier_distribution.csv"), title="All Tier Distribution", output_filename="all_tier_distribution.html")
# save_sankey_diagram(os.path.join("analysis", "tier_distribution_male.csv"), title="Male Tier Distribution", output_filename="male_tier_distribution.html")
# save_sankey_diagram(os.path.join("analysis", "tier_distribution_female.csv"), title="Female Tier Distribution", output_filename="female_tier_distribution.html")