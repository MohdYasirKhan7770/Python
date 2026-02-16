# Student details
name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
sapid = input("Enter SAP ID: ")
sem = input("Enter Semester: ")
course = input("Enter Course: ")

print("\nEnter marks out of 100")

pds = int(input("PDS: "))
python = int(input("Python: "))
chemistry = int(input("Chemistry: "))
english = int(input("English: "))
physics = int(input("Physics: "))


total = pds + python + chemistry + english + physics
percentage = total / 5
cgpa = percentage / 10

# Grade decision
if cgpa >= 0 and cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"


print("\n--------- GRADE SHEET ---------")
print("Name:", name)
print("Roll Number:", roll, "     SAPID:", sapid)
print("Sem:", sem, "            Course:", course)

print("\nSubject Name : Marks")
print("PDS        :", pds)
print("Python     :", python)
print("Chemistry  :", chemistry)
print("English    :", english)
print("Physics    :", physics)

print("\nPercentage:", percentage, "%")
print("CGPA:", round(cgpa, 1))
print("Grade:", grade)
