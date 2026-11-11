print("UNIVERSITY SCHOLARSHIP ALLOCATION")

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ")

    mark1 = float(input("Enter marks in Subject 1: "))
    mark2 = float(input("Enter marks in Subject 2: "))
    mark3 = float(input("Enter marks in Subject 3: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: ₹"))

    aggregate = (mark1 + mark2 + mark3) / 3

    if (mark1 >= 40 and mark2 >= 40 and mark3 >= 40
            and attendance >= 75 and income <= 250000):

        students.append(
            (name, aggregate, attendance, income)
        )

# Sort by aggregate marks
# If aggregate is same, higher attendance gets priority
students.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\n========== SCHOLARSHIP ELIGIBLE STUDENTS ==========")

if students:
    for rank, student in enumerate(students, start=1):
        name, aggregate, attendance, income = student

        print(f"\nRank: {rank}")
        print("Student Name:", name)
        print("Aggregate Marks:", round(aggregate, 2))
        print("Attendance:", attendance, "%")
        print("Family Income: ₹", income)
else:
    print("No eligible students found.")

print("====================================================")

