from tkinter import*
from tool_classes import Decks, Benefits
from game_functions import next_card, stop_game, new_game
#---------------------------------------------------------------------------------------
"""
Initial properties:
"""
window = Tk()
window.title("Black Jack")
window.geometry('740x440')

canvas_main = Canvas(window, width = 740, height = 440, bg = "green")
canvas_main.pack()
#---------------------------------------------------------------------------------------
deck_prop = Decks()
benefits_prop = Benefits(window)
#---------------------------------------------------------------------------------------
"""
Layout properties:
"""
label_player = Label(window, text = "Player", font = ('Verdana', 16), bg = "green")
label_player.place(x = 50, y= 30, anchor = 'center')

label_dealer = Label(window, text = "Dealer", font = ('Verdana', 16), bg = "green")
label_dealer.place(x = 50, y= 235, anchor = 'center')

label_score = Label(window, text = "Score:  0", font = ('Verdana', 14), bg = "green")
label_score.place(x = 200, y= 25, anchor = 'center')

label_score_dealer = Label(window, text = "Score:  0", font = ('Verdana', 14), bg = "green")
label_score_dealer.place(x = 200, y= 235, anchor = 'center')
#------------------------------------------------
# Bets:
label_bet_title = Label(window, text = "Current Bet:", font = ('Times New Roman', 12), bg = 'grey', borderwidth = 1, relief = 'solid', width = 22)
label_bet_title.place(x = 525, y= 100)

label_bet = Label(window, text = "100 $", font = ('Times New Roman', 15), bg = 'white', borderwidth = 3, relief = 'ridge', width = 17)
label_bet.place(x = 530, y= 130)
#--------------------------------------------------------------------
"""
Button properties:
"""
button_next_card = Button(window, text = 'Next Card', font = ('Helvetia', 14), background="lightblue", 
                    command = lambda: next_card(benefits_prop, deck_prop, canvas_main, label_score, label_score_dealer))
button_next_card.place(x = 525, y = 8)

button_stop = Button(window, text = 'Stand', font = ('Helvetia', 14), background="lightblue", width = 8, 
                    command = lambda: stop_game(benefits_prop, button_next_card, button_stop))
button_stop.place(x = 635, y = 8)

button_newgame = Button(window, text = 'New Game', font = ('Helvetia', 11), background="orange", width = 22, height = 1, 
                    command = lambda: new_game(button_next_card, button_stop, canvas_main, deck_prop,benefits_prop, label_score, label_score_dealer))
button_newgame.place(x = 525, y = 52)
#-----------------
window.mainloop()