import random #hint
from blackjack_art import logo #Game logo


def main():
      tens = ['king','queen','jack']
      others = [2, 3, 4, 5, 6, 7, 8, 9, 10]
      cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'king','queen','jack', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'king','queen','jack', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'king','queen','jack', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'king','queen','jack']
      cards_length = len(cards)
      dealer = [cards[random.randint(0,cards_length)], cards[random.randint(0,cards_length)]]
      player = [cards[random.randint(0,cards_length)], cards[random.randint(0,cards_length)]]

      def get_points(person):
         points = 0
         for card in person:
            if card in tens:
                  points += 10
            elif card in others:
                  points += card
            else:
                  if points <= 10:
                     points += 11
                  else:
                     points += 1
         return points

      choice = "deal"

      while choice == "deal":
         print(f"Dealer = [{dealer[0]}] \nPlayer = {player}")
         player_points, dealer_points  = get_points(player), get_points(dealer)

         answer = input("Would you like to deal or pass? ").lower().replace(" ","")

         if answer == 'deal' or player_points < 17:
            player.append(cards[random.randint(0,cards_length)])

         else:
            if player_points > 21 or dealer_points > player_points:
               print("You lost :(")
            elif player_points == 21:
               print("BlackJackkkk!!!")
            elif player_points > dealer_points:
               print("You win :)")
               break
            elif player_points == dealer_points:
               print("It's a draw :/")
      choice = answer

print(logo)
main()