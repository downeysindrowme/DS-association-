print("=== Shipping Cost Calculator ===")
weight = float(input("Enter total weight (lbs): "))
destination = input("Destination (domestic/international): ").lower()
membership = input("Membership (standard/premium): ").lower()

base_cost = 10
extra_cost = 5 if weight > 20 else 0
total_cost = base_cost + extra_cost

if membership == "premium":
    # Premium members: no international fee, 20% discount
    discount = 0.20
    final_cost = total_cost * (1 - discount)
    details = f"Base ${base_cost} + Overweight ${extra_cost}, Premium 20% discount applied, International fee waived."
else:
    # Standard members
    if destination == "international":
        total_cost *= 2  # Double cost for international
    final_cost = total_cost
    details = f"Base ${base_cost} + Overweight ${extra_cost}, Destination: {destination}."

print(f"Final Shipping Cost: ${final_cost:.2f}")
print(f"(Details: {details})")