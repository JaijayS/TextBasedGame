# Developer: Jantzen Springer
# Class: IT-140/ Professor Ogoh
# Theme: The pug that lost his way

def exit_game():
    # Exit room function for user to quit game.
    answer = ''
    print('You are in the "Exit Room".\nWould you like to quit? (yes or no)')
    while answer != ['yes', 'no']:
        answer = input()
        if answer == 'yes':
            print('Thanks for playing. You are exiting the game!')
            exit(0)
        elif answer == 'no':
            print('Okay. Lets restart!')
            player_movement()

    else:
        print("Please type 'yes or no'. Thank you!")


def item_pickup(current_location, inventory):
    # Pickup Function
    replay_answer = ''
    get_answer = ''
    # Rooms with associated items.
    room_items = {'Control Room': 'ID-card',
                  'Feline Kennels': 'Freckles',
                  'Storage Room': 'Collar',
                  'Kitchen': 'Animal Snacks',
                  'Bunk Room': 'Ray\'s phone',
                  'Garage': 'Truck keys',
                  'Break Room': 'Officer Ray'}
    # Loop for item pickup
    while get_answer != f'get {room_items[current_location]}':
        # End game if user meets Officer Ray before inventory has all 6 items
        if room_items[current_location] == 'Officer Ray' and len(inventory) < 6:
            print('*' * 30)
            print(f'You see {room_items[current_location]}')
            print(f'He throws you back in your cage..Game Over')
            print('*' * 30)
            print('Would you like to play again? (Y / N)')
            replay_answer = input()
            replay_answer.lower()
            if (replay_answer == 'yes'or replay_answer == 'y'):
                main()
            elif (replay_answer == 'no' or replay_answer == 'n' ):
                print('Thanks for playing the game. Hope you enjoyed it.')
                exit_game()
            else:
                print("Please type 'yes or no'. Thank you!")
        # If items are found in room.
        if room_items[current_location] not in inventory:
            print(f'You see a {room_items[current_location]}')
            print(f'Enter your move:')
            get_answer = input()
            # User picking up item from room.
            if get_answer in ['quit', 'exit']:
                exit_game()
            elif get_answer == f'get {room_items[current_location]}':
                inventory.append(room_items[current_location])
                print(f'Inventory: ')
                # Print all items in inventory
                for items in inventory:
                    print(f' - {items}')
                # If all 6 items are in inventory, user wins.
                if len(inventory) == 6:
                    print('*' * 30)
                    print('You collected all the items.')
                    print('You broke out of the pound. You win!!')
                    print('*' * 30)
                    exit(0)
            else:
                print('Invalid Input. type [get \'item name\']')
            print('=' * 30)

        else:
            print('You already got an item from this room!')
            break


def player_movement():
    # Player movement
    inventory = []
    # Valid movements
    movements_list = ['go north', 'go east', 'go south', 'go west']
    exit_list = ['exit', 'quit']
    # Rooms dictionary with adjacent rooms relative to location.
    rooms = {'K-9 Kennels': {'east': 'Control Room'},
             'Control Room': {'north': 'Kitchen', 'east': 'Feline Kennels', 'south': 'Storage Room',
                              'west': 'K-9 Kennels'},
             'Feline Kennels': {'west': 'Control Room'},
             'Storage Room': {'north': 'Control Room'},
             'Kitchen': {'north': 'Garage', 'east': 'Break Room', 'south': 'Control Room', 'west': 'Bunk Room'},
             'Bunk Room': {'east': 'Kitchen'},
             'Garage': {'south': 'Kitchen'},
             'Break Room': {'west': 'Kitchen'}
             }
    direction = ''
    current_location = 'K-9 Kennels'
    # Movement while loop continues until user types exit or quit.
    while direction != ['quit', 'exit']:
        print('Location: {}'.format(current_location))
        if current_location != 'K-9 Kennels':
            item_pickup(current_location, inventory)
            print('Location: {}'.format(current_location))
        print('Enter your move:')
        direction = input()
        direction = direction.lower()
        # If user input is same as valid movements, they will be moved to that location.
        if direction in exit_list:
            exit_game()
        elif direction in movements_list:
            direction = direction[3:]
            if direction in rooms[current_location].keys():
                current_location = rooms[current_location].get(direction)
                print('=' * 30)
            else:
                print('=' * 30)
                print('Spot tries to go that way but cant find a way out. \nTry another direction.')
                print()
        else:
            print('Invalid movement')
            print('=' * 30)


def main():
    # title format
    title = "THE LOST DOG AND CAT"
    x = title.center(100)
    print()
    print(x)
    print()
    print("""   Your dog Spot and cat Freckles are lost! While trying to find their way home, Animal control officer 
    Ray snatched up Spot and freckles Officer Ray is currently watching late-night shows in the break room. Fortunately,
    the kennel that your Spot was put in did’t lock and Spot could get out. To escape the 
    grasps of officer Ray, your Spot must find (6) items before he finds you! He must find the ID-CARD in the control room to open the 
    exterior doors, your best friend the FRECKLES in the cat kennels, your COLLAR from the storage room, ANIMAL SNACKS from
    the kitchen for energy, RAY'S PHONE from the bunk room for GPS, and finally the TRUCK KEYS so they can drive home.  
    """)
    # Instructions to user on how to move throughout the house.
    print('COMMANDS:')
    print("Movement: go [cardinal-direction]")
    print("Pickup Item: get [Item-name]")
    print("To end game: 'quit' or 'exit' ")
    print()
    answer = ''
    # Asking user if they are ready to begin the game.
    while answer != ['yes', 'no']:
        print('Are you ready? (yes/no)')
        answer = input()
        if answer == 'yes':
            print('=' * 30)
            player_movement()
        if answer == 'no':
            print('Okay thanks for coming.')
            exit(0)
        else:
            print('Please enter a valid response.')


main()
