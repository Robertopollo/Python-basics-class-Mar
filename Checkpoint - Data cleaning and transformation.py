import pandas as pd

# 1. Create the DataFrame
data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
    'Experience': [3, 7, 2, 5, 10, 4]
}
employee_df = pd.DataFrame(data)
print("Original DataFrame:")
print(employee_df)

# 2. Use iloc to select the first 3 rows
first_three_rows = employee_df.iloc[:3]
print("\nFirst 3 rows (iloc):")
print(first_three_rows)

# 3. Use loc to select rows where Department is "Marketing"
marketing_dept = employee_df.loc[employee_df['Department'] == 'Marketing']
print("\nMarketing Department (loc):")
print(marketing_dept)

# 4. Use iloc to select Age and Gender (cols 2 & 3) for the first 4 rows
# Age is index 2, Gender is index 3
subset_iloc = employee_df.iloc[:4, [2, 3]]
print("\nAge and Gender for first 4 rows (iloc):")
print(subset_iloc)

# 5. Use loc to select Salary and Experience for all rows where Gender is "Male"
male_salary_exp = employee_df.loc[
    employee_df['Gender'] == 'Male', ['Salary', 'Experience']
]
print("\nSalary and Experience for Males (loc):")
print(male_salary_exp)
