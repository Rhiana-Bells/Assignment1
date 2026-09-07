# ---------- Part (i): Students and Marks Dictionary ----------

# Dictionary of five students and their marks
students = {
    "Tendai": 100,
    "Takunda": 50,
    "Tatenda": 78,
    "Kelvin": 23,
    "Misheck": 13
}

# Display all students and their marks
print("Student Marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")

# Find the student with the highest mark
top_student = max(students, key=students.get)
print(f"\nStudent with the highest mark: {top_student} ({students[top_student]})")



class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        print()

# Instantiate two book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 15.99)
book2 = Book("1984", "George Orwell", 12.50)

# Display details of both books
print("Book Details:")
book1.display_details()
book2.display_details()