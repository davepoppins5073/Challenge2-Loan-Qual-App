# *Challenge2-Loan-Qual-App*
**Showing off my new software engineering by adding save csv functionality to the code base**

---


## Directory

[Dependencies](code)
> "...  Here are the app.py dependencies:
> Standard Libraries
* import sys
* import os
* import fire
* import questionary
* from pathlib import Path
* import csv

[User Defined libraries](code) 
These exist in the qualifier folder in the repo with the two subfolders:
<img width="777" alt="Screen Shot 2022-04-09 at 11 39 15 PM" src="https://user-images.githubusercontent.com/101449950/162600535-ec05b3ee-dd28-4911-bd09-7b96255cb8a8.png">

* ... from qualifier.utils.fileio import load_csv
* ... from qualifier.utils.calculators import (
*    calculate_monthly_debt_ratio
*    calculate_loan_to_value_ratio

(Update: added new function.py file will call a function from)
* ... from qualifier.utils.functions import file_save_location


* from qualifier.filters.max_loan_size import filter_max_loan_size
* from qualifier.filters.credit_score import filter_credit_score
* from qualifier.filters.debt_to_income import filter_debt_to_income
* from qualifier.filters.loan_to_value import filter_loan_to_value


##[Code Snippets and Explanations](code)
> "...CODE SNIPPET 1: def save_csv(csvpath, data, header=None)
> "... As is good coding practice I wanted the save CSV function to do only that save the csv, nothing more or nothing less. The one thing i did here is told the user where the file would be saved to.
> 
> def save_csv(csvpath, data, header=None):
    """ Saves the CSV file from path provided.

    Args:
        1. csvpath (Path): The CSV file path.
        2. data (list of lists): A list of the rows of data for the CSV file.
        3. header (list): An optional header for the CSV.

    """
    header = ['Lender','Max Loan Amount','Max LTV','Max DTI','Min Credit Score','Interest Rates']
    
    with open('Qualifying_loans_v2.csv', 'w') as f: 
        write = csv.writer(f) 
        write.writerow(header)
        write.writerows(data)


> "... CODE SNIPPET 2: def file_save_location(qualifying_loans)
> "... Here I wanted to firstly prompt the user with information, let them know where we were storing their file as well as the name of the file.
> "... Next I wanted to let them know that this script didnt have the functionality to create folders for  every instance a user wanted to save their output
> 
> def file_save_location(qualifying_loans):
    
    location = os.getcwd()+ "/"
    
    print(f"FYI: this is where we will save your file: {location}.")
    yesno_to_location = questionary.text("Do you have any objections to saving the file 'Qualifying_loans.csv' here Yes|No ?").ask()
    
    if type(yesno_to_location) ==str and yesno_to_location.lower() == 'no':
        save_csv(location, qualifying_loans)
    
    else:
        sys.exit("Version 2 of this app allows user to create new folders where files can be saved. Start over, do not pass go, do not collect $200 !!!")


[Data files](data)

>" ... This file needs to take data from the csv file in the data folder: daily_rate_sheet.csv.
the data in this case is a list of loans:
<img width="881" alt="App_Screenshot" src="https://user-images.githubusercontent.com/101449950/162363653-af8557ce-7a2b-495b-9bf0-a63297b1d0bb.png">



[Code thoughts](thoughts)
I felt it was important to use an if elif and else loop to make cover all cases if the user input a yes or no or some undefined word. I also wanted to account for ifthe user entered caps or some mixed
