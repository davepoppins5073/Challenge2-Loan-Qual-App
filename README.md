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


```python
from qualifier.utils.fileio import load_csv
from qualifier.utils.calculators import (
calculate_monthly_debt_ratio
calculate_loan_to_value_ratio
```

(Update: added new function.py file will call a function from)
```python
from qualifier.utils.functions import file_save_location
```

```python
from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value
```

[Code Snippets and Explanations](code)
> "...CODE SNIPPET 1:  def save_csv(csvpath, data, header=None)
> "... As is good coding practice I wanted the save CSV function to do only that save the csv, nothing more or nothing less. The one thing i did here is told the user where the file would be saved to.

```python
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
```

> "... CODE SNIPPET 2: def file_save_location(qualifying_loans)
> "... Here I wanted to firstly prompt the user with information, let them know where we were storing their file as well as the name of the file.
> "... Next I wanted to let them know that this script didnt have the functionality to create folders for  every instance a user wanted to save their output
> 
```python
> def file_save_location(qualifying_loans):
    
    location = os.getcwd()+ "/"
    
    print(f"FYI: this is where we will save your file: {location}.")
    yesno_to_location = questionary.text("Do you have any objections to saving the file 'Qualifying_loans.csv' here Yes|No ?").ask()
    
    if type(yesno_to_location) ==str and yesno_to_location.lower() == 'no':
        save_csv(location, qualifying_loans)
    
    else:
        sys.exit("Version 2 of this app allows user to create new folders where files can be saved. Start over, do not pass go, do not collect $200 !!!")
```
CODE SNIPPET 3: def save_qualifying_loans(qualifying_loans)
>" ... This to me is the where the magic happens in this script. There are multiple conditionals here
> first If clause --  if there was some data in the qualifying loans list of list, then we could proceed
> nested if: if the user didnt enter a string the they should know. Used a sys.exit() here
> 1st elif: if the answer is a string  and equal to "no" or anything else the user should know. Used another sys.exit() here
> 2nd elif: if the answer is a string & is a "yes" we called the file_save_location function
> else  if the list of list was empty i.e. no qualifying loans we should send the person away
> 

```python
def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.
        
        We should only save the qualifying loans to a csv pIf there are loans in the dataframe. 
        There exists the possibility that the the user qualified for no loans and as such we need 
        to let them know. 

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    
    if len(qualifying_loans):
        savecsvfle_ans = questionary.text("Do you want to save this of qualifying loans as a file. (Yes|No)").ask()
        
        # Verifies the answer input was a string
        if type(savecsvfle_ans) !=str:
            sys.exit("You have embarassed your family & teachers by your inability to type: 'yes' or 'no'. Scram.")
        
        elif type(savecsvfle_ans) ==str and savecsvfle_ans.lower() != 'yes':
            sys.exit("You either answered 'No' or typed in ?1?! Buh-Bye! We don't want you to use our app anyways.")
        
        elif type(savecsvfle_ans) ==str and savecsvfle_ans.lower() == 'yes':
            file_save_location(qualifying_loans)
        
    else:
        print("No loans muchacho")
        sys.exit("In the words of Rick Ross: Get your money up. Bye !")
```
>" ...

[Data files](code)
<img width="777" alt="Screen Shot 2022-04-10 at 12 48 37 AM" src="https://user-images.githubusercontent.com/101449950/162601952-4c071bdd-ce99-404f-85c1-338bf4e44a4d.png">


>" ... This file needs to take data from the csv file in the data folder: daily_rate_sheet.csv.
the data in this case is a list of loans.


[Code Screenshots](code)
<img width="881" alt="App_Screenshot" src="https://user-images.githubusercontent.com/101449950/162363653-af8557ce-7a2b-495b-9bf0-a63297b1d0bb.png">



[Code thoughts](thoughts)
I got the following feedback and decided to go through the code and make some updates:
>"  Great job understanding the techniques behind the application and solving the required TODOS. Your coding logic and intuition was good when you tried to save the qualified loans to a csv file. However, you focused more on applying write rows techniques, than on using the libraries imported above, such as sys, path and questionary. These libraries were imported to help you with save qualifying loan logic. 

So to that end i changed the structure of my code around to do the following
1. In app.py I changed the save_qualifying_loans function to utilize the sys.exit() more
2. Created a separate function.py with two functions, only one of which was called. I made sure to make use of questionary and sys.exit()
