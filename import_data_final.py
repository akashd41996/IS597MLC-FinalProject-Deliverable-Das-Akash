import time
from datetime import timedelta
import pandas as pd
import nltk
import os
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.model_selection import train_test_split
import numpy as np
import zipfile
import shutil
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder



def load_and_create_dataframes(directory_path):
    """
    Processes and converts ZIP and CSV files in a given directory into pandas DataFrames. 
    Organizes DataFrames in a dictionary by file name.
    """
    # Ensure the target directory for unzipped files exists, create if it doesn't
    target_directory = os.path.join(directory_path, 'unzippedfiles')
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Process each file in the directory: unzip or move CSVs
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Unzip if the file is a zip file
        if filename.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(target_directory)
                # Remove __MACOSX folder if it exists
                macosx_path = os.path.join(target_directory, '__MACOSX')
                if os.path.exists(macosx_path):
                    shutil.rmtree(macosx_path)

        # Move if the file is a CSV file
        elif filename.endswith('.csv'):
            shutil.move(file_path, os.path.join(target_directory, filename))

    # Create dataframes from CSV files in the target directory
    dataframes = {}
    for file_name in os.listdir(target_directory):
        if file_name.startswith('olist_') and file_name.endswith('_dataset.csv'):
            df_key = file_name.replace('olist_', '').replace('_dataset.csv', '')
            dataframes[df_key] = pd.read_csv(os.path.join(target_directory, file_name))
            print(f"DataFrame for {df_key} created with shape {dataframes[df_key].shape}")

        # Handling the 'product_category_name_translation' dataframe
        elif file_name == 'product_category_name_translation.csv':
            dataframes['product_category_name_translation'] = pd.read_csv(os.path.join(target_directory, file_name))
            print(f"DataFrame for product_category_name_translation created with shape {dataframes['product_category_name_translation'].shape}")

    return dataframes