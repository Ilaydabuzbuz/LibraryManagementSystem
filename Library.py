class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for index, line in enumerate(lines, start=1):
            book_title = line.split(',')[0].strip()
            author = line.split(',')[1].strip()
            print(f"\n{index}. Book title: {book_title} \n   Author: {author}")

    def add_book(self):
        book_title = input("Type a book title, please: \n")
        author = input("Type the author: \n")
        release_date = input("Type the release date: \n")
        num_of_pages = input("Type the number of pages: \n")
        self.file.seek(0)
        line = f"{book_title}, {author}, {release_date}, {num_of_pages}\n"
        self.file.write(line)
        print("Book is successfully added to the list!")

    def remove_book(self):
        book_title = input("Type the book title you want to remove, please: \n")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        found = False
        for line in lines:
            if book_title == line.split(',')[0].strip():
                lines.remove(line)
                found = True
                print("Book is found and removed from the list!")
                break
        if not found:
            print("The book is not present in the list!")
        self.file.truncate(0)
        for line in lines:
            self.file.write(line + '\n')

    @staticmethod
    def display_menu():
        menu = "*** MENU *** \n0) Quit \n1) List Books \n2) Add Book \n3) Remove Book"
        print(menu)


lib = Library("books.txt")
while True:
    print()
    lib.display_menu()
    try:
        user_input = int(input("\nChoose your option from the menu, please: "))
        if user_input == 0:
            print("Quitting...")
            break
        elif user_input == 1:
            lib.list_books()
        elif user_input == 2:
            lib.add_book()
        elif user_input == 3:
            lib.remove_book()
        else:
            raise ValueError("Invalid input!")
    except ValueError as e:
        print("Invalid input. Type a valid option, please: ")
