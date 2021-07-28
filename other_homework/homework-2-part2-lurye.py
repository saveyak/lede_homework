#Sharon Lurye
#6/12/21
#Homework 2, Part 2

#Lists

countries = ["Costa Rica", "Azerbaijan", "Uzbekistan", "Japan", "United States"]

print("Here is a list of countries:")
for country in countries:
    print(country)

countries.sort()

print("Alphabetically, the first country is", countries[0]) 
print("Alphabetically, the second-to-last country is", countries[-2]) 

countries.remove('Japan')

print("Here is a new list of countries:")
for country in countries:
    print(country.upper())

#Dictionaries

tree = {
    'name': 'Methuselah',
    'species': 'Great Basin bristlecone pine',
    'age': 4852,
    'location_name': 'Inyo National Forest, California',
    'latitude': 37.3794,
    'longitude': -118.1618 
}

print(f"{tree['name']} is a {tree['age']}-year-old tree that is in {tree['location_name']}.")

if tree['latitude'] < 40.7128:
    print(f"The tree {tree['name']} in {tree['location_name']} is south of NYC")
else:
    print(f"The tree {tree['name']} in {tree['location_name']} is north of NYC")

user_age = int(input("How old are you?"))

if user_age > tree['age']:
    print("You are", user_age-tree['age'], "years older than", tree['name'])
else:
    print(tree['name'], "was", tree['age']-user_age, "years old when you were born.")

# Lists of dictionaries

cities = [
    {'name':'Moscow', 'latitude':55.7558, 'longitude':37.6173},
    {'name':'Tehran', 'latitude':35.6892, 'longitude':51.3890},
    {'name':'Falkland Islands', 'latitude':-51.7963, 'longitude':-59.5236},
    {'name':'Seoul', 'latitude':37.5665, 'longitude':126.9780},
    {'name':'Santiago', 'latitude':-33.4489, 'longitude':-70.6693},
]

for city in cities:
    if city['name'] == 'Falkland Islands':
        print("The", city['name'], "are below the equator. The Falkland Islands are a biogeographical part of the mild Antarctic zone.")
    elif city['latitude'] > 0:
        print(city['name'], "is above the equator.")
    else:
        print(city['name'], "is below the equator.")


for city in cities:
    if city['latitude'] > tree['latitude']:
        print(city['name'], ": north of the", tree['name'], "tree.")
    else:
        print(city['name'], ": south of the", tree['name'], "tree.")