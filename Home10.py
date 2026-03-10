#Homework:
#you have one list of student marks.
#create two sub lists for even and odd marks student.

stud_marks = [45, 60, 72, 33, 88, 91, 54]

even_marks = []
odd_marks = []

for m in stud_marks:
    if m % 2 == 0:
        even_marks.append(m)
    else:
        odd_marks.append(m)

print("Even marks:", even_marks)
print("Odd marks:", odd_marks)