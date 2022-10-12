import random
from tkinter import messagebox

"""
Function definitions:
"""
def next_card_dealer(benefits_prop, deck_prop, canvas_main, label_score_dealer):
    if benefits_prop.bet_current != 0:
        # Place Dealer's card + update score (stop criteria for dealer: 15 point):
        if benefits_prop.score_dealer < 15:
            card_dealer = random.choice(list(deck_prop.deck_dealer.items()))
            card_name_dealer = card_dealer[1][0] + "_" + card_dealer[1][1]
            benefits_prop.score_dealer += card_dealer[1][-1]

            # Delete Dealer's card from deck:
            del deck_prop.deck_dealer[card_dealer[0]]
            deck_prop.used_figures_dealer.append(card_dealer[1][0])

            # Note + place hidden card:
            if len(deck_prop.deck_dealer) == 51:
                deck_prop.hidden_card_name = card_name_dealer
                deck_prop.hidden_card_value = card_dealer[1][-1]
                canvas_main.create_image(70, 350, image = deck_prop.card_back, anchor = 'center')
            else:
                card_pic_dealer = deck_prop.cards_pics[card_name_dealer]
                canvas_main.create_image(70 + deck_prop.x_shift, 350, image = card_pic_dealer, anchor = 'center')

        # Modify Dealer's score:
        if benefits_prop.score_dealer > 21 and 'A' in deck_prop.used_figures_dealer:
            benefits_prop.score_dealer -= 10
            deck_prop.used_figures_dealer.remove('A')
        # Plot score:
        label_score_dealer.config(text = f"Score: ? + {str(benefits_prop.score_dealer - deck_prop.hidden_card_value)}")
#--------------------------------------------------------------------------------
def next_card_player(benefits_prop, deck_prop, canvas_main, label_score):
    if benefits_prop.bet_current != 0:
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

        # Plot score:
        label_score.config(text = f"Score:  {str(benefits_prop.score)}")
        
        deck_prop.x_shift_count()

        benefits_prop.button_add.config(state = "disabled")
        benefits_prop.button_minus.config(state = "disabled")
#--------------------------------------------------------------------------------
def stop_game(benefits_prop, deck_prop, canvas_main, button_next_card, button_stop, label_score_dealer):
    # Placing remaining cards from Dealer: ---------------------------------------
    while benefits_prop.score_dealer < 15 or 'A' in deck_prop.used_figures_dealer:
        # Check if Dealer has Black Jack:
        if benefits_prop.score_dealer == 21:
            break
        else:
            # Place Dealer's card + update score:
            if benefits_prop.score_dealer < 15:
                card_dealer = random.choice(list(deck_prop.deck_dealer.items()))
                card_name_dealer = card_dealer[1][0] + "_" + card_dealer[1][1]
                card_pic_dealer = deck_prop.cards_pics[card_name_dealer]
                canvas_main.create_image(70 + deck_prop.x_shift, 350, image = card_pic_dealer, anchor = 'center')
                benefits_prop.score_dealer += card_dealer[1][-1]

                # Delete Dealer's card from deck:
                del deck_prop.deck_dealer[card_dealer[0]]
                deck_prop.used_figures_dealer.append(card_dealer[1][0])

            # Modify Dealer's score:
            if benefits_prop.score_dealer > 21 and 'A' in deck_prop.used_figures_dealer:
                benefits_prop.score_dealer -= 10
                deck_prop.used_figures_dealer.remove('A')
            # Plot score:
            label_score_dealer.config(text = f"Score: ? + {str(benefits_prop.score_dealer - deck_prop.hidden_card_value)}")
    #-------------------------------------------------------------------------
    # Show hidden card + score label update
    card_pic_hidden = deck_prop.cards_pics[deck_prop.hidden_card_name]
    canvas_main.create_image(70, 350, image = card_pic_hidden, anchor = 'center')
    label_score_dealer.config(text = 'Score: ' + str(benefits_prop.score_dealer))

    # ------ Cases for end of game: ------
    # Black Jack (we win):
    benefits_prop.win_flag = True if benefits_prop.score == 21 else False
        
    # Double black jack:
    if benefits_prop.score == 21 and benefits_prop.score_dealer == 21:
            benefits_prop.win_flag = None

    # When we are under 21:
    if benefits_prop.score < 21:
        # And also Dealer:
        if benefits_prop.score_dealer < 21:
            # We win:
            if benefits_prop.score > benefits_prop.score_dealer:
                benefits_prop.win_flag = True
            # Equal scores:
            elif benefits_prop.score == benefits_prop.score_dealer:
                benefits_prop.win_flag = None
        # But Dealer above 21:
        elif benefits_prop.score_dealer > 21:
            benefits_prop.win_flag = True

    # When we are above 21 (and also Dealer):
    if benefits_prop.score_dealer > 21 and benefits_prop.score > 21 and (
        benefits_prop.score_dealer < benefits_prop.score):
        benefits_prop.win_flag = True

    # Update game status: ---------------------
    if benefits_prop.win_flag:
        messagebox.showinfo(title="GAME OVER", message = "You win!")
        benefits_prop.remained_money += benefits_prop.bet_current
        benefits_prop.label_total.config(text = str(benefits_prop.remained_money) + ' $')

    elif benefits_prop.win_flag == False:
        messagebox.showinfo(title="GAME OVER", message = "Dealer win!")
        benefits_prop.bet_current = 0
        benefits_prop.label_bet.config(text = '0 $')

    elif benefits_prop.win_flag == None:
        messagebox.showinfo(title="GAME OVER", message = "Tie!")

    # Buttons deactivated:
    button_next_card.config(state = "disabled")
    button_stop.config(state = "disabled")
    benefits_prop.button_add.config(state = "normal")
    benefits_prop.button_minus.config(state = "normal")
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