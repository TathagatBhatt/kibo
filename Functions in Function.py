#modules imports
import string
import random
import os
import sympy
import turtle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import pickle
from collections import Counter
import math
from sympy import rad
import googletrans
from googletrans import Translator
import sympy as sp
translator = Translator()
import sympy as sp
import mysql.connector
def sql():
    password = input("enter the password:")
    mydb = mysql.connector.connect(host="localhost",user="root",password=password)
    cursor = mydb.cursor()
    while True:
        command = input("input sql command (or exit to exit this function):")
        if command.lower() == "exit":
            break
        cursor.execute(command)
        for X in  cursor :
            print(X)  
def SQL_MENU():
    while True:
        print("***SQL MENU*** \n1.SQL COMMAND LINE \n2.EXIT")
        choice = input("select an option :")
        if choice == "1":
            sql()
        if choice == "2":
            confrimation=input("are you sure ?(yes/no)\n")
            if confrimation == "yes":
                break
def definite_integration():
    var = input("Enter the variable of integration: ")
    function_str = input("Enter the function to integrate: ")
    lower_limit = float(input("Enter the lower limit of integration: "))
    upper_limit = float(input("Enter the upper limit of integration: "))
    x = sp.symbols(var)
    function = sp.sympify(function_str)
    integral = sp.integrate(function, (x, lower_limit, upper_limit))
    print(f"The definite integral of {function} from {lower_limit} to {upper_limit} with respect to {var} is: {integral}")
def integrate_function():
    var = input("Enter the variable to integrate with respect to: ")
    function_str = input("Enter the desired function: ")
    x = sp.symbols(var)
    function = sp.sympify(function_str)
    integral = sp.integrate(function, x)
    print("The integral of", function, "with respect to", var, "is:", integral,"+ C")
def differentiate_function():
    var = input("Enter the variable to differentiate with respect to: ")
    function_str = input("Enter the desired function: ")
    x = sp.symbols(var)
    function = sp.sympify(function_str)
    derivative = sp.diff(function, x)  
    print("The derivative of", function, "with respect to", var, "is:", derivative)
def Degree_To_Radian():
    Degrees = int(input("Enter the degree of which you need the value of in radian :"))
    angle_degrees = Degrees
    angle_radians = rad(angle_degrees)
    print(f"{angle_degrees} degrees is equal to {angle_radians} radians.")
def Sin():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Sin on",Degrees,"Degrees is:",math.sin(Degrees))
def Cos():
     Degrees = int(input("Enter the degree of which you need the value of :"))
     print("The value of Cos on",Degrees,"Degrees is:",math.cos(Degrees))
def Tan():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Tan on",Degrees,"Degrees is:",math.tan(Degrees))
def Cosec():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Cosec on",Degrees,"Degrees is:",math.cosec(Degrees))
def Sec():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Sec on",Degrees,"Degrees is:",math.sec(Degrees))
def Cot():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Cot on",Degrees,"Degrees is:",math.cot(Degrees))
def Function_Value():
    while True :
        print("***Trigonomteric Value Calculator Functions***\n1.Sin\n2.Cos\n3.Tan\n4.Cosec\n5.Sec\n6.Cot\n7.Exit")
        Choice = input("Select The Desired Function:")
        if Choice == "1":
            Sin()
        elif Choice == "2":
            Cos()
        elif Choice == "3":
            Tan()
        elif Choice == "4":
            Cosec()
        elif Choice == "5":
            Sec()
        elif Choice == "6":
            Cot()
        elif Choice == "7":
            confirmation = input("Are You Sure (yes/no):")
            if confirmation.lower()=="yes":
                break
def Trigonometeric_Functions():
    while True:
        print("***Trigonometry Function Menu*** \n1.Value Calculator\n2.Degree To Radian\n3.Exit")
        Choice = input("Select An Option:")
        if Choice =="1":
          Function_Value()
        if Choice == "2":
            Degree_To_Radian()
        if Choice == "3":
            confrimation = input("Are You Sure ? (yes/no) \n")
            if confrimation.lower() == "yes":
                break
def Calculate():
    def addition():
        Result = X+Y
        print (Y,"added to",X,"gives:",Result)
    def subtract():
        Result = X-Y
        print (Y,"Subtracted from",X, "is:",Result)
    def multiplie():
        Result = X*Y
        print (X,"multiplied by",Y,"is:",Result)
    def devide():
        Result = X/Y
        print (X,"devide by",Y,"is:",Result)
    def square():
        Result = X**Y
        print (X,"raised to the power",Y,"is:",Result)
    def percentage():
        Result = X/Y * 100
        print ("The Percentage is:", Result , "%")
    def Factorial():
        Result = math.factorial(X)
        print ("The Factorial of",X,"is:",Result)
    while True:
        print("***Ca1culator Menu***\n 1.Addition\n 2.Subtract\n 3.Multiplie \n 4.Devide \n 5.Square\n 6.Percentage\n 7.Factorial \n 8. Trigonometric Functions\n9.Integrate\n10.Definite Integration\n11.Differentiate\n 12.Exit")
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
            Trigonometeric_Functions()
        if Choice == "9":
            integrate_function()
        if Choice == "10":
            definite_integration()
        if Choice == "11":
            differentiate_function()
        if Choice == "12":
            confirmation = input("Are you sure \n")
            if confirmation.lower() == "yes" :
                break
def english_to_japanese():
    english_text = input("Enter the text:")
    janpanese_translation = translator.translate(english_text, src='en',dest='ja')
    print(english_text,"in japanese means:",janpanese_translation.text)
def japanese_to_english():
    japanese_text = input("Enter the text:")
    english_translation = translator.translate(japanese_text, src='ja',dest='en')
    print(japanese_text,"in english means:",english_translation.text)
def english_to_korean():
    english_text = input("Enter the text:")
    korean_translation = translator.translate(english_text, src='en',dest='ko')
    print(english_text,"in korean means:",korean_translation.text)
def korean_to_english():
    korean_text = input("Enter the text:")
    english_translation = translator.translate(korean_text, src='ko',dest='en')
    print( korean_text,"in english means:",english_translation.text)
def english_to_hindi():
    english_text = input("Enter the text:")
    hindi_translation = translator.translate(english_text, src='en',dest='hi')
    print(english_text,"in hindi means:",hindi_translation.text)
def hindi_to_english():
    hindi_text = input("Enter the text:")
    english_translation = translator.translate(hindi_text, src='hi',dest='en')
    print(hindi_text,"in english means:",english_translation.text)
def Translate_Hindi():
    while True:
        print("***Hindi Translator*** \n1.Hindi To English \n2.English To Hindi \n3.Exit")
        Choice = int(input("Select An Option :"))
        if Choice == 1:
             hindi_to_english()
        if Choice == 2:
            english_to_hindi()
        if Choice == 3:
            break
def Translate_Korean():
    while True:
        print("***Korean Translator*** \n1.Korean To English \n2.English To Korean \n3.Exit")
        Choice = int(input("Select An Option :"))
        if Choice == 1:
             korean_to_english()
        if Choice == 2:
            english_to_korean()
        if Choice == 3:
            break
def Translate_Japanese():
    while True:
        print("***Japanese Translator*** \n1.Japanese To English \n2.English To Japanese \n3.Exit")
        Choice = int(input("Select An Option :"))
        if Choice == 1:
             japanese_to_english()
        if Choice == 2:
            english_to_japanese()
        if Choice == 3:
            break
def Translation_Menu():
    while True:
        print("***TRANSLATOR***\n1.Japanese\n2.Korean\n3.Hindi\n4.Exit")
        Choice = int(input("Select An Option:"))
        if Choice == 1:
            Translate_Japanese()
        if Choice == 2:
            Translate_Korean()
        if Choice == 3:
            Translate_Hindi()
        if Choice == 4:
            confirmation = input("Are You Sure ? (yes/no):")
            if confirmation.lower() == "yes":
                break
def Fact_Lab():
    Fact_lib =[
    "Fact 1 : Though less common than earthquakes, the moon actually has moonquakes, too.",
    "Fact 2 : You actually lose a large percentage of your taste buds while on an airplane. This might explain a lot about those less-than-stellar in-flight meals, or why you find yourself craving the saltiest foods while in the sky.",
    "Fact 3 : Although it may sound counterintuitive, your small intestine is actually the largest (internal) organ in your body.",
    "Fact 4 : You probably know that snails are petty slow creatures, but did you know that they also take the longest naps? One nap can last up to three years!",
    "Fact 5 : You may be jealous of a bird's ability to fly, but it may soothe your envy to learn they can't live in space because they need gravity to swallow.",
    "Fact 6 : Bees can sting other bees — usually if they feel threatened or are protecting their territory. In other words, you're not the only one who's scared of getting stung.",
    "Fact 7 : Whether you've seen a tiger in real life or in a photo, you know that they have striped fur. But they actually have striped skin, as well.",
    "Fact 8 : If you're a cat lover, then you may be surprised by this interesting fact: Cats can't taste anything that's sweet. That's probably why they can't get enough of their favorite salty snack.",
    "Fact 9 : Most people know dolphins have incredible sonar abilities. But did you know they were studied as war tools during the Cold War? They really are as smart as people say they are.",
    "Fact 10 : Not only are sea lions totally adorable, but they're also very musical. They are the only animal that can clap to a beat.",
    "Fact 11 : Like humans, koalas actually have unique individual fingerprints. If you place a koala and human finger print side by side, they're actually pretty hard to differentiate. ",
    "Fact 12 : You may know that everyone's fingerprints are different, but did you know that the same is true of everyone's tongue print?",
    "Fact 13 : Your brain uses 10 watts of energy to think, but it can't feel pain. You know what they say: Mind over matter.",
    "Fact 14 : Brendan Fraser almost died while filming The Mummy (he passed out while filming a scene). Pretty scary, right?",
    "Fact 15 : In a group of 23 people, there is a 50% chance that two will share the same birthday.",
    "Fact 16 : Will Ferrell consumed so much sugar while filming Elf that he actually became physically ill. If you've seen the famous spaghetti scene, then you can probably understand why.",
    "Fact 17 : It may feel a lot longer in the moment, but the average person spends two weeks of their life sitting at traffic lights.",
    "Fact 18 : The Hollywood sign in Los Angeles once said Hollywoodland, but was changed in 1949",
    "Fact 19 : The most expensive film ever made was Pirates of the Caribbean: On Stranger Tides, which cost 378 million dollars to create. For reference, the average budget for a big studio movie is around $65 million.",
    "Fact 20 : If E.T. is one of your favorite movies of all time, then you'll be interested to know that someone squished their hands in jelly to make the sound effect for E.T. walking around"
    ]
    print(random.choice(Fact_lib))
def Questions():
    points = 0
    Ans1 = ["Neil A.","Alden Armstrong","Neil Armstrong","Neil Alden Armstrong"]
    Ans2 = ["sun","Sun","SUN"]
    Ans3 = ["Everest","Mt.Everest","Mount Everest"]
    Ans4 = ["moon","MOON","Moon"]
    Ans5 = ["Pluto","pluto","PLUTO"]
    Ans6 =["Homosapiens","HOMOSAPIENS","Homo Sapiens","Homo sapiens","Homo-sapiens","Homo-Sapiens","Homosapien","HOMOSAPIEN","Homo Sapien","Homo sapien","Homo-sapien","Homo-Sapien"]
    Ans7 =["Gravity","gravity","GRAVITY"]
    Ans8 =["mammals","MAMMALS","mammal","MAMMAL"]
    Ans9 =["Aryabhata","Aryabhatt","ARYABHATA","ARYABHATT","aryabhatt","aryabhata"]
    Ans10=["east","East","EAST"]
    while True :
        print("Who was the first man to step on moon ? \n")
        Answer = input("")
        if Answer in Ans1:
            print("CORRECT ANSWER!!!!")
            points +=1
        if Answer not in Ans1:
            print("INCORRECT ANSWER!!!!")
            pass
        while True:
            print("Name the largest star in our so1ar system  \n")
            Answer = input("")
            if Answer in Ans2:
                print("CORRECT ANSWER!!!!")
                points +=1
            if Answer not in Ans2:
                print("INCORRECT ANSWER!!!!")
                pass
            while True:
                print("What's The Highest Mountain Cliff ? \n")
                Answer = input("")
                if Answer in Ans3:
                    points +=1
                    print("CORRECT ANWSER!!!!")
                if Answer not in Ans3:
                    print("INCORRECT ANSWER!!!!")
                    pass
                while True:
                    print("What is the name of earth's the natural satellite ? \n")
                    Answer = input("")
                    if Answer in Ans4:
                        print("CORRECT ANWSER!!!!")
                        points +=1
                    if Answer not in Ans4:
                        print("INCORRECT ANSWER!!!!")
                        pass
                    while True :
                        print("Name The Dwarf Planet In Our Solar System  \n")
                        Answer = input("")
                        if Answer in Ans5 :
                            print("CORRECT ANWSER!!!!")
                            points += 1
                        if Answer not in Ans5 :
                            print("INCORRECT ANSWER!!!!")
                            pass
                        while True :
                            print("What is the scientific name of humans ? \n")
                            Answer = input("")
                            if Answer in Ans6:
                                print("CORRECT ANWSER!!!!")
                                points +=1
                            if Answer not in Ans6:
                                print("INCORRECT ANSWER!!!!")
                                pass
                            while True:
                                print("Name the force which pulls us to the ground \n")
                                Answer = input("")
                                if Answer in Ans7:
                                    print("CORRECT ANWSER!!!!")
                                    points +=1
                                if Answer not in Ans7:
                                    print("INCORRECT ANSWER!!!!")
                                    pass
                                while True:
                                    print("Name the type of animal that milkfeed their babies \n")
                                    Answer = input("")
                                    if Answer in Ans8:
                                        print("CORRECT ANWSER!!!!")
                                        points +=1
                                    if Answer not in Ans8:
                                        print("INCORRECT ANSWER!!!!")
                                        pass
                                    while True:
                                        print("Who disocvered zero ? \n")
                                        Answer = input("")
                                        if Answer in Ans9:
                                             print("CORRECT ANWSER!!!!")
                                             points += 1
                                        if Answer not in Ans9:
                                            print("INCORRECT ANSWER!!!!")
                                            pass
                                        print("From which direction does sun rise from ? \n")
                                        Answer = input("")
                                        if Answer in Ans10:
                                            print("CORRECT ANWSER!!!!")
                                            points += 1
                                        if Answer not in Ans10:
                                            print("INCORRECT ANSWER!!!!")
                                            pass
                                        Name = input("Enter Your First Name :")
                                        while points <=5:
                                            print("Congrats",Name,"You Scored",points,"points out of 10! Nice Try")
                                            return
                                        while points <= 8:
                                            print("Congrats",Name,"You Scored",points,"points out of 10! Great Job!")
                                            return
                                        while points <= 10:
                                            print("Congrats",Name,"You Scored",points,"points out of 10! Perfect!")
                                            return
                    
def Quiz():               
    while True:
        print("***General Know1edge Quiz*** \n1.Start Quiz \n2.Exit")
        Choice = input("Se1ect An Option :")
        if Choice == "2":
            break
        if Choice == "1":
            while True :
                print("***Ru1es*** \n1.This Quiz Has 10 questions \n2.you'll be rewarded 1 point for each correct answer \n3. There's no negative Marking \n4.points system: \n 1-5 points Nice Try \n 6-8 Great Job! \n 9-10 Perfect!!")
                Choice = input("Do you wish to continue (yes/no):")
                if Choice.lower()== "no":
                    break
                if Choice.lower()== "yes":
                    Questions()
                    break
        break
def most_frequently_used_function():
    most_common_function = Counter(function_usage).most_common(1)
    return most_common_function[0][0]
function_usage = {
    "Password Function": 0,
    "Stack Function": 0,
    "Calculator": 0,
    "Encryption": 0,
    "Turtle Graphic": 0,
    "File Function": 0,
    "Quiz" : 0,
    "Fun Fact" : 0,
    "Translator" : 0,
    "SQL" : 0
}
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
#Turtle graphic code
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
            print("The Generated Password Is:",password)
        elif choice == "2":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_letters + string.digits)
            print("The Generated Password Is:",password)
        elif choice == "3":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_letters)
            print("The Generated Password Is:",password)
        elif choice == "4":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_lowercase)
            print("The Generated Password Is:",password)
        elif choice == "5":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_uppercase)
            print("The Generated Password Is:",password)
        elif choice == "6":
            confirmation = input("Are you sure?\n")
            if confirmation.lower() == "yes":
                break
def main_menu():
    while True:
        print("***FUNCTION MENU***\n1. Password Function\n2. Stack Function\n3. Calculator\n4. Encryption\n5. Turtle Graphic\n6. File Function\n7. Quiz\n8. Fun Fact \n9. History  \n10. Translator \n11.SQL \n12. Exit")
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
            Quiz()
            function_usage["Quiz"] += 1
        elif Choice == "8":
            Fact_Lab()
            function_usage["Fun Fact"] += 1
        elif Choice == "9":
            print("Most frequently used function:", most_frequently_used_function())
        elif Choice == "10":
            Translation_Menu()
            function_usage["Translator"] += 1
        elif Choice == "11":
            SQL_MENU()
            function_usage["SQL"] += 1
        elif Choice == "12":
            confirmation = input("Are You Sure?\n")
            if confirmation.lower() == "yes":
                break
main_menu()
