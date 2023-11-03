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

print("\n All data from Emissions.csv has been read into a dictionary.\n")

year_to_find = input("select a year to find statistics 1997 -2010\n\n\n")

if year_to_find in myDict['CO2 per capita']:
    year_index = myDict['CO2 per capita'].index(year_to_find)
    print(f"Emissions in {year_to_find} for each country:    ")
    for country, emissions in myDict.items():
        if country != 'CO2 per capita':
            emission_value = emissions[year_index]
            print(f"{country}: {emission_value}")
else:
    print(f"{year_to_find} is not in the list of years.")
    
    
# check if year is present in the list of years, which is the 'CO2 per capita' key in the dictionary
if year_to_find in myDict['CO2 per capita']:
    #If the entered year is found in the list of years, this line determines the index of 
    #the entered year within the list and stores it in the year_index variable.
    year_index = myDict['CO2 per capita'].index(year_to_find)
    
    #This line creates a dictionary, emissions_for_year, which contains the CO2 emissions data for each country in 
    #the specified year. It uses a dictionary comprehension to iterate through the data dictionary, 
    #excluding the 'CO2 per capita' key, and converts the emissions values to floating-point numbers.
    emissions_for_year = {country: float(emissions[year_index]) for country, emissions in myDict.items() if country != 'CO2 per capita'}

    # Find the country with the lowest emissions
    lowest_country = min(emissions_for_year, key=emissions_for_year.get)

    # Find the country with the highest emissions
    highest_country = max(emissions_for_year, key=emissions_for_year.get)

    # Calculate the average emissions
    average_emissions = sum(emissions_for_year.values()) / len(emissions_for_year)

    print(f"In {year_to_find}:")
    print(f"Country with the lowest emissions: {lowest_country} ({emissions_for_year[lowest_country]})")
    print(f"Country with the highest emissions: {highest_country} ({emissions_for_year[highest_country]})")
    print(f"Average emissions: {average_emissions}")
else:
    print(f"{year_to_find} is not in the list of years.")






    
    

