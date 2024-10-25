import circle
import rectangal
area_circle_choice = 1
circumference_choice = 2
area_rectangal_choice = 3
perimeter_rectangle_choice = 4
Quit = 5

def main():
    choice = 0
    while choice != Quit:
        display()
        choice = int(input('enter your choice: '))
        if choice == area_circle_choice:
            radius = float(input('enter the circles radius: '))
            print('the area is', circle.area(radius))
        elif choice == circumference_choice:
            radius = float(input('enter the circles radius: '))
            print('the circumference is', \
                  circle.circumference(radius))
        elif choice == area_rectangal_choice:
            width= float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The area is', rectangal.area (width, length))
        elif choice == perimeter_rectangle_choice:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is', \
                rectangal.perimeter (width, length))
        elif choice == Quit:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
            
def display():
    print('        MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')
main()