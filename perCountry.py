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
