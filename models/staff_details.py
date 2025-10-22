from utils import load_data, dump_data
import emoji
from rich import print
import re
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Staff:
    def __init__(self, user_path, user_auth_path, staff_path, staff_auth_path, rented_books_path, books_path):
        self.user_path = user_path
        self.user_auth_path = user_auth_path
        self.staff_path = staff_path
        self.staff_auth_path = staff_auth_path
        self.rented_books_path = rented_books_path
        self.books_path = books_path

        self.books = load_data(self.books_path)
        self.users = load_data(self.user_path)
        self.user_authentication = load_data(self.user_auth_path)
        self.staff = load_data(self.staff_path)
        self.staff_authentication = load_data(self.staff_auth_path)
        self.rented_books = load_data(self.rented_books_path)
    
    def add_staff(self,name,email,phone,role,password,username):
        if self.staff:
            last_id = max(int(s['id'][3:]) for s in self.staff)
            staff_id = f"STF{str(last_id+1).zfill(3)}"
        else:
            staff_id = "STF001"
        self.staff.append({
            "id": staff_id,
            "name": name,
            "email": email,
            "phone": phone,
            "role": role
        })
        self.staff_authentication.append({
            "id":staff_id,
            "username":username,
            "password":password
        })
        dump_data(self.staff_auth_path,self.staff_authentication)
        dump_data(self.staff_path, self.staff)
        print(f"[bold green]Staff member {name} added successfully![/bold green]")
    
    def delete_staff(self,id):
        if not any(s['id'] == id for s in self.staff):
            print(f"[bold red]No staff found with ID {id}[/bold red]")
            return
        self.staff = [s for s in self.staff if s["id"] != id]
        self.staff_authentication = [a for a in self.staff_authentication if a["id"] != id]

        dump_data(self.staff_path, self.staff)
        dump_data(self.staff_auth_path, self.staff_authentication)
        print(f"[bold green]Staff with ID {id} deleted successfully![/bold green]")
    
    def delete_users(self,id):
        if not any(u['id'] == id for u in self.users):
            print(f"[bold red]No user found with ID {id}[/bold red]")
            return
        self.users = [u for u in self.users if u['id'] != id]
        self.user_authentication = [a for a in self.user_authentication if a['id'] != id]

        dump_data(self.user_path,self.users)
        dump_data(self.user_auth_path,self.user_authentication)
        print(f"[bold green]User with ID {id} deleted successfully![/bold green]")

    def modify_staff_details(self, id):
        staff_member = next((s for s in self.staff if s['id'] == id), None)
        if not staff_member:
            print(f"[bold red]Staff ID {id} not found![/bold red]")
            return

        while True:
            print("\n[bold cyan]Modify Staff Details[/bold cyan]")
            print("1. Name")
            print("2. Email")
            print("3. Phone")
            print("4. Role")
            print("0. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                name = input("Enter new name: ").strip()
                if name:
                    staff_member['name'] = name
                    print("[bold green]Name updated successfully![/bold green]")
                else:
                    print("[bold red]Invalid name![/bold red]")

            elif choice == "2":
                email = input("Enter new email: ").strip()
                if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
                    staff_member['email'] = email
                    print("[bold green]Email updated successfully![/bold green]")
                else:
                    print("[bold red]Invalid email format![/bold red]")

            elif choice == "3":
                phone = input("Enter new phone number: ").strip()
                if re.fullmatch(r"[6-9]\d{9}", phone):
                    staff_member['phone'] = phone
                    print("[bold green]Phone updated successfully![/bold green]")
                else:
                    print("[bold red]Invalid phone number! Must be 10 digits.[/bold red]")

            elif choice == "4":
                role = input("Enter new role: ").strip()
                if role:
                    staff_member['role'] = role
                    print("[bold green]Role updated successfully![/bold green]")
                else:
                    print("[bold red]Invalid role![/bold red]")

            elif choice == "0":
                print("[bold yellow]Exiting staff modification...[/bold yellow]")
                break

            else:
                print("[bold red]Invalid choice! Please enter a valid option.[/bold red]")

            # Save changes after every update
            dump_data(self.staff_path, self.staff)

    def update_staff_auth(self, id):
        auth_member = next((a for a in self.staff_authentication if a['id'] == id), None)
        if not auth_member:
            print(f"[bold red]Authentication info not found for Staff ID {id}[/bold red]")
            return

        while True:
            print("\n[bold cyan]Update Username / Password[/bold cyan]")
            print("1. Username")
            print("2. Password")
            print("0. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                username = input("Enter new username: ").strip()
                if username:
                    auth_member['username'] = username
                    dump_data(self.staff_auth_path, self.staff_authentication)
                    print("[bold green]Username updated successfully![/bold green]")
                else:
                    print("[bold red]Invalid username![/bold red]")

            elif choice == "2":
                while True:
                    print("Password must contain at least 4 chars, uppercase, lowercase, and a special character")
                    password = input("Enter new password: ").strip()
                    if re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{4,}", password):
                        auth_member['password'] = password
                        dump_data(self.staff_auth_path, self.staff_authentication)
                        print("[bold green]Password updated successfully![/bold green]")
                        break
                    else:
                        print("[bold red]Password does not meet criteria[/bold red]")

            elif choice == "0":
                print("[bold yellow]Exiting authentication update...[/bold yellow]")
                break

            else:
                print("[bold red]Invalid choice! Please enter a valid option.[/bold red]")
    
    def add_books(self,title, author, publisher, language, copies):
        id = f"{str((len(self.books)+1).zfill(3))}"
        self.books.append({
            "id":id,
            "title":title,
            "author":author,
            "publisher":publisher,
            "language":language,
            "copies":copies
        })
        dump_data(self.books_path,self.books)

    def filter_emails(self):
        email_list=[]
        for rent_entry in self.rented_books:
            user_id = rent_entry['user_id']
            user = next((u for u in self.users if u['id']==user_id),None)
            if not user:
                continue
            user_email = user['email']
            for book in rent_entry['books_rented']:
                email_list.append({
                    "email":user_email,
                    "due_date":book['due_date'],
                    "book_name":book['title']
                })
        return email_list
    
    def send_due_emails(self):
        email_list = self.filter_emails()
        sender_email = "praveenkumarre23@gmail.com"
        sender_password = "@password@123"

        for entry in email_list:
            recipient = entry['email']
            book_name = entry['title']
            due_date = entry['due_date']

            subject = f"Remainder:  sumbit \"{book_name}\" by \"{due_date}\" "
            body = (
                f"Dear Library Member,\n\n"
                f"This is a reminder to return the book '{book_name}' "
                f"by {due_date} to avoid late fees.\n\n"
                f"Thank you,\nYour Library Team"
            )

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['Subject'] = subject
            msg['To'] = recipient
            msg.attach(MIMEText(body,"plain"))

            try:
                with smtplib.SMTP("smtp.gmail.com",587) as server:
                    server.starttls()
                    server.login(sender_email,sender_password)
                    server.send_message(msg)
                    print(f"✅ Email sent to {recipient}")
            except Exception as e:
                print(f"❌ Failed to send email to {recipient}: {e}")