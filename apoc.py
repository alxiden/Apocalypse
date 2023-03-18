print("              ______   ______   ______                               ______    _____   _______ ")
print("     /\      |      | |      | |            /\      |       |     | |      |  |       |       |")
print("    /  \     |      | |      | |           /  \     |       |     | |      |  |       |       |")
print("   /    \    |______| |      | |          /    \    |       |_____| |______|  |_____  |_______|")
print("  /______\   |        |      | |         /______\   |             | |               | |        ")
print(" /        \  |        |      | |        /        \  |             | |               | |        ")
print("/          \ |        |______| |______ /          \ |______  _____| |         ______| |_______ ")



rooms = {"empty" : {"name" : "empty room",
                    "north" : "supermarket",
                    "east" : "fuel station",
                    "text" : "The house is empty, already picked clean by looters", "1": "north", "2": "east", "item": ""},
        "supermarket":{"name": "supermarket",
                       "south": "empty",
                       "west" : "police station",
                       "text": "most of the shelves are already picked clean but you still gain some food", "item":"food", "1" : "south", "2" : "west"},
        "fuel station": {"name": "fuel stataion",
                        "south": "car",
                        "west" : "empty",
                        "text": "The pumps are dry but there is a crowbar hidden in the shop", "item":"crowbar", "1" : "south", "2" : "west"},
        "police station": {"name" : "police station",
                           "east" : "supermarket",
                           "text" : "the station is locked tight maybe if you had a crowbar you could get in",
                           "text2" : "Using the crowbar you get in and find a gun",
                           "item":"gun", "1" : "east", "2" : " "},
        "car": {"name":"car",
                "north" : "fuel station",
                "west": "old shop",
                "text" :"An abandoned car, if only you had some fuel",
                "text2": "You get in the car and drive off to the safe zone. Someone trys to mug you, without a gun the mugger takes your car and you die",
                "text3" : "You get in the car and drive off to the safe zone. Someone trys to mug you, but using your gun you kill them first and you live another day",
                "1": "west", "2" : "north"},
        "old shop" : {"name" : "old shop", "east": "car",
                                            "text" :"you search the old shop and find a fuel can in the backroom",
                                            "item" : "fuel", "1" : "east","2" : " "}}

          
direction = ["north","south","east","west"]
current_room = rooms["empty"]

fuel = 0
gun = 0
crowbar = 0
food = 0
items = []

def item_check ():
    global fuel
    global gun
    global crowbar
    global food
    global items
    if "item" in current_room:
        if current_room["item"] == "fuel":
            if fuel != "1":
                items.append("Fuel")
            else:
                pass
            fuel = "1"
            return fuel
        elif current_room["item"] == "gun":
            if gun != "1":
                items.append("Gun and ammo")
            else:
                pass
            gun ="1"
            return gun
        elif current_room["item"] == "crowbar":
            if crowbar != "1":
                items.append("Crowbar")
            else:
                pass
            crowbar = "1"
            return crowbar
        elif current_room["item"] == "food":
            if food != "1":
                items.append("Food")
            else:
                pass
            food = "1"
            return food
        else:
            pass

def check():
    if current_room["name"] in "police station" and crowbar == "1":
        print(current_room["text2"])
    elif current_room["name"] in "car" and fuel == "1" and gun == "1":
        print(current_room["text3"])
    elif current_room["name"] in "car" and fuel == "1":
        print(current_room["text2"])
    else:
        print(current_room["text"])
    
while True:
    print()
    print("you are currently in the {} ".format(current_room["name"]))
    print("you can go {}".format(current_room["1"]))
    if current_room["2"] == " ":
        pass
    else:
        print("or {}".format(current_room["2"]))
    check()
    print("Inventory:")
    print(items)
    
    command = input("Where would you like to go? ").strip().lower()

    if command in direction:
        if command in current_room:
            current_room = rooms[current_room[command]]
            item_check()               
                 
        else:
            print("you cant go that way")
    elif command in "q":
            break

    else:
        print("I dont understand")
