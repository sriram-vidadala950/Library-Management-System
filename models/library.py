import emoji
from rich import print
from utils import load_data, dump_data

class Library:
    def __init__(self, user_details, staff_details, library_details):
        self.user_path = user_details
        self.staff_path = staff_details
        self.library_path = library_details

        self.user_details = load_data(self.user_path)
        self.staff_details = load_data(self.staff_path)
        self.library_details = load_data(self.library_path)
    
    def library_books_details(self):
        if not self.library_details:
            print("[bold red] No Books in the library [/bold red]")
            return 

        # Group books by language
        grouped = {}
        for book in self.library_details:
            language = book["language"]
            if language not in grouped:
                grouped[language] = []
            grouped[language].append(book)
        
        # Display books by language
        for language, books in grouped.items():
            print(f"\n📚 {language} Books:")
            print("-" * 70)
            for book in books:
                print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | "
                    f"Publisher: {book['publisher']} | Copies: {book['copies']}")
            print("-" * 70)

    
    def library_staff_details(self):
        if not self.staff_details:
            print("[bold red]No Staff in the library[/bold red]")
            return
        print("[bold]Library Staff Details:[/bold]")
        print("=" * 40)
        for staff in self.staff_details:
            print(f"ID: [bold]{staff['id']}[/bold]")
            print(f"Name: [bold]{staff['name']}[/bold]")
            print(f"Role: [bold]{staff['role']}[/bold]")
            print(f"Phone: [bold]{staff['phone']}[/bold]")
            print(f"Email: [bold]{staff['email']}[/bold]")
            print("-" * 40)
    
    def library_user_details(self):
        if not self.user_details:
            print("[bold red] No Members in the library[/bold red]")
            return
        print("[bold orange]Library Members list : [/bold orange]")
        print("="*40)
        for member in self.user_details:
            print(f"ID : [bold]{member['id']}[/bold]")
            print(f"NAME : [bold]{member['name']}[/bold]")
            print(f"AGE : [bold]{member['age']}[/bold]")
            print(f"GENDER : [bold]{member['gender']}[/bold]")
            print(f"CONTACT : [bold]{member['contact']}[/bold]")
            print(f"ADDRESS : [bold]{member['address']}[/bold]")
            print(f"MEMBERSHIP TYPE : [bold]{member['membership_type']}[/bold]")
            print("-" * 40)
