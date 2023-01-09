# Part 1
#
# 1. Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
# BMI = (weight in Kg)/(Height in Meters)^2.
#
# 2. Write code that can accept the weight and height of a person and calculate their BMI.
# Make sure to use a function that accepts the height and weight values and returns the BMI value.

def bmi_calculator(weight, height):
    return (weight / height)**2

# Part 2
#
# 3. Write a function which would divide two numbers, design the function in a manner that it handles the divide by
# zero exception.


def divide(num1, num2):
    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError as e:
        print("e")

# Part 3


# 4. Write Python code to open a file named demo.txt and write some random data into it.
file = open('demo.txt', 'w')
file.write('this is the text written to the file')
file.close()

# 5. Open the file, read the contents, and display them as output.
file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()

# 6. Write code to add additional text to the existing file on a new line without deleting the previous contents.
file = open('demo.txt', 'a')
file.write('This is the new text')
file.close()

# Part 4
#
# 7. Write code that accepts the name of a product and in turn returns their respective prices.


def price_return(product):
    return product_list[product]

# 8. Make sure to use a dictionary to store products and their respective prices.
# 9. The dictionary should include at least 5 elements.


product_list = {
    "wallet": 30.00,
    "water": 2.00,
    "lotion": 4.00,
    "lamp": 50.00,
    "phone": 800.00
}


price_return("wallet")

# Part 5
#
# 10. List out all the odd numbers from 1 to 100 using lists in Python.
#
# 11. use list(), range(), and a for loop with a conditional statement that outputs the numbers.

num_list = [*range(1, 101)]

for num in num_list:
    if num % 2 != 0:
        print(num)