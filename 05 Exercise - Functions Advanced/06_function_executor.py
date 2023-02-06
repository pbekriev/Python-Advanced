def func_executor(*func_data):
    result = []
    for func, args in func_data:
        result.append(f"{func.__name__} - {func(*args)}")

    return "\n".join(result)
