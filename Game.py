# Import necessary modules
import random
import os

# Define the values of the cards
valueCard = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
# Define the types of the cards
typeCard = ['♠', '♥', '♦', '♣']

# Function to get the value of a card
def get_card_value(card):
    return valueCard[card]

# Function to count the value of a hand of cards
def count_cards(cards):
    num_aces = 0
    total = 0
    for card in cards:
        value = get_card_value(card[0])
        if value == 11:
            num_aces += 1
        total += value
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1
    return total

# Function to deal cards
def deal_cards(num_cards):
    cards = []
    for i in range(num_cards):
        # Choose a random card from the list
        randomvalue = random.choice(list(valueCard.keys()))
        randomtype = random.choice(typeCard)

        card = (randomvalue, randomtype)

        cards.append(card)

    return cards

# Function to print the dealer's hand
def print_dealer_hand(cards, reveal_hidden_card=False):
    print("The dealer's hand:")
    if not reveal_hidden_card:
        print("○------○\n|      |\n|      |\n|      |\n○------○") # Hide the first card
    else:
        print(f"○------○\n|    {cards[0][1]} |\n|   {cards[0][0]}  |\n| {cards[0][1]}    |\n○------○")
    for card in cards[1:]:
        print(f"○------○\n|    {card[1]} |\n|   {card[0]}  |\n| {card[1]}    |\n○------○")

# Function to print the player's hand
def print_player_hand(cards):
    print("\nThe player's hand:")
    for card in cards:
        print(f"○------○\n|    {card[1]} |\n|   {card[0]}  |\n| {card[1]}    |\n○------○")

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define a function called "play_game"
def play_game():
    # Prompt the user to ask if they are ready to play
    ready = input("Are you ready to play? (Y/N): ")
    
    # If the user is ready to play, deal 2 cards to the dealer and player
    if ready == "Y":
        dealer_cards = deal_cards(2)
        player_cards = deal_cards(2)
        
        # Print the dealer's first card and update the dealer's count
        print_dealer_hand(dealer_cards)
        dealer_count = count_cards(dealer_cards[1:])
        print(f"Dealer's count: {dealer_count}")
        
        # Print the player's cards and update the player's count
        print_player_hand(player_cards)
        player_count = count_cards(player_cards)
        print(f"Player's count: {player_count}")
    else:
        # If the user is not ready to play, exit the function
        print("Okay, maybe next time.")
        return
    
    # Prompt the user to ask if they want to add a card
    add_card = input("Do you want to add a card? (Y/N): ")
    
    # Loop while the user wants to add a card
    while add_card == "Y":
        # Deal one card to the player and update the screen
        player_cards.append(deal_cards(1)[0])
        clear_terminal()
        print_dealer_hand(dealer_cards, reveal_hidden_card=True)
        dealer_count = count_cards(dealer_cards) # update dealer count
        print(f"Dealer's count: {dealer_count}")
        print_player_hand(player_cards)
        player_count = count_cards(player_cards)
        print(f"Player's count: {player_count}")
        
        # Check if the player has busted or won, and exit the loop if so
        if player_count > 21:
            print("Bust! You lose.")
            return
        elif player_count > dealer_count:
            print("You win!")
            return
        
        # Prompt the user to ask if they want to add another card
        add_card = input("Do you want to add another card? (Y/N): ")
    
    # Update the screen and print the final result
    clear_terminal()
    print_dealer_hand(dealer_cards, reveal_hidden_card=True)
    dealer_count = count_cards(dealer_cards) # update dealer count
    print(f"Dealer's count: {dealer_count}")
    print_player_hand(player_cards)
    print(f"Player's count: {player_count}")
    
    if player_count <= dealer_count:
        print("You lose.")
    else:
        print("You win!")

# Call the "play_game" function to start the game
play_game()