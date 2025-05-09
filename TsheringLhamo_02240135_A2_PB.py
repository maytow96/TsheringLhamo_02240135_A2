import pickle
import os   #It provides a way to interact with the file system and environment in a way that's portable between different operating systems

#sets the limit of pokedex cards that can be added and each page's layout.
max_pokedex = 1025
card_per_page = 64
rows = 8
columns = 8

class pokemon_binding_manager:
    def __init__(self):
        #these are the in-memory data structures to store the binder and added cards.
        self.binder = {}
        self.added_cards = set() #built-in set to store unique card numbers
        self.save_file = "binder_session.pkl"  
        '''this defines the file name for saving the session. 
        The .pkl stands for Pickle which is used to serialize and deserialize data.
        this is used to save the status of a programor to transfer data between programs '''
        self.load_session()  #this will load the previos session even if the program is closes.

    def load_session(self):
        """Load the previous session from a file."""
        if os.path.exists(self.save_file):
            with open(self.save_file, "rb") as file:
                data = pickle.load(file)
                self.binder = data.get("binder", {})
                self.added_cards = data.get("added_cards", set())
                print("Previous session loaded .")
        else:
            print("No previous session found. Starting fresh.")

    def save_session(self):
        """Save the current session to a file for future reference"""
        with open(self.save_file, "wb") as file:
            data = {"binder": self.binder, "added_cards": self.added_cards}
            pickle.dump(data, file)
        print("Session saved successfully.")

    def position_card(self):
        """promt the user to add pokedex . Figures out the position of the pokedex in he binder."""
        try:
            card_number = int(input("Enter the Pokedex card number from 1-1025: "))
            #error andling for input range
            if card_number < 1 or card_number > max_pokedex:
                print("INVALID input Card number must be between 1 and 1025.")
                return {"status": "invalid range"}
            
            #error handling for duplicate cards
            if card_number in self.added_cards:
                print("Card already added to the binder.")
                return {"status": "duplicate"}

        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        #this algorith calculates the page number and position of the card in the binder.
        page = (card_number - 1) // card_per_page + 1       #findes page number
        position = (card_number - 1) % card_per_page        #findes the position of the card in the page
        row = position // columns + 1                  #findes the row number  
        column = position % columns + 1                #findes the column number
        status = "pokedex added"

        self.binder[card_number] = (page, row, column, status)
        self.added_cards.add(card_number)

        return {
            "page": page,
            "row": row,
            "column": column,
            "status": "Card successfully added",
            "card_number": card_number
        }
    
    def reset_binder(self):
        '''defines a function to clear the binder and reset. clears out all the pokedex'''
        self.binder.clear()
        self.added_cards.clear()
        if os.path.exists(self.save_file):
            os.remove(self.save_file)  # Delete the session file
        print("Binder has been reset and session cleared.")

    def status_viewer(self):
        '''it will display the current status of the binder. shows the persentage of the completiion of the collector'''
        if not self.binder:
            print("\nCurrent Binder Contents:\nThe binder is empty.")
        else:
            print("\nCurrent Binder Contents:")
            for number in sorted(self.binder):
                page, row, col, status = self.binder[number]
                print(f"Pokedex #{number}:\n  Page: {page} \nPosition: Row -{row}, \nColumn- {col}\n \n Status: {status}")
        #show how much is completed
        total_cards = len(self.binder)
        percent = (total_cards / max_pokedex) * 100
        print(f"\nTotal cards in binder: {total_cards}")
        print(f"% completion: {percent:.1f}%")
        if total_cards == max_pokedex:
            print("You have caught them!")
        
    def main(self):
        """this display the menu where user can choose what to do"""
        print("\nWelcome to the Pokemon Binder Manager!")
        while True:
            print("\n1. Add card")
            print("2. Reset binder")
            print("3. View current binder")
            print("4. exit")

            option = input("Enter your option: ")

            if option == "1":
                result = self.position_card()
                if result and result["status"] == "Card successfully added":
                    print(f"→ Page {result['page']}, Row {result['row']}, Column {result['column']}, Status: {result['status']}")

            elif option == "2":
                confirmation = input("WARNING!!! Are you sure you want to reset? \nThis will delete all your cards from the binder.\n Enter 'CONFIRM' to reset: ")
                if confirmation.strip().upper() == "CONFIRM":
                    self.reset_binder()
                else:
                    print("Reset cancelled.")

            elif option == "3":
                self.status_viewer()

            elif option == "4":
                self.save_session()
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    booksystem = pokemon_binding_manager()
    booksystem.main()
