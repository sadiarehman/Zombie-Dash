from tkinter import *
import random


class deck_cards():          
    def __init__(self):
        self.window = Toplevel()                            #to create a window on top of main window
        self.window.title("Deck of Cards")  
        self.window.resizable(width=False, height=False)    #window can not be resized
        self.window.geometry("500x450")

        self.suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']  #list of suits
        self.cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] #list of cards
        self.deck = []                                      #creates empty deck list 
        self.Score = 0                                      #initializing score to zero
        value = 1                                           #value of card
        for i in range(0, 4):                               # generates a deck of cards(with value for each card)                            
            for k in range(0, 13):
                if value > 13:
                    value = 1
                card = ([f"{self.cards[k]} of {self.suits[i]}", value]) #generates list of each card with name and value
                self.deck.append(card)                      #appending card list in deck list
                value += 1
        

        random.shuffle(self.deck)                           #to shuffle generated deck of cards

        self.score = Label(self.window, text="Score=0")     #to display score
        self.score.pack()
        self.card_one = self.deck.pop(0)                    # chooses first card
        
        # generates a deck of cards(with value for each card)
        self.card_two = None                                
        self.message = None
        self.option = None
        self.current_card = None
        self.nameofcard1 = self.card_one[0]                 #getting name of chosen card from its list          
        self.nameofcard2 = None

        photo = PhotoImage(file=f"{self.nameofcard1}.png")   
        self.l = Label(self.window, image=photo)            #displays image of current card    
        self.l.pack()

        #creating buttons for higher and lower option
        self.higher = Button(self.window, text="Higher", width='10',font=("Chiller","18","bold"), command=self.higher_button_pressed)
        self.higher.pack()
        self.lower = Button(self.window, text="Lower", width='10',font=("Chiller","18","bold"), command=self.lower_btn_pressed)
        self.lower.pack()

        #to display name of current card
        self.current_card = Label(self.window, text=f"Current card:{self.nameofcard1}",font=("Chiller",'18','bold'))
        self.current_card.pack()
        self.option = Label(self.window, text="Higher or Lower",font=("Chiller","18","bold"))
        self.option.pack()
        self.message = Label(self.window, text="")      #initializes the message label
        self.message.pack()

        self.deckofcards()                              #calling the function
        self.window.mainloop()

    def nextcard(self):                                 #to update name of current card
        self.current_card.configure(text=f"Current Card={self.nameofcard2}",font=("Chiller",'18','bold'))
        
    def deckofcards(self):                              #to get name of card 1 and card 2
        self.nameofcard1 = self.card_one[0]
        self.card_two = self.deck.pop(0)                #chooses next card
        self.nameofcard2 = self.card_two[0]

    def score_update(self,Score):                   #to update score
        self.score.configure(text=f"Score:{Score}")
        self.score['bg'] = 'light blue'

    def higher_button_pressed(self):                #if user presses the higher button

        if self.card_two[1] > self.card_one[1]:     #if value of next card is higher then the current card 

            self.message.configure(text="Correct choice!",font=("Chiller",'18','bold')) 
            self.message.pack()

            self.Score += 10                        #increasing score by 10 
            self.score_update(self.Score)           #calling function to update score

        elif self.card_two[1] < self.card_one[1]:   #if value of next card is less then the current card 
            self.message.configure(text="Wrong choice! Try again",font=("Chiller",'18','bold'))
            self.message.pack()

            self.score_update(self.Score)           

        else:                                       #if value of next card is equal to the current card 
            self.message.configure(text="Draw!Try again",font=("Chiller",'18','bold'))
            self.message.pack()

            self.score_update(self.Score)
        self.card_one = self.card_two               
        self.image()                                #updating image of card
        self.nextcard()                             #update name of card
        if self.Score < 30:                         #continue the game until score is equal to 30
            self.deckofcards()
        elif self.Score==30:
            self.lower.configure(state=DISABLED)        #to disable higher and lower button
            self.higher.configure(state=DISABLED)
            self.message.configure(text="Congratulations! You have won!",font=("Chiller",'18','bold'),foreground='red') #display end result
            self.end_btn=Button(self.window, text='Press to continue', font=("Chiller",'18','bold'),command=self.window.destroy)    #button to close the window
            self.end_btn.pack()

    def lower_btn_pressed(self):                #if user presses the lower button
        if self.card_two[1] < self.card_one[1]:         #if value of next card is lower then the current card
            self.message.configure(text="Correct choice!",font=("Chiller",'18','bold'))
            self.message.pack()
            self.Score += 10                            #increasing score by 10
            self.score_update(self.Score)               #updating score              
        elif self.card_two[1] > self.card_one[1]:       #if value of next card is higher then the current card
            self.message.configure(text="Wrong choice! Try again",font=("Chiller",'18',"bold"))
            self.message.pack()
            self.score_update(self.Score)
        else:                                           #if value of next card is equal to the current card
            self.message.configure(text="Draw!Try again",font=("Chiller",'18','bold'))
            self.message.pack()
            self.score_update(self.Score)
        self.card_one = self.card_two
        self.image()                                    #generating image of updated card                    
        self.nextcard()                                 #updating name of current card
        if self.Score < 30:                             #if score is less then 30 continue the game
            self.deckofcards()
        elif self.Score==30:                            #if score becomes equal to 30
            self.lower.configure(state=DISABLED)        #to disable higher and lower button
            self.higher.configure(state=DISABLED)
            self.message.configure(text="Congratulations! You have won!",font=("Chiller",'18','bold'),foreground='red')
            self.end_btn=Button(self.window, text='Press to continue', font=("Chiller",'18','bold'),command=self.window.destroy)
            self.end_btn.pack()


    def image(self):                                    #to generate image of updated card
        photo = PhotoImage(file=f"{self.nameofcard2}.png")
        self.l.configure(image=photo)
        self.l.image = photo
        self.l['bg'] = "light blue"
        return

    def congrats(self):                                 #to destroy the window
        self.window.destroy()

