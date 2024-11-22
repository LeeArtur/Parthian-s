# import only system from os
from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

lastName = input("Enter your last name, please: ")
firstName = input("Enter your first name, please: ")

while True:
    schoolCertification = input("Do you have a school education certificate?\n"
                            "1 - yes\n"
                            "0 - no\n"
                            "Your answer: ")
    if schoolCertification == "1" or schoolCertification == "0":
        break
    else:
        print("Wrong input. Please repeat")

while True:
    ORTscore = int(input("Enter your ORT certificate score: "))
    if 240 > ORTscore > 0:
        break
    else:
        print("Wrong input. Please repeat")

while True:
    englishLevel = input("Enter your English level proficiency level (A1, A2, B1, B2, C1, C2): ")
    if englishLevel in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
        break
    else:
        print("Wrong input. Please repeat")

recommendation = False

clear()

if schoolCertification == "1":
    if ORTscore >= 110:
        if englishLevel != 'A1' and englishLevel != 'A2':
            print("Congratulations! You are recommended for admission to university!")
            recommendation = True
        else:
            print("Sorry your English level is too low. "
                  "You can participate in 0ne-year preparatory English language course (Foundation Course AIU) at the university")
    else:
        print("Sorry you are not recommended")
else:
    print("Sorry you are not recommended")

programs = ['Computer Engineering',
            "Artificial Intelligence",
            "Psychology",
            "Journalism",
            "International Relations",
            "Law",
            "Management",
            "Medicine"]
prices = [2500, 2200, 1900, 1700, 2200, 1800, 2200, 3300]
discountPercent = 0
if 140 <= ORTscore <= 155:
    discountPercent = 5
elif 156 <= ORTscore <= 174:
    discountPercent = 10
elif 175 <= ORTscore <= 199:
    discountPercent = 25
elif 200 <= ORTscore <= 209:
    discountPercent = 50
elif 210 <= ORTscore <= 218:
    discountPercent = 75
elif 219 <= ORTscore <= 240:
    discountPercent = 100

if recommendation:
    print("Choose your program")
    for i in range(len(programs)):
        print(str(i) + ' - ' +  programs[i] + ' ' + str(prices[i]))
    chosenProgram = int(input())
    clear()
    if ORTscore >= 140:
        print("Dear " + firstName + ' ' + lastName + ', we congratulate you! You have been admitted to the ' + programs[chosenProgram] + ' program at Ala-Too International University. The cost of your tuition with a ' + str(discountPercent) + '% discount will be ' + str(int(prices[chosenProgram] - prices[chosenProgram] * (discountPercent * 0.01))) + '$ per year.' )
    else:
        print("Dear " + firstName + ' ' + lastName + ', we congratulate you! You have been admitted to the ' + programs[
            chosenProgram] + ' program at Ala-Too International University. The cost of your tuition will be ' + str(prices[chosenProgram]) + '$ per year.')
