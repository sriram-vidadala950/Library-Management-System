import re
import emoji
from rich import print
class Library:
    def __init__(self):
        self.library_books = {
        "10001": {"title": "A Tale of Two Cities", "author": "Charles Dickens", "available": True, "copies": 5},
        "10002": {"title": "Brave New World", "author": "Aldous Huxley", "available": True, "copies": 3},
        "10003": {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "available": True, "copies": 4},
        "10004": {"title": "Dune", "author": "Frank Herbert", "available": True, "copies": 6},
        "10005": {"title": "Emma", "author": "Jane Austen", "available": True, "copies": 2},
        "10006": {"title": "Frankenstein", "author": "Mary Shelley", "available": True, "copies": 5},
        "10007": {"title": "Great Expectations", "author": "Charles Dickens", "available": True, "copies": 3},
        "10008": {"title": "Hamlet", "author": "William Shakespeare", "available": True, "copies": 7},
        "10009": {"title": "Invisible Man", "author": "Ralph Ellison", "available": True, "copies": 4},
        "10010": {"title": "Jane Eyre", "author": "Charlotte Brontë", "available": True, "copies": 6}
    }

        self.library_staff = [
                    {"id": "L001", "name": "Amit Sharma", "role": "Librarian", "phone": "+91-98765-43210", "email": "amit.sharma@saraswathililb.com"},
                    {"id": "L002", "name": "Priya Verma", "role": "Assistant Librarian", "phone": "+91-87654-32109", "email": "priya.verma@saraswathililb.com"},
                    {"id": "L003", "name": "Rajesh Kumar", "role": "Catalog Manager", "phone": "+91-76543-21098", "email": "rajesh.kumar@saraswathililb.com"},
                    {"id": "L004", "name": "Neha Singh", "role": "IT Support", "phone": "+91-65432-10987", "email": "neha.singh@saraswathililb.com"},
                    {"id": "L005", "name": "Vikram Reddy", "role": "Front Desk Assistant", "phone": "+91-54321-09876", "email": "vikram.reddy@saraswathilib.com"}
                ] 

        self.library_members = [
                    {"Member ID": 101, "Name": "Aarav Sharma", "Age": 25, "Gender": "Male", "Contact": "9876543210", "Address": "Delhi", "Membership Type": "Regular"},
                    {"Member ID": 102, "Name": "Priya Verma", "Age": 30, "Gender": "Female", "Contact": "9876543211", "Address": "Mumbai", "Membership Type": "Premium"},
                    {"Member ID": 103, "Name": "Rahul Iyer", "Age": 22, "Gender": "Male", "Contact": "9876543212", "Address": "Chennai", "Membership Type": "Regular"},
                    {"Member ID": 104, "Name": "Neha Gupta", "Age": 28, "Gender": "Female", "Contact": "9876543213", "Address": "Kolkata", "Membership Type": "Premium"},
                    {"Member ID": 105, "Name": "Rohan Mehta", "Age": 35, "Gender": "Male", "Contact": "9876543214", "Address": "Bangalore", "Membership Type": "Regular"},
                    {"Member ID": 106, "Name": "Ananya Reddy", "Age": 24, "Gender": "Female", "Contact": "9876543215", "Address": "Hyderabad", "Membership Type": "Regular"},
                    {"Member ID": 107, "Name": "Vikram Singh", "Age": 40, "Gender": "Male", "Contact": "9876543216", "Address": "Jaipur", "Membership Type": "Premium"},
                    {"Member ID": 108, "Name": "Sneha Nair", "Age": 27, "Gender": "Female", "Contact": "9876543217", "Address": "Kochi", "Membership Type": "Regular"},
                    {"Member ID": 109, "Name": "Kunal Chatterjee", "Age": 32, "Gender": "Male", "Contact": "9876543218", "Address": "Kolkata", "Membership Type": "Premium"},
                    {"Member ID": 110, "Name": "Divya Malhotra", "Age": 29, "Gender": "Female", "Contact": "9876543219", "Address": "Chandigarh", "Membership Type": "Regular"}
                ]

    def library_details(self):
        print("🏛️  Library Name : [bold]Saraswathi Grandhalayam[/bold]")
        print("📍 Address :")
        print("🏢 [bold]Saraswathi Grandhalayam[/bold]")
        print("🏠 [bold]32-121, Naidu Vari Street[/bold]")
        print("🌆 [bold]Chilakaluripeta, Palnadu Dist[/bold]")
        print("🌍 [bold]Andhra Pradesh, India[/bold]")

    def staff_details(self):
        if not self.library_staff:
            print("[bold red]No Staff in the library[/bold red]")
            return
        print("[bold]Library Staff Details:[/bold]")
        print("=" * 40)
        for staff in self.library_staff:
            print(f"ID: [bold]{staff['id']}[/bold]")
            print(f"Name: [bold]{staff['name']}[/bold]")
            print(f"Role: [bold]{staff['role']}[/bold]")
            print(f"Phone: [bold]{staff['phone']}[/bold]")
            print(f"Email: [bold]{staff['email']}[/bold]")
            print("-" * 40)

    def library_members_list(self):
        if not self.library_members:
            print("[bold red] No Membersin the library[/bold red]")
            return
        print("[bold orange]Library Members list : [/bold orange]")
        print("="*40)
        for member in self.library_members:
            print(f"ID : [bold]{member['Member ID']}[/bold]")
            print(f"NAME : [bold]{member['Name']}[/bold]")
            print(f"AGE : [bold]{member['Age']}[/bold]")
            print(f"GENDER : [bold]{member['Gender']}[/bold]")
            print(f"CONTACT : [bold]{member['Contact']}[/bold]")
            print(f"ADDRESS : [bold]{member['Address']}[/bold]")
            print(f"MEMBERSHIP TYPE : [bold]{member['Membership Type']}[/bold]")
            print("-" * 40)
            
    def library_books_list(self):
        if not self.library_books:
            print("[bold red] No Books in the library [bold red]")
            return 
        print(f"[bold orange]Library Books list : {emoji.emojize(':book:', language="alias")}[/bold orange]")
        print("="*40)
        for key,val in self.library_books.items():
            print(f"BOOK NUM : [bold]{key}[/bold]")
            print(f"TITLE : [bold]{val['title']}[/bold]")
            print(f"AUTHOR : [bold]{val['author']}[/bold]")
            print(f"Copies : [bold]{val['copies']}[/bold]")
            print(f"AVAILABILITY : [bold]{val['available']}[/bold]")
            print("-"*40)
class Staff(Library):
    def add_staff(self, id, name, role, phone):
        for staff in self.library_staff:
            if staff["id"] == id:
                print(f"[bold red]Staff ID {id} already exists..{emoji.emojize(':warning:')}[/bold red]")
                return
        self.library_staff.append({"id": id, "name": name, "role": role, "phone": phone, "email": name.lower().replace(" ", "") + "@saraswathililb.com"})
        print(f"[bold green]Staff {name} is entered successfully ✅[/bold green]")

    def delete_staff(self,id):
        for staff in self.library_staff:
            if staff["id"] == id:
                self.library_staff.remove(staff)
                print(f"[bold green]Staff member with id {id} removed successfully. ✅[bold green]")
                return
        print(f"[bold red]staff member with id {id} not existed.{emoji.emojize(':warning:')}[/bold red]")

    def update_staff_details(self,id):
        found = False
        for staff in self.library_staff:
            if staff["id"] == id:
                found = True
                while True:
                    print("[bold]Staff Modification Method[/bold]")
                    print("0. Stop  changes 🛑")
                    print("1. Modify Name ✏️")
                    print("2. Modify Role 🏢")
                    print("3. Modify Phone 📞")
                    print("4. Modify Email 📧")
                    try:    
                        choice = int(input("Select your modification  : "))
                        if choice == 1:
                                print(f"previous Name = {staff["name"]}")
                                while True:
                                    name = input("Enter a name : ")
                                    if not re.fullmatch(r"^[A-Za-z ]+$",name):
                                        print(f"[bold] Invalid NAME {name}❌ Please enter only letters (A-Z, a-z).[/bold]")
                                    else:
                                        break
                                staff["name"] = name.strip().capitalize()
                                staff["email"] = name.replace(" ","").lower()+"@saraswathilib.com"
                                print(f"[bold green]Name {name} modified successfully ✅[/bold green]")
                        elif choice == 2:
                                print(f"previous Role = {staff["role"]}")
                                while True:
                                    role = input("Enter a role : ").strip()
                                    if not re.fullmatch(r"^[A-Za-z ]+$",role):
                                        print(f"[bold] Invalid ROLE {role}❌ Please enter only letters (A-Z, a-z).[/bold]")
                                    else:
                                        break
                                staff["role"] = role.title()
                                print(f"[bold green]Modified Successfull ✅[/bold green]")
                        elif choice == 3:
                                print(f"previous PHONE NUMBER = {staff["phone"]}")
                                while True:
                                    phone = input("Enter a phone number : ").strip()
                                    if not re.fullmatch(r"^[6-9]\d{9}$",phone):
                                        print(f"[bold red]Number {phone} is Invalid ❌.. Try one more time[/bold red]")
                                    else:
                                        staff["phone"] = f"+91 {phone[:3]}-{phone[3:6]}-{phone[6:]}"
                                        print(f"[bold green]phone number {phone} modified successfully ✅[/bold green]")
                                        break
                        elif choice == 4:
                                print(f"Previous Email = {staff["email"]}")
                                print("Your Name : ",staff["name"])
                                email = input("Enter your name without space : ").replace(" ","")
                                staff["email"] = email+"@saraswathilib.com"
                                print(f"[bold green]Email Modified Successfully {emoji.emojize(":check_mark_button:")}[/bold green]")
                        elif choice == 0:
                            print("[bold red]Terminated from modifications menu... 🛑[bold red] ")
                            print("[bold]Going back to STAFF class[/bold]")
                            break
                        else:
                            print(f"[bold]Enter proper modification Number {emoji.emojize(":cross_mark:")}[/bold]")
                    except Exception as e:
                        print(f"[bold red] Error occured in modifications. ERROR : {e} {emoji.emojize(":warning:")}[/bold red]")  
        if not found:
             print(f"[bold red]No staff with id {id}.. {emoji.emojize(":cross_mark:")}[/bold red]")
             
class Book(Library):
    def add_book(self,id,title,author,copies,available):
        if id in self.library_books:
            print(f"[bold red]id {id} already exists[/bold red]")
            return
        self.library_books[id] = {
            "title" : title,
            "author" : author,
            "copies" : copies,
            "available":available
        }
        print(f"[bold green]Book {title} added successfully {emoji.emojize(':white_check_mark:')}[/bold green]")
    def delete_book(self,id):
        if id in self.library_books:
            del self.library_books[id]
            print(f"[bold green]{id}successfully deleted{emoji.emojize(':white_check_mark:')}[bold green]")
            return
        print(f"[bold red]{id} id not existed in library books list {emoji.emojize(':warning:')}[/bold red]")
    def update_book(self,id):
        if id in self.library_books:
            while True:
                try:
                    print("[bold]Books Modification Method [/bold]")
                    print(f"Enter {emoji.emojize(':keycap_0:')} to exit from modifications")
                    print(f"Enter {emoji.emojize(':keycap_1:')} to modify book name")
                    print(f"Enter {emoji.emojize(':keycap_2:')} to modify author name")
                    print(f"Enter {emoji.emojize(':keycap_3:')} to modify available status")
                    print(f"Enter {emoji.emojize('4')} to update count of books")
                    uchoice = int(input("select book modificatioin : "))
                    if uchoice == 0:
                        print(f"[bold]Exited from Update Book Method {emoji.emojize(':man_running:')}[/bold]")
                        break
                    elif uchoice == 1:
                        while True:
                            print(f"[bold]Previous Book title = {self.library_books[id]['title']}[/bold]")
                            title = input("Enter title to modify : ").strip().title()
                            if not re.fullmatch(r"^[a-zA-Z ]+$",title):
                                print(f"[bold red]Title {title} should contain only alphabets (a-z/A-Z)[/bold red]")
                            else:
                                break
                        self.library_books[id]['title'] = title
                        print(f"[bold green]{title} modified successfully {emoji.emojize(':white_check_mark:')}[bold green]")
                    elif uchoice == 2:
                        while True:
                            print(f"[bold]Previous Author name = {self.library_books[id]['author']}[/bold]")
                            author = input("Enter name of the author to modify : ").strip().title()
                            if not re.fullmatch(r"^[a-zA-Z ]+$",author):
                                print(f"[bold red]Author {author} should contain only alphabets (a-z/A-Z)[/bold red]")
                            else:
                                break
                        self.library_books[id]['author'] = author
                        print(f"[bold green]{author} Updated Successfully {emoji.emojize(':white_check_mark:')}[/bold green]")
                    elif uchoice == 3:
                        while True:
                            print(f"[bold]Previous Available Status = {self.library_books[id]['available']}[/bold]")
                            available = input("Enter Book Availability Status (True/False) : ").replace(" ","").capitalize()
                            if available not in ["True","False"]:
                                print(f"[bold red]{available} should be either True or False[/bold red]")
                            else:
                                break
                        self.library_books[id]['available'] = True if available == "True" else False
                        print(f"[bold green]Book available {available} updated successfully {emoji.emojize(':white_check_mark:')}[/bold green]")
                    elif uchoice == 4:
                        while True:
                            print(f"[bold]Previous count = {self.library_books[id]['copies']}[/bold]")
                            copies =input("update the copies count : ").replace(" ","")
                            if not re.fullmatch(r"^[0-9]+$",copies):
                                print("[bold red] copies count should be an Interger[/bold red]")
                            else:
                                copies = int(copies)
                                break
                        self.library_books[id]['copies'] = copies
                        print(f"[bold green]Copies count {copies} updated successfully {emoji.emojize(':white_check_mark:')}")
                    else:
                        print(f"[bold red]Enter proper Book Modification {emoji.emojize(':cross_mark:')}[/bold red]")
                except Exception as e:
                    print(f"[bold red] Error occurred in Book's Modification method. Error = {e} {emoji.emojize(':warning:')}[/bold red]")
        else:
            print(f"[bold red]Id {id} not in the library books list [/bold red]")
class Members(Library):
    def add_member(self,id,name,age,gender,contact,address,membershipType):
        for member in self.library_members:
            if member["Member ID"] == id:
                print(f"[bold red]Id with {id} already exists[/bold red]")
                return
        self.library_members.append({"Member ID":id,"Name":name,"Age":age,"Gender":gender,"Contact":contact,"Address":address,"Membership Type":membershipType})
        print(f"[bold green]Member {name} is entered successfully {emoji.emojize(':heavy_check_mark:')}[/bold green]")
    
    def delete_member(self,id):
        for member in self.library_members:
            if member["Member ID"] == id:
                self.library_members.remove(member)
                print(f"[bold green]Member with {id} deleted successfully {emoji.emojize(':heavy_check_mark:')}[bold green]")
                return
        print(f"[bold red]Member with id {id} not existed..[bold red]")

    def modify_member_details(self,id):
        found = False
        for member in self.library_members:
            if member["Member ID"]==id:
                found = True
                while True:
                    print("[bold]Members Modifications options are [/bold]")
                    print(f"Enter {emoji.emojize(':keycap_0:')} to Exit {emoji.emojize(':door:')}")
                    print(f"Enter {emoji.emojize(':keycap_1:')} to modify Name {emoji.emojize(':bust_in_silhouette:')}")
                    print(f"Enter {emoji.emojize(':keycap_2:')} to modify Age {emoji.emojize(':hourglass:')}")
                    print(f"Enter {emoji.emojize(':keycap_3:')} to modify Gender {emoji.emojize(':male_sign:')}/{emoji.emojize(':female_sign:')}")
                    print(f"Enter {emoji.emojize(':keycap_4:')} to modify Contact {emoji.emojize(':telephone:')}")
                    print(f"Enter {emoji.emojize(':keycap_5:')} to modify Address {emoji.emojize(':house:')}")
                    print(f"Enter {emoji.emojize(':keycap_6:')} to modify Membership Type {emoji.emojize(':card_index:')}")
                    try:
                        mchoice = int(input("Select preferable option (Enter corresponding number ) : "))
                        if mchoice == 0:
                            print(f"[bold]Exited from modifications.. {emoji.emojize(':man_running:')}[/bold]")
                            break
                        elif mchoice == 1:
                            print(f"previous Name = {member["Name"]}")
                            while True:
                                name = input("Enter new member name : ").strip().title()
                                if  not re.fullmatch(r"^[a-zA-z ]+$",name):
                                    print(f"[bold]❌ Invalid NAME {name}! Please enter only letters (A-Z, a-z).[/bold]")
                                else:
                                    break
                            member["Name"] = name
                            print(f"[bold green]Modification done successfully {emoji.emojize(':heavy_check_mark:')}[/bold green]")
                        elif mchoice == 2:
                            print(f"previous Age = {member["Age"]}")
                            member["Age"] = int(input("Enter your age : "))
                            print(f"[bold green]Modification done successfully {emoji.emojize(':heavy_check_mark:')}[/bold green]")
                        elif mchoice == 3:
                            print(f"previous Gender = {member["Gender"]}")
                            while True:
                                gender = input("Enter your gender(Male/Female/Others) : ").strip().capitalize()
                                if gender not in ["Male","Female","Others"]:
                                    print(f"[bold]❌ Invalid GENDER {gender}! Please enter (Male/Female/Others).[/bold]")
                                else:
                                    break
                            member["Gender"] = gender
                            print(f"[bold green]Modification done successfully {emoji.emojize(':heavy_check_mark:')}[/bold green]")
                        elif mchoice == 4:
                            print(f"previous Phone Number = {member["Contact"]}")
                            phone = input("Enter your phone number : ").strip()
                            if not re.fullmatch(r"^[6-9]\d{9}$",phone):
                                print(f"Entered phone number {phone} is invalid..{emoji.emojize(':cross_mark:')}")
                                print(f"Phone number should contain 10 digits and should start with 6-9 ")
                            else:
                                member["Contact"] = f"+91 {phone[:3]}-{phone[3:6]}-{phone[6:]}"
                                print(f"[bold green]Modification done successfully {emoji.emojize(':heavy_check_mark:')}[/bold green]")
                        elif mchoice == 5:
                            print(f"previous Address = {member["Address"]}")
                            member["Address"] = input("Enter your Address : ").strip().capitalize()
                            print(f"[bold green]Modification done successfully {emoji.emojize(':heavy_check_mark:')}[/bold green]")
                        elif mchoice == 6:
                            print(f"Previous membership type = {member["Membership Type"]}")
                            mtype = input("Enter membership Type (Premium/Regular) : ").strip().capitalize()
                            if mtype == "Premium" or mtype == "Regular":
                                member["Membership Type"] = mtype
                                print(f"[bold green]Modification done successfully {emoji.emojize(':heavy_check_mark:')}[/bold green]")
                            else:
                                print(f"[bold red]Entered Type {mtype} not a membership type {emoji.emojize(':cross_mark:')}[/bold red]")
                        else:
                            print(f"[bold]Enter proper modification corresponding number [/bold]")
                    except Exception as e:
                        print(f"[bold red]Error occurred in members modifications list. Error : {str(e)}  {emoji.emojize(':warning:')}[/bold red]")
        if not found:
            print(f"[bold red]Member with id {id} not existed..{emoji.emojize(':cross_mark:')}[/bold red]")

s = Staff()
b = Book()
m = Members()
while True:
    print("\n🙏🏻[bold bright_cyan] WELCOME TO THE LIBRARY 📚🏛️ [/bold bright_cyan]🙏🏻")  
    print(f"Enter {emoji.emojize(':keycap_0:', language="alias")} to stop {emoji.emojize(':stop_sign:',language="alias")}") 
    print("Enter 1️⃣  To Know About Library 🏛️")  
    print("Enter 2️⃣  Staff Details 👨‍🏫")  
    print("Enter 3️⃣  Membership 🆕🎫")  
    print("Enter 4️⃣  Books 📖📚") 
    try:
        print(f"\n[bold]Now you are in Home page.. {emoji.emojize(':house:', language='alias')}[/bold]\n")
        choice = int(input("Enter your preferrd option : "))
        if choice == 1:
            l = Library()
            while True:
                print(f"Enter {emoji.emojize(':keycap_0:', language='alias')}   to stop {emoji.emojize(':stop_sign:', language='alias')}")
                print(f"Enter {emoji.emojize(':keycap_1:', language='alias')}   to know about library")
                print(f"Enter {emoji.emojize(':keycap_2:', language='alias')}   to know about staff")
                print(f"Enter {emoji.emojize(':keycap_3:', language='alias')}   to know about member list")
                print(f"Enter {emoji.emojize(':keycap_4:', language='alias')}   to know about books")
                try:
                    print("\n[bold orange1]Now you are in LIBRARY class 🏛️[/bold orange1] \n")
                    lchoice = int(input("Enter your preferred option : "))
                    if lchoice == 1:
                        l.library_details()
                    elif lchoice == 2:
                        l.staff_details()
                    elif lchoice == 3:
                        l.library_members_list()
                    elif lchoice == 4:
                        l.library_books_list()
                    elif lchoice == 0:
                        print("Exited from library class 🛑")
                        break
                    else:
                        print(f"Enter proper options {emoji.emojize(':warning:')}")
                except Exception as e:
                    print(f"Error : {e} {emoji.emojize(':cross_mark:')}")
        elif choice == 2:
            while True:
                print("\n[bold orange1]You are in STAFF class 👨‍🏫[/bold orange1]\n")
                print(f"Enter {emoji.emojize('0')} to stop {emoji.emojize(':stop_sign:')}")
                print(f"Enter {emoji.emojize('1')} to know staff details")
                print(f"Enter {emoji.emojize('2')} to add new staff")
                print(f"Enter {emoji.emojize('3')} to delete staff")
                print(f"Enter {emoji.emojize('4')} for modifications")
                try:
                    
                    schoice = int(input("select you Staff class method options : "))
                    if schoice == 0:
                        print("Exited from STAFF class 🛑")
                        break
                    elif schoice == 1:
                        s.staff_details()
                    elif schoice == 2:
                        print(f"[bold] ADD NEW STAFF [/bold]")
                        while True:
                            name = input("Enter your name : ").strip().capitalize()
                            if not re.fullmatch(r"^[A-Za-z ]+$",name):
                                print("[bold]❌ Invalid NAME {name}! Please enter only letters (A-Z, a-z).[/bold]")
                            else:
                                break
                        while True:
                            if s.library_staff:
                                last_id = s.library_staff[-1]["id"]
                                print(f"[bold green] Last Staff ID: {last_id}[/bold green]")
                            id = input("Enter the id of the staff(L00..) : ").replace(" ","").capitalize()
                            if not re.fullmatch(r"^[A-Za-z0-9]+$",id):
                                print("[bold]❌ Invalid ID {id}! Please enter only numbers ( 0-9 ).[/bold]")
                            else:
                                break
                        while True:
                            role = input("Enter the role of the staff : ").strip().capitalize()
                            if not re.fullmatch(r"^[a-zA-Z ]+$",role):
                                print("[bold]❌ Invalid ROLE {role}! Please enter only letters (A-Z, a-z).[/bold]")
                            else:
                                break
                        while True:
                            phone = input("Enter the phone number : ").replace(" ","")
                            if not re.fullmatch(r"^[6-9]\d{9}$",phone):
                                print("[bold]❌ Invalid PHONE NUMBER {phone}! Please enter only 10 digit numbers ( 0-9 ).[/bold]")
                            else:
                                s.add_staff(id,name,role,phone)
                                break
                    elif schoice == 3:
                        print(f"[bold] DELETE STAFF [/bold]")
                        while True:
                            id = input("Enter the id of the staff : ").replace(" ","").capitalize()
                            if not re.fullmatch(r"^[lL][0-9]+$",id):
                                print("[bold]❌ Invalid ID {id}! Please enter only numbers ( 0-9 ).[/bold]")
                            else:
                                break
                        s.delete_staff(id)
                    elif schoice == 4:
                        print("[bold]MODIFY STAFF DETAILS[/bold]")
                        while True:
                            id = input("Enter the id of the staff : ").replace(" ","").capitalize()
                            if not re.fullmatch(r"^[lL][0-9]+$",id):
                                print("[bold]❌ Invalid ID {id}! Please enter only numbers ( 0-9 ).[/bold]")
                            else:
                                break
                        s.update_staff_details(id)
                    else:
                        print(f"[bold]Enter proper options {emoji.emojize(':warning:')}[/bold]")
                except Exception as e:
                    print(f"[bold red]Error : {e} {emoji.emojize(':cross_mark:')}[/bold red]")
        elif choice == 3:
            while True:
                print("[bold orange1]Yor are in MEMBERS CLASS 🆕🎫[/bold orange1]")
                print(f"Enter {emoji.emojize(':keycap_0:')} to exit form members class ")
                print(f"enter {emoji.emojize(':keycap_1:')} to add new member")
                print(f"Enter {emoji.emojize(':keycap_2:')} to delete member")
                print(f"Enter {emoji.emojize(':keycap_3:')} to modify the members details")
                print(f"Enter {emoji.emojize(':keycap_4:')} to display all members")
                try:
                    mchoice = int(input("Enter you preferable option : "))
                    if mchoice == 0:
                        print(f"[bold]Exited from MEMBERS class [/bold] {emoji.emojize(':man_running:')}")
                        break
                    elif mchoice == 1:
                        print(f"[bold]ADD NEW MEMBER[/bold]")
                        last_id = m.library_members[-1]["Member ID"] if m.library_members else 0
                        print(f"[bold green] Last Member ID: {last_id}[/bold green] ")
                        id = int(input("Enter new member id : "))
                        while True:
                            name = input("Enter new member name : ").strip().capitalize()
                            if  not re.fullmatch(r"^[a-zA-Z]+$",name):
                                print(f"[bold]❌ Invalid NAME {name}! Please enter only letters (A-Z, a-z).[/bold]")
                            else:
                                break
                        age = int(input("Enter new member age : "))
                        while True:
                                gender = input("Enter your gender(Male/Female/Others) : ").strip().capitalize()
                                if gender not in ["Male","Female","Others"]:
                                    print(f"[bold]❌ Invalid GENDER {gender}! Please enter (Male/Female/Others).[/bold]")
                                else:
                                    break
                        while True:
                            contact = input("Enter new member contact : ").strip()
                            if not re.fullmatch(r"^[6-9]\d{9}$", contact):
                                print(f"[bold]Member contact {contact} is invalid {emoji.emojize(':cross_mark:')}[/bold]")
                                print(f"[bold]Enter contact with 10 digits and should start from 6-9 [/bold]")
                            else:
                                break
                        address = input("Enter new member address : ").strip().capitalize()
                        while True:
                            membershipType = input("Enter new member type (Regular/Premium): ").strip().capitalize()
                            if membershipType not in ["Regular", "Premium"]:
                                print(f"[bold]Member ship type {membershipType} is invalid {emoji.emojize(':cross_mark:')}[/bold]")
                                print(f"[bold]Enter either Premium or Regular [/bold]")
                            else:
                                break
                        m.add_member(id,name,age,gender,contact,address,membershipType)
                    elif mchoice == 2:
                        print(f"[bold] Delete member [/bold]")
                        id = int(input("Enter the id of the Member : "))
                        m.delete_member(id)
                    elif mchoice == 3:
                        id = int(input("Enter the id of the Member : "))
                        m.modify_member_details(id)
                    elif mchoice == 4:
                        m.library_members_list()
                    else:
                        print(f"[bold red]Entered method not in the Member class. {emoji.emojize(':cross_mark:')} [/bold red]")
                except Exception as e:
                    print(f"[bold red]Error occurred in Member class. Error : {e}{emoji.emojize(':warning:')} [/bold red]")
                            
        elif choice == 4:
            while True:
                print("\n[bold orange1]You are in BOOK class[/bold orange1]\n")
                print(f"Enter {emoji.emojize(':keycap_0:')} to exit from book class")
                print(f"Enter {emoji.emojize(':keycap_1:')} to new book ")
                print(f"Enter {emoji.emojize(':keycap_2:')} to delete a book")
                print(f"Enter {emoji.emojize(':keycap_3:')} to modify book details ")
                print(f"Enter {emoji.emojize(':keycap_4:')} to view all books")
                bchoice = int(input("select a method of Book class : "))
                try:
                    if bchoice == 0:
                        print("[bold]Exited from BOOK class[/bold]")
                        break
                    elif bchoice == 1:
                        print("[bold]ADD A BOOK[/bold]")
                        while True:
                            last_id = next(reversed(b.library_books))
                            print(f"[bold]previous id = {last_id}[/bold]")
                            id = input("Enter the id of book : ").replace(" ","")
                            if not re.fullmatch(r"^[0-9]+$",id):
                                print(f"[bold red]Entered id {id} should contain only letter (0-9)[/bold red]")
                            else:
                                break
                        while True:
                            title = input("Enter the title of book : ").strip().title()
                            if not re.fullmatch(r"^[A-Za-z ]+$",title):
                                print(f"[bold red]Entered title {title} should contain only alphabets (a-z/A-Z)[/bold red]")
                            else:
                                break
                        while True:
                            author = input("Enter the name of the author : ").strip().title()
                            if not re.fullmatch(r"^[a-zA-Z ]+$",author):
                                print(f"[bold red]Entered author {author} should contain only alphabets (a-z/A-Z)[/bold red]")
                            else:
                                break
                        while True:
                            copies = input("Enter number of copies : ").replace(" ","")
                            if not re.fullmatch(r"^[0-9]+$",copies):
                                print("[bold red] copies count should contain only Intergers [/bold red]")
                            else:
                                copies = int(copies)
                                break
                        while True:
                            available = input("Enter availability of book : ").replace(" ","").capitalize()
                            if available not in ["True","False"]:
                                print(f"[bold red]Entered available {available} should contain only (True/False)[/bold red]")
                            else:
                                break
                            available = True if available == "True" else False
                        b.add_book(id,title,author,copies,available)
                    elif bchoice == 2:
                        print("[bold]Delete Method[/bold]")
                        while True:
                            # last_id = next(reversed(b.library_books))
                            # print(f"Previous Book id = {last_id}")
                            id = input("Enter the id of book : ").replace(" ","")
                            if not re.fullmatch(r"^[0-9]+$",id):
                                print(f"Entered {id} should contain only Integers(0-9)")
                            else:
                                break
                        b.delete_book(id)
                    elif bchoice == 3:
                        print("[bold]Update Method[/bold]")
                        while True:
                            # last_id = next(reversed(b.library_books))
                            # print(f"Pre")
                            id = input("Enter the id of book : ").replace(" ","")
                            if not re.fullmatch(r"^[0-9]+$",id):
                                print(f"Entered {id} should contain only Integers (0-9)")
                            else:
                                break
                        b.update_book(id)
                    elif bchoice == 4:
                        b.library_books_list()
                    else:
                        print(f"[bold red]Enter proper book class method {emoji.emojize(':cross_mark:')}[/bold red]")
                except Exception as e:
                        print(f"[bold red]Error occurred in Book class. Error : {e}{emoji.emojize(':warning:')} [/bold red]")
        elif choice == 0:
            print("Logout-->🛑")
            break
        else:
            print(f"[bold red]Enter proper options {emoji.emojize(':cross_mark:')}[/bold red]")
    except Exception as e:
        print(f"[bold red]Error : {e} {emoji.emojize(':warning:')}[/bold red]")
