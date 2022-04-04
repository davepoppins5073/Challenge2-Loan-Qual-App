# *Challenge2-Loan-Qual-App*
**Showing off my new software engineering by adding save csv functionality to the code base**

---


## Directory

[Programs](code)
Here are the app.py dependencies:

### - Standard Libraries
*import sys
*import os
*import fire
*import questionary
*from pathlib import Path
*import csv

### - User Defined libraries. These exist in the qualifier folder in the repo with the two subfolders:
*1 - filters
*2 - utils

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value



[Data files](data)
this file needs to take data from the csv file in the data folder: daily_rate_sheet.csv.
the data in this case is a list of loans


