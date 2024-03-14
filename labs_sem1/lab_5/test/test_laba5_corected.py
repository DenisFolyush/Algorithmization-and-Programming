from laba5_corected import Country, sort_by_gdp, calculator, guess_country_by_area, GovernmentType


def test_sort_by_gdp():
    country1 = Country("Ukraine", "Kyiv", "UA", 40000000, 603500, 150000000000, GovernmentType.DEMOCRACY)
    country2 = Country("USA", "Washington D.C.", "US", 331449281, 9833520, 22600000000000, GovernmentType.DEMOCRACY)
    country3 = Country("China", "Beijing", "CN", 1401812367, 9596960, 16600000000000, GovernmentType.DEMOCRACY)

    sorted_countries = sort_by_gdp([country1, country2, country3])

    assert sorted_countries == [country2, country3, country1]


def test_guess_country_by_area():
    assert guess_country_by_area(603500) == "It's Ukraine"
    assert guess_country_by_area(9596960) == "It's China"
    assert guess_country_by_area(9833520) == "It's USA"
    assert guess_country_by_area(123456) == "Sorry, I don't recognize the country for the given area"


def test_calculator():
    country1 = Country("Ukraine", "Kyiv", "UA", 40000000, 603500, 150000000000, GovernmentType.DEMOCRACY)
    current = calculator([country1])
    expected = 66.286003314001657
    assert current == expected
