# List of five favourite fruits
fruits = ["strawberry", "kiwi", "apple", "blueberry", "blackberry"]

# Write the fruits to fruits.txt, each on a separate line
with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

# Read the contents of fruits.txt and display each fruit
with open("fruits.txt", "r") as file:
    print("Favourite fruits:")
    for line in file:
        print(line.strip())