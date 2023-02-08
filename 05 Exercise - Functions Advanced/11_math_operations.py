def math_operations(*num, **kwargs):
    for i in range(len(num)):
        key = list(kwargs.keys())[i % 4]

        if key == "a":
            kwargs[key] += num[i]
        elif key == "s":
            kwargs[key] -= num[i]
        elif key == "d":
            if num[i] != 0:
                kwargs[key] /= num[i]
        elif key == "m":
            kwargs[key] *= num[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{k}: {v:.1f}" for k, v in kwargs)
