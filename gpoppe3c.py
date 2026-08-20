#Garrett Poppe

def grader():
    average = 0
    for i in range(3):
        score1 = float(input("Enter your a test score:"))
        if score1 > 89:
            print("Score is an A")
        elif score1 > 79 and score1 < 90:
            print("Score is a B")
        elif score1 > 69 and score1 < 80:
            print("Score is a C")
        elif score1 > 59  and score1 < 70:
            print("Score is a D")
        else:
            print("score is an F")
        average = score1 + average
    ave = average/3
    return ave

def gradeave(x):
    print("final average is")
    if x > 89:
        print("Score is an A")
    elif x > 79 and x < 90:
        print("Score is a B")
    elif x > 69 and x < 80:
        print("Score is a C")
    elif x > 59  and x < 70:
        print("Score is a D")
    else:
        print("score is an F")


print("user1")
aveg = grader()
gradeave(aveg)

print("user2")
aveg1 = grader()
gradeave(aveg1)

print("user3")
aveg2 = grader()
gradeave(aveg2)

#trouble with average
#print("aveg = ",aveg,"aveg1 =",aveg1,"aveg2=",aveg2)

totalave = (aveg + aveg1 + aveg2)/3

print("average score is ",totalave," and the average ")

if totalave > 89:
    print("Score is an A")
elif totalave > 79 and score1 < 90:
    print("Score is a B")
elif totalave > 69 and score1 < 80:
    print("Score is a C")
elif totalave > 59  and score1 < 70:
    print("Score is a D")
else:
    print("score is an F")

