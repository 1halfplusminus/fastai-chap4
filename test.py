import json
import pandas as pd
# Load the data. 
# Replace 'yourfile.json' with the path to your JSON file
with open('data.json') as f:
    data = json.load(f)

# Normalize the data
# Read data from JSON file
df = pd.json_normalize(data["value"])
""" print(df.columns) """
unique_values = pd.DataFrame(df['Description'].unique(), columns=['Description'])

# Print the data
unique_values.to_csv('unique_descriptions.csv', index=False)