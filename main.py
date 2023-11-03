"""
Name: Python Data Analysis
Purpose: Read CSV File and store data in dictionary

Algorithm:

Step 1: Opening File in read mode and looping through data
Step 2: Printing the data just to ensure successful read

"""

print("A Simple Data Analysis Program")
print()

myDict = {}
"""
Step 1: Opening File using with in read mode and looping through data
"""

with open('Emissions.csv', 'r') as file:
    # Read in file object and spliting it with '\n'
    for data in file.read().split('\n'):
        # Updating the dictionary file | Splitting the string by COMMA(,) - Store first value as KEY
        # and Store other value as VALUE
        myDict.update({data.split(',')[0]: data.split(',')[1:]})

"""
Step 2: Printing the data just to ensure successful read
"""
for x, y in myDict.items():
    print(x, end=" - ")
    print(y)

print("\n All data from Emissions.csv has been read into a dictionary.")
