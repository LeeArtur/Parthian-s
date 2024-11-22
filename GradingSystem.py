A = 0
B = 0
C = 0
D = 0
F = 0
aver = 0
grades = [int(s) for s in input("Enter your grades: ").split()]
for i in range(len(grades)):
    if 90 <= grades[i] <= 100:
        A += 1
    elif 75 <= grades[i] <= 89:
        B += 1
    elif 60 <= grades[i] <= 74:
        C += 1
    elif 50 <= grades[i] <= 59:
        D += 1
    elif grades[i] < 50:
        F += 1

def average(grade):
    return float("{:.2f}".format((grade/len(grades))*100))

print("A: " + str(A) + " grades " + "(" + str(average(A)) +  ")%" 
      "\nB: " + str(B) + " grades " + "(" + str(average(B)) + ")%" 
      "\nC: " + str(C) + " grades " + "(" + str(average(C)) + ")%" 
      "\nD: " + str(D) + " grades " + "(" + str(average(D)) + ")%" 
      "\nF: " + str(F) + " grades " + "(" + str(average(F)) + ")%" )