print("=== Task 3: Unit Conversion ===")
inches = int(input("Enter inches: "))
feet = inches // 12
remaining = inches % 12
print(f"{inches} inches = {feet} feet and {remaining} inches")
print()