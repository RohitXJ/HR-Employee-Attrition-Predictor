import os
import sys
import pandas as pd

# Add the project root directory to sys.path
# This allows Python to find 'src' as a module when test1.py is run from testing_area.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now, import from src should work
from src.data_preprocessing import process_data

# Use forward slashes for paths to avoid SyntaxWarning and for cross-platform compatibility
df = pd.read_csv('data/Test_Dataset_1_10.csv')
X = df.drop(['Attrition'], axis="columns")
y = df['Attrition'] # You might want to use 'y' later, but it's not used in this snippet

print("Original DataFrame head:")
print(X.head(2)) # Printing X (features) instead of df (original with target) for clarity

print("\nProcessed DataFrame head:")
# Ensure 'process_data' handles potential errors, e.g., if models are missing
processed_X = process_data(X.copy()) # Pass a copy to avoid modifying original df
print(processed_X.head(2))
