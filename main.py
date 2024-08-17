user_marks = input("Enter marks: ")
marks = float(user_marks)

if 0.00 <= marks <= 39.99:
    print("Grade: F")
    print("Description: Failure")
elif 40.00 <= marks <= 54.99:
    print("Grade: D")
    print("Description: Ordinary Pass")
elif 55.00 <= marks <= 65.99:
    print("Grade: C")
    print("Description: Credit Pass")
elif 66.00 <= marks <= 74.99:
    print("Grade: B")
    print("Description: Very Good Pass")
elif 75.00 <= marks <= 100.00:
    print("Grade: A")
    print("Description: Distinction")
else:
    print("Invalid input")