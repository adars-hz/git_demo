import datetime

# 1. Ask the user for their name
name = input("Enter your name: ")

# 2. Ask the user for their birth year and convert it to an integer
birth_year = int(input("Enter your birth year (e.g., 1995): "))

# 3. Get the current year automatically
current_year = datetime.date.today().year

# 4. Calculate the user's age
age = current_year - birth_year

# 5. Display a personalized greeting and the calculated age
print(f"\nHello, {name}!")
print(f"You are turning {age} years old this year.")
