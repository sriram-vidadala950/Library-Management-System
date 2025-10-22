from models.library import Library
from models.staff_details import Staff
from models.user_details import Users
from utils import load_data, dump_data
import os, json, re
from rich import print

# ------------------ Paths ------------------
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

USER_DETAILS_JSON = os.path.join(DATA_DIR, "user_details.json")
USER_AUTHENTICATION_JSON = os.path.join(DATA_DIR, "user_auth.json")
USER_RENTED_BOOKS_JSON = os.path.join(DATA_DIR, "user_rented_books.json")
STAFF_DETAILS_JSON = os.path.join(DATA_DIR, "staff_details.json")
STAFF_AUTHENTICATION_JSON = os.path.join(DATA_DIR, "staff_auth.json")
LIBRARY_BOOKS_DETAILS_JSON = os.path.join(DATA_DIR, "library_details.json")

# ------------------ Objects ------------------
library = Library(USER_DETAILS_JSON, STAFF_DETAILS_JSON, LIBRARY_BOOKS_DETAILS_JSON)
staff_obj = Staff(USER_DETAILS_JSON, USER_AUTHENTICATION_JSON, STAFF_DETAILS_JSON, STAFF_AUTHENTICATION_JSON, USER_RENTED_BOOKS_JSON, LIBRARY_BOOKS_DETAILS_JSON)
users = Users(USER_DETAILS_JSON, USER_AUTHENTICATION_JSON, LIBRARY_BOOKS_DETAILS_JSON, USER_RENTED_BOOKS_JSON)

# ------------------ Load JSON ------------------
with open(USER_AUTHENTICATION_JSON, "r") as f:
    user_authentication = json.load(f)
with open(USER_DETAILS_JSON, "r") as f:
    user_details = json.load(f)
with open(STAFF_AUTHENTICATION_JSON, "r") as f:
    staff_authentication = json.load(f)
with open(STAFF_DETAILS_JSON, "r") as f:
    staff_details = json.load(f)

# ------------------ User Portal ------------------
def UserDetails(user_id, name):
    print(f"Welcome {name}")
    while True:
        print("==== USER MENU ====")
        print("0. Exit")
        print("1. Update Credentials")
        print("2. Update User Details")
        print("3. Rent a Book")
        print("4. Return a Book")
        print("5. Library Books details")
        print("6. Staff details")
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Exiting User portal...")
            break
        elif choice == "1":
            users.update_password_username(user_id)
        elif choice == "2":
            users.modify_user_details(user_id)
        elif choice == "3":
            while True:
                book_id = input("Enter book ID (B00XXX): ").strip()
                if book_id.startswith("B00"):
                    users.rent_book(user_id, book_id)
                    break
                else:
                    print("Book ID must start with 'B00'")
        elif choice == "4":
            while True:
                book_id = input("Enter book ID (B00XXX): ").strip()
                if book_id.startswith("B00"):
                    users.return_book(user_id, book_id)
                    break
                else:
                    print("Book ID must start with 'B00'")
        elif choice =='5':
            library.library_staff_details()
        elif choice =='6':
            library.library_staff_details()
        else:
            print("Choose proper features")

# ------------------ Staff Portal ------------------
def StaffDetails(staff_obj, staff_id, staff_name):
    print(f"Welcome Mr. {staff_name}!")
    while True:
        print("\n==== STAFF MENU ====")
        print("0. Exit")
        print("1. Add Users")
        print("2. Add Staff")
        print("3. Delete Staff")
        print("4. Delete Users")
        print("5. Add Books")
        print("6. Update Staff Credentials")
        print("7. Update Staff Details")
        print("8. Filter Pending Books Emails")
        print("9. Send Due Email")
        print("10. Library Books Details")
        print("11. Library Staff Details")
        print("12. Library Users Details")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("[bold yellow]Exiting Staff Portal...[/bold yellow]")
            break

        elif choice == "1":  # Add Users
            # Validation
            while True:
                name = input("Enter user name (First Last): ").strip()
                if not name or len(name.split()) < 2:
                    print("[bold red]Please enter full name (first and last)![/bold red]")
                else:
                    break
            while True:
                age = input("Enter user age: ").strip()
                if not age.isdigit() or int(age) <= 0:
                    print("[bold red]Invalid age[/bold red]")
                else:
                    break
            while True:
                gender = input("Enter gender (Male/Female/Other): ").strip().capitalize()
                if gender not in ["Male", "Female", "Other"]:
                    print("[bold red]Invalid gender[/bold red]")
                else:
                    break
            while True:
                contact = input("Enter contact number: ").strip()
                if not re.fullmatch(r"[6-9]\d{9}", contact):
                    print("[bold red]Invalid contact[/bold red]")
                else:
                    break
            while True:
                address = input("Enter address: ").strip()
                if not address:
                    print("[bold red]Address cannot be empty[/bold red]")
                else:
                    break
            while True:
                membership = input("Enter membership type (Basic/Premium): ").strip().capitalize()
                if membership not in ["Basic", "Premium"]:
                    print("[bold red]Invalid membership type[/bold red]")
                else:
                    break
            while True:
                email = input("Enter email: ").strip()
                if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
                    print("[bold red]Invalid email[/bold red]")
                else:
                    break

            # Auto generate username/password
            first_name, last_name = name.split()[0], name.split()[1]
            username = f"{first_name.lower()}.{last_name[0].lower()}"
            password = f"{first_name.capitalize()}@123"

            users.add_user(name, int(age), gender, contact, address, membership, email, username, password)
            print(f"[bold green]User '{name}' added successfully![/bold green]")
            print(f"[bold cyan]Initial username: {username}, password: {password}[/bold cyan]")

        elif choice == "2":  # Add Staff
            while True:
                if not name or len(name.split()) < 2:
                    name = input("Enter staff name (First Last): ").strip()
                    print("[bold red]Please enter full name[/bold red]")
                else:
                    break
            while True:
                email = input("Enter email: ").strip()
                if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
                    print("[bold red]Invalid email[/bold red]")
                else:
                    break
            while True:
                phone = input("Enter phone: ").strip()
                if not re.fullmatch(r"[6-9]\d{9}", phone):
                    print("[bold red]Invalid phone[/bold red]")
                else:
                    break
            while True:
                role = input("Enter role: ").strip()
                if not role:
                    print("[bold red]Role cannot be empty[/bold red]")
                else:
                    break

            first_name, last_name = name.split()[0], name.split()[1]
            username = f"{first_name.lower()}.{last_name[0].lower()}"
            password = f"{first_name.capitalize()}@123"

            staff_obj.add_staff(name, email, phone, role, password, username)
            print(f"[bold green]Staff '{name}' added successfully![/bold green]")
            print(f"[bold cyan]Initial username: {username}, password: {password}[/bold cyan]")

        elif choice == "3":
            del_id = input("Enter staff ID (STFXXX): ").strip().upper()
            if not re.fullmatch(r"STF\d{3}", del_id):
                print("[bold red]Invalid staff ID[/bold red]")
                continue
            staff_obj.delete_staff(del_id)

        elif choice == "4":
            del_id = input("Enter user ID (USRXXX): ").strip().upper()
            if not re.fullmatch(r"USR\d{3}", del_id):
                print("[bold red]Invalid user ID[/bold red]")
                continue
            staff_obj.delete_users(del_id)

        elif choice == "5":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            publisher = input("Enter publisher: ").strip()
            language = input("Enter language: ").strip()
            copies = input("Enter number of copies: ").strip()

            if not title or not author or not publisher or not language:
                print("[bold red]All fields required[/bold red]")
                continue
            if not copies.isdigit() or int(copies) <= 0:
                print("[bold red]Copies must be positive[/bold red]")
                continue

            staff_obj.add_books(title, author, publisher, language, int(copies))
            print(f"[bold green]Book '{title}' added successfully[/bold green]")

        elif choice == "6":
            staff_obj.update_staff_auth(staff_id)
        elif choice == "7":
            staff_obj.modify_staff_details(staff_id)
        elif choice == "8":
            emails = staff_obj.filter_emails()
            if not emails:
                print("[bold yellow]No pending books[/bold yellow]")
            else:
                for e in emails:
                    print(f"{e['email']} | Book: {e['book_name']} | Due: {e['due_date']}")
        elif choice == "9":
            staff_obj.send_due_emails()
        elif choice =="10":
            library.library_books_details()
        elif choice =="11":
            library.library_staff_details()
        elif choice == "12":
            library.library_user_details()
        else:
            print("[bold red]Invalid choice[/bold red]")

# ------------------ Login ------------------
def Login():
    userId = input("Enter your user ID: ").strip().upper()
    password = input("Enter your password: ").strip()

    if userId.startswith("USR"):
        for user in user_authentication:
            if user['id'] == userId:
                name = next((u['name'] for u in user_details if u['id'] == userId), None)
                UserDetails(userId, name)
                break
        else:
            print("User ID does not exist")

    elif userId.startswith("STF"):
        for s in staff_authentication:
            if s['id'] == userId:
                name = next((s_['name'] for s_ in staff_details if s_['id'] == userId), None)
                StaffDetails(staff_obj, userId, name)
                break
        else:
            print("Staff ID does not exist")
    else:
        print("Invalid ID format")

# ------------------ Create Account ------------------
def create_account():
    while True:
        name = input("Enter user name (First Last): ").strip()
        if not name or len(name.split()) < 2:
            print("[bold red]Please enter full name (first and last)![/bold red]")
        else:
            break
    while True:
        age = input("Enter user age: ").strip()
        if not age.isdigit() or int(age) <= 0:
            print("[bold red]Invalid age[/bold red]")
        else:
            break
    while True:
        gender = input("Enter gender (Male/Female/Other): ").strip().capitalize()
        if gender not in ["Male", "Female", "Other"]:
            print("[bold red]Invalid gender[/bold red]")
        else:
            break
    while True:
        contact = input("Enter contact number: ").strip()
        if not re.fullmatch(r"[6-9]\d{9}", contact):
            print("[bold red]Invalid contact[/bold red]")
        else:
            break
    while True:
        address = input("Enter address: ").strip()
        if not address:
            print("[bold red]Address cannot be empty[/bold red]")
        else:
            break
    while True:
        membership = input("Enter membership type (Basic/Premium): ").strip().capitalize()
        if membership not in ["Basic", "Premium"]:
            print("[bold red]Invalid membership type[/bold red]")
        else:
            break
    while True:
        email = input("Enter email: ").strip()
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            print("[bold red]Invalid email[/bold red]")
        else:
            break

        # All inputs are valid, generate username/password
        first_name, last_name = name.split()[0], name.split()[1]
        username = f"{first_name.lower()}.{last_name[0].lower()}"
        password = f"{first_name.capitalize()}@123"

        users.add_user(name, int(age), gender, contact, address, membership, email, username, password)
        print(f"[bold green]User '{name}' created successfully![/bold green]")
        print(f"[bold cyan]Initial username: {username}, password: {password}[/bold cyan]")

        users.add_user(name,age,gender,contact,membership,email,username,password)  # Exit loop after successful creation

    # After creation, proceed to login
    Login()


# ------------------ Main Loop ------------------
print("Welcome to Saraswathi Library!!")
while True:
    print("0. Logout")
    print("1. Login")
    print("2. Create an Account")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        Login()
    elif choice == "2":
        create_account()
    elif choice == "0":
        print("Logging out...")
        break
    else:
        print("Invalid choice")
