from tkinter import *
import tkinter
from tkinter import messagebox
from random import randint
from graphics_rockpapersci import level_3
from GuessPassword import guess_password
from QUIZ_GAME import quiz_gam
from deck_of_cards import deck_cards

def main_game():
    user_window.destroy()           #destroying the registration window
    zombie=Tk()                     #creating game window with diff levels
    zombie.title("ZOMBIE DASH")
    zombie.geometry("650x642")
    zombie.resizable(height=False,width=False)      #restricting the player from changing window size
    click=''                        #initializing click to empty string
    level=1                         #initializing level to 1
    energy=4                        #setting initial energy =4

    #to store different images that will be used in game
    full=PhotoImage(file='energy_full.png')
    medium=PhotoImage(file='energy_meduim.png')
    half=PhotoImage(file='energy_half.png')
    low=PhotoImage(file='energy_low.png')
    img1=PhotoImage(file='11_1.png')
    img2=PhotoImage(file='11_2.png')
    img3=PhotoImage(file='11_3.png')
    img4=PhotoImage(file='11_4.png')
    background_label = Label(image=img1, anchor=NW)     #creating background of game window
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    energy_btn=Button(zombie,font=("Chiller",'18','bold'),image=full)   #creating energy bar in the window
    energy_btn.place(x=481,y=23)

    #to create and place button for each level
    button3=Button(zombie,bg="olivedrab2",font=("Chiller",'18','bold'),text="LEVEL 3",command=lambda:change_click('rockpapersci'))
    button3.place(x=340,y=488)
    button4=Button(zombie,bg="olivedrab2",font=("Chiller",'18','bold'),text="LEVEL 4",command=lambda:change_click('password'))
    button4.place(x=520,y=200)
    button1=Button(zombie,bg="olivedrab2",font=("Chiller",'18','bold'),text="LEVEL 1",command=lambda:change_click('quiz'))
    button1.place(x=80,y=457)
    button2=Button(zombie,bg="olivedrab2",font=("Chiller",'18','bold'),text="LEVEL 2",command=lambda:change_click('deck'))
    button2.place(x=180,y=252)

    def change_click(game_name):            #this function will run deoending on what button user selected
        nonlocal level,img2,img3,img4,energy,energy_btn
        click=game_name
        try_1=''                            #energy tries for level 1
        try_2=''                            #energy tries for level 2
        
        def energy_check():             #this function will change emergy bar depending on energy level
            if energy==0:               #if energy level becomes zero
                zombie.destroy()        #destroy game window
                energy_win=Tk()         #create new window to display end result
                energy_win.geometry('650x642')
                img=PhotoImage(file='gameLost.png')
                bg= Label(energy_win,image=img, anchor=NW)    #creating background image for result window
                bg.place(x=0, y=0)
                energy_win.mainloop()
            elif energy==1:
                energy_btn.configure(image=low)
            elif energy==2:
                energy_btn.configure(image=half)
            elif energy==3:
                energy_btn.configure(image=medium)
                    
        if click=='quiz' and level==1:          #if user clicks on level 1 button when game starts
            quiz_gam()                          #calling quiz game function
            level+=1                            #increasing level by 1
            try_1='end'                         #to check that user has tried this level
                
        elif click=='quiz' and level==2 and try_1!='end':   #if user presses click again when level is 2
            with open('score.txt','r') as score_file:       #opening score file to check score
                scores=score_file.readline()
            if scores!='':                                  #this will only work if file has some number stored in it
                if int(scores)< 20:                         #if score in level 1 is less then 20
                    energy-=1                               #decreasing energy by 1
                    quiz_gam()                              #calling quiz game again
                    energy_check()                          #to update energy bar
            else:                                           #if the score file is empty
                level-=1                                    #so that user can move onto first condition again

       
        elif level==2 and click=='deck':                    #if user clicks on level 2 button when level is 2
            with open('score.txt','r') as score_file:       #checking if user has cleared level 1
                scores=score_file.readline()
            if scores!='':
                if int(scores)>=20:                         #if score is atleast 20
                    level+=1                                #increasing level by 1
                    background_label.configure(image=img2)  #changing background image describing each level
                    deck_cards()                            #calling deck of cards game
 
            else:
                level-=1

        #working of level 3 and level 4 button is same as that of level 1 and level 2
        elif click=='rockpapersci' and level==3:            
            level_3()
            level+=1
            background_label.configure(image=img3)
            try_2=='end'
            
        elif click=='rockpapersci' and level==4 and try_2!='end':
            with open('score.txt','r') as score_file:
                scores=score_file.readline()
            if scores!='':
                if int(scores)< 20:
                    energy-=1
                    level_3()
                    energy_check()
                    
            else:
                level-=1       
                
        elif level==4 and click=='password':
            with open('score.txt','r') as score_file:
                scores=score_file.readline()
            if scores!='':
                if int(scores)>=20:
                    background_label.configure(image=img4)
                    zombie.destroy()
                    guess_password()

            else:
                level-=1
            
    zombie.mainloop()

def store_name(event=None):         #to store user name in a file 
    player_name=entry.get()         #to get username from entry
    with open('username.txt','w') as file:          #opening username file to store name
        file.write(player_name)
    entry.configure(state=DISABLED)                 #so user can not make any furthur changes in name
        
user_window=Tk()                    #creating registration window
data_file=open('username.txt','w')
data_file.close()
user_window.title('ZOMBIE DASH-START')
user_window.geometry('650x642')

start_photo=PhotoImage(file='start.png')    #to create background for registration window
background= Label(image=start_photo, anchor=NW)
background.place(x=0, y=0)

name=Label(user_window , bg='olivedrab3',font=("Chiller",'20','bold'),text='Enter Your Name:')
name.place(x=250,y=60)
entry=Entry(user_window , bg='olivedrab3',fg='red',font=("Chiller",'20','bold'))        #to get name from player
entry.place(x=200,y=100)
entry.bind('<Return>',store_name )          #to store answer once user presses enter

#to create start button for registration window
Btn=Button(user_window,font=("Chiller",'20','bold'),text='Press to Start!',bg='olivedrab3',command=main_game)
Btn.place(x=260,y=524)
user_window.mainloop()

