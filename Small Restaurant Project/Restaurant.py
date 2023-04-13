class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"The address of this franchise is {self.address}"

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Brunch menu
brunch_items = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

# Early bird menu
early_bird_items = {
    'salumeria plate': 8.00,
    'pizza with quattro formaggi': 12.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)

# Dinner menu
dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'ceaser salad': 16.00,
    'pizza with quattro formaggi': 20.00,
    'duck confit': 25.00,
    'spaghetti carbonara': 18.00,
    'coffee': 2.00,
    'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

# Kids menu
kids_items = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}
kids_menu = Menu('Kids', kids_items, 1000, 1400)

# Menu instances
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu('Arepas Place', arepas_items, 1000, 1630)

# Franchise instances
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
franchises = [flagship_store, new_installment]
arepas_place = Franchise("189 Fitzgerald Avenue", menus)

# Business instance
basta = Business("Basta Fazoolin' with my Heart", franchises)
TakeArepa = Business("Take a' Arepa", franchises)

print(arepas_place)
print(arepas_menu)
