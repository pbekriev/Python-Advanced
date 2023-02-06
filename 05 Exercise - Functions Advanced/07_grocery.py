def grocery_store(**products):
    products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []

    for product, quontity in products:
        result.append(f"{product}: {quontity}")

    return "\n".join(result)
