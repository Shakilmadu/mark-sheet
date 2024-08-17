total_marks = 0
count = 0
highest_mark = float('-inf')  # Initialize with negative infinity
lowest_mark = float('inf')    # Initialize with positive infinity

you_want_enter_input = True
while you_want_enter_input:

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
        print("Invalid input!please enter a correct value ")

    total_marks += marks
    count += 1

    if marks > highest_mark:
        highest_mark = marks

    if marks < lowest_mark:
        lowest_mark = marks

    looking_ahead = input("Do you need to enter more data? yes/no: ")
    if looking_ahead == "no":
        break
    elif looking_ahead == "yes":
        continue

if count > 0:
     average = total_marks / count
     print("Average marks: ",average)
     print("Highest mark:", highest_mark)
     print("Lowest mark:", lowest_mark)
else:
     print("No marks entered.")

print( "Total marks : ",total_marks)
print("numer of time data was entered: ",count)

