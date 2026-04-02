Boxes = 4
Triangles = 3
Circles = 0

user_input = input("Enter the a number of shapes you want to draw 1-4: ")
if user_input == "4":
    print("Drawing a box!")
elif user_input == "3":
    print("Drawing a triangle!")
elif user_input == "0":
    print("Drawing a circle!")
else:
    print("Invalid input. Please enter a number between 1 and 4.")
