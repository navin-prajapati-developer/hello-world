# Student Grade Calculator
name = input("Enter student name: ")

print("Enter marks out of 100:")
math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
hindi = int(input("Hindi: "))
computer = int(input("Computer: "))

total = math + science + english + hindi + computer
average = total / 5

print("\n--- Result Card ---")
print("Student: " + name)
print("Math: " + str(math))
print("Science: " + str(science))
print("English: " + str(english))
print("Hindi: " + str(hindi))
print("Computer: " + str(computer))
print("Total: " + str(total) + "/500")
print("Average: " + str(average) + "%")

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F - Failed")
