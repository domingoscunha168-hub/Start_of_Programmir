name = input("What is your name? ").strip()
print(f"Welcome, {name}!")

while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Invalid age. Please enter a whole number.")

if age >= 18:
    print("You are of legal age. You may continue with the registration.")
else:
    print("You are underage. Registration cannot continue.")
    raise SystemExit

while True:
    gender = input("What is your gender? (Female/Male) ").strip().title()
    if gender in {"Female", "Male"}:
        break
    print("Invalid value. Please enter Female or Male.")

while True:
    try:
        height = float(input("What is your height in meters? "))
        if height >= 1.78:
            break
        print("The height is below the minimum allowed for registration.")
    except ValueError:
        print("Invalid height. Please enter a numeric value.")

print(
    f"Thank you, {name}. Your registration was completed successfully. "
    f"Your age is {age} years, your gender is {gender}, and your height is {height:.2f} meters."
)