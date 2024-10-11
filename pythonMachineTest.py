import os
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")

    while not is_valid_email(email):
        print("Invalid email format. Please try again.")
        email = input("Enter Email: ")

    phone = input("Enter Phone Number (10 digits): ")

    while not is_valid_phone(phone):
        print("Invalid phone number. It must be 10 digits. Please try again.")
        phone = input("Enter Phone Number (10 digits): ")

    with open('users.csv', mode='a', encoding='utf-8') as file:
        if file.tell() == 0:  
            file.write("Name,Email,Phone Number\n") 

        file.write(f"{name},{email},{phone}\n")

    print("User added successfully!")

def display_users():
    if os.path.isfile('users.csv'):
        with open('users.csv', mode='r', encoding='utf-8') as file:
            print("\nUsers Data:")
            header = file.readline()  # Read the header line
            print(f"{'Name':<20} {'Email':<30} {'Phone Number':<15}")  
            print('-' * 65) 
            for line in file:
                line = line.strip()
                if line:  # Check if the line is not empty
                    name, email, phone = line.split(',')
                    print(f"{name:<20} {email:<30} {phone:<15}")  
    else:
        print("No users found.")

def main():
    while True:
        print("\nMake a choice to proceed:\n")
        print("Press '1' to Add User")
        print("Press '2' to Display Users")
        print("Press '3' to Exit")
        
        choice = input("\nPress any above key to continue:")

        if choice == '1':
            add_user()
        elif choice == '2':
            display_users()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

main()