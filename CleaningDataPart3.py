#creating data for a list of dictionaries representing U.S. cities and their populations in millions
city_data = [
    {'City': 'New York', 'Population (millions)': 8.80},
    {'City': 'Los Angeles', 'Population (millions)': 3.90},
    {'City': 'Chicago', 'Population (millions)': 2.75},
    {'City': 'Houston', 'Population (millions)': 2.30},
    {'City': 'Phoenix', 'Population (millions)': 1.61},
    {'City': 'Philadelphia', 'Population (millions)': 1.60},
    {'City': 'San Antonio', 'Population (millions)': 1.43},
    {'City': 'San Diego', 'Population (millions)': 1.39}
]

#positional identifiers
print("U.S. City Populations:\n")

for i, row in enumerate(city_data): #index position, stored in i
    print(f"Index {i}: {row}") #row itself, stored in row

#check the range of identifiers using len()
last_index = len(city_data) - 1
print(f"\nIdentifiers range from 0 to {last_index}")

#meaningful identifiers
data_by_city = {
    row['City']: {'Population (millions)': row['Population (millions)']}
    for row in city_data
}

print("\nData with City as Identifier:")
for city, pop_data in data_by_city.items():
    print(f"'{city}': {pop_data}")

print("\nPopulation of Chicago:", data_by_city['Chicago'])

#Resetting Back to Numeric Identifiers
reset_city_data = [
    {'City': city, 'Population (millions)': pop_data['Population (millions)']}
    for city, pop_data in data_by_city.items()
]

print("\nData After Resetting to Numeric Identifiers:\n")
for i, row in enumerate(reset_city_data):
    print(f"Index {i}: {row}")



#NEW DATASET
#removing duplicates with set()
raw_colors = ['Red', 'Blue', 'Green', 'Red', 'Yellow', 'Blue'] #contains duplicates
unique_colors = list(set(raw_colors))
#set(raw_colors) creates a set of unique colors
#list() converts it back to a list
#sets do not preserve the orginal order

print("\nUnique Colors:", unique_colors)



#NEW DATASET
#Using set() for Fast Membership Testing
login_attempts = ['user123', 'user456', 'user789', 'user999', 'user000']
blacklisted_ids = set(['user000', 'user888', 'user123', 'user777'])

for user_id in login_attempts:
    if user_id in blacklisted_ids:
        print(f"Access denied for {user_id} (blacklisted)")
    else:
        print(f"Access granted for {user_id}")

#blacklisted_ids is stored as a set.
#The expression user_id in blacklisted_ids checks whether the current user ID is present in that set.
#If it is present, access is denied. Otherwise, access is granted.



#NEW DATASET
#Normalizing Values for Consistent Comparisons > NORMALIZATION
values = ['data', 'Data', 'DATA', 'data ', ' DATA']
normalized = [v.strip().lower() for v in values]
unique_normalized = list(set(normalized))

'''This is a list comprehension. It means:

take each value v in the list values,
apply .strip() to remove spaces from the beginning and end,
then apply .lower() to convert everything to lowercase,
and collect the cleaned results into a new list'''

print("All values normalized:\n", normalized)
print("\nUnique normalized values:\n", unique_normalized)