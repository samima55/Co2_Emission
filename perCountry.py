import matplotlib.pyplot as plt

myDict = {}

# Read data from the 'Emissions.csv' file and update the dictionary
with open('Emissions.csv', 'r') as file:
    lines = file.read().split('\n')
    header = lines[0].split(',')
    years = [int(year) for year in header[1:]]  # Extract the years

    for data in lines[1:]:
        parts = data.split(',')
        country = parts[0]
        emissions = [float(value) for value in parts[1:]]  # Convert the emissions to a list of floats
        myDict[country] = emissions

# Get the user's selected country
country_to_find = input("Choose the country: ")

# Check if the selected country exists in the data
if country_to_find in myDict:
    # Extract emissions data for the selected country
    country_emissions = myDict[country_to_find]

    # Create a plot using the extracted years as x-axis
    plt.plot(years, country_emissions, marker='o')
    plt.title(f'Emissions Data for {country_to_find}')
    plt.xlabel('Year')
    plt.ylabel('Emissions')
    plt.grid(True)

    # Show the plot
    plt.show()
else:
    print(f"Data for {country_to_find} not found.")


 ![DD655CF7-D366-47FD-8497-1462907F041E](https://github.com/samima55/Co2_Emission/assets/54752074/c0568687-e797-4535-831a-fd3e9bbc8978)


#for the jupyternotebook
import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
data = """CO2 per capita,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010
Afghanistan,0.052333365,0.048546686,0.037446034,0.034170007,0.027255262,0.014583427,0.022703695,0.02747237,0.036779904,0.047089636,0.068311633,0.131601903,0.213325007,0.262173714
Albania,0.499261188,0.569225594,0.971341941,0.983553048,1.047320154,1.214003077,1.382066271,1.332965957,1.353788699,1.224310364,1.27942017,1.297752738,1.215054777,1.336544035
Algeria,3.015670427,3.608257648,3.060244617,2.879527679,2.720453311,2.889312783,2.899236274,2.762219639,3.257009779,3.113135178,3.312874684,3.328944661,3.564360549,3.480976541
Andorra,7.061602855,7.533542944,8.022713657,8.112345412,7.897775769,7.700515138,7.414281032,7.499690095,7.390954533,6.839939571,6.622435189,6.527241242,6.178519784,6.092100302
Angola,0.576990561,0.556212458,0.677616537,0.685079070,0.676339193,0.850521392,0.587810214,1.177610138,1.161661852,1.308848969,1.435043652,1.474353388,1.500053579,1.593917842
Antigua and Barbuda,4.664325286,4.497461473,4.584238117,4.438377803,4.353775869,4.50892469,4.756310474,4.913204085,4.893782672,5.006748909,5.162816858,5.275415031,5.679445419,5.786645624
Argentina,3.770570751,3.80967752,3.981141308,3.819693795,3.555285353,3.273067083,3.502902225,4.072843801,4.160611395,4.464492014,4.582394268,4.785169983,4.48356446,4.466338068
Armenia,1.045668737,1.095600733,0.989444203,1.126427051,1.155322737,0.994206704,1.120167569,1.190051716,1.421960886,1.427325514,1.648352304,1.804106217,1.410814574,1.364888442
Aruba,21.74312968,19.21445326,19.02942041,24.73662638,24.21604611,23.83821726,23.27741935,22.80421892,22.50914228,22.13329958,22.62093228,21.68186039,21.52978401,21.59310807
Australia,18.00758857,18.51527047,17.1783559,17.19727773,16.7592018,17.39286776,17.46183995,17.34623728,17.7739756,17.89312837,17.85990598,18.01631327,18.03726854,16.75230078
"""

# Split the data into lines
lines = data.split('\n')

# Extract the header (years) and convert them to integers
header = lines[0].split(',')
years = [int(year) for year in header[1:]]

# Initialize a dictionary to store the emissions data
myDict = {}

# Iterate through the data and store it in the dictionary
for line in lines[1:]:
    parts = line.split(',')
    country = parts[0]
    emissions = [float(value) for value in parts[1:]]
    myDict[country] = emissions

# Set the selected country
country_to_find = "Albania"

# Check if the selected country exists in the data
if country_to_find in myDict:
    # Extract emissions data for the selected country
    country_emissions = myDict[country_to_find]

    # Create a plot using the extracted years as x-axis
    plt.plot(years, country_emissions, marker='o')
    plt.title(f'Emissions Data for {country_to_find}')
    plt.xlabel('Year')
    plt.ylabel('Emissions')
    plt.grid(True)

    # Show the plot
    plt.show()
else:
    print(f"Data for {country_to_find} not found.")
