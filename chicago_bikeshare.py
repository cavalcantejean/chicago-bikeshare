
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt
from collections import Counter

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read, delimiter= ',')
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]
for i in range(20):
    print(data_list[0:][i])
# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

for i in range(20):
    print(data_list[i][6])
# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders
input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """Get the specified data of a list and export to another list.

    INPUT:
    data: list. The whole list.
    index: int. The specified column of a list that you want to export to another list.

    OUTPUT:
    column_list: list. The exported data with the column that you want to use later.
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for i in range(len(data)):
        column_list.append(data[i][index])
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
for i in range(len(data_list)):
    if data_list[i][6] == "Male":
        male += 1
    elif data_list[i][6] == "Female":
        female += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """Count the genders of a specified list.

    INPUT:
    data_list: list. The list that you want to count the number of occurrences of each gender.

    OUTPUT:
    [male, famale]: list. The number of occurrences of each gender (Male/Female).
    """
    male = 0
    female = 0

    for i in range(len(data_list)):
        if data_list[i][6] == "Male":
            male += 1
        elif data_list[i][6] == "Female":
            female += 1

    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """Decides with gender is the most popular of a list.

    INPUT:
    data_list: list. The list that contained the genders that you want to count.

    OUTPUT:
    answer: string. The answer with the most popular gender.
    """
    answer = ""

    male = 0
    female = 0

    qtd_generos = []

    for i in range(len(data_list)):
        if data_list[i][6] == "Male":
            male += 1
        elif data_list[i][6] == "Female":
            female += 1

    qtd_generos.append(male)
    qtd_generos.append(female)

    if qtd_generos[0] > qtd_generos[1]:
        answer = "Male"
    elif qtd_generos[0] < qtd_generos[1]:
        answer = "Female"
    else:
        answer = "Equal"

    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

def count_user_types(data_list):
    """Count the user types of a specified list.

    INPUT:
    data_list: list. The list that you want to count the number of occurrences of each type of user.

    OUTPUT:
    [subscriber, dependent, customer]: list. The number of occurrences of each user type
                                             (subscriber/dependent/customer).
    """
    subscriber = 0
    dependent = 0
    customer = 0

    for i in range(len(data_list)):
        if data_list[i] == "Subscriber":
            subscriber += 1
        elif data_list[i] == "Dependent":
            dependent += 1
        elif data_list[i] == "Customer":
            customer += 1

    return [subscriber, dependent, customer]

user_types_list = column_to_list(data_list, 5)
types_user = ["Subscriber", "Dependent", "Customer"]
quantity_user = count_user_types(user_types_list)
y_pos_user = list(range(len(types_user)))
plt.bar(y_pos_user,quantity_user)
plt.ylabel('Quantity')
plt.xlabel('Typer of User')
plt.xticks(y_pos_user,types_user)
plt.title('Quantity by Type of User')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because some values are empty"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
soma = 0.

for valor in trip_duration_list:
    if min_trip == 0.:
        min_trip = int(valor)
    elif int(valor) < min_trip:
        min_trip = int(valor)

for valor in trip_duration_list:
    if max_trip == 0.:
        max_trip = int(valor)
    elif int(valor) > max_trip:
        max_trip = int(valor)

for valor in trip_duration_list:
    soma += int(valor)

mean_trip = soma/len(trip_duration_list)

trip_duration_list = [int(i) for i in trip_duration_list]

ordered_list = sorted(trip_duration_list)
size_duration_list = len(trip_duration_list)
less_one_duration = size_duration_list - 1

median_trip = (ordered_list[int(size_duration_list/2)] + ordered_list[int(less_one_duration/2)]) / 2.0

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", str(min_trip), "Max: ", str(max_trip), "Mean: ", str(mean_trip), "Median: ", str(median_trip))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()


print("\nTASK 10: Printing start stations:")

user_types = column_to_list(data_list, 3)

user_types = set(user_types)

print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
    param1: The first parameter.
    param2: The second parameter.
Returns:
    List of X values
"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
answer = input("Will you face it?")


def count_items(column_list):
    """Count item of a specified column.

    INPUT:
    column_list: list. The list that you want to count the number of occurrences.

    OUTPUT:
    item_types: list. A description of the different types of contents
    count_items: list. The count of each type of different content.
    """

    count_items = Counter(column_list)
    count_items = count_items.values()
    count_items = list(count_items)

    item_types = Counter(column_list)
    item_types = item_types.keys()
    item_types = list(item_types)

    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
