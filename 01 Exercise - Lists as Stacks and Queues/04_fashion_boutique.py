clothes = [int(n) for n in input().split()]
racks_space = int(input())

racks_count = 1
current_rack_space = racks_space

while clothes:
    cloth = clothes.pop()

    if current_rack_space - cloth >= 0:
        current_rack_space -= cloth
    else:
        racks_count += 1
        current_rack_space = racks_space - cloth

print(racks_count)
