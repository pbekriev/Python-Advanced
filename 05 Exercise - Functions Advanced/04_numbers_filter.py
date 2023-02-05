def even_odd_filter(**numbers):
    if "odd" in numbers:
        numbers["odd"] = [n for n in numbers["odd"] if n % 2 == 1]

    if "even" in numbers:
        numbers["even"] = list(filter(lambda x: x % 2 == 0, numbers["even"]))

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))
