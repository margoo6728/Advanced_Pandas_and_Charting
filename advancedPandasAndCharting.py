# Marleyna Goodrich
# 4.7 Performance Assessment: Advanced Pandas and Charting

import matplotlib.pyplot as plt
import csv
import pandas as pd

# Assign the CSV file path
path="C:\\PythonFiles\\classroomRoster.csv"

# Reads the CSV file and create bar chart
x = []
mathGrades = []
scienceGrades = []

# Display Student ID
print("margoo6728")

# Open and read the CSV file
with open(path, 'r') as csvfile:

    # Display each row of data
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(row[0])
        mathGrades.append(int(row[1]))
        scienceGrades.append(int(row[2]))

# Create a MultiIndex for students and subjects
index = pd.MultiIndex.from_product(
    [x,["Math", "Science"]],
    names=["Student", "Subject"]
)

# Organize the grades for the DataFrame
grades = []

# Create list containing the grades
for i in range(len(x)):
    grades.append(mathGrades[i])
    grades.append(scienceGrades[i])

# Create DataFrame using MultiIndex
df = pd.DataFrame(grades, index=index, columns=["Grade"])

# Display DataFrame
print(df)

# Calculate the average grade for each subject
averageGrades = df.groupby(level="Subject").mean()

# Display average grade
print(averageGrades)

# Assigning Subject and Grades for the Vertical Bar Graph 
plt.bar(averageGrades.index, averageGrades["Grade"])
plt.xlabel("Average Grade by Subject")
plt.show()
