from collections import deque

textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))

created_item = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    textile_element = textiles.popleft()
    medicament_element = medicaments.pop()
    combine_elements_sum = textile_element + medicament_element

    if combine_elements_sum == 30:
        created_item["Patch"] += 1

    elif combine_elements_sum == 40:
        created_item["Bandage"] += 1

    elif combine_elements_sum == 100:
        created_item["MedKit"] += 1

    elif combine_elements_sum > 100:
        created_item["MedKit"] += 1
        remaining_resources = combine_elements_sum - 100
        medicaments[-1] += remaining_resources

    elif combine_elements_sum < 100:
        medicaments.append(medicament_element + 10)

if not textiles and medicaments:
    print("Textiles are empty.")
elif not medicaments and textiles:
    print("Medicaments are empty.")
else:
    print("Textiles and medicaments are both empty.")

for name, value in sorted(created_item.items(), key=lambda x: (-x[1], x[0])):
    if value > 0:
        print(f"{name} - {value}")

if medicaments:
    print(f"Medicaments left: {', '.join(reversed(list(map(str, medicaments))))}")
if textiles:
    print(f"Textiles left: {', '.join(list(map(str, textiles)))}")
