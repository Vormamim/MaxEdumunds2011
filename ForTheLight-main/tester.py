
from data import Elissus_Rooms 
import shared
from functions import directional_choices


shared.player = {
        "name": "",
        "progress": 0,
        "player_health": 100,
        "player_dmg": 0,
        "player_def": 0,
        "currency": 0,
        "location": "your_room",
    }

from colorama import init, Fore, Style
init(autoreset=True)  # Resets colour after each print


def start_room():
    starting_room = "your_room"
    return starting_room

def main():
    

    current_room = start_room()
    print("Current room:", current_room)
    

    items = []

    print ("Only the stars may tell this story.")
    print ("For as long as anyone can remember, there have been five planets.")
    print (Fore.GREEN + "Elissus, Planet of Fertility.")
    print (Fore.BLUE + "Fragira, Planet of Mystery.")
    print (Fore.MAGENTA + "Chystalv, Planet of Weather.")
    print (Fore.CYAN + "Nolox, Planet of Technology.")
    print (Fore.YELLOW + "And Varunii, Planet of Light.")

    print ("The only way to cross between them is when they align...")
    print ("And for all five to align, it takes a milennia.")
    print (Style.BRIGHT + Fore.YELLOW + "Welcome...to The Final Alignment")
    print ("...")

    shared.player ["name"] = input("What is your name? ").strip()
    print(f"Welcome, {shared.player['name']}.")
    
    while True:
        open_menu = input("Press 'Enter' to start the game. Type 'z' to check the controls. Type 'c' to check progress.").lower()

        if open_menu == "":
            current_location = "your_room"
            break

        elif open_menu == "z":
            print("Controls:")
            print("Use the arrow keys to move.")
            print("Press 'Enter' to interact with objects.")
            print("Press 'Esc' to pause the game.")
            print("Type 'c' to check your progress at any time.")

        elif open_menu == "c":
            print("Progress:")
            print(f"Your current progress is {shared.player ['progress']}%")

        else:
            print("Invalid option. Please try again.")

    # Main game loop - handle room interactions
    while True:
        if current_location == "your_room":
            print(Elissus_Rooms[current_location]["description"])
            command = input(Elissus_Rooms[current_location]["choice"]).lower()
            if command in ['w', 'a', 's', 'd']:
                print(f"DEBUG: Current location before move = {shared.player['location']}")
                new_location = directional_choices(command)
                if new_location:
                    shared.player["location"] = new_location
                    current_location = new_location
                print(f"DEBUG: Current location after move = {shared.player['location']}")
               
            else:
                print("Invalid command. Please try again.")
                continue

        elif current_location == 'your_wardrobe':
            print(Elissus_Rooms["your_wardrobe"]["description"])
            shared.player ["currency"] += 5
            print(f"You found 5 currency! You now have {shared.player['currency']} currency.")
            command = input("Press any key to continue...").lower()
            # After visiting wardrobe, return to room selection
            current_location = "your_room"
                
        elif current_location == 'town_street':
            print(Elissus_Rooms["town_street"]["description"])
            street_choice1 = input(Elissus_Rooms["town_street"]["choice"]).lower()
            
            if street_choice1 == 'a':
                print("You approach the friendly stranger.")
                shared.player ["currency"] += 10
                print(f"You received 10 currency! You now have {shared.player['currency']} currency.")
                print("You thank him and head down the street.")
            elif street_choice1 == 's':
                print("You decide to continue down the street.")
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # After town street interaction, allow further movement
            command = input("Where would you like to go? (w/a/s/d): ").lower()
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command)
                if new_location:
                    shared.player["location"] = new_location
                    current_location = new_location
        
        else:
            print(f"Location '{current_location}' not implemented yet.")
            break
        
if __name__ == "__main__":
    main()