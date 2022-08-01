# We're going to create a couple of new cars and then update their mileage.

# *** FP Example ***
print("\n\n*** FP Example ***")


# 1. Define a function to build our vehicles:
def make_vehicle(make, model, color, odometer=0):
    return {
        "make": make,
        "model": model,
        "color": color,
        "odometer": odometer,
    }

# 3. Define a function to print information on a vehicle
def show_vehicle(vehicle):
    print("\n\t", end="")
    for k, v in vehicle.items():
        print(f"{k}: {v}", end="; ")


# 3. Make our vehicles
my_suv = make_vehicle("Kia", "Niro", "Blue")
my_truck = make_vehicle("Nissan", "Navara", "Orange")

# 4. Print our new vehicles:
print("New vehicles", end="")
show_vehicle(my_suv)
show_vehicle(my_truck)

# 5. Add some trips to our vehicles:
my_suv["odometer"] += 1000
my_truck["odometer"] += 600

# 6. Print our used vehicles:
print("\nUsed vehicles", end="")
show_vehicle(my_suv)
show_vehicle(my_truck)
