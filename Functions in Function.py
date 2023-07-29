import string
import random
def ENCRYPT():
    try:
        user_input = input("Enter the text to encrypt: ")
        shift_amount = int(input("Enter the shift amount (an integer): "))
        encrypted_data = caesar_cipher_encrypt(user_input, shift_amount)
        print("Encrypted data:", encrypted_data)
    except ValueError:
        print("Invalid shift amount. Please enter an integer.")

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += shifted_char.upper() if is_upper else shifted_char
        else:
            encrypted_text += char
    return encrypted_text
def Stack():
    stack = []
    def push(item):
        stack.append(item)
        print("Element", item, "is inserted successfully into the stack")
    def pop(item):
        if not is_empty():
            popped_item = stack.pop()
            return popped_item
        else:
            return None
    def Display():
        if not is_empty():
            print("stack content is:")
            for item in reversed(stack):
                print(item)
    def is_empty():
        return len(stack) == 0
    while True:
        print("STACK MENU")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        Choice = input("Enter Your Choice:")
        if Choice == "1":
            element = input("Enter element to PUSH :")
            push(element)
            print(stack)
        if Choice == "2":
            confirmation = input("Are you sure ? \n")
            pop(confirmation)
            print(stack)
        if Choice == "3":
            confirmation = input("do you wanna display the stack ? \n")
            if confirmation == "yes":
                print(stack)
        if Choice == "4":
            confirmation = input("Are you sure ? \n")
            if confirmation.lower() == "yes":
                break
def generate_password(pass_len, chars):
    password = ""
    for i in range(pass_len):
        password += random.choice(chars)
    return password
def main():
    while True:
        print("\n **PASSWORD_MENU** \n 1.Pincode \n 2.Alphanumeric \n 3.Alphabetically \n 4.Lowecase \n 5.Uppercase \n 6.EXIT")
        choice = input("Select an option:")
        if choice == "1":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.digits)
            print(password)
        elif choice == "2":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_letters + string.digits)
            print(password)
        elif choice == "3":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_letters)
            print(password)
        elif choice == "4":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_lowercase)
            print(password)
        elif choice == "5":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_uppercase)
            print(password)
        elif choice == "6":
            confirmation = input("Are you sure?\n")
            if confirmation.lower() == "yes":
                break
def Encryptor():
    while True:
        print("***ENCRYPTION MENU*** \n 1.Encryption Function \n 2.Exit")
        Choice  = input("Select An Option:")
        if Choice == "1":
            ENCRYPT()
        if Choice == "2":
            Confrimation = input("Are You Sure ? \n")
            Confrimation.lower() == "yes"
def Calculate():
    def addition():
        Result = X+Y
        print (Result)
    def subtract():
        Result = X-Y
        print (Result)
    def multiplie():
        Result = X*Y
        print (Result)
    def devide():
        Result = X/Y
        print (Result)
    def square():
        Result = X**Y
        print (Result)
    def percentage():
        Result = X/Y * 100
        print (Result)
    while True:
        print("***Ca1culator Menu***\n 1.Addition\n 2.Subtract\n 3.Multiplie \n 4.Devide \n 5.Square\n 6.Percentage\n 7.Exit")
        Choice = input("Select An Option:")
        if Choice == "1":
            X = float(input("ENTER NUMBER:"))
            Y = float(input("ENTER THE NUMBER TO BE ADDED INTO:"))
            addition()
        if Choice == "2":
            X = float(input("ENTER NUMBER TO BE SUBTRACTED FROM:"))
            Y = float(input("ENTER NUMBER TO BE SUBTRACTED:"))
            subtract()
        if Choice == "3":
            X = float(input("ENTER THE NUMBER:"))
            Y = float(input("ENTER THE NUMBER:"))
            multiplie()
        if Choice == "4":
            X = float(input("ENTER DIVIDEND:"))
            Y = float(input("ENTER THE DIVISOR:"))
            devide()
        if Choice == "5":
            X = float(input("ENTER THE NUMBER:"))
            Y = float(input("ENTER IT'S POWER:"))
            square()
        if Choice == "6":
            X = float(input("ENTER PORTION AMOUNT:"))
            Y = float(input("ENTER THE TOTAL AMOUNT:"))
            percentage()
        if Choice == "7":
            confirmation = input("Are you sure \n")
            if confirmation.lower() == "yes" :
                break
def main_menu():
    while True :
        print("***FUNCTION MENU***\n 1.Password Function\n 2.Stack Function\n 3.Calculator \n 4.Encryption")
        Choice = input("Select a Function:")
        if Choice == "1":
            main()
        if Choice == "2":
            Stack()
        if Choice == "3":
            Calculate()
        if Choice == "4":
            Encryptor()
main_menu()