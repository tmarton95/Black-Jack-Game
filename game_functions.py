import random
from tkinter import messagebox
"""
Function definitions:
"""
def next_card(benefits_prop, deck_prop, canvas_main, label_score, label_score_dealer):
    # Place Dealer's card + update score:
    if benefits_prop.score_dealer < 17:
        card_dealer = random.choice(list(deck_prop.deck_dealer.items()))
        card_name_dealer = card_dealer[1][0] + "_" + card_dealer[1][1]
        benefits_prop.score_dealer += card_dealer[1][-1]

        # Delete Dealer's card from deck:
        del deck_prop.deck_dealer[card_dealer[0]]
        deck_prop.used_figures_dealer.append(card_dealer[1][0])

        if benefits_prop.score_dealer == card_dealer[1][-1]:
            deck_prop.hidden_card_value = card_dealer[1][-1]
            canvas_main.create_image(70, 350, image = deck_prop.card_back, anchor = 'center')
        else:
            card_pic_dealer = deck_prop.cards_pics[card_name_dealer]
            canvas_main.create_image(70 + deck_prop.x_shift, 350, image = card_pic_dealer, anchor = 'center')

    # Modify Dealer's score:
    elif benefits_prop.score_dealer > 21 and 'A' in deck_prop.used_figures_dealer:
        benefits_prop.score_dealer -= 10
        deck_prop.used_figures_dealer.remove('A')
    #-----------------------------------------------------
    # Place Player's card + update score:
    card = random.choice(list(deck_prop.deck.items()))
    card_name = card[1][0] + "_" + card[1][1]
    card_pic = deck_prop.cards_pics[card_name]
    canvas_main.create_image(70 + deck_prop.x_shift, 130, image = card_pic, anchor = 'center')
    benefits_prop.score += card[1][-1]

    # Delete Player's card from deck:
    del deck_prop.deck[card[0]]
    deck_prop.used_figures.append(card[1][0])

    # Modify Player's score and check game over:
    if benefits_prop.score > 21 and 'A' in deck_prop.used_figures:
        benefits_prop.score -= 10 
        deck_prop.used_figures.remove('A')

    # Plot scores:
    label_score.config(text = f"Score:  {str(benefits_prop.score)}")
    label_score_dealer.config(text = f"Score: ? + {str(benefits_prop.score_dealer - deck_prop.hidden_card_value)}")
    deck_prop.x_shift_count()
#--------------------------------------------------------------------------------
def stop_game(benefits_prop, button_next_card, button_stop):
    # When we lost:
    if benefits_prop.score > 21:
        messagebox.showinfo(title="GAME OVER", message = f"Dealer win!")

    # When we are under 21 (and also Dealer):
    elif benefits_prop.score_dealer < 21:
        # We win:
        if benefits_prop.score > benefits_prop.score_dealer:
            messagebox.showinfo(title="GAME OVER", message = f"You win!")
        # Black Jack (we win):
        elif benefits_prop.score == 21:
            messagebox.showinfo(title="GAME OVER", message = f"You win!")
        # Dealer win:
        elif benefits_prop.score < benefits_prop.score_dealer:
            messagebox.showinfo(title="GAME OVER", message = f"Dealer win!")
        # Equal scores:
        elif benefits_prop.score == benefits_prop.score_dealer:
            messagebox.showinfo(title="GAME OVER", message = f"Tie!")

    # Double black jack:
    if benefits_prop.score == 21 and benefits_prop.score_dealer == 21:
            messagebox.showinfo(title="GAME OVER", message = f"Tie!")
    elif benefits_prop.score != 21 and benefits_prop.score_dealer == 21:
            messagebox.showinfo(title="GAME OVER", message = f"Dealer win!")

    # Buttons deactivated:
    button_next_card.config(state = "disabled")
    button_stop.config(state = "disabled")
#--------------------------------------------------------------------------------
def new_game(button_next_card, button_stop, canvas_main, deck_prop, benefits_prop, label_score, label_score_dealer):
    button_next_card.config(state = "normal")
    button_stop.config(state = "normal")
    canvas_main.delete("all")
    deck_prop.new_game()
    benefits_prop.score = 0
    benefits_prop.score_dealer = 0
    label_score.config(text = "Score:  0")
    label_score_dealer.config(text = "Score:  0")
#--------------------------------------------------------------------------------