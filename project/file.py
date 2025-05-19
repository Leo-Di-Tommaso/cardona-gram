import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('C:/Users/Leonardo/Documents/GitHub/cardona-gram/project/files/it_full.csv')

# Apply regex to remove numbers from a specific column (e.g., 'word_column')
df['word_column'] = df['word_column'].apply(lambda x: re.sub(r'\s\d+$', '', str(x)))

# Save the cleaned data back to CSV
df.to_csv('it_full.csv', index=False)