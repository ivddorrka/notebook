"""
Menu
"""
import sys
from notebook import Notebook, Note

class Menu:
    """To work with menu"""
    def __init__(self):
        """Init func"""
        self.notebook = Notebook()
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_note,
        "4": self.modify_note,
        "5": self.quit
        }
    def display_menu(self):
        """To show menu"""
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    def run(self):
        """To run this file as long as user uses it"""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    def show_notes(self, notes=None):
        """To check which notes you already have"""
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
            note.id, note.tags, note.memo))
    def search_notes(self):
        """To search for key words in all your notes"""
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    def add_note(self):
        """To add new note"""
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")
    def modify_note(self):
        """To mdify notes"""
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
    def quit(self):
        """To stop runing this project"""
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()