from _collections import deque

name_of_players = input().split(' ')
step_of_hot_potato = int(input())
players_deque = deque(name_of_players)


while len(players_deque) > 1:
    for _ in range(step_of_hot_potato - 1):
        players_deque.append(players_deque.popleft())

    print(f'Removed {players_deque.popleft()}')

print(f'Last is {players_deque.pop()}')