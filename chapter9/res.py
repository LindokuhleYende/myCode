class Resturant:
    def __init__(self, res_name, cusine_type):
        self.res_name = res_name
        self.cusine_type = cusine_type
    def describe_restaurant(self):
        print(f"{self.res_name} offers {self.cusine_type}")
    def open_restaurant(self):
        print(f"{self.res_name} is open for business from 9am")

# eat = Resturant("Pizza hut", "italian")
# eat.describe_restaurant()
# eat.open_restaurant()
# 
# dine = Resturant("Sushi world", "Japanese")
# dine.describe_restaurant()
# dine.open_restaurant()
# 
# lunch = Resturant("Taco town", "Mexican")
# lunch.describe_restaurant()
# lunch.open_restaurant()

#9.6 Ice Cream Stand:
class IceCreamStand(Resturant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
    def display_flavors(self):
        print("We offer the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
my_ice_cream_stand = IceCreamStand("Sweet Scoops", "Dessert", ["Vanilla", "Chocolate", "Strawberry", "Mint"])
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()