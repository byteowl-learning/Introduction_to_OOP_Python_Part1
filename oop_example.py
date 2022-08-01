# We're going to create a couple of new cars and then update their mileage.

# *** OOP Example ***
print("\n\n*** OOP Example ***")


# 1. Define a generic vehicle object(class):


class Vehicle:
    role = "Private transportation vehicle"

    def __init__(self, make, model, color):
        """This is the class constructor"""
        self.make = make
        self.model = model
        self.color = color
        self._odometer = 0

    def add_trip(self, distance):
        self._odometer += distance

    def show(self):
        print(
            f"\t"
            f"make: {self.make}; "
            f"model: {self.model}; "
            f"color: {self.color}; "
            f"odometer: {self._odometer}"
        )


# 2. Create a couple of vehicles:

my_suv = Vehicle("Kia", "Niro", "Blue")
my_truck = Vehicle("Nissan", "Navara", "Orange")

# 3. Show the new vehicles:

print("New vehicles")
my_suv.show()
my_truck.show()

# 4. Add some trips to our vehicles:

my_suv.add_trip(1000)
my_suv.add_trip(200)
my_truck.add_trip(600)
my_suv.add_trip(500)

# 5. Show the used vehicles:

print("Used vehicles")
my_suv.show()
my_truck.show()
