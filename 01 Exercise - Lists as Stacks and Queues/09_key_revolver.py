from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split(" ")))
locks = deque([int(n) for n in input().split(" ")])
intelligence_value = int(input())
bullet_used = 0
reload = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]
    bullet_used += 1
    reload += 1
    if lock >= bullet:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    if reload == gun_barrel_size and bullets:
        print("Reloading!")
        reload = 0
if not locks:
    bull_cost = bullet_used * bullet_price
    money_earned = intelligence_value - bull_cost
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
