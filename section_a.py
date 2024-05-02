# (a)(i)
def calculate_grade(percentage):
    if percentage >= 90 and percentage <= 100:
        return 'A'
    elif percentage >= 80 and percentage <= 89:
        return 'B'
    elif percentage >= 70 and percentage <= 79:
        return 'C'
    elif percentage >= 60 and percentage <= 69:
        return 'D'
    elif percentage >= 50 and percentage <= 59:
        return 'E'
    else:
        return 'Fail'

def main():
    try:
        percentage = float(input("Enter the student's percentage: "))
        if percentage < 0 or percentage > 100:
            print("Percentage should be between 0 and 100")
        else:
            grade = calculate_grade(percentage)
            print(f"The student's grade is: {grade}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()



# (a) (ii)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

def main():
    try:
        choice = input("Enter '1' to convert from Celsius to Fahrenheit or '2' to convert from Fahrenheit to Celsius: ")
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        else:
            print("Invalid choice. Please enter '1' or '2'.")
    except ValueError:
        print("Please enter a valid temperature.")

if __name__ == "__main__":
    main()



# (b) (i)
def calculate_triangle_area(base, height):
    # Formula for calculating the area of a triangle
    area = 0.5 * base * height
    return area

# Getting the user input for base and height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = calculate_triangle_area(base, height)

# Printing the result
print("The area of the triangle is:", area)



# (b) (ii)
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Sample list
sample_list = [9, 2, 3, 5, 8]

# Calling the function to get the sum
result = sum_of_list(sample_list)

# Printing the result
print("Sum of the numbers in the list:", result)
