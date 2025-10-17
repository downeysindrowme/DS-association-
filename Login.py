
print("=== Task 5: Login System ===")
user = "alice"
pwd = "wonderland"
code = "123456"
is_2fa = True

u = input("Username: ")
p = input("Password: ")
y = input("2FA enabled? (y/n): ")

if y == "y":
    c = input("Enter 2FA code: ")
else:
    c = ""

if u == user and p == pwd and (not is_2fa or c == code):
    print("Login successful!")
else:
    print("Login failed!")
print()