"""
laba5_corrected.py

This module contains the definition of the 'GovernmentType' enumeration,
which represents different types of government.
"""
from enum import Enum


class GovernmentType(Enum):
    """Enumeration representing different types of government."""
    DEMOCRACY = 1
    REPUBLIC = 2
    AUTOCRACY = 3
    MONARCHY = 4
    ANARCHY = 5


class Land:
    """Class representing a piece of land."""

    def __init__(self, name, population, area, government_type):
        """
        Initializes a new Land object.

        Parameters:
        - name (str): The name of the land.
        - population (int): The population of the land.
        - area (int): The area of the land.
        - government_type (GovernmentType): The type of government in the land.
        """
        self.name = name
        self.population = population
        self.area = area
        self.government_type = government_type


class Country(Land):
    """Class representing a country, inheriting from the Land class."""

    def __init__(self, name, capital, code, population, area, gdp, government_type):
        """
        Initializes a new Country object.

        Parameters:
        - name (str): The name of the country.
        - capital (str): The capital city of the country.
        - code (str): The country code.
        - population (int): The population of the country.
        - area (int): The area of the country.
        - gdp (float): The Gross Domestic Product (GDP) of the country.
        - government_type (GovernmentType): The type of government in the country.
        """
        super().__init__(name, population, area, government_type)
        self.capital = capital
        self.code = code
        self.gdp = gdp


def sort_by_gdp(countries):
    """
    Sorts a list of countries based on their GDP in descending order.

    Parameters:
    - countries (list of Country): List of Country objects.

    Returns:
    - list of Country: List of Country objects sorted by GDP in descending order.
    """
    return sorted(countries, key=lambda x: x.gdp, reverse=True)


def calculator(countries):
    """
    Calculates and prints the population density for each country.

    Parameters:
    - countries (list of Country): List of Country objects.
    """
    for self_country in countries:
        density = self_country.population / self_country.area
        print(f"Population density of {self_country.name} is {density} people per square unit.")
    # Return the density of the last country in the list
    return density


def guess_country_by_area(area):
    """
    Guesses the country based on the provided area.

    Parameters:
    - area (int): The area for which the country is to be guessed.

    Prints:
    - str: A message indicating the guessed country or an apology if the country is not recognized.
    """
    if area == 603500:
        return "It's Ukraine"
    elif area == 9596960:
        return "It's China"
    elif area == 9833520:
        return "It's USA"
    else:
        return "Sorry, I don't recognize the country for the given area"


# Example usage:
# Uncomment the line below if you want to take user input for country_area
# country_area = int(input("Guess country by area: "))
country_area = 603500

guess_result = guess_country_by_area(country_area)
print(guess_result)

if __name__ == '__main__':
    # Creating Country objects with different government types
    country1 = Country("Ukraine", "Kyiv", "UA", 40000000,
                       603500, 150000000000, GovernmentType.DEMOCRACY)
    country2 = Country("USA", "Washington D.C.", "US", 331449281, 9833520,
                       22600000000000, GovernmentType.REPUBLIC)
    country3 = Country("China", "Beijing", "CN", 1401812367, 9596960,
                       16600000000000, GovernmentType.AUTOCRACY)

    # Using the calculator function
    calculator([country1, country2, country3])

    # Sorting and printing countries by GDP
    sorted_countries = sort_by_gdp([country1, country2, country3])
    print("Top countries by GDP:")
    for country in sorted_countries:
        print(f"{country.name}: {country.gdp} $")
