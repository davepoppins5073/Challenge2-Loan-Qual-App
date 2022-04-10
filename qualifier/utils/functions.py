"""Helper functions for dealing with user input for saving files."""

import csv
from pathlib import Path
import sys
import questionary




def file_save_location(list_of_lists):
    
    root_pth = '/Users/comdrpaquiot/Desktop/FintechWorkSpace/Python_Project/Mod2_Challenge/GitHub_Uploader/data/'
    folder = questionary.text("Please enter the folder name where we'll save this file there for you:").ask()
    
    new_path = root_pth + folder + "/"
        print(f"FYI: this is where we will save your file: {new_path}.")
        
        save_csv(new_path, data)
        
        
        

def save_csv(csvpath, data, header=None):
    """Saves the CSV file from path provided.

    Args:
        csvpath (Path): The CSV file path.
        data (list of lists): A list of the rows of data for the CSV file.
        header (list): An optional header for the CSV.

    """
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)
