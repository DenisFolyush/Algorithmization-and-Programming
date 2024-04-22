def beers(workers, beer_types, like_bear):
    types_of_beer = 0
    beers_set = set()

    for i in range(workers):
        possible_set = set()

        for j in range(beer_types):
            if like_bear[i * beer_types + j] == "Y":
                possible_set.add(j)  # додаємо пиво до possible_set , якщо працівник любить його

        # якшо працівник не любить всі види пива, які вже є
        if possible_set.isdisjoint(beers_set):
            beers_set.update(possible_set)  # Додаєм пиво
            types_of_beer += 1  # пива + 1
    # обмежння
    if workers <= 0 or workers >= 50 or beer_types <= 0 or beer_types >= 50:
        return None
    if 'Y' not in like_bear:
        return None

    if types_of_beer == 0:

        return None
    else:
        return types_of_beer
