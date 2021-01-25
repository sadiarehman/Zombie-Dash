from tkinter import *
from tkinter.font import BOLD
import random

def level_3():
    window=Toplevel()    #creating window for level 3
    window.title('ROCK PAPER SCISSORS')
    window.resizable(width=False , height=False)   #it will restrict the user from changing slide size
    window.configure(bg="black")

    click=True       #initializing click to True
    tries=3         #setting total number of tries to 3
    score=0         #initializing score to zero

    #storing different images
    rHand=PhotoImage(file='rockHand.png')
    pHand=PhotoImage(file='paperHand.png')
    sHand=PhotoImage(file='scissorHand.png')
   
    win=PhotoImage(file='win.png')
    lose=PhotoImage(file='lose.png')
    tie=PhotoImage(file='tie.png')

    #defining variables for buttons
    rHandButton=''
    pHandButton=''
    sHandButton=''

    #creating buttons to display options score,result and tries to user
    your_pick=Button(window, text='ROCK' ,font=('chiller',15,BOLD))
    comp_pick=Button(window,text='PAPER',font=('chiller',15,BOLD))
    end=Button(window,text='SCISSOR',font=('chiller',15,BOLD))
    try_button=Button(window,text='TRIES:3',font=('chiller',15,BOLD))
    score_btn=Button(window,text='SCORE:0',font=('chiller',15,BOLD))

    def play():     #function that will genrate buttons and perform appropriate tasks when pressed
        nonlocal rHandButton,pHandButton,sHandButton,your_pick,comp_pick,end,try_button,score_btn

        rHandButton=Button(window,image=rHand,command=lambda:youPick('rock'))   
        pHandButton=Button(window,image=pHand,command=lambda:youPick('paper'))
        sHandButton=Button(window,image=sHand,command=lambda:youPick('scissor'))

        #placing buttons in window
        rHandButton.grid(row=1, column=0)
        pHandButton.grid(row=1, column=1)
        sHandButton.grid(row=1, column=2)
        your_pick.grid(row=0,column=0)
        comp_pick.grid(row=0,column=1)
        end.grid(row=0,column=2)
        try_button.grid(row=2,column=0,columnspan=3)
        score_btn.grid(row=3,column=0,columnspan=3)

    def youPick(yourChoice):        #function to compare user selected option with computer selected
        nonlocal click , tries,score
        compPick=random.choice(['rock','paper','scissor'])  #picking random option from list
        
        if click==True and tries>0:                     
            your_pick.configure(text='YOU CHOSE:')      #updating options to selected option and result
            comp_pick.configure(text='COMPUTER CHOSE:')
            end.configure(text='RESULT:')
            
            if yourChoice=='rock':          
                if compPick=='rock':        #if user and computer select same option
                    pHandButton.configure(image=rHand)
                    sHandButton.configure(image=tie)
                    click=False             #click changes to false after each try
                elif compPick=='paper':     #if computer wins
                    pHandButton.configure(image=pHand)
                    sHandButton.configure(image=lose)
                    tries-=1                #decrementing tries by 1
                    click=False
                else:                       #if user wins
                    pHandButton.configure(image=sHand)
                    sHandButton.configure(image=win)
                    tries-=1                #decrementing tries by one
                    score+=10               #increasing score by 10
                    click=False

            #working of user selecting paper or scissor is same as user selecting rock
            elif yourChoice=='paper':   
                rHandButton.configure(image=pHand)
                if compPick=='rock':        
                    pHandButton.configure(image=rHand)
                    sHandButton.configure(image=win)
                    tries-=1
                    score+=10
                    click=False
                elif compPick=='paper':
                    pHandButton.configure(image=pHand)
                    sHandButton.configure(image=tie)
                    click=False
                else:
                    pHandButton.configure(image=sHand)
                    sHandButton.configure(image=lose)
                    tries-=1
                    click=False
            
            elif yourChoice=='scissor':
                rHandButton.configure(image=sHand)
                if compPick=='rock':
                    pHandButton.configure(image=rHand)
                    sHandButton.configure(image=lose)
                    tries-=1
                    click=False
                elif compPick=='paper':
                    pHandButton.configure(image=pHand)
                    sHandButton.configure(image=win)
                    tries-=1
                    score+=10
                    click=False
                else:
                    pHandButton.configure(image=sHand)
                    sHandButton.configure(image=tie)
                    click=False

            try_button.configure(text=f'TRIES:{tries}')     #updating tries in try button
            score_btn.configure(text=f'SCORE:{score}')      #updating score in score button
            
        elif click==False and tries>0:                  #to change updated settings to initial settings for the next try
            if yourChoice=='rock' or yourChoice=='paper' or yourChoice=='scissor': #if the user presses any of the button

                #changing the button images to previous images
                your_pick.configure(text='ROCK')
                comp_pick.configure(text='PAPER')
                end.configure(text='SCISSOR')
                rHandButton.configure(image=rHand)
                pHandButton.configure(image=pHand)
                sHandButton.configure(image=sHand)
                click= True                                 #setting click to true 

        elif click==False and tries==0:                     #if user runs out of tries
            try_button.configure(text='YOU HAVE ZERO TRIES LEFT!!')
            score_btn.configure(text=f'SCORE:{score}')
            with open('score.txt','w') as file:             #opening score file to write final score
                file.write(f'{score}')
            end_btn=Button(window ,text='Press to continue' ,font=('chiller',15,BOLD),command=window.destroy)
            end_btn.grid(row=4,columnspan=3)

    play()                              


        


