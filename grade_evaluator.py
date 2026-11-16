print("--- Student Grade Evaluator ---")
grade = float(input("Enter the grade (0 - 100): "))

if grade > 100 or grade < 0:
    print("Error: Please enter a valid grade between 0 and 100.")
elif grade >= 90:
    print("Your grade: Excellent")
elif grade >= 75:
    print("Your grade: Good")
elif grade >= 50:
    print("Your grade: Acceptable")
else:
    print("Your grade: Weak")
