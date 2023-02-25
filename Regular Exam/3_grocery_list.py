def shop_from_grocery_list(budget, grocery_list, *data):
    budget_left = int(budget)
    purchased_list = []
    products = data
    for name, value in products:
        if name in grocery_list and name not in purchased_list:
            if value > budget_left or not grocery_list:
                break
            grocery_list.remove(name)
            purchased_list.append(name)
            budget_left -= value

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
