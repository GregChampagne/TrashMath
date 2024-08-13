"""
Project: TrashMath - Math for the game of Trash at every step
Company: A.W. Schultz Inc.
Developer: Gregory H. Champagne
Date: 8-12-24
"""
import random

# Creates a deck, and shuffles it
def shuffle_deck(deck):
    # Create an empty deck, and a deck in order
    shuffler = []
    count = 0
    for i in range(1,14):
        for ii in range(0,4):
            shuffler.append(i)

    # Pick random indexes to append the next number to (aka shuffle)
    for i in range(0,52):
        found = False
        while not found:
            rando = random.randint(0, 51)
            if deck[rando] == 0:
                deck[rando] = shuffler[i]
                found = True

    return deck


# How many turns on average does it take to solve?
# Figure out a way a get a guess for that, then simulate
# Assuming no other player, how long on average?

# Play the game of trash solo
def play_game():
    # Start the game with 10 slots
    hand_size = 10
    done = False
    while not done:
        print("Here we go")
        pos = 0
        my_deck = [0] * 52
        my_deck = shuffle_deck(my_deck)
        hand = []
        flipped = [0] * hand_size
        # Deal out the amount of cards needed
        for i in range(0, hand_size):
            hand.append(my_deck[pos])
            pos+=1

        ongoing = True
        print(hand)
        while ongoing:
            # Take the top card
            if pos != 52:
                my_card = my_deck[pos]
                pos+=1
            else:
                ongoing = False
                done = True
            print("Draw " + str(pos - hand_size) + ": " + str(my_card))
            # print(flipped)



            # If top card is a Jack, assign it to the lowest spot available
            """ IGNORING WILDCARDS FOR THE TIME BEING SO I CAN MAKE IT WORK AHHHH
            if my_card == 11:
                chosen = False
                hand_index = 0
                while not chosen:
                    if filled[hand_index] == 0:
                        bonus_card = hand[hand_index]
                        hand[hand_index] = my_card
                        my_card = bonus_card
                        filled[hand_index] = 1
                        chosen = True
                        placed = True
            """
            # If my card is a card that I need, place it, and repeat until I don't
            out = False
            while not out:
                # If my card is a card I could need
                if my_card <= hand_size:
                    # If that card index has not been flipped
                    if flipped[my_card - 1] == 0:
                        flipped[my_card - 1] = 1
                        # If that card is not equal to this position
                        if hand[my_card - 1] != my_card:
                            # Swap my card and the card that was there
                            top_card = hand[my_card - 1]
                            hand[my_card - 1] = my_card
                            my_card = top_card
                            print(hand)
                            print("Swap Card: " + str(my_card))
                        else:
                            out = True
                    else:
                        out = True
                else:
                    out = True

                # Check if all cards have been flipped
                if check_hand(flipped):
                    print("Round " + str(hand_size) + " done in " + str(pos - hand_size))
                    out = True
                    ongoing = False
            discard = my_card
            done = True

# Check to see if the hand has won already
def check_hand(checker):
    sum = 0
    for i in range(0, len(checker)):
        sum += checker[i]

    # print(str(sum) + " / " + str(len(checker)))
    if sum == len(checker):
        return True
    else:
        return False



play_game()