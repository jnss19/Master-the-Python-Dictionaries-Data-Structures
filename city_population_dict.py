cities_population = {
    'Manila': 13929286,
    'Cebu': 16787941,
    'Davao': 24870895,
    'BGC': 12325232,
    'Makati': 9209944,
    'Marikina': 20076000,
    'Quezon City': 21000000,
    'Valenzuela': 20411000,
    'Malabon': 21540000,
    'Navotas': 26910000
}


print("Cities and their populations:", cities_population)


sixth_city = list(cities_population.keys())[5]  
print("Population of the 6th city ({}): {}".format(sixth_city, cities_population[sixth_city]))


third_city = list(cities_population.keys())[2]  
cities_population[third_city] = 30000000
print("Updated population of the 3rd city ({}): {}".format(third_city, cities_population[third_city]))

# Delete the 9th city from the dictionary
ninth_city = list(cities_population.keys())[8]
del cities_population[ninth_city]
print("Deleted the 9th city ({}).".format(ninth_city))

print("Last key-value pair in the dictionary:", list(cities_population.items())[-1])