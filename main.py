from tkinter import*
from tool_classes import Decks, Benefits
from game_functions import next_card_dealer, next_card_player, stop_game, new_game
#---------------------------------------------------------------------------------------
"""
Initial properties:
"""
window = Tk()
window.title("Black Jack")
window.geometry('740x448')
window.configure(bg = 'green')
window.configure(relief='ridge', borderwidth=1)

window.call('wm', 'iconphoto', window._w, PhotoImage(file = "card_pics\\J_spade.png"))

canvas_table = Canvas(window, width = 510, height = 440, bg = "green", relief='ridge', borderwidth=0.75)
canvas_table.place(x = 0, y= 0)

canvas_table.create_line(5, 215, 511, 215, width = 2, fill = 'darkgrey')
#---------------------------------------------------------------------------------------
"""
Layout properties:
"""
label_player = Label(window, text = "Player", font = ('Verdana', 16, "italic"), bg = "green")
label_player.place(x = 55, y= 25, anchor = 'center')

label_dealer = Label(window, text = "Dealer", font = ('Verdana', 16, "italic"), bg = "green")
label_dealer.place(x = 55, y= 245, anchor = 'center')

label_score = Label(window, text = "Score:  0", font = ('Verdana', 13), bg = "green")
label_score.place(x = 200, y= 25, anchor = 'center')

label_score_dealer = Label(window, text = "Score:  0", font = ('Verdana', 13), bg = "green")
label_score_dealer.place(x = 200, y= 245, anchor = 'center')

# Bets:
label_bet_title = Label(window, text = "Current Bet:", font = ('Times New Roman', 12), bg = 'grey', borderwidth = 1, relief = 'solid', width = 21)
label_bet_title.place(x = 530, y= 100)

label_total_title = Label(window, text = "Total Cash:", font = ('Times New Roman', 12), bg = 'grey', borderwidth = 1, relief = 'solid', width = 21)
label_total_title.place(x = 530, y= 320)
#---------------------------------------------------------------------------------------
"""
Instances of classes:
"""
deck_prop = Decks()
benefits_prop = Benefits(window)
#---------------------------------------------------------------------------------------
"""
Button properties:
"""
button_next_card = Button(window, text = 'Next Card', font = ('Helvetia', 14), background="lightblue", 
                    command = lambda: [next_card_dealer(benefits_prop, deck_prop, canvas_table, label_score_dealer), 
                                        next_card_player(benefits_prop, deck_prop, canvas_table, label_score)])
button_next_card.place(x = 525, y = 8)

button_stop = Button(window, text = 'Stand', font = ('Helvetia', 14), background="lightblue", width = 8, 
                    command = lambda: stop_game(benefits_prop, deck_prop, canvas_table, button_next_card, button_stop, label_score_dealer))
button_stop.place(x = 635, y = 8)

button_newgame = Button(window, text = 'New Game', font = ('Helvetia', 11), background="orange", width = 22, height = 1, 
                    command = lambda: new_game(button_next_card, button_stop, canvas_table, deck_prop, benefits_prop, label_score, label_score_dealer))
button_newgame.place(x = 525, y = 52)
#-----------------
window.mainloop()