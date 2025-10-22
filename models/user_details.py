from utils import dump_data, load_data
import emoji
from rich import print
import re
from datetime import datetime, timedelta

class Users:
    def __init__(self, user_path, auth_path,books_path,rent_books):
        self.user_path = user_path
        self.auth_path = auth_path
        self.books_path = books_path
        self.rent_books = rent_books

        self.rented_books = load_data(self.rent_books)
        self.books = load_data(self.books_path)
        self.users = load_data(self.user_path)
        self.auth_data = load_data(self.auth_path)
    
    def display_users(self):
        if not self.users:
            print("[bold red]No users found[/bold red]")
            return
        print("[bold green]Library Users:[/bold green]")
        print("=" * 40)
        for user in self.users:
            print(f"ID: {user['id']} | Name: {user['name']} ")
            print(f"Age: {user['age']} | Gender: {user['gender']}")
            print(f"Contact: {user['contact']} | Email: {user['email']}")
            print(f"Address: {user['address']} | Membership: {user['membership_type']}")
            print("-" * 40)
    
    def add_user(self, name, age, gender, contact, address, membership_type, email, username, password):
        user_id = f"USR{str(len(self.users)+1).zfill(3)}"
        
        self.users.append({
            "id": user_id,
            "name": name,
            "age": age,
            "gender": gender,
            "contact": contact,
            "email": email,
            "address": address,
            "membership_type": membership_type
        })
        
        self.auth_data.append({
            "id": user_id,
            "username": username,
            "password": password
        })
        
        dump_data(self.user_path, self.users)
        dump_data(self.auth_path, self.auth_data)

        print(f"[bold green]User {name} added successfully![/bold green]")
    
    def update_password_username(self, id):
        for user in self.auth_data:
            if user["id"] == id:
                while True:
                    print("1. Username")
                    print("2. Password")
                    print("0. Exit")
                    choice = input("Enter your choice: ").strip()
                    
                    if choice == "1":
                        username = input("Enter your username: ").strip()
                        if username:
                            user['username'] = username
                            dump_data(self.auth_path, self.auth_data)
                            print(f"[bold green]Username updated successfully![/bold green]")
                        else:
                            print("[bold red]Invalid username![/bold red]")

                    elif choice == "2":
                        while True:
                            print("Your password should contain at least 4 characters, uppercase, lowercase, and a special character")
                            password = input("Enter your password: ").strip()
                            if re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{4,}", password):
                                user['password'] = password
                                dump_data(self.auth_path, self.auth_data)
                                print(f"[bold green]Password updated successfully![/bold green]")
                                break
                            else:
                                print("[bold red]Password must meet the criteria[/bold red]")

                    elif choice == "0":
                        print("[bold yellow]Exiting username/password update...[/bold yellow]")
                        break
                    else:
                        print("[bold red]Enter a valid choice![/bold red]")
                break
        else:
            print("[bold red]User ID not found[/bold red]")

    def modify_user_details(self, id):
        for user in self.users:
            if user['id'] == id:
                while True:
                    print("\n[bold cyan]Modify User Details[/bold cyan]")
                    print("1. Name")
                    print("2. Age")
                    print("3. Gender")
                    print("4. Contact")
                    print("5. Email")
                    print("6. Address")
                    print("7. Membership Type")
                    print("0. Exit")
                    choice = input("Enter your choice: ").strip()

                    if choice == "1":
                        name = input("Enter new name: ").strip()
                        if name:
                            user['name'] = name
                            print("[bold green]Name updated successfully![/bold green]")
                        else:
                            print("[bold red]Invalid name![/bold red]")

                    elif choice == "2":
                        try:
                            age = int(input("Enter new age: ").strip())
                            if age > 0:
                                user['age'] = age
                                print("[bold green]Age updated successfully![/bold green]")
                            else:
                                print("[bold red]Age must be positive![/bold red]")
                        except ValueError:
                            print("[bold red]Invalid input! Enter a valid number.[/bold red]")

                    elif choice == "3":
                        gender = input("Enter new gender (Male/Female/Other): ").strip().capitalize()
                        if gender in ["Male", "Female", "Other"]:
                            user['gender'] = gender
                            print("[bold green]Gender updated successfully![/bold green]")
                        else:
                            print("[bold red]Invalid gender![/bold red]")

                    elif choice == "4":
                        contact = input("Enter new contact number: ").strip()
                        if re.fullmatch(r"[6-9]\d{9}", contact):
                            user['contact'] = contact
                            print("[bold green]Contact updated successfully![/bold green]")
                        else:
                            print("[bold red]Invalid contact number! Must be 10 digits.[/bold red]")

                    elif choice == "5":
                        email = input("Enter new email: ").strip()
                        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
                            user['email'] = email
                            print("[bold green]Email updated successfully![/bold green]")
                        else:
                            print("[bold red]Invalid email format![/bold red]")

                    elif choice == "6":
                        address = input("Enter new address: ").strip()
                        if address:
                            user['address'] = address
                            print("[bold green]Address updated successfully![/bold green]")
                        else:
                            print("[bold red]Address cannot be empty![/bold red]")

                    elif choice == "7":
                        membership = input("Enter new membership type (Basic/Premium): ").strip().capitalize()
                        if membership in ["Basic", "Premium"]:
                            user['membership_type'] = membership
                            print("[bold green]Membership type updated successfully![/bold green]")
                        else:
                            print("[bold red]Invalid membership type![/bold red]")

                    elif choice == "0":
                        print("[bold yellow]Exiting user modification...[/bold yellow]")
                        break

                    else:
                        print("[bold red]Invalid choice! Please enter a valid option.[/bold red]")

                    dump_data(self.user_path, self.users)
                break
        else:
            print("[bold red]User ID not found![/bold red]")

    def rent_book(self, user_id, book_id):
        # Check user
        user = next((u for u in self.users if u['id'] == user_id), None)
        if not user:
            print(f"[bold red]User ID {user_id} not found[/bold red]")
            return

        # Check book
        book = next((b for b in self.books if b['id'] == book_id), None)
        if not book:
            print(f"[bold red]Book ID {book_id} not found[/bold red]")
            return
        
        # Reduce count of books & books copies check
        for book in self.books:
            if book['id'] == book_id:
                if book['copies']>0:
                    book['copies']-=1
                else:
                    print(f"[bold red]Book '{book['title']}' is not available[/bold red]")
                    return
        # Find or create user's rent entry
        user_rent_entry = next((r for r in self.rented_books if r['user_id'] == user_id), None)
        if not user_rent_entry:
            user_rent_entry = {"user_id": user_id, "books_rented": []}
            self.rented_books.append(user_rent_entry)

        # Normalize returned key for all existing books
        for b in user_rent_entry['books_rented']:
            if "returned" not in b:
                b["returned"] = False

        # Check if the user already rented this book and not returned it
        already_rented = any(
            b["book_id"] == book_id and not b["returned"]
            for b in user_rent_entry['books_rented']
        )

        if already_rented:
            print(f"[bold yellow]Warning: {user['name']} has already rented '{book['title']}' and has not returned it yet.[/bold yellow]")
            return

        # Membership-based book limit
        max_books = 5 if user.get("membership_type", "Regular") == "Premium" else 2
        active_books = sum(1 for b in user_rent_entry['books_rented'] if not b["returned"])
        if active_books >= max_books:
            print(f"[bold red]User {user['name']} has reached the maximum allowed rented books ({max_books}).[/bold red]")
            return

        # Issue and due dates
        issue_date = datetime.today().strftime("%Y-%m-%d")
        return_date = (datetime.today() + timedelta(days=2)).strftime("%Y-%m-%d")

        # Add to user's rented books
        user_rent_entry['books_rented'].append({
            "book_id": book['id'],
            "title": book['title'],
            "author": book['author'],
            "language": book['language'],
            "issue_date": issue_date,
            "due_date": return_date,
            "returned": False
        })

        # Save updated rent data
        dump_data(self.rent_books, self.rented_books)
        dump_data(self.books_path,self.books)

        # Success message
        print(f"[bold green]{user['name']} rented '{book['title']}' successfully![/bold green]")
        print(f"Return by: [bold]{return_date}[/bold]")
    
    def return_book(self, user_id, book_id):
        # Find the user in rented_books
        user_rent_entry = next((r for r in self.rented_books if r['user_id'] == user_id), None)
        if not user_rent_entry:
            print(f"[bold red]User ID {user_id} not found in rented books[/bold red]")
            return

        # Find the book in user's rented books
        book_entry = next((b for b in user_rent_entry['books_rented'] if b['book_id'] == book_id), None)
        if not book_entry:
            print(f"[bold red]Book ID {book_id} not found for user {user_id}[/bold red]")
            return

        #update book count
        for book in self.books:
            if book['id'] == book_id:
                book['copies']+=1

        # Remove the book from rented_books
        user_rent_entry['books_rented'].remove(book_entry)
        print(f"[bold green]Book '{book_entry['title']}' returned successfully by user {user_id}![/bold green]")

        # If user has no more rented books, remove the user entry
        if not user_rent_entry['books_rented']:
            self.rented_books.remove(user_rent_entry)

        # Save changes
        dump_data(self.rent_books, self.rented_books)
        dump_data(self.books_path,self.books)