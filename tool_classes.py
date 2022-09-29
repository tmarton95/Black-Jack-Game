from tkinter import PhotoImage, Button
""""
Creating / initalization deck:
"""
class Decks():
    def __init__(self):
        # Creating decks + images:
        deck_initial = {}
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
                deck_initial[id] = [figs, cols, value]
        #----------------------------------------------
        cards_pics = {}
        for figs in figures:
            for cols in colors:
                card_id = figs + '_' + cols
                filename = "card_pics\\"  + card_id + ".png"
                card_pic = PhotoImage(file = filename)
                cards_pics[card_id] = card_pic
        #------------------------------------------------------------------
        self.cards_pics = cards_pics
        self.card_back = PhotoImage(file = "card_pics\\card_back.png")
        self.deck_initial = deck_initial
        self.deck = deck_initial.copy()
        self.deck_dealer = deck_initial.copy()
        self.x_shift = 0
        self.x_shift_dealer = 0
        self.used_figures = []
        self.used_figures_dealer = []
        self.hidden_card_value = 0

    def x_shift_count(self):
        if self.x_shift >= 3*130:
            self.x_shift = 30
        else: 
            self.x_shift += 130

        if self.x_shift_dealer >= 3*130:
            self.x_shift_dealer = 30
        else: 
            self.x_shift_dealer += 130

    def new_game(self):
        # Update variables:
        self.x_shift = 0
        self.x_shift_dealer = 0
        self.deck = self.deck_initial.copy()
        self.deck_dealer = self.deck_initial.copy()
        self.used_figures = []
        self.used_figures_dealer = []
        self.hidden_card_value = 0


class Benefits():
    def __init__(self, window):
        self.score = 0
        self.score_dealer = 0
        self.bet_current = 0
        self.remained_money = 1000

        self.button_raise_1 = Button(window, text = "200 $", font = ('Times New Roman', 13), bg = 'lightgrey', borderwidth = 3, relief = 'ridge', width = 12, height = 1,
                                    command = self.raise1)
        self.button_raise_1.place(x = 530, y= 180)

        self.button_raise_2= Button(window, text = "100 $", font = ('Times New Roman', 13), bg = 'lightgrey', borderwidth = 3, relief = 'ridge', width = 12, height = 1,
                                    command = self.raise2)
        self.button_raise_2.place(x = 530, y= 225)

        self.button_raise_3= Button(window, text = "25 $", font = ('Times New Roman', 13), bg = 'white', borderwidth = 3, relief = 'ridge', width = 12, height = 1,
                                    command = self.raise3)
        self.button_raise_3.place(x = 530, y= 270)

        self.button_add = Button(window, text = "+", font = ('Arial', 18, 'bold'), bg = 'lightgrey', borderwidth = 2, relief = 'ridge', height = 1, width = 2)
        self.button_add.place(x = 680, y= 180)

        self.button_cut = Button(window, text = "-", font = ('Arial', 18, 'bold'), bg = 'lightgrey', borderwidth = 2, relief = 'ridge', height = 1, width = 2)
        self.button_cut.place(x = 680, y= 255)

    def raise1(self):
        self.button_raise_1.config(bg = 'white')
        self.button_raise_2.config(bg = 'lightgrey')
        self.button_raise_3.config(bg = 'lightgrey')

    def raise2(self):
        self.button_raise_1.config(bg = 'lightgrey')
        self.button_raise_2.config(bg = 'white')
        self.button_raise_3.config(bg = 'lightgrey')

    def raise3(self):
        self.button_raise_1.config(bg = 'lightgrey')
        self.button_raise_2.config(bg = 'lightgrey')
        self.button_raise_3.config(bg = 'white')