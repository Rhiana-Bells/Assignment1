while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for your age.")

print(f"Your age is: {age}")