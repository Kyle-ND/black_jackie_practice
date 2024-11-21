import random #hint
from blackjack_art import logo #Game logo

card_suits = ["Hearts","Clubs","Diamonds","Spades"]
card_ranks= ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
deck = []
def points(person):
   my_value = 0
   my_a = 0
   for char in person:
      if type(char) == str:
         point == char.lower()
         if point in ["king","queen","jack"]:
            my_value += 10
         elif point == 'ace':
            my_value += 11
            my_a += 1
         elif type(char) == int:
            my_value += char
            while my_value > 21 and my_a:
               my_value -= 10
               my_a -= 1
   return my_value
            
def main():
   for suits in card_suits:
      for rank in card_ranks:
         deck.append([suits,rank])
   count = len(deck)
   player = [deck[random.randint(0,count)],deck[random.randint(0,count)]]
   dealer = [deck[random.randint(0,count)],deck[random.randint(0,count)]]
   
   choice = "deal"
   
   while choice == "deal":
      print(f"Dealer = [{dealer[0]}] \nPlayer = {player}")
      player_points, dealer_points = points(player), points(dealer)
      
      answer = input("Would you like to deal or pass? ").lower().replace(" ","")
      if answer == 'deal' or player_points < 17:
         player.append(deck[random.randint(0,count)])
      else:
         if player_points > 21 or dealer_points > player_points:
            print("You lost the game.")
            break
         elif player_points == 21:
            print("Player BlackJack.")
         elif dealer_points == 21:
            print("Dealer BlackJack.")
         elif player_points > dealer_points:
            print("You win the game.")
            break
         elif player_points == dealer_points:
            print("It is Tie.")
            
   choice = answer
 
 
 
"""TODO: Blackjack Game Implementation

This module will simulate a simplified version of a Blackjack card game.

Features to Implement:
1. Game Setup:
   - Create a deck of 52 cards (without jokers) using standard suits and ranks.
   - Shuffle the deck before dealing cards.

2. Player and Dealer Setup:
   - Implement player and dealer hands.
   - Each hand should be able to hold cards and calculate its total value.
   - Aces can count as either 1 or 11, depending on the hand's value.

3. Game Flow:
   - Deal two cards to both the player and the dealer.
   - Allow the player to "hit" (get another card) or "stand" (stop drawing cards).
   - Dealer should follow the standard rules (e.g., hit until reaching 17 or higher).

4. Determine Outcomes:
   - Implement the winning conditions:
     - Player or dealer gets Blackjack (21 points with two cards).
     - Player or dealer busts (exceeds 21 points).
     - Player's hand is closer to 21 than the dealer's hand without going over.
   - Implement conditions for a push (tie).

5. User Interface:
   - CLI interface for the game.
   - Display the player's hand, dealer's visible card, and game status.
   - Announce the winner at the end of each game.


7. Code Optimizations and Error Handling:(BONUS NOT A MUST !!!)
   - Add input validation for player choices (hit or stand).
   - Handle edge cases (e.g., deck running out of cards).
   - Ensure proper game loop for continuous play.

"""



print(logo)
main()