# Save directory tree as a CSV and remove unnecessary rows/columns

# Steps:
# 1. Download this script anywhere.
# 2. From the terminal, navigate to the folder/directory whose tree you want as a CSV.
# 3. Run the command "python /path/to/dirTree2Csv.py" (replacing /path/to with the correct path).

import os
import csv

data = []
for root, dirs, files in os.walk('.'):
    for f in files:
        l = root.split('/') + [f]
        data.append(l)

with open('dirTree.csv', 'wb') as f:
    writer = csv.writer(f)
    for d in data:
        d[0] = os.getcwd().split('/')[len(os.getcwd().split('/'))-1]
        if d[len(d)-1] != '.DS_Store':
            writer.writerow(d)
