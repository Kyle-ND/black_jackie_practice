import random #hint
from blackjack_art import logo #Game logo


def main():
   # 1.

   suits = ['Hearts','Diamond','Clubs','Spades']
   ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

   deck = []

   for suit in suits:
      for rank in ranks:
         deck.append(f'{rank} of {suit}')
   random.shuffle(deck)

   # 2.
   def deal_cards(deck, hand):

    card = deck.pop()
    hand.append(card)

   def calculate_hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]

        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            has_ace = True
            value += 11

    if has_ace and value > 21:
        value -= 10

    return value
   
   # 3.
   player_hand = []
   dealer_hand = []

   deal_cards(deck, player_hand)
   deal_cards(deck, player_hand)
   deal_cards(deck, dealer_hand)
   deal_cards(deck, dealer_hand)

   while True:
      print(f'Player hand: {player_hand} ({calculate_hand_value(player_hand)})')
      print(f'Dealer hand: [{dealer_hand[0]}, <face down>]')

      if calculate_hand_value(player_hand) > 21:
         print('Player busts!')
         break

      action = input('Do you want to hit or stand? ')

      if action.lower() == 'hit':
         deal_cards(deck, player_hand)
      else:
         break

   print(f'Player hand: {player_hand} ({calculate_hand_value(player_hand)})')
   print(f'Dealer hand: {dealer_hand} ({calculate_hand_value(dealer_hand)})')

   if calculate_hand_value(player_hand) > 21:
      print('Player busts!')
   elif calculate_hand_value(dealer_hand) > 21:
      print('Dealer busts! Player wins!')
   elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
      print('Player wins!')
   elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
      print('Dealer wins!')
   else:
      print('Push!')

   
     
"""
TODO: Blackjack Game Implementation

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