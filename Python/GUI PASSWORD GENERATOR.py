import tkinter as tf
from tkinter import *
from tkinter import messagebox, simpledialog
import string
import random
from Crypto.Util.Padding import pad, unpad
def DECRYPTION():
    def Ask_Data():
        root = tf.Tk()
        root.withdraw()
        message = simpledialog.askstring("Enter the message to decrypt", "Enter the message to decrypt: ")
        root.destroy()
        return message

    def Ask_Key():
        root = tf.Tk()
        root.withdraw()
        key = simpledialog.askinteger("Enter the key", "Enter the key: ")
        root.destroy()
        return key

    encrypted_message = Ask_Data()
    if encrypted_message is None:
        return "No message entered."

    key = Ask_Key()
    if key is None:
        return "No key entered."

    decrypted_message = ""
    key_index = 0
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - key)  
        key_index = (key_index + 1) % len(str(key))
    return decrypted_message
def ENCRYPTION():
    def Ask_Data():
        root = tf.Tk()
        root.withdraw()
        message = simpledialog.askstring("Enter the message to encrypt", "Enter the message to encrypt: ")
        root.destroy()
        return message

    def Ask_Key():
        root = tf.Tk()
        root.withdraw()
        key = simpledialog.askinteger("Enter the key", "Enter the key: ")
        root.destroy()
        return key

    message = Ask_Data()
    if message is None:
        return "No message entered."

    key = Ask_Key()
    if key is None:
        return "No key entered."

    encrypted_message = ""
    key_index = 0

    for char in message:
        encrypted_message += chr(ord(char) + key)  
        key_index = (key_index + 1) % len(str(key))

    return encrypted_message
def cryotograohy_menu():
    menu_popup = Toplevel(root)
    menu_popup.title("CrytoGraphy Menu")
    cryptography_options = "**CrytoGraphy Menu** \n1.Encryption \n2.Decryption\n3.Exit"
    menu_lable = Label(menu_popup,text=cryptography_options , justify='left' )
    menu_lable.pack()
    user_input = Entry(menu_popup)
    user_input.pack()
    def cryptography_manger():
        choice = user_input.get()
        if choice == '1':
            result = ENCRYPTION()
            messagebox.showinfo("Encypted data", result)
        if choice == '2':
            result = DECRYPTION()
            messagebox.showinfo("Decypted data", result)
        if choice == '3':
            root.destroy()
    execute_button = Button(menu_popup, text="Execute", command=cryptography_manger)
    execute_button.pack()
def password_generator_Aplhabetical_Upper():
    root = tf.Tk()
    root.withdraw()  
    choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

    if choice is not None:
        characters = string.ascii_uppercase
        result = ''.join(random.choice(characters) for _ in range(choice))
        return result
    else:
        return None
def password_generator_Aplhabetical_Lower():
    root = tf.Tk()
    root.withdraw()  
    choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

    if choice is not None:
        characters = string.ascii_lowercase
        result = ''.join(random.choice(characters) for _ in range(choice))
        return result
    else:
        return None
def password_generator_Aplhabetical():
    root = tf.Tk()
    root.withdraw()  
    choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

    if choice is not None:
        characters = string.ascii_letters
        result = ''.join(random.choice(characters) for _ in range(choice))
        return result
    else:
        return None
def password_generator_Aplhanumeric():
    root = tf.Tk()
    root.withdraw()  
    choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

    if choice is not None:
        characters = string.digits +  string.ascii_letters
        result = ''.join(random.choice(characters) for _ in range(choice))
        return result
    else:
        return None
def password_generator_pincode():
    root = tf.Tk()
    root.withdraw()  
    choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

    if choice is not None:
        characters = string.digits  
        result = ''.join(random.choice(characters) for _ in range(choice))
        return result
    else:
        return None
def password_menu():
    menu_popup = Toplevel(root)
    menu_popup.title("Password Menu")
    password_options = "**PASSWORD_MENU**\n1. Pincode\n2. Alphanumeric\n3. Alphabetically\n4. Lowercase\n5. Uppercase\n6. EXIT"
    menu_label = Label(menu_popup, text=password_options, justify='left')
    menu_label.pack()

    user_input = Entry(menu_popup)
    user_input.pack()

    def handle_password_choice():
        choice = user_input.get()
        if choice == '1':
            generated_password = password_generator_pincode()
            messagebox.showinfo("Generated Password", generated_password)
        if choice == '2':
            generated_password = password_generator_Aplhanumeric()
            messagebox.showinfo("Generated Password", generated_password)
        if choice == '3':
            generated_password = password_generator_Aplhabetical()
            messagebox.showinfo("Generated Password", generated_password)
        if choice == '4':
            generated_password = password_generator_Aplhabetical_Lower()
            messagebox.showinfo("Generated Password", generated_password)
        if choice == '5':
            generated_password = password_generator_Aplhabetical_Upper()
            messagebox.showinfo("Generated Password", generated_password)
        elif choice == '6':
            menu_popup.destroy()  

    execute_button = Button(menu_popup, text="Execute", command=handle_password_choice)
    execute_button.pack()
root = tf.Tk()
root.title("MENU")
root.geometry('280x280')
entry = Entry(root)
entry.pack()
LP = Listbox(root)
LP.insert(1, " 1. Password Generator")
LP.insert(2,"2. Cryptography")
LP.insert(2,"3. Exit")
LP.place(x='0', y='10')
entry.place(x='1', y='176')
def user_input_handler():
    user_input = entry.get()
    if user_input == '1':
        password_menu()
    if user_input == '2':
        cryotograohy_menu()
    if user_input == '3':
        root.destroy()
execute_button = Button(root, text="Execute", command=user_input_handler)
execute_button.place(x=120, y=176)

root.mainloop()
