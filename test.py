best_buy_items = [
    {
        "name": "El Cinco",
        "price": 399.99,
        "department": "Consoles",
    },
    {
        "name": "El Cuatro",
        "price": 199.99,
        "department": "Consoles",
    },
    { 
        "name": "El Tres",
        "price": 119.99,
        "department": "Consoles",
    },
    {
        "name": "El Dos",
        "price": 94.99,
        "department": "Consoles",
    },
    { 
        "name": "El Uno",
        "price": 49.99,
        "department": "Consoles",
    }
]
print("Which one would you like to buy? Please pick one.")
cart = []
total = 0
done = False
while not done:
    for index, item in enumerate(best_buy_items):
        print(index,":", item["name"])
        print(index,":", item["price"])
        print(index,":", item["department"] )
    choice = int(input("Pick an item:"))
    item = best_buy_items[choice]
    cart += [item["name"]]
    total += float(item['price'])
    done = input("Are you done?) (yes or no)")
    if done == "yes":
        done = True
        print("Items purchased", cart)
        print("Total Cost", total)
    elif done == "no":
        done = False