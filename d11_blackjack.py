import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_score = sum(player_cards)
dealer_cards = []
game_state = True
does_player_have_ace = ""

def blackjack_check(player_card_check, dealer_card_check):
    if sum(player_card_check) == 21:
        print("BlackJack! You win!")
    if sum(dealer_card_check) == 21:
        print("Dealer has BlackJack! You Loose!")

def score_checker(player_score_check,):
    if player_score_check > 22:
        does_player_have_ace = player_cards.index[11]
        if does_player_have_ace == 0 or 1:
            player_cards[does_player_have_ace] = 1

#        hit_or_stand = input("Would you like to Hit or Stand?").lower()
#        if hit_or_stand == "hit":
#            player_cards.append(random.choice(cards))

print("Welcome to BlackJack!")
while game_state == True:
    game_state = input("Do you want to play a game of BlackJack? Y or N\n").lower()
    if game_state == "y":
        game_state = True
    player_cards = []
    dealer_cards = []
#    player_cards.extend([random.choice(cards), random.choice(cards)])
    player_cards.extend([11, 12])
    dealer_cards.extend([random.choice(cards), random.choice(cards)])

    print(f"Your card's are: {player_cards} with a scrore of {sum(player_cards)}")
    print(f"The dealer's card is: {dealer_cards[0]}")

    blackjack_check(player_cards, dealer_cards)
    score_checker(player_score)
    player_score = sum(player_cards)

    print(player_cards)
    print(player_score)
    print(dealer_cards)
    print(game_state)
