import pandas as pd

class Calculator:
    """
        This class provides the function to support calculating total expenses of colleges.
    """
    def __init__(self):
        self.data = None
        self.benefits = None

  
    def view_benefits(self):
        ##load benefits.csv into self.benefits
      if self.benefits is None:
        # Load the CSV file with long strings
        self.benefits = pd.read_csv('benefits.csv', dtype={'long_strings': str})
        # Set the display options to show the entire column
        pd.set_option('display.max_colwidth', None)
        ##prompt user to enter name of college
      school_name = input("Enter the name of the school: ")
      if school_name not in self.benefits["Name"].values:
        print("Error: School not found.")
      else:
        benefit = self.benefits.loc[self.benefits["Name"] == school_name, "Benefit"].values[0]
        ##print three benefits for that college
        print(benefit)

      

    def load_data(self):
        """
        Prompts the user to enter the name of a CSV file, reads it into a pandas DataFrame, and stores the DataFrame as
        an instance variable.

        Returns:
            True if the data was loaded successfully, False otherwise.
        """
        filename = input("Enter the name of the CSV file: ")
        try:
            self.data = pd.read_csv(filename)  
            self.validate_data()
            print("Data loaded successfully.")
            self.data["Scholarship"] = 0
            print(self.data)
            return True
        except FileNotFoundError:
            print(f"Error: Could not open file {filename}.")
            return False
        except ValueError as v:
            self.data=None
            print(v)
        except TypeError as t:
            self.data=None
            print(t)
       

    def validate_data(self):
        ##validate that data file has the correct number of columns
        if len(self.data.columns) != 7:
            raise ValueError("Data file should contain 7 columns")
        ##validate that column 1-6 contain numeric data
        if not all(self.data.iloc[:, 1:].applymap(lambda x: isinstance(x, (int, float))).all(axis=0)):
            raise TypeError("Columns 2 to 7 should contain numeric data")
  

  
    def calculate_totals(self):
        """
    Calculates the total cost for each school by summing the values in columns 1 to the second to last column, then subtracting any value in the last column (scholarship), and adding a new column called Total to the data frame.
        """
        if self.data is None:
          print("Error: No data loaded yet.")
        else:
        # Sum values in columns 1 to second to last column
          
          total_cost_cols = ["Tuition", "Room", "Board","Other_Expenses", "Books", "Fees"]
          total_cost = self.data[total_cost_cols].sum(axis=1)
        
        # Subtract scholarship (if exists) from total cost
          if "Scholarship" in self.data.columns:
            total_cost -= self.data["Scholarship"]
        
          # Add new Total column to data frame
          self.data["Total"] = total_cost
        
          # Print updated data frame
          print(self.data)


    def sort_by_total_cost(self):
        """
    Sorts the loaded data by the "Total" column in ascending order (least to greatest) if the column exists in the data
    frame. Otherwise, prints an error message.
        """
        if self.data is None:
          print("Error: No data loaded yet. First, try selecting option 1.")
        elif "Total" not in self.data.columns:
          print("Cannot sort by total cost yet. Calculate the total costs before sorting.")
        else:
          sorted_data = self.data.sort_values(by="Total")
          print(sorted_data)

    def subtract_scholarship(self):
      """
    Prompts the user to enter the name of a school and a scholarship amount,
    and then adds the scholarship amount to the existing scholarship (if any) 
    for the selected school in the 'Scholarship' column. 
    Prints the updated data frame to the screen.
      """
      if self.data is None:
        print("Error: No data loaded yet.")
      else:
        school_name = input("Enter the name of the school: ")
        if school_name not in self.data["Name"].values:
            print("Error: School not found.")
        else:
            scholarship_input = input("Enter the scholarship amount: ")
            if scholarship_input == "":
                scholarship_amount = 0
            else:
                try:
                  scholarship_amount = float(scholarship_input)
                  current_scholarship = self.data.loc[self.data["Name"] == school_name, "Scholarship"]
                  self.data.loc[self.data["Name"] == school_name, "Scholarship"] = current_scholarship + scholarship_amount
                  self.calculate_totals()
                except ValueError:
                  print("Invalid scholarship amount. Please enter a valid number.")
                

   