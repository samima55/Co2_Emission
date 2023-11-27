import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path ="/content/drive/MyDrive/Co2 Emission/Emissions.csv";

df = pd.read_csv(path);
df.head()

myDict={}

with open(path, 'r') as file:
    # Read in file object and spliting it with '\n'
    for data in file.read().split('\n'):
        # Updating the dictionary file | Splitting the string by COMMA(,) - Store first value as KEY
        # and Store other value as VALUE
        myDict.update({data.split(',')[0]: data.split(',')[1:]})




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

    year_index = myDict['CO2 per capita'].index(year_to_find)


    emissions_for_year = {country: float(emissions[year_index]) for country, emissions in myDict.items() if country != 'CO2 per capita'}

    # Find the country with the lowest emissions
    lowest_country = min(emissions_for_year, key=emissions_for_year.get)

    # Find the country with the highest emissions
    highest_country = max(emissions_for_year, key=emissions_for_year.get)
    # Find the country with the avgerage emissions
    # Calculate the average emissions
    average_emissions = sum(emissions_for_year.values()) / len(emissions_for_year)

    # Find the country with the average emissions
    average_country = min(emissions_for_year, key=lambda x: abs(emissions_for_year[x] - average_emissions))

print(f"Year: {year_to_find}")
print(f"Country with Lowest Emissions: {lowest_country} - {emissions_for_year[lowest_country]} CO2 per capita")
print(f"Country with Highest Emissions: {highest_country} - {emissions_for_year[highest_country]} CO2 per capita")
print(f"Country with Average Emissions: {average_country} - {emissions_for_year[average_country]} CO2 per capita (Average: {average_emissions})")


# User selects a country
selected_country =input("select a country you want  plot for \n\n\n")

# Capitalize the first character of the selected country
selected_country= selected_country.capitalize()

# Check if the selected country exists in the data
if selected_country in myDict:
    # Extract emissions data for the selected country
    country_emissions = myDict[selected_country]
    years = list(myDict['CO2 per capita'])
    plt.figure(figsize=(10, 4))
    # Create a plot using the extracted years as x-axis
    plt.plot(years, country_emissions, marker='o')
    plt.title(f'Emissions Data for {selected_country}')
    plt.xlabel('Year')
    plt.ylabel('Emissions')
    plt.grid(True)

    # Show the plot
    plt.show()
else:
    print(f"Data for {selected_country} not found.")


# User enters countries separated by commas
selected_countries_input = input("Enter countries separated by commas: ")

# Split the input into a list of countries
selected_countries = [country.strip().capitalize() for country in selected_countries_input.split(',')]

# Initialize a flag to check if at least one country is found in the data
at_least_one_country_found = False

# Initialize a list to store the country_emissions data for each country
all_countries_emissions = []

# Iterate over the selected countries
for selected_country in selected_countries:
    # Check if the selected country exists in the data
    if selected_country in myDict:
        # Capitalize the first character of the selected country
        selected_country_capitalized = selected_country.capitalize()

        # Extract emissions data for the selected country
        country_emissions = myDict[selected_country]
        all_countries_emissions.append((selected_country_capitalized, country_emissions))

        # Set the flag to indicate at least one country is found
        at_least_one_country_found = True

    else:
        print(f"Data for {selected_country} not found.")

# Check if at least one country is found
if at_least_one_country_found:
    # Create a bar plot with bars for each country
    plt.figure(figsize=(12, 6))

    # Set the width of the bars
    bar_width = 0.35
    index = np.arange(len(years))

    for i, (country, emissions) in enumerate(all_countries_emissions):
        plt.bar(index + i * bar_width, emissions, bar_width, label=country)

    plt.title('Emissions Data for Selected Countries')
    plt.xlabel('Year')
    plt.ylabel('Emissions')
    plt.xticks(index + (len(all_countries_emissions) - 1) * bar_width / 2, years)
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("No valid data found for any of the entered countries.")

# User enters countries separated by commas
selected_countries_input = input("Enter countries separated by commas: ")

# Split the input into a list of countries
selected_countries = [country.strip().capitalize() for country in selected_countries_input.split(',')]

# Initialize a flag to check if at least one country is found in the data
at_least_one_country_found = False

# Initialize a list to store the country_emissions data for each country
all_countries_emissions = []

# Iterate over the selected countries
for selected_country in selected_countries:
    # Check if the selected country exists in the data
    if selected_country in myDict:
        # Capitalize the first character of the selected country
        selected_country_capitalized = selected_country.capitalize()

        # Extract emissions data for the selected country
        country_emissions = myDict[selected_country]
        all_countries_emissions.append((selected_country_capitalized, country_emissions))

        # Set the flag to indicate at least one country is found
        at_least_one_country_found = True

    else:
        print(f"Data for {selected_country} not found.")

# Check if at least one country is found
if at_least_one_country_found:
    # Create a line plot with separate lines for each country
    plt.figure(figsize=(12, 6))

    for country, emissions in all_countries_emissions:
        plt.plot(years, emissions, marker='o')

    plt.title('Emissions Data for Selected Countries')
    plt.xlabel('Year')
    plt.ylabel('Emissions')
    plt.show()
else:
    print("No valid data found for any of the entered countries.")

import matplotlib.pyplot as plt
import numpy as np

# User enters two years separated by commas
selected_years_input = input("Enter two years separated by commas: ")

# Split the input into a list of two years
selected_years = [year.strip() for year in selected_years_input.split(',')]

# Validate that two years are provided
if len(selected_years) != 2:
    print("Please enter exactly two years.")
    exit()

# Check if the selected years exist in the dataset
if any(year not in years for year in selected_years):
    print("One or both of the selected years are not present in the dataset.")
    exit()

# Initialize a list to store the emissions data for each country
all_countries_emissions = []

# Iterate over all countries
for country, emissions in myDict.items():
    # Skip the 'CO2 per capita' key
    if country != 'CO2 per capita':
        # Extract emissions data for the selected years
        selected_emissions = [emissions[years.index(selected_years[0])],
                              emissions[years.index(selected_years[1])]]

        all_countries_emissions.append(selected_emissions)

# Create a line plot with lines for each country
plt.figure(figsize=(12, 6))

for emissions in all_countries_emissions:
    plt.plot(selected_years, emissions, marker='o')

plt.title(f'CO2 Emissions Comparison for All Countries in {selected_years[0]} and {selected_years[1]}')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions per Capita')
plt.grid(True)
plt.show()




# User enters two years separated by commas
selected_years_input = input("Enter two years separated by commas: ")

# Split the input into a list of two years
selected_years = [year.strip() for year in selected_years_input.split(',')]

# Validate that two years are provided
if len(selected_years) != 2:
    print("Please enter exactly two years.")
    exit()

# Check if the selected years exist in the dataset
if any(year not in years for year in selected_years):
    print("One or both of the selected years are not present in the dataset.")
    exit()

# Initialize lists to store the emissions data for each country
all_countries_emissions = []

# Iterate over all countries
for country, emissions in myDict.items():
    # Skip the 'CO2 per capita' key
    if country != 'CO2 per capita':
        # Convert emissions data to numeric values
        numeric_emissions = [float(emission) for emission in emissions]

        # Extract emissions data for the selected years
        selected_emissions = [numeric_emissions[years.index(selected_years[0])],
                              numeric_emissions[years.index(selected_years[1])]]

        all_countries_emissions.append(selected_emissions)

# Convert to NumPy array for easier manipulation
all_emissions_array = np.array(all_countries_emissions)

# Scatter plot for average, max, and min
plt.figure(figsize=(12, 6))

average_emissions = np.mean(all_emissions_array, axis=0)
max_emissions = np.max(all_emissions_array, axis=0)
min_emissions = np.min(all_emissions_array, axis=0)



# Scatter plot for average
plt.scatter(selected_years, average_emissions, marker='o', label='Average')

# Scatter plot for max
plt.scatter(selected_years, max_emissions, marker='o', label='Max')

# Scatter plot for min
plt.scatter(selected_years, min_emissions, marker='o', label='Min')

plt.title(f'CO2 Emissions Statistics for All Countries in {selected_years[0]} and {selected_years[1]}')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions per Capita')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.boxplot(all_emissions_array, labels=selected_years)
plt.title('Box Plot of CO2 Emissions for Selected Years')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions per Capita')
plt.show()


plt.figure(figsize=(12, 6))
plt.hist(all_emissions_array, bins=20, label=[selected_years[0],selected_years[1]], alpha=0.7)
plt.title('Histogram of CO2 Emissions for Selected Years')
plt.xlabel('CO2 Emissions per Capita')
plt.ylabel('Frequency')
plt.legend()
plt.show()



percentage_change = (all_emissions_array[:, 1:] / all_emissions_array[:, :-1] - 1) * 100
print(f'Percentage change in CO2 emissions for each country between consecutive years:\n{percentage_change}')


import numpy as np
import matplotlib.pyplot as plt

# Assuming percentage_change is the variable containing your data
# Make sure percentage_change is a 1D array for this example
percentage_change = np.array(percentage_change)

# Assuming you have the years as x-axis values
# You may need to replace this with your actual years data
years = np.arange(1, len(percentage_change) + 1)

# Perform linear regression using numpy's polyfit
slope, intercept = np.polyfit(years, percentage_change, 1)

# Create a line using the slope and intercept
line = slope * years + intercept

# Plot the data and the linear fit
plt.plot(years, percentage_change, 'o', label='Percentage Change')
plt.plot(years, line, label=f'Linear Fit: {slope:.2f}x + {intercept:.2f}')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Percentage Change in CO2 Emissions')
plt.title('Linear Fit of Percentage Change in CO2 Emissions Over Years')
plt.legend()

# Show the plot
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Assuming percentage_change is the variable containing your data
# Make sure percentage_change is a 1D array for this example
percentage_change = np.array(percentage_change)

# Assuming you have the years as x-axis values
# You may need to replace this with your actual years data
years = np.arange(1, len(percentage_change[0]) + 1)

# Perform quadratic regression using polyfit
coefficients = np.polyfit(years, percentage_change[1], 2)

# Generate a quadratic fit using the coefficients
quadratic_fit = np.polyval(coefficients, years)

# Plot the data and the quadratic fit
plt.plot(years, percentage_change[0], 'o', label='Percentage Change')
plt.plot(years, quadratic_fit, label=f'Quadratic Fit: {coefficients[0]:.2f}x^2 + {coefficients[1]:.2f}x + {coefficients[2]:.2f}')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Percentage Change in CO2 Emissions')
plt.title('Quadratic Fit of Percentage Change in CO2 Emissions Over Years')
plt.legend()

# Show the plot
plt.show()

