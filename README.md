# *Challenge2-Loan-Qual-App*
**Showing off my new software engineering by adding save csv functionality to the code base**

---


## Directory

[Programs](code)
> "...  Here are the app.py dependencies:
> Standard Libraries
* import sys
* import os
* import fire
* import questionary
* from pathlib import Path
* import csv

User Defined libraries. These exist in the qualifier folder in the repo with the two subfolders:
> "... 1 - filters
... 2 - utils

* ... from qualifier.utils.fileio import load_csv
* ... from qualifier.utils.calculators import (
*    calculate_monthly_debt_ratio
*    calculate_loan_to_value_ratio

* from qualifier.filters.max_loan_size import filter_max_loan_size
* from qualifier.filters.credit_score import filter_credit_score
* from qualifier.filters.debt_to_income import filter_debt_to_income
* from qualifier.filters.loan_to_value import filter_loan_to_value

#### Central save functionality code 
> "...
> def save_qualifying_loans(qualifying_loans):
   
    location = os.getcwd()
    savecsvfle_ans = questionary.text("Do you want to save this of qualifying loans as a file. (Yes|No)").ask()
    
    if savecsvfle_ans.lower() == 'yes':
        with open('Qualifying_loans_2.csv', 'w') as f: 
            write = csv.writer(f) 
            write.writerows(qualifying_loans)
            print(f"Your file was sent to this folder: {location} ")
    
    elif savecsvfle_ans.lower() == 'no':
        print(f"You must have a good memory then. Peace out!")
    
    else:
        print(f"You didn't enter (yes) or (no)")
        print(f"Sorry, I'm shutting down, this is the penalty for not typing correctly")



[Data files](data)

>" ... This file needs to take data from the csv file in the data folder: daily_rate_sheet.csv.
the data in this case is a list of loans:
![data file view](https://github.com/davepoppins5073/Challenge2-Loan-Qual-App/img/App_Screenshot.png)


[Code thoughts](thoughts)
I felt it was important to use an if elif and else loop to make cover all cases if the user input a yes or no or some undefined word. I also wanted to account for ifthe user entered caps or some mixed
