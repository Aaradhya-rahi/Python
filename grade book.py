students = ["Aaradhya", "Rishita", "Jack", "Gina", "Aarav"]
marks = { 100 , 90 , 80 , 70 , 60}

grade_book = {students:marks for students,marks in zip(students,marks)}
print("students' marks are:", grade_book)

print("Highest marks are scored by Aaradhya- 100 marks")
print("lowest marks are scored by Aarav- 60 marks")

choose=print(input ("choose the student's name who's mark you want to see"))

if choose(Aaradhya):
    print("100")

if choose(Rishita):
    print("90")

if choose(Jack):
    print("80")

if choose(Gina):
    print("70")
    