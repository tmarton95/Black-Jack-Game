import random

""""
Creating / initalization deck:
"""
deck = {}
figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
colors = ['spade', 'heart', 'club', 'diamond']

for figs in figures:
    if figs in ['J', 'Q', 'K']:
        value = 10
    elif figs == 'A':
        value = 11
    else:
        value = int(figs)

    for cols in colors:
        id = cols + '_' + figs
        deck[id] = [figs, cols, value] 

deck_dealer = deck.copy()
card = random.choice(list(deck.items()))
card_dealer = random.choice(list(deck_dealer.items()))

score = 0
score_dealer = 0

used_cards = []
used_figures = []
used_cards_dealer = []
used_figures_dealer = []

"""
Start Game Loop:
"""

for i in range(52):
    score += card[1][-1]
    if score_dealer < 17:
        score_dealer += card_dealer[1][-1]

    if card[0] not in used_cards:
        del deck[card[0]]
        used_cards.append(card[0])
        used_figures.append(card[1][0])

    if card_dealer[0] not in used_cards_dealer:
        print(used_cards_dealer)
        del deck_dealer[card_dealer[0]]
        used_cards_dealer.append(card_dealer[0])
        used_figures_dealer.append(card[1][0])

    """
    For dealer:
    """
    print("===========\nDealer\n===========") 

    if score_dealer > 21 and 'A' in used_figures_dealer:
        score_dealer -= 10
        used_figures_dealer.remove('A')

    print(card_dealer[0], f" , Score: {score_dealer}")

    if score_dealer > 21:
        print("===========\n Dealer is over \n===========")
    elif score_dealer < 17:
        card_dealer = random.choice(list(deck_dealer.items()))

    print("-----------------------------------------------")
    """
    For Player:
    """
    print("===========\nPlayer\n===========")
    if score > 21 and 'A' in used_figures:
        score -= 10 
        used_figures.remove('A')

    print(card[0], f" , Score: {score}")

    if score > 21:
        print("===========\n Game over \n===========")
        break

    print("Do you want another card?")
    action = input()
    if action == 'n':
        break
    elif action == 'y':
        card = random.choice(list(deck.items()))

if action == 'n':
    if score > score_dealer and score_dealer < 22:
        print("\n---> You Win !! <---")
    elif score < score_dealer and score_dealer < 22:
        print("\n---> Dealer Win !! <---")
    elif score == score_dealer:
        print("\n---> Tie <---")
    elif score_dealer > 21:
        print("\n---> You Win !! <---")