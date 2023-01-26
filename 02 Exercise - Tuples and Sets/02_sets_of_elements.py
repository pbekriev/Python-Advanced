n, m = [int(x) for x in input().split()]

first_set = set(int(input()) for _ in range(n))
second_set = set(int(input()) for _ in range(m))

print(*set(first_set.intersection(second_set)), sep="\n")

