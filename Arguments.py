# Mania, Emyl Bien I. 
# BSDSA 2

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}.")

print("=== Part 1: Basic Function Arguments ===")
describe_pet("dog", "Doggo")
describe_pet("cat", "Meow Meow")
describe_pet("chicken", "Adolf Chickler")
describe_pet("pig", "Chris P Bacon")


print("\n=== Part 2: Positional vs Keyword Arguments ===")
describe_pet("pig", "Chris P Bacon") 
describe_pet(pet_name="Tony Tony Chopper", animal_type="deer")  


def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} and its name is {pet_name}.")

print("\n=== Part 3: Default Arguments ===")

describe_pet("Toink")              
describe_pet("Egg Sheeran", "chicken")   

def order_drink(drink, size="medium", iced=False):
    if iced:
        temp = "iced"
    else:
        temp = "hot"
    return f"Your order: {size} {temp} {drink}"

print("\n=== Part 4: Order Drink Function ===")
print(order_drink("tea"))
print(order_drink("chocolate", size="large", iced=False))
print(order_drink("milk tea", size="small", iced=True))


def compute(operation, num1, num2=1):

    if operation == "add":
        return num1 + num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "subtract":
        return num1 - num2

    else:
        return "Invalid operation"

print("\n=== Part 5: Mini Calculator ===")

print("compute('add', 5, 10) =", compute("add", 5, 10))
print("compute('multiply', num1=3, num2=4) =", compute("multiply", num1=3, num2=4))
print("compute('subtract', 20) =", compute("subtract", 20))  
print("compute('divide', 10, 2) =", compute("divide", 10, 2))