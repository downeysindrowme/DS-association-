
print("=== Task 4: Movie Ticket Price ===")
age = int(input("Enter age: "))
is_student = input("Student? (True/False): ").capitalize() == "True"
price = 12

if age <= 12:
    price -= 3
elif age >= 65:
    price -= 4
elif is_student:
    price -= 2

print("Ticket price: $", price)
print()