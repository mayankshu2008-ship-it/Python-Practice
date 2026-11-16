#Student Marks Analyzer
name = input("Enter your name: ")
marks = []
subject = ["Maths", "Science", "English", "History", "Geography"]
for i in range(5):
    mark = int(input("Enter marks for {}: ".format(subject[i])))
    marks.append(mark)
    if mark < 0 or mark > 100:
        print("Invalid marks entered. Please enter marks between 0 and 100.")
        exit()
print("STUDENT REPORT CARD")
a = {subject[i]: marks[i] for i in range(5)}
print("Name: ", name)
for subject, mark in a.items():
    print(subject, ":", mark)
Total = sum(marks)
print("Total Marks: ", Total)

Avg_percentage = (Total / 500) * 100
print("Average Percentage is: ", Avg_percentage)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
if Avg_percentage >= 90:
    print("Grade: A")
elif Avg_percentage >= 80:
    print("Grade: B")
elif Avg_percentage >= 70:
    print("Grade: C")
elif Avg_percentage >= 60:
    print("Grade: D")
elif Avg_percentage >= 35 and Avg_percentage < 60:
    print("Grade: E")
else:
    print("You Failed Loser!")
    


