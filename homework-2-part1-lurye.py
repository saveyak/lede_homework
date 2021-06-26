#Sharon Lurye
#6/11/2021
#Homework 2, Part 1

#Lists

numbers = [22, 90, 0, -10, 3, 22, 48]
print("here is a list of numbers:", numbers)
print("there are", len(numbers), "elements in the list")
print("the 4th element is", numbers[3])
print("2nd element + 4th element =", numbers[1] + numbers[3])
sorted_numbers = sorted(numbers)
print("The 2nd-largest value in the list is", sorted_numbers[-2])
print("The last element of the list is", numbers[-1])
print("The sum of all numbers divided by 2 is", sum(numbers)/2)

#How to find the median: https://www.geeksforgeeks.org/find-median-of-list-in-python/

import statistics

median = statistics.median(numbers)
mean = statistics.mean(numbers)

print("The median is", median,"and the mean is", mean)

if median == mean:
    print("The median and the mean are equal.")
elif median > mean:
    print("The median is higher than the mean.")
else:
    print("The mean is higher than the median.")

#Dictionaries

movie = {
    'title': 'Spirited Away',
    'year': 2001,
    'director': 'Hayao Miyazaki'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie['budget'] = 15000000
movie['revenue'] = 383400000

print(f"Difference between revenue and budget: ${movie['revenue'] - movie['budget']:,}") 

if movie['budget'] > movie['revenue']:
    print("That was a bad investment.")
elif movie['revenue'] > 5 * movie['budget']:
    print("That was a great investment.")
else:
    print("That was an OK investment.")

population = {
    'Manhattan': 1.6,
    'Brooklyn': 2.6,
    'Bronx': 1.4,
    'Queens': 2.3,
    'Staten Island': 0.47 
}

print("The population of Brooklyn is", population['Brooklyn'], "million people.")

pop_count = 0

for borough in population.values(): 
    #print(borough) 
    pop_count = pop_count + borough

print("The total population of NYC is", pop_count,"million people.")
print(round(population['Manhattan']/pop_count*100,1), "percent of New Yorkers live in Manhattan.")