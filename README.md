# College Expenses


## Name
college-expenses


## Description

Create an application in python that reads in data from a data store, displays it, and lets the user change it, and then save it to the data store. Use generative AI/ chatGPT to generate blocks of code and test cases. 



## Project Organization

- [ ] src- source code for project
- [ ] test- test plan and test report
- [ ] data- data sources to run and test program
- [ ] project- project plan and epics


## Usage

Clone the project repository to a local workspace.

```
git clone https://gitlab.clarityinnovations.biz/jconway/college-expenses.git
```

Cd into college-expenses
Run the program

```
$ python main.py 

Menu:
1. Load data
2. Calculate totals
3. Sort by total cost
4. Exit program
Select an option: 
```

Select option 1 and enter the name of a valid csv file to load data into the program.

```
Menu:
1. Load data
2. Calculate totals
3. Sort by total cost
4. Exit program
Select an option: 1
Enter the name of the CSV file: expense.csv
Data loaded successfully.
                       Name  Tuition   Room  Board  Books  Fees  Other_Expenses  Scholarship
0    University of Maryland    20000  12000   5500   1050   750            1500            0
1                Penn State    35000  10250   5000    975   670            5000            0
2             Florida State    36550  11500   5050   1100   730            1300            0
3  James Madison University    29500  15000   7000    500   450            2750            0
4             Virginia Tech    33857  12200   6700    830   590            2000            0
5    University of Delaware    36880  15470   6700   1200  3400            1750            0
6                    Towson    18516  10080   8070    550  1500             900            0
7                 Salisbury    11188  10900   8500   3750  3700            1200            0
```

Select option 2 to calculate the total cost for each college in data. 
```
Menu:
1. Load data
2. Calculate totals
3. Sort by total cost
4. Exit program
5. Enter scholarship cost
6. See benefits for each school
Select an option: 2
                        Name  Tuition   Room  Board  Books  Fees  Other_Expenses  Scholarship  Total
0    University of Maryland    20000  12000   5500   1050   750            1500            0  40800
1                Penn State    35000  10250   5000    975   670            5000            0  56895
2             Florida State    36550  11500   5050   1100   730            1300            0  56230
3  James Madison University    29500  15000   7000    500   450            2750            0  55200
4             Virginia Tech    33857  12200   6700    830   590            2000            0  56177
5    University of Delaware    36880  15470   6700   1200  3400            1750            0  65400
6                    Towson    18516  10080   8070    550  1500             900            0  39616
7                 Salisbury    11188  10900   8500   3750  3700            1200            0  39238
```

Select option 3 to sort the colleges by the total cost.
```
Menu:
1. Load data
2. Calculate totals
3. Sort by total cost
4. Exit program
5. Enter scholarship cost
6. See benefits for each school
Select an option: 3
                       Name  Tuition   Room  Board  Books  Fees  Other_Expenses  Scholarship  Total
7                 Salisbury    11188  10900   8500   3750  3700            1200            0  39238
6                    Towson    18516  10080   8070    550  1500             900            0  39616
0    University of Maryland    20000  12000   5500   1050   750            1500            0  40800
3  James Madison University    29500  15000   7000    500   450            2750            0  55200
4             Virginia Tech    33857  12200   6700    830   590            2000            0  56177
2             Florida State    36550  11500   5050   1100   730            1300            0  56230
1                Penn State    35000  10250   5000    975   670            5000            0  56895
5    University of Delaware    36880  15470   6700   1200  3400            1750            0  65400
```

Select option 5 and enter the name of a college and scholarship amount to calculate the net cost for that college.
```
Menu:
1. Load data
2. Calculate totals
3. Sort by total cost
4. Exit program
5. Enter scholarship cost
6. See benefits for each school
Select an option: 5
Enter the name of the school: University of Delaware
Enter the scholarship amount: 5000
                       Name  Tuition   Room  Board  Books  Fees  Other_Expenses  Scholarship  Total
0    University of Maryland    20000  12000   5500   1050   750            1500            0  40800
1                Penn State    35000  10250   5000    975   670            5000            0  56895
2             Florida State    36550  11500   5050   1100   730            1300            0  56230
3  James Madison University    29500  15000   7000    500   450            2750            0  55200
4             Virginia Tech    33857  12200   6700    830   590            2000            0  56177
5    University of Delaware    36880  15470   6700   1200  3400            1750         5000  60400
6                    Towson    18516  10080   8070    550  1500             900            0  39616
7                 Salisbury    11188  10900   8500   3750  3700            1200            0  39238
```

Select option 6 to enter the name of a college in the data and see the three benefits for that college.
```
Menu:
1. Load data
2. Calculate totals
3. Sort by total cost
4. Exit program
5. Enter scholarship cost
6. See benefits for each school
Select an option: 6
Enter the name of the school: University of Maryland
The University of Maryland offers strong academic programs and research opportunities a convenient location near Washington D.C. for internships and career opportunities and a diverse campus community and vibrant student life.
```

Select option 4 to exit the program. 
```
Menu:
1. Load data
2. Calculate totals
3. Sort by total cost
4. Exit program
5. Enter scholarship cost
6. See benefits for each school
Select an option: 4
 
```


## Testing
There are 23 test cases in my test plan. I ran four test runs to varify that everything was working. See the test folder for these documents.


## Authors and acknowledgment
I would like to acknowledgment the help and guidence from my internship mentor Mike Lanciano from Clarity Innovations.
