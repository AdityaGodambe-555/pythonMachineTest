import os

def add_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")

    with open('users.csv', mode='a', encoding='utf-8') as file:

        if file.tell() == 0:  
            file.write("Name,Email,Phone Number\n") 

        file.write(f"{name},{email},{phone}\n")

    print("User added successfully!")

def display_users():
    if os.path.isfile('users.csv'):
        with open('users.csv', mode='r', encoding='utf-8') as file:
            print("\nUsers:")
            print(f"{'Name':<20} {'Email':<30} {'Phone Number':<15}")  
            print('-' * 65) 
            for line in file:
                name, email, phone = line.strip().split(',')
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