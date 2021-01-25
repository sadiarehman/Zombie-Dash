from tkinter import *
from tkinter import messagebox
from random import randint
def guess_password():
    global text
    rand1=randint(100,999)                                  #first three digits of the number will be generated
    rand4 = randint(0,9)                                    #contains the fourth digit which is to be guessed
    rand=str(rand1)+str(rand4)                              #combines the first 3 with the fourth digit
    rand=int(rand)                                          #converting into integer
    print(rand)
    game = Tk()                                             #creating level 4 window
    C = Canvas(game, height=50, width=100)                  #inserting background image
    filename = PhotoImage(file = "shelter.png")
    background_label = Label(image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    game.title("Guess The Password")
    game.option_add('*Font', 'Chiller 20')
    game.geometry("864x512")
    game.resizable(width=False , height=False)              #it will restrict the user from changing window size
    
    label = Label(game, bg='olivedrab4', fg='red', relief='flat',text=f"Guess The Complete Password |||{rand1}?||| \n Before The Zombies Eat You Alive")
    label.pack()
    entry = Entry(game,bg='olivedrab4',fg='red',width=20, borderwidth=4)    #user will guess the password here
    entry.pack()

    tries4=3                #initializing tries to 3

    def destroy_win(result):
        with open('username.txt' , 'r') as file:        #open userfile to get username
            name=file.readline()
        game.destroy()                                  #destroying level 4 window
        final_result=Tk()                               #creating final window to display result
        final_result.title('ZOMBIE DASH-END')
        final_result.geometry('650x642')
        final_result.resizable(width=False,height=False)     #it will restrict the user from changing final window size
        result_pic=PhotoImage(file='start.png')           #create background image for final window
        result_bg= Label(final_result, image=result_pic, anchor=NW)
        result_bg.place(x=0, y=0)
        
        if result=='won':       #if user correctly guessed the password within 3 tries
            result_label=Label(final_result,fg='red',bg='olivedrab3', font=("Chiller",'25','bold') , text=f'CONGRATULATIONS {name}!! You Escaped' )
            result_label.place(x=100,y=500)
        else:                   #if user was unable to guess the password
            result_label=Label(final_result,fg='red',bg='olivedrab3', font=("Chiller",'25','bold') , text=f'Unfortunately {name} You Didn\'t Survive The Apocalypse')
            result_label.place(x=30,y=500)
        
        final_result.mainloop()  
        
    def check_rand():
        nonlocal tries4
        
        answer = entry.get()            #to get the guessed number entered in the entry
        if answer.isdigit()==True:      #it only allows user to enter digits
            tries4-=1                   #with each turn tried will be decremented by 1
            if rand == int(answer):     #if user correctly guesses the number
                message.set("YOU HAVE MANAGED TO ESCAPE FROM THE ZOMBIES!!\n CONGRATULATIONS")
                destroy_win('won')
                
            elif tries4 == 0:           #if the user runs out of tries
                message.set("You are out of tries goodbye!")
                destroy_win('lost')     #calling function to destroy level 4 window and display result
                
            elif int(answer) < rand:    #user will be prompted to enter a higher number if the guessed number is lower
                message.set(f"Incorrect! - You have {tries4} remaining tries - Go higher!")
                entry.delete(0, END)
            elif int(answer) > rand:    #user will be prompted to enter a lower number if the guessed number is higher
                message.set(f"Incorrect! - You have {tries4} remaining tries- Go lower!")
                entry.delete(0, END)
        else:                           #if user enters non digit character tries will not be wasted
            pass

    #button to check entered number 
    button_check = Button(game,bg='olivedrab4',fg='red', text="Check", command=check_rand)
    button_check.pack()
    message = StringVar()    
    message.set("You have 3 tries! Good luck")
    answer_tries = Label(game,bg='olivedrab4',textvariable=message)
    answer_tries.pack()
    game.mainloop()






