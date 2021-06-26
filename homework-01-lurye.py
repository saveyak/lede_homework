#Sharon Lurye
# 6/7/2021
#Homework 1

birth_year = int(input("What year were you born?"))
age = 2021-birth_year

if age<0:
    birth_year = int(input("No really, what year were you born?"))

#Assume average of 80 human heartbeats per minute, 6 whale heartbeats per minute, 220 rabbit heartbeats per minute
human_beats = 80 * 60 * 24 * 365 * age
whale_beats = 6 * 60 * 24 * 365 * age
rabbit_beats = 220 * 60 * 24 * 365 * age

print(f'You are {age} years old. Your heart has beaten {human_beats:,} times.')
print(f'If you were a whale, your heart would have beaten {whale_beats:,} times.')

if rabbit_beats < 1000000:
    print(f'If you were a rabbit, your heart would have beaten {rabbit_beats:,} times.')
else:
    print(f'If you were a rabbit, your heart would have beaten {round(rabbit_beats / 1000000):,} million times.')

#Alternatively, instead of doing math within the print function, you can create a separate variable first:
#rabbit_beats = round(rabbit_beats/1000000)

#One Venus year = 225 days. One Neptune year = 60182 years. 
print(f"You are {round(age * 365/225, 2)} in Venus years")
print(f"You are {round(age * 365/60182, 2)} in Neptune years.")

if age == 28:
    print("You're one year younger than me!")
elif age < 28:
    print(f"You're {29-age} years younger than me!")
elif age > 29:
    print(f"You're {age-29} years older than me!")
else:
    print("We're the same age!")

if birth_year % 2 == 0:
    print("You were born in an even year.")
else: 
    print("You were born in an odd year.")

#How many times there has been a president from the Democratic Party in office since they were born? (1960 onward, and each president only counts once)
#Which US President was in office when they were born (1960 onward)?
#For simplicity, I will assume that these people were president in these years: Eisenhower 1960, JFK 1961-63, LBJ 1964-68, Nixon 1969-74, Ford 1975-76, Carter 1977-80, Reagan 1981-88, George H.W. Bush 1989-92, Clinton 1993-2000, George W. Bush 2001-2008, Obama 2009-2016, Trump 2017-2020, Biden 2021

if birth_year > 2016:
    print("There has been one Democratic president since you were born.")
elif birth_year > 2000:
    print("There have been two Democratic presidents since you were born.")
elif birth_year > 1980:
    print("There have been three Democratic presidents since you were born.")
elif birth_year > 1968:
    print("There have been four Democratic presidents since you were born.")
elif birth_year > 1963:
    print("There have been five Democratic presidents since you were born.")
elif birth_year > 1959:
    print("There have been six Democratic presidents since you were born.")
else:
    print("You're too old for me to figure out how many Democratics have been president since you were born.")

#StackOverflow discussions that helped me figure out how to do this: 
# https://stackoverflow.com/questions/48894060/how-to-print-specific-key-value-from-a-dictionary
#https://stackoverflow.com/questions/18265935/python-create-list-with-numbers-between-2-values

presidents = {
    'Eisenhower': [1960],
    'JFK': list(range(1961, 1963)),
    'LBJ': list(range(1964, 1968)),
    'Nixon': list(range(1969, 1974)),
    'Ford': [1975, 1976],
    'Carter': [1977, 1979, 1980],
    'Reagan': list(range(1981,1988)),
    'George H.W. Bush': list(range(1989, 1992)),
    'Clinton': list(range(1993,2000)),
    'George W. Bush': list(range(2001, 2008)),
    'Obama': list(range(2009, 2016)),
    'Trump': list(range(2017, 2020)),
    'Biden': [2001] 
} 

if birth_year < 1960:
    print ("You're too old for me to figure out who was president when you were born.")
else:
    for key, value in presidents.items():
        if (birth_year in value):
            print(key, "was president when you were born.")
