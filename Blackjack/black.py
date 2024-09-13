import numpy as np
import random as rand

# region main
run_main = True

if run_main:

  Face_value = list(range(2,11,1))
  Ten_value = ['Q', 'K', 'J']
  Ace = ['A']
  Deck_cards = np.concatenate((Face_value, Ten_value, Ace), dtype = object)
  # print(f'Deck cards is {Deck_cards}')

  def deal (hand, deck, num_picks):
    pick = None
    for _ in range(num_picks):
      pick = rand.choice(deck)
      pick = 10 if pick in Ten_value else 11 if pick == Ace[0] else pick
      hand.append(pick)
    
    hand_sum = np.sum(hand)

    if 11 in hand and hand_sum > 21: 
      hand.remove(11)
      hand.append(1)
      hand_sum = np.sum(hand)
    
    return hand, hand_sum
  
  def play_again():
    attempts = 3
    user_input = input(f'Do you want to play again "Yes" or "No"\n: ')
    user_input = user_input.lower()

    if user_input != 'no' and user_input != 'yes':
      for n in range(attempts):
        user_input = input(f'Do you want to play again "Yes" or "No"\n {n - 1} attempts left: ')
        
        if user_input == 'yes': break

        if n == attempts or user_input == 'no' : 
          print(f'Game finished')
          exit()
      
      return None

  def display_hands():
    print(f'Player card are {player} and the sum is {player_sum}')
    print(f'Dealer card are {dealer} and the sum is {dealer_sum}')

  player = []
  dealer = []

  player, player_sum = deal(player, Deck_cards, 2)
  dealer, dealer_sum = deal(dealer, Deck_cards, 2)
  if player_sum == 21: print('Blackjack YOU WON!')

  print(f'Player card are {player} and the sum is {player_sum}')
  print(f'Dealer card are [{min(dealer)}:###]')

  while True: 
    user_input = input(f'Do you want to Hit or Stand?\n: ')
    user_input = user_input.lower()

    if user_input != 'hit' and user_input!= 'Stand': 
      print(f'Please type either "Hit" or "Stand"')
    
    if user_input == 'hit':
      player, player_sum = deal(player, Deck_cards, 1)
      dealer, dealer_sum = deal(dealer, Deck_cards, 1)

      display_hands()

      if player_sum == 21: print('Blackjack YOU WON!')
      if player_sum > 21: 
        print(f'You have lost')
      break

    elif user_input == 'Stand':
      display_hands()
      if player_sum == 21: print('Blackjack YOU WON!')
      if player_sum > 21: 
        print(f'You have lost')

      elif dealer_sum < 17:
        dealer, dealer_sum = deal(dealer, Deck_cards, 1)

    display_hands()
    
    if player_sum == dealer_sum: print('Draw')
    if player_sum > dealer_sum: print('You won')
    else: print('You lose')




  # return hand, hand_sum
  
  # player, player_sum = deal(player, Deck_cards, 2)
  # print(f'Player card are {player} and the sum is {player_sum}')

# endregion

# region Test
test_run = False
if test_run:
  hand = []
  for _ in range(3):
    list_ = ['A', 1, 2 , 3, 5]
    pick = rand.choice(list_)
    pick = 33 if pick == 'A' else pick
    hand.append(pick)
  print(hand)
# endregion

num = None
val = 'a'

if val == 'a': 
  num = 10
else: num = 8

num = 10 if val == 'a' else 8

#####

# val = []
# for n in range(11):
#   val.append(n)

# val = [n for n in range(11)]

list_1 = [1, 3, 4, 3]

min_val = min(list_1)

list_1 = np.array(list_1)

min_val = np.min(list_1)
min_val = list_1.min()

# list_1.remove(3)
# # list.pop(2)


# print(list_1)
