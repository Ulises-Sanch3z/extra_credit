from random import choice
from cowsay import cow

guests = ["Alice", "Bob", "Charlie", "David", "Eva",
    "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Kelly", "Leo", "Mia", "Nathan", "Olivia",
    "Paul", "Quinn", "Ryan", "Sara", "Tom",
    "Ursula", "Vincent", "Wendy", "Xander",
    "Yvonne", "Zack"]

menu = [
    "macaroni and cheese",
    "pecan pie",
    "winter squash",
    "sweet potatoes",
    "coffee",
    "biscuits",
    "salad",
    "dressing",
    "gravy",
    "corn",
    "cranberry sauce",
    "quiche",
    "fresh fruit plate",
    "pumpkin pie",
    "apple cider",
    "rolls",
    "tea",
    "green beans",
    "turkey",
    "corn bread",
    "butter",
    "green bean casserole",
    "stuffing",
    "apple pie",
    "sweet potato pie",
    "mashed potatoes",
    "cru de te",
    "mac and cheese"
    ]

class ThanksgivingGuestList:

    def __init__(self, guest_list, menu_items):
        self.guest_list = guest_list
        self.menu_items = menu_items
        self.rando_list = {}

    def shuffle(self):
        for guest in self.guest_list:
            self.rando_list[guest] = choice(self.menu_items)
            
    def display(self):
        print("Thanksgiving Guest List:")
        print()
        for guest in self.guest_list:
            print(f"{guest}: {self.rando_list[guest]}")

    def guest_info(self, guest):
        if guest in self.guest_list:
            cow(f"{guest}: {self.rando_list[guest]}")
        else:
            cow(f"{guest} not found")

dinner = ThanksgivingGuestList(guests, menu)

dinner.shuffle()
print()
dinner.display()
print()
dinner.guest_info("Eva")

cow("Hellow")