def sum_positive():
    sum_of_numbers = 0
    for num in numbers:
        if num > 0:
            sum_of_numbers += num
    return sum_of_numbers


def sum_negative():
    sum_of_numbers = 0
    for num in numbers:
        if num < 0:
            sum_of_numbers += num
    return sum_of_numbers


def print_result(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = list(map(int, input().split()))

positive_num = sum_positive()
negative_num = sum_negative()
print_result(positive_num, negative_num)
