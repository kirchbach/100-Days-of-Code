MENU = {
    "Espresso": {
        "Zutaten": {
            "Wasser": 50,
            "Milch":0,
            "Kaffee": 18,
        },
        "Preis": 1.50,
    },
    "Latte": {
        "Zutaten": {
            "Wasser": 200,
            "Milch": 150,
            "Kaffee": 24,
        },
        "Preis": 2.50,
    },
    "Cappuccino": {
        "Zutaten": {
            "Wasser": 250,
            "Milch": 100,
            "Kaffee": 24,
        },
        "Preis": 3.00,
    }
}


resources = {
    "Wasser": 300,
    "Milch": 200,
    "Kaffee": 100,
}
profit=0

# TODO: 1. Report


# TODO: 2. Ask which drink they want
end_process = False
def check_resources(drink, resources):
    water = MENU[drink]["Zutaten"]["Wasser"]
    milk = MENU[drink]["Zutaten"]["Milch"]
    coffee = MENU[drink]["Zutaten"]["Kaffee"]
    remaining_water = resources["Wasser"]-water
    remaining_milk = resources["Milch"]-milk
    remaining_coffee = resources["Kaffee"]-coffee
    remaining_resources = {
        "Wasser": remaining_water,
        "Milch": remaining_milk,
        "Kaffee": remaining_coffee,
    }
    return remaining_resources


while not end_process:
    drink = input("Was hätten Sie gern? (Espresso/Latte/Cappuccino):")
    if drink == "aus":
        end_process=True
    elif drink == "report":
        print(resources)
        print(f"Profit={profit}")
    else:
        # TODO: 3. check resources for drink and stop if too low
        for resource in check_resources(drink, resources):
            if check_resources(drink, resources)[resource] <0:
                print(f"Entschuldigung es gibt nicht genug {resource}.")
                end_process = True
        if not end_process:
            resources = check_resources(drink, resources)
            print(resources)
        # TODO: 4. tell price, ask how many of each coin
            cost = MENU[drink]["Preis"]
            print(f"Ein {drink} kostet {cost}$. Bitte zahlen Sie mit Münzgeld")
            tweuro = 2 * int(input("Wie viele 2-Euro Münzen?:"))
            euro = 1 * int(input("Wie viele 1-Euro Münzen?:"))
            twenty = 0.2 * int(input("Wie viele 20-Cent Stücke?:"))
            ten = 0.1 * int(input("Wie viele 10-Cent Stücke?:"))
            five = 0.05 * int(input("Wie viele 5-Cent Stücke:"))
            one = 0.01 * int(input("Wie viele 1-Cent Stücke:"))
            change = round(tweuro + euro + twenty + ten + five + one - cost, 2)
            if change < 0:
                print("Entschuldigung, das ist nicht genug Geld.")
                end_process = True

            else:
                profit += cost
                print(f"Hier sind Ihr Rückgeld: {change}€\n und Ihr {drink} ☕ Vielen Dank!")

# TODO: 5. price minus sum coins, give change
# TODO: 6. subtract resources
# TODO: 7. give drink
# TODO: 8. start again
