import random as r

def calculateValue(hand):
    total = 0
    num_aces = 0
    for card in hand:
        total += int(card)
        if int(card) == 1:
            total += 10
            num_aces += 1

    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1
    return total


def deal_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[r.randint(0, len(cards) - 1)]

def main():
    '''
    # TODO: Blackjack Game Implementation

    # This module will simulate a simplified version of a Blackjack card game.

    # Features to Implement:
    # 1. Game Setup:
    #    - Create a deck of 52 cards (without jokers) using standard suits and ranks.
    #    - Shuffle the deck before dealing cards.

    # 2. Player and Dealer Setup:
    #    - Implement player and dealer hands.
    #    - Each hand should be able to hold cards and calculate its total value.
    #    - Aces can count as either 1 or 11, depending on the hand's value.

    # 3. Game Flow:
    #    - Deal two cards to both the player and the dealer.
    #    - Allow the player to "hit" (get another card) or "stand" (stop drawing cards).
    #    - Dealer should follow the standard rules (e.g., hit until reaching 17 or higher).

    # 4. Determine Outcomes:
    #    - Implement the winning conditions:
    #      - Player or dealer gets Blackjack (21 points with two cards).
    #      - Player or dealer busts (exceeds 21 points).
    #      - Player's hand is closer to 21 than the dealer's hand without going over.
    #    - Implement conditions for a push (tie).

    # 5. User Interface:
    #    - CLI interface for the game.
    #    - Display the player's hand, dealer's visible card, and game status.
    #    - Announce the winner at the end of each game.

    # 7. Code Optimizations and Error Handling:(BONUS NOT A MUST !!!)
    #    - Add input validation for player choices (hit or stand).
    #    - Handle edge cases (e.g., deck running out of cards).
    #    - Ensure proper game loop for continuous play.

    '''
    player = []
    dealer = []
    for i in range(2):
        player.append(deal_card())
        dealer.append(deal_card())
    player_total = calculateValue(player)
    dealer_total = calculateValue(dealer)

    if player_total == 21 or dealer_total == 21:
        if player_total == dealer_total:
            print(f"User_deck : {player} \n dealer_deck : {dealer} \nIt's a Draw")
        elif player_total == 21:
            print(f"User_deck : {player} \n dealer_deck : {dealer} \nBlackjack!, you win!")
        else:
            print(f"User_deck : {player} \n dealer_deck : {dealer} \nBlackjack!, you lose!")
    else:
        game_on = True
        while game_on:
            print(f"User_deck : {player} \n dealer_deck : {dealer[0]}")
            choice = input("Type 'h' to hit or 's' to stand ")
            if choice.lower() == 'h':
                player.append(deal_card())
                player_total = calculateValue(player)
            else:
                game_on = False
                if player_total < 17:
                    player.append(deal_card())
                    player_total = calculateValue(player)

            if player_total > 21:
                print(f"User_deck : {player} \ndealer_deck : {dealer} \nYou lose!")
                return
            elif player_total == 21:
                print(f"User_deck : {player} \ndealer_deck : {dealer} \nYou win!")
                return
        dealer_on = True
        while dealer_on:
            if dealer_total < 17:
                dealer.append(deal_card())
                dealer_total = calculateValue(dealer)
            elif dealer_total == 21:
                print(f"User_deck : {player} \ndealer_deck : {dealer} \nYou lose!")
                return
            elif dealer_total > 21:
                print(f"User_deck : {player} \ndealer_deck : {dealer} \nYou win!")
                return
            else:
                dealer_on = False

        if dealer_total == player_total:
            print(f"User_deck : {player} \ndealer_deck : {dealer} \nIt's a draw")
        elif dealer_total > player_total:
            print(f"User_deck : {player} \ndealer_deck : {dealer} \nYou lose")
        else:
            print(f"User_deck : {player} \ndealer_deck : {dealer} \nYou win!")


isGame = True

while isGame:
    main()
    play = input("Type 'y' to play again or 'end' to stop. ")
    if play.lower() != "play":
        isGame = False
