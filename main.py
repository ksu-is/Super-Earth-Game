def start_game():
    print("You are humanity's last hope against the Intergalactic Empire. Choose wisely.")
    input("Press Enter to begin the game.\n")
    first_choice()

def first_choice():
    print("\nNews reports flood in. An extraterrestrial has appeared.")
    print("It's humanoid in appearance, but seems hostile. Naturally, you fly to the city to investigate.")
    print("1. Attempt to communicate with the being.")
    print("2. Engage in combat")
    choice = input("What do you do? (1/2): ")
    if choice == '1':
        print("\nThe galactic fighter ignores your words. 'Prepare, human!' It flies at you with incredible speeds. Get ready to fight!")
        start_combat("Mysterious Alien Warrior")
    elif choice == '2':
        start_combat("Mysterious Alien Warrior")
    else:
        print("Invalid choice. Please try again.")
        first_choice()

def start_combat(enemy_name):
    player_hp = 100
    enemy_hp = 100

start_game()