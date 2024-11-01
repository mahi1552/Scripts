import pandas as pd
import re

# File paths
input_file = 'example.txt'
output_file = 'expenses_report.xlsx'

# Read the content of the file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Define lists to store data
time_list = []
date_list = []
spent_by_list = []
remarks_list = []
amount_list = []

# Regular expression pattern to match the required data
pattern = re.compile(r'\[(\d{1,2}:\d{2} [apm]{2}), (\d{1,2}/\d{1,2}/\d{4})\] ([A-Z]+): (.+) ([a-zA-Z0-9.]+)')

# Process each line with a count for "Match not found"
for index, line in enumerate(lines):
    match = pattern.search(line)
    if match:
        time_list.append(match.group(1))
        date_list.append(match.group(2))
        spent_by_list.append(match.group(3))
        remarks_list.append(match.group(4))
        amount_list.append(match.group(5))
    else:
        print(f"Match not found at line {index + 1}")

# Create a DataFrame
df = pd.DataFrame({
    'Time': time_list,
    'Date': date_list,
    'Spent By': spent_by_list,
    'Remarks': remarks_list,
    'Amount': amount_list
})

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Excel file saved as {output_file}")
