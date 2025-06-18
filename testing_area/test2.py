import os
import sys

# Get the current directory of this script
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Traverse up the directory tree until 'src' is found, or we hit the root
project_root = current_script_dir
while not os.path.exists(os.path.join(project_root, 'src')) and project_root != os.path.dirname(project_root):
    project_root = os.path.dirname(project_root)

# If 'src' is found in the current directory, then the current directory is the project root
if os.path.exists(os.path.join(current_script_dir, 'src')):
    project_root = current_script_dir

# Add the determined project root to sys.path if not already there
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.predictor import predict_attrition
import pandas as pd

df = pd.read_csv('data/Test_Dataset_1_10.csv') # Ensure this path is correct relative to the project root
print(df.head(2))

print("result", predict_attrition(df.drop(['Attrition'], axis="columns")))