import random

ship_coordinates = [2, 6, 5]
weights = [200, 300, 213]
total_weight = 713

def asking_user():
    user_coordinates = []
    for i in range(3):
        while True:
            user_input = input(f"Enter coordinate number {i + 1}: ")
            if user_input.isdigit():
                user_coordinates.append(int(user_input))
                break
            else:
                print("Invalid input. Please enter a positive integer.")
    return user_coordinates

def randomizer():
    return [random.randint(1, 10) for _ in range(3)]

while True:
    user_coordinates = asking_user()

    sum_weight = 0
    for coord in user_coordinates:
        if coord in ship_coordinates:
            sum_weight += weights[ship_coordinates.index(coord)]

    if sum_weight == total_weight:
        print("Congratulations! You've found all the cargo!")
        break
    else:
        print(f"Total weight found: {sum_weight} kg. Try again!")
        ship_coordinates = randomizer()
        print(f"New ship coordinates: {ship_coordinates}")