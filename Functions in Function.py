import string
import random
import os
import turtle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import pickle
from collections import Counter
import math
import numpy as np
import scipy.special
def most_frequently_used_function():
    most_common_function = Counter(function_usage).most_common(1)
    return most_common_function[0][0]
function_usage = {
    "Password Function": 0,
    "Stack Function": 0,
    "Calculator": 0,
    "Encryption": 0,
    "Turtle Graphic": 0,
    "File Function": 0
}
def Rainbow_spiral():
    l=['red','blue','black','green','black','yellow']
    turtle.speed(1000)
    for i in range(1,400):
        turtle.circle(i/5)
        turtle.right(13)
        if i %10==1:
            turtle.color(random.choice(l))
    for i in range(200):
      for j in range(500):
          pass
      turtle.bye()
def read_txt():
    File_Name = input("Enter File Name : ")
    File = open(File_Name+".txt","r")
    print(File.read())
def append_text():
    File_Name = input("Enter File Name : ")
    Content = input("Enter Content:")
    File = open(File_Name+".txt","a")
    File.write("\n"+Content)
def write_text():
    File_Name = input("Enter File Name : ")
    Content = input("Enter Content:")
    File = open(File_Name+".txt","w")
    File.write(Content)
def File_Handle_Menu():
    while True:
        print("***File Menu*** \n 1.TEXT FILE \n 2.BINARY FILE \n 3.EXIT")
        Choice = int(input("Select An Option:"))
        if Choice == 1:
            while True:
                print("***TEXT FULE MENU*** \n1.Write(Previous Data Will Be Lost)\n2.Append \n3.Read\n4.Exit")
                Choice = int(input("Select An Option:"))
                if Choice == 1:
                    write_text()
                if Choice == 2:
                    append_text()
                if Choice == 3:
                  read_txt()
                if Choice == 4:
                  confrimation = input("Are You Sure \n")
                  if confrimation == "yes":
                          break
        if Choice == 2:
            while True:
                print("***BINARY FULE MENU*** \n1.Write(Previous Data Will Be Lost)\n2.Append \n3.Read\n4.Exit")
                Choice = int(input("Select An Option:"))
                if Choice == 1:
                    write_binary()
                if Choice == 2:
                    append_binary()
                if Choice == 3:
                  read_binary()
                if Choice == 4:
                  confrimation = input("Are You Sure \n")
                  if confrimation == "yes":
                          break
        if Choice == 3:
            confrimation = input("Are You Sure \n")
            if confrimation == "yes":
                break
class MyClass:
    def __init__(self, value):
        self.value = value
def write_binary():
    File_Name = input("Enter File Name : ")
    Extension = input("Enter The Desired Extension Of The File :")
    Content = input("Enter Content:")
    my_data = MyClass(Content)
    with open(File_Name+"."+Extension, "wb") as f:
        pickle.dump(my_data, f)
def read_binary():
    File_Name = input("Enter File Name : ")
    Extension = input("Enter The Desired Extension Of The File :")
    with open(File_Name + "." + Extension, "rb") as f:
        while True:
            try:
                my_data = pickle.load(f)
                print(my_data.value)
            except EOFError:
                break
def append_binary():
    File_Name = input("Enter File Name : ")
    Extension = input("Enter The Desired Extension Of The File :")
    Content = input("Enter Content:")
    my_data = MyClass(Content)
    with open(File_Name+"."+Extension, "ab") as f:
        pickle.dump(my_data, f)

def Turtle_Menu():
    def Square():
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()
    def Circle():
        turtle.circle(100,370)
        turtle.done()
    def ChessBoard():
        sc = turtle.Screen()
        pen = turtle.Turtle()

        def draw():
            for i in range(4):
                pen.forward(30)
                pen.left(90)
            pen.forward(30)

        sc.setup(600, 600)
        pen.speed(100)
        for i in range(8):
            pen.up()
            pen.setpos(0, 30 * i)
            pen.down()
            for j in range(8):
                if (i + j) % 2 == 0:
                    col = 'black'
                else:
                    col = 'white'
                pen.fillcolor(col)
                pen.begin_fill()
                draw()
                pen.end_fill()
        pen.hideturtle()
        turtle.done()
    while True:
        print("***Turtle Menu*** \n1.ChessBoard \n2.Circle \n3.Square \n4.RainBow Spiral\n5.Exit")
        Choice = input("Select An Option:")
        if Choice == "1":
            ChessBoard()
        if Choice == "2":
            Circle()
        if Choice == "3":
            Square()
        if Choice == "4":
            Rainbow_spiral()
        if Choice == "5":
            confermation = input("Are You Sure ? \n")
            if confermation.lower() == "yes":
                break
def DECRYPTION():
    encrypted_data = input("Enter the encrypted data: ")
    key = input("Enter the key: ")
    cipher = AES.new(key, AES.MODE_CBC)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data
def ENCRYPTION():
    message = input("Enter the message to encrypt: ")
    key = input("Enter the key: ")
    encrypted_message = ""
    key_index = 0
    for char in message:
        encrypted_message += chr(ord(char) + ord(key[key_index]))
        key_index = (key_index + 1) % len(key)
    return encrypted_message
def DECRYPT():
    encrypted_message = input("Enter the encrypted message: ")
    key = input("Enter the key: ")
    decrypted_message = ""
    key_index = 0
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - ord(key[key_index]))
        key_index = (key_index + 1) % len(key)
    return decrypted_message
def ENCRYPT():
    try:
        user_input = input("Enter the text to encrypt: ")
        key = os.urandom(32)
        encrypted_data = aes_encrypt(user_input, key)
        print("Key:", key)
        print("Encrypted data:", encrypted_data)
        return encrypted_data, key
    except ValueError:
        print("Invalid input. Please make sure the key is 16, 24, or 32 bytes long.")
def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = cipher.iv
    return (iv + ct_bytes)

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
        print("***STACK MENU***")
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
        print("***ENCRYPTION MENU*** \n 1.AES Encryptor Function \n 2.Simple Encryptor \n 3.AES Decryptor \n 4.Simple Decryptor \n 5.Exit")
        Choice  = input("Select An Option:")
        if Choice == "1":
            print(ENCRYPT())
        if Choice == "2":
            print(ENCRYPTION())
        if Choice == "3":
            print(DECRYPTION())
        if Choice == "4":
            print(DECRYPT())
        if Choice == "5":
            Confrimation = input("Are You Sure ? \n")
            if Confrimation.lower() == "yes":
                break
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
    def Factorial():
        Result = math.factorial(X)
        print (Result)
    while True:
        print("***Ca1culator Menu***\n 1.Addition\n 2.Subtract\n 3.Multiplie \n 4.Devide \n 5.Square\n 6.Percentage\n 7.Factorial \n 8.Exit")
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
            Y = float(input("ENTER THE NUMBER TO BE MULTIPLIED WITH:"))
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
            X = int(input("ENTER THE NUMBER:"))
            Factorial()
        if Choice == "8":
            confirmation = input("Are you sure \n")
            if confirmation.lower() == "yes" :
                break
def main_menu():
    while True:
        print("***FUNCTION MENU***\n1. Password Function\n2. Stack Function\n3. Calculator\n4. Encryption\n5. Turtle Graphic\n6. File Function\n7. History\n8. Exit")
        Choice = input("Select a Function:")
        if Choice == "1":
            main()
            function_usage["Password Function"] += 1
        elif Choice == "2":
            Stack()
            function_usage["Stack Function"] += 1
        elif Choice == "3":
            Calculate()
            function_usage["Calculator"] += 1
        elif Choice == "4":
            Encryptor()
            function_usage["Encryption"] += 1
        elif Choice == "5":
            Turtle_Menu()
            function_usage["Turtle Graphic"] += 1
        elif Choice == "6":
            File_Handle_Menu()
            function_usage["File Function"] += 1
        elif Choice == "7":
            print("Most frequently used function:", most_frequently_used_function())
        elif Choice == "8":
            confirmation = input("Are You Sure?\n")
            if confirmation.lower() == "yes":
                break
main_menu()