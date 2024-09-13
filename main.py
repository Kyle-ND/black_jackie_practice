import random #hint
from blackjack_art import logo #Game logo

print(logo)

def main():
# TODO: Blackjack Game Implementation

# This module will simulate a simplified version of a Blackjack card game.

# Features to Implement:
# 1. Game Setup:
#    - Create a deck of 52 cards (without jokers) using standard suits and ranks.
#    - Shuffle the deck before dealing cards.

   dealer = []
   player = []

   for i in range(2):
      player.append(deal_card())
      dealer.append(deal_card())

   player_total = calculateValue(player)
   dealer_total = calculateValue(dealer)

   # players logic

  



   # dealers logic


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
      play = input("Type 'play' to play again or 'end' to end game. ")
      if play.lower() != "play":
         isGame = False


# 2. Player and Dealer Setup:
#    - Implement player and dealer hands.
#    - Each hand should be able to hold cards and calculate its total value.
#    - Aces can count as either 1 or 11, depending on the hand's value.

def calculateValue (hand):
   pass

# 3. Game Flow:
#    - Deal two cards to both the player and the dealer.
#    - Allow the player to "hit" (get another card) or "stand" (stop drawing cards).
#    - Dealer should follow the standard rules (e.g., hit until reaching 17 or higher).

def deal_card ():
   deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   return deck[random.randint(0, len(deck)-1)]

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


