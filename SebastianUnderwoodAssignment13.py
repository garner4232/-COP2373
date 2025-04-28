#This program creates a database with the population growth of the one of
#the ten cities listed. this program uses matplotlib to show the user a
#graph of population growth for 20 years.
import sqlite3
import matplotlib.pyplot as plt

#creates the database
def createDatabase():
#connects/creates5 the database
    conn = sqlite3.connect('population_SU.db')
    cursor = conn.cursor()

#creates the population table
    cursor.execute('''CREATE TABLE IF NOT EXISTS population (
                        city TEXT,
                        year INTEGER,
                        population INTEGER)''')

# list of 10 Florida cities and their original populations
    cityData = [('Miami', 449514),
        ('Sarasota', 55968),
        ('Orlando', 316081),
        ('Tampa', 407599),
        ('St. Augustine', 14831),
        ('Tallahassee', 201731),
        ('Jacksonville', 971319),
        ('Lake Worth', 42804),
        ('Gainesville', 145212),
        ('Naples', 19537)]


#inserts original population data
    for city, population in cityData:
        cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city, 2023, population))

    conn.commit()
    conn.close()

#simulates the population growth for 20 years at rate of 2%
def simulateGrowth():
    #connects to the database
    conn = sqlite3.connect('population_SU.db')
    cursor = conn.cursor()

#retrieves the original populations
    cursor.execute("SELECT city, population FROM population WHERE year = 2023")
    cityPopulations = cursor.fetchall()

#shows the population growth for 20 years
    for city, population in cityPopulations:
        currentPopulation = population
        for year in range(2024, 2044):
            currentPopulation = int(currentPopulation * 1.02)
            cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                           (city, year, currentPopulation))

    conn.commit()
    conn.close()

#this function creates the plot and graphs the population growth
def plotCityGrowth():
#connects to the database and the list of the cities
    conn = sqlite3.connect('population_SU.db')
    cursor = conn.cursor()
    cityList = ['Miami', 'Sarasota', 'Orlando', 'Tampa', 'St. Augustine',
                'Tallahassee', 'Jacksonville', 'Lake Worth', 'Gainesville', 'Naples']

#shows city options to user
    print("\nChoose a city to view its population growth:")
    for i in range(len(cityList)):
        print(f"{i + 1}. {cityList[i]}")

#gets the users choice
    choice = int(input("\nEnter the number of your choice: "))
    selectedCity = cityList[choice - 1]

#retreives population data for the selected city
    cursor.execute("SELECT year, population FROM population WHERE city = ?", (selectedCity,))
    data = cursor.fetchall()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

#plots the data
    plt.plot(years, populations)
    plt.title(f"Population Growth of {selectedCity}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()

    conn.close()

#calls the functions in order
def main():
    createDatabase()
    simulateGrowth()
    plotCityGrowth()



main()
