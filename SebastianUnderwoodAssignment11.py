#This program randomly draws five cards for a poker game.
#the user then has the option to change whatever cards they like

import random

#creates the deck of cards lists, will shuffle the order they are called
def createDeck():
    shapes = ["Clubs", "Diamonds", "Hearts", "Spades"]
    numbers = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
#shuffles and returns the lists
    deck = [(number, shape) for shape in shapes for number in range(1, 14)]
    random.shuffle(deck)
    return deck, numbers

#draws 5 cards from the deck, then asks the user if he/she wants to
#draw different cards
def pokerGame():
    deck, numbers = createDeck()
    hand = [deck.pop() for i in range(5)]

#displays the cards from the shuffled deck
    print("\nYour current hand:")
    for i, (number, shape) in enumerate(hand):
        print(f"{i + 1}: {numbers[number]} of {shape}")

#if the user wants, their deck will be reshuffled
    response = input("Enter the card's number to replace (formated like, 1 2 3 4 5), or press Enter to keep all: ")

#checks to see if the user entered numbers
    if response.strip():
        try:
            indices = map(int, response.split())
            for i in indices:
                if 1 <= i <= 5:
                    hand[i - 1] = deck.pop()
                else:
                    print(f"Please enter number(s) 1-5")
        except ValueError:
            print("No cards were redrawn.")

#displays the final hand
    print("\nYour final hand:")
    for i, (number, shape) in enumerate(hand):
        print(f"{i + 1}: {numbers[number]} of {shape}")



pokerGame()
