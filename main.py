'''
After run the Python file, main.py
copy paste the following arg on terminal 
python -m http.server 8000

Then, you can view the output by pasting the following link on the web browser
http://localhost:8000/index.html

'''


import pandas as pd
import json

# Load the Excel file
file_path = 'ULCC.xlsx'
df = pd.read_excel(file_path, sheet_name='Combined List')

# Create a dictionary to hold the data
data = {}

# Process the DataFrame
for index, row in df.iterrows():
    city = row['City']
    date = row['Date'].strftime('%Y-%m-%d')
    if date not in data:
        data[date] = {}
    if city not in data[date]:
        data[date][city] = {
            'morning': row['M_Status'],
            'afternoon': row['A_Status'],
            'evening': row['E_Status']
        }

# Save the data to a JSON file
with open('electricity_data.json', 'w') as f:
    json.dump(data, f, indent=4)
