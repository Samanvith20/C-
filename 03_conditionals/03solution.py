studentscore = int(input("Enter your score: "))

if studentscore >= 90 and studentscore <= 100:
    print("Grade A")
elif studentscore >= 80 and studentscore < 90:
    print("Grade B")
elif studentscore >= 70 and studentscore < 80:
    print("Grade C")
elif studentscore >= 60 and studentscore < 70:
    print("Grade D")
else:
    print("Grade F")


# or another solution is
score = 185

if score >= 101:
    print("Please verify your grade again")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)