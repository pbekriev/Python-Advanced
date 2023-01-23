from collections import deque
from datetime import datetime, timedelta

robots = {data.split("-")[0]: [int(data.split("-")[1]), 0] for data in input().split(";")}
factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(product)
        continue

    robots[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")
