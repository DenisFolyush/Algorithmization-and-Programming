from enum import Enum


class GovernmentType(Enum):
    DEMOCRACY = 1
    REPUBLIC = 2
    AUTOCRACY = 3
    MONARCHY = 4
    ANARCHY = 5


class Land:
    def __init__(self, name, population, area, government_type):
        self.name = name
        self.population = population
        self.area = area
        self.government_type = government_type


class Country(Land):
    def __init__(self, name, capital, code, population, area, gdp, government_type):
        super().__init__(name, population, area, government_type)
        self.capital = capital
        self.code = code
        self.GDP = gdp


def sort_by_gdp(countries):
    return sorted(countries, key=lambda x: x.GDP, reverse=True)


# def sort_by_area(countries):
#     return sorted(countries, key=lambda x: x.area, reverse=True)


def calculator(countries):
    for country in countries:
        density = country.population / country.area
        print(f"Population density of {country.name} is {density} people per square unit.")


if __name__ == '__main__':
    country1 = Country("Ukraine", "Kiyv", "UA", 40000000, 603500, 150000000000, GovernmentType.DEMOCRACY)
    country2 = Country("USA", "Washington D.C.", "US", 331449281, 9833520, 22600000000000, GovernmentType.DEMOCRACY)
    country3 = Country("China", "Beijing", "CN", 1401812367, 9596960, 16600000000000, GovernmentType.DEMOCRACY)

    countries = [country1, country2, country3]
    calculator(countries)

    countries_GDP = [country1.GDP, country2.GDP, country3.GDP]
    countries_GDP.sort()
    print(countries_GDP)

    sorted_countries = sort_by_gdp(countries)
    print("Top countries by GDP:")
    for country in sorted_countries:
        print(f"{country.name}: {country.GDP} $")

    # area_sorted_countries = sort_by_area(countries)
    # print("Top countries by area:")
    # for country in area_sorted_countries:
    #     print(f"{country.name}: {country.area} ")
