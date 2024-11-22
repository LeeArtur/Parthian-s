import random

ship_coordinates = [2,6,5]
weight = [200, 300, 213]
total_weight = 713
user_coordinates = []
sum_weight = 0
for i in range(3):
    while True:
        user_input = input(f"Enter coordinate number {i + 1}: ")
        if user_input.isdigit():
            user_coordinates.append(int(user_input))
            break
        else:
            print("Invalid input. Try again!")

for i in range(3):
    if user_coordinates[i] in ship_coordinates:
        sum_weight += weight[ship_coordinates.index(user_coordinates[i])]
        print(sum_weight)
        if sum_weight == total_weight:
            print("Congrats")
#gfjhwsjdhwgdjhgwgujgsghj