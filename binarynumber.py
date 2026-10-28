import math

number = input("Please input a number:  ")
binary = [0]
binary.remove(0)
def binary_machine():
    try:
        int_number = int(number)
        while int_number != 0: (binary.append(int_number % 2),
                int_number := (int_number // 2))
        binary.reverse()
        print(binary)   
    
    except ValueError:
        print("put in a number next time.")

binary_machine()