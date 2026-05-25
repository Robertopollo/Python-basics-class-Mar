import numpy as np
import requests
import io

# Direct download link for Google Drive
file_path = 'https://drive.google.com/uc?export=download&id=16RjrvW2NG8Rt0AbblsflA8iJdxSXfl5C'

# Fetch the content from the URL using requests
try:
    response = requests.get(file_path)
    response.raise_for_status()  
    # Use io.StringIO to treat the string content as a file-like object
    data_io = io.StringIO(response.text)
    # np.genfromtxt can now read from this file-like object
    loan_data = np.genfromtxt(data_io, delimiter=',', skip_header=1, usecols=(8))
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    loan_data = np.array([]) 

# Perform basic statistical analysis only if data was loaded and contains valid numbers
if loan_data.size > 0:
    # Filter out NaN values for statistical calculations
    valid_loan_data = loan_data[~np.isnan(loan_data)]
    if valid_loan_data.size > 0: # Check if there's any valid data after filtering
        loan_mean = np.mean(valid_loan_data)
        loan_median = np.median(valid_loan_data)
        loan_std = np.std(valid_loan_data)

        # Print the results
        print(f"Mean Loan Amount: {loan_mean:.2f}")
        print(f"Median Loan Amount: {loan_median:.2f}")
        print(f"Standard Deviation of Loan Amounts: {loan_std:.2f}")
    else:
        print("No valid numerical data found after filtering NaN values.")
else:
    print("Could not process loan data or no valid numerical data found.")
