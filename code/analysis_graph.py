import os
import pandas as pd
import plotly.graph_objects as go
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


labels = ["Tier 1", "Tier 2", "Tier 3", "Others"]
source = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
target = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
values = [15.08, 6.35, 2.38, 76.19, 3.57, 5.36, 3.57, 87.50, 2.22, 0.00, 3.33, 94.44, 0.00, 0.00, 0.00, 0.00]

# Create custom labels with values
custom_labels = [f"{label}<br>{value}%" for label, value in zip(labels, values)]

fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=custom_labels  # Use custom labels with values
    ),
    link=dict(
        source=source,
        target=target,
        value=values
        #color=["blue", "red", "green", "purple", "orange", "pink", "cyan", "brown"]  # Change colors of branches
    )
))

fig.update_layout(
    title="School Tier to Placement Tier All Candidates",
    font=dict(size=10)
)

fig.show()


#Let's do the visualization of the male Candidates
labels = ["Tier 1", "Tier 2", "Tier 3", "Others"]
source = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
target = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
values = [18.18, 9.09, 9.09, 63.64, 5.56, 5.56, 0.00, 88.89, 0.00, 0.00, 3.23, 0.00, 0.00, 0.00, 0.00]

# Create custom labels with values
custom_labels = [f"{label}<br>{value}%" for label, value in zip(labels, values)]

fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=custom_labels  # Use custom labels with values
    ),
    link=dict(
        source=source,
        target=target,
        value=values
        #color=["blue", "red", "green", "purple", "orange", "pink", "cyan", "brown"]  # Change colors of branches
    )
))

fig.update_layout(
    title="School Tier to Placement Tier Male  Candidates",
    font=dict(size=10)
)

fig.show()

#Let's do the visualization of the male Candidates
labels = ["Tier 1", "Tier 2", "Tier 3", "Others"]
source = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
target = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
values = [30.77, 7.69, 7.69, 53.85, 0.00, 0.00, 0.00, 100.00, 0.00, 0.00, 20.00, 80.00, 0.00, 0.00, 0.00, 0.00]

# Create custom labels with values
custom_labels = [f"{label}<br>{value}%" for label, value in zip(labels, values)]

fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=custom_labels  # Use custom labels with values
    ),
    link=dict(
        source=source,
        target=target,
        value=values
        #color=["blue", "red", "green", "purple", "orange", "pink", "cyan", "brown"]  # Change colors of branches
    )
))

fig.update_layout(
    title="School Tier to Placement Tier Female Candidates",
    font=dict(size=10)
)

fig.show()
