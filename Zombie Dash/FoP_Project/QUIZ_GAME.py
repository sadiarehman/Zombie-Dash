from tkinter import *
import tkinter as tk

def quiz_gam():
    file=open('score.txt','w')              #to delete data in already present score file
    file.close()
    def easy_level():                       
        quiz_game.destroy()                 #destroying the menu window
        def counter():                      #function to update the score
            total.set(total.get() + 10)
        def answer(event=None):             
            ans=answer_1.get()              #get the answer entered by the user 
            if ans=='365':                  #if user enters correct answer  
                label=Label(easy_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.25,anchor='center')
                answer_1.configure(state=tk.DISABLED)   #once the player has entered his answer answer_1 will get disabled 
                counter()
            else:                           #if user enters incorrect answer 
                label=Label(easy_level,text='Unfortunately your answer is wrong and the correct answer is 365',bg='red')
                label.place(relx=0.5,rely=0.25,anchor='center')
                answer_1.configure(state=tk.DISABLED)   #once the player has entered his answer answer_1 will get disabled

        #working of answer_a and answer_b is same as answer
        def answer_a(event=None):
            ans=answer_2.get()              
            if ans=='12':
                label=Label(easy_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.55,anchor='center')
                answer_2.configure(state=tk.DISABLED)
                counter()
            else:
                label=Label(easy_level,text='Unfortunately your answer is wrong and the correct answer is 12',bg='red')
                label.place(relx=0.5,rely=0.55,anchor='center')
                answer_2.configure(state=tk.DISABLED)

        def answer_b(event=None):
            ans=answer_3.get()                  
            if ans=='35':
                label=Label(easy_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.85,anchor='center')
                answer_3.configure(state=tk.DISABLED)
                counter()
                num=total.get()
                with open('score.txt','w') as file:             #open score file to save final score
                    file.write(f'{num}')
                button_result=Button(easy_level,text='Show Result',command=show_result,bg='yellow').place(relx=0.4,rely=0.96, anchor='center')
                button_exit=Button(easy_level,text='Exit Program',command=easy_level.destroy,bg='yellow').place(relx=0.6,rely=0.96, anchor='center')
            else:
                label=Label(easy_level,text='Unfortunately your answer is wrong and the correct answer is 35',bg='red')
                label.place(relx=0.5,rely=0.85,anchor='center')
                answer_3.configure(state=tk.DISABLED)
                num=total.get()
                with open('score.txt','w') as file:             #open score file to save final score
                    file.write(f'{num}')

                #to display exit and view result option to user
                button_result=Button(easy_level,text='Show Result',command=show_result,bg='yellow').place(relx=0.4,rely=0.96, anchor='center') 
                button_exit=Button(easy_level,text='Exit Program',command=easy_level.destroy ,bg='yellow').place(relx=0.6,rely=0.96, anchor='center')
        def show_result():                                      #function to display result 
            gained_score=total.get()                                       #to get final score
            Label(easy_level, text="Total:",bg='light blue').place(relx=0.8,rely=0.96, anchor='center')
            Label(easy_level, text=gained_score,bg='light blue').place(relx=0.9,rely=0.96, anchor='center')            
        easy_level= Tk()                                        #creating the level window
        total = IntVar()                                        #initializing the variable
        easy_level.title('EASY LEVEL')
        easy_level.geometry('500x300')
        easy_level.resizable(False,False)                       #it will restrict the user from changing the window size
        easy_level.configure(bg="black")                        
        question_1= Label(easy_level, text='Question 1. How many days are there in a year?',bg='light grey')
        question_1.place(relx=0.5,rely=0.05,anchor='center')
        answer_1=Entry(easy_level)                              #creating the answer box
        answer_1.place(relx=0.5,rely=0.15,anchor='center')
        answer_1.bind('<Return>', answer)                        #answer will be saved when the user presses enter and will also check whether answer is correct or incorrect


        question_2= Label(easy_level, text='Question 2. What is the square root of 144?',bg='light grey')
        question_2.place(relx=0.5,rely=0.35,anchor='center')
        answer_2=Entry(easy_level)
        answer_2.place(relx=0.5,rely=0.45,anchor='center')
        answer_2.bind('<Return>', answer_a)

        question_3=Label(easy_level, text='What is the next number in the sequence 7,14,21,28?',bg='light grey')
        question_3.place(relx=0.5,rely=0.65,anchor='center')
        answer_3=Entry(easy_level)
        answer_3.place(relx=0.5,rely=0.75,anchor='center')
        answer_3.bind('<Return>', answer_b)
        easy_level.mainloop()

    #working of hard_level and medium_level function is same as easy_level
    def medium_level():
        quiz_game.destroy()
        def counter():
            total.set(total.get() + 10)
        def answer(event=None):
            ans=str.lower(answer_1.get())
            if ans=='mercury':
                label=Label(medium_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.25,anchor='center')
                answer_1.configure(state=tk.DISABLED)
                counter()
            else:
                label=Label(medium_level,text='Unfortunately your answer is wrong and the correct answer is mercury',bg='red')
                label.place(relx=0.5,rely=0.25,anchor='center')
                answer_1.configure(state=tk.DISABLED)
        def answer_a(event=None):
            ans=str.lower(answer_2.get()) 
            if ans=='thomus edison':
                label=Label(medium_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.55,anchor='center')
                answer_2.configure(state=tk.DISABLED)
                counter()
            else:
                label=Label(medium_level,text='Unfortunately your answer is wrong and the correct answer is thomus edison',bg='red')
                label.place(relx=0.5,rely=0.55,anchor='center')
                answer_2.configure(state=tk.DISABLED)

        def answer_b(event=None):
            ans=answer_3.get()  
            if ans=='12':
                label=Label(medium_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.85,anchor='center')
                answer_3.configure(state=tk.DISABLED)
                counter()
                num=total.get()
                with open('score.txt','w') as file:
                    file.write(f'{num}')
                button_result=Button(medium_level,text='Show Result',command=show_result,bg='yellow').place(relx=0.4,rely=0.96, anchor='center')
                button_exit=Button(medium_level,text='Exit Program',command=medium_level.destroy,bg='yellow').place(relx=0.6,rely=0.96, anchor='center')
            else:
                label=Label(medium_level,text='Unfortunately your answer is wrong and the correct answer is 12',bg='red')
                label.place(relx=0.5,rely=0.85,anchor='center')
                answer_3.configure(state=tk.DISABLED)
                num=total.get()
                with open('score.txt','w') as file:
                    file.write(f'{num}')
                button_result=Button(medium_level,text='Show Result',command=show_result,bg='yellow').place(relx=0.4,rely=0.96, anchor='center')
                button_exit=Button(medium_level,text='Exit Program',command=medium_level.destroy,bg='yellow').place(relx=0.6,rely=0.96, anchor='center')
        def show_result():
            b=total.get()
            Label(medium_level, text="Total:",bg='light blue').place(relx=0.8,rely=0.96, anchor='center')
            Label(medium_level, text=b,bg='light blue').place(relx=0.9,rely=0.96, anchor='center')            

        medium_level= Tk()
        total = IntVar()
        medium_level.title('MEDIUM LEVEL')
        medium_level.geometry('500x300')
        medium_level.resizable(False,False)
        medium_level.configure(bg="#000000")
        question_1= Label(medium_level, text='Question 1. Which planet is the smallest. Neptune or Mars or Mercury?',bg='light grey')
        question_1.place(relx=0.5,rely=0.05,anchor='center')
        answer_1=Entry(medium_level)
        answer_1.place(relx=0.5,rely=0.15,anchor='center')
        answer_1.bind('<Return>', answer)


        question_2= Label(medium_level, text='Question 2. Who invented the Light Bulb?',bg='light grey')
        question_2.place(relx=0.5,rely=0.35,anchor='center')
        answer_2=Entry(medium_level)
        answer_2.place(relx=0.5,rely=0.45,anchor='center')
        answer_2.bind('<Return>', answer_a)

        question_3=Label(medium_level, text='Question 3.How many straight edges does  cube have?',bg='light grey')
        question_3.place(relx=0.5,rely=0.65,anchor='center')
        answer_3=Entry(medium_level)
        answer_3.place(relx=0.5,rely=0.75,anchor='center')
        answer_3.bind('<Return>', answer_b)
        medium_level.mainloop()

    def HARD_level():
        quiz_game.destroy()
        def counter():
            total.set(total.get() + 10)
        def answer(event=None):
            ans=str.lower(answer_1.get())   
            if ans=='mars':
                label=Label(HARD_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.25,anchor='center')
                answer_1.configure(state=tk.DISABLED)
                counter()
            else:
                label=Label(HARD_level,text='Unfortunately your answer is wrong and the correct answer is mars',bg='red')
                label.place(relx=0.5,rely=0.25,anchor='center')
                answer_1.configure(state=tk.DISABLED)
        def answer_a(event=None):
            ans=str.lower(answer_2.get())    
            if ans=='water':
                label=Label(HARD_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.55,anchor='center')
                answer_2.configure(state=tk.DISABLED)
                counter()
            else:
                label=Label(HARD_level,text='Unfortunately your answer is wrong and the correct answer is WATER,',bg='red')
                label.place(relx=0.5,rely=0.55,anchor='center')
                answer_2.configure(state=tk.DISABLED)

        def answer_b(event=None):
            ans=str.lower(answer_3.get())
            if ans=='mount everest':
                label=Label(HARD_level,text='Absolutely correct',bg='light green')
                label.place(relx=0.5,rely=0.85,anchor='center')
                answer_3.configure(state=tk.DISABLED)
                counter()
                num=total.get()
                with open('score.txt','w') as file:
                    file.write(f'{num}')
                button_result=Button(HARD_level,text='Show Result',command=show_result,bg='yellow').place(relx=0.4,rely=0.96, anchor='center')
                button_exit=Button(HARD_level,text='Exit Program',command=HARD_level.destroy,bg='yellow').place(relx=0.6,rely=0.96, anchor='center')
            else:
                label=Label(HARD_level,text='Unfortunately your answer is wrong and the correct answer is mount everest',bg='red')
                label.place(relx=0.5,rely=0.85,anchor='center')
                answer_3.configure(state=tk.DISABLED)
                num=total.get()
                with open('score.txt','w') as file:
                    file.write(f'{num}')
                button_result=Button(HARD_level,text='Show Result',command=show_result,bg='yellow').place(relx=0.4,rely=0.96, anchor='center')
                button_exit=Button(HARD_level,text='Exit Program',command=HARD_level.destroy,bg='yellow').place(relx=0.6,rely=0.96, anchor='center')
        def show_result():
            b=total.get()
            Label(HARD_level, text="Total:" ,bg='light blue').place(relx=0.8,rely=0.96, anchor='center')
            Label(HARD_level, text=b,bg='light blue').place(relx=0.9,rely=0.96, anchor='center')            

        HARD_level= Tk()
        HARD_level.configure(bg="#000000")
        total = IntVar()
        HARD_level.title('HARD LEVEL')
        HARD_level.geometry('500x300')
        HARD_level.resizable(False,False)

        question_1= Label(HARD_level, text='Question 1. Which planet is known as Red Planet?',bg='light grey')
        question_1.place(relx=0.5,rely=0.05,anchor='center')
        answer_1=Entry(HARD_level)
        answer_1.place(relx=0.5,rely=0.15,anchor='center')
        answer_1.bind('<Return>', answer)


        question_2= Label(HARD_level, text='Question 2. What makes up 80% of our brains volume?',bg='light grey')
        question_2.place(relx=0.5,rely=0.35,anchor='center')
        answer_2=Entry(HARD_level)
        answer_2.place(relx=0.5,rely=0.45,anchor='center')
        answer_2.bind('<Return>', answer_a)

        question_3=Label(HARD_level, text='Question 3.What is the highest mountain in the world?',bg='light grey')
        question_3.place(relx=0.5,rely=0.65,anchor='center')
        answer_3=Entry(HARD_level)
        answer_3.place(relx=0.5,rely=0.75,anchor='center')
        answer_3.bind('<Return>', answer_b)
        HARD_level.mainloop()

    quiz_game=Toplevel()       #creating the menu window
    quiz_game.geometry('500x374')
    quiz_game.configure(bg="black")
    quiz_game.title('SURVIVAL QUIZ')
    quiz_game.resizable(False,False)   #it will restrict the window from changing window size

    top_label=Label(quiz_game, text='''    **WELCOME TO THE SURVIVAL QUIZ**
                   
         ~~DEATH NOTE:
    IN ORDER TO ESCAPE THIS BUILDING YOU
    HAVE TO CORRECTLY GUESS ALTEAST 2
         OUT OF 3 QUESTION~~''',font=('Chiller', '18','bold'),bg='black',foreground='white').place(relx=0.5, rely=0.1,anchor='center')
    middle_label=Label(quiz_game,text='SELECT THE LEVEL OF DIFFICULTY',font=('Chiller', '18','bold'),bg='black',foreground='white').place(relx=0.5, rely=0.5,anchor='center')

    #creating buttons for each level
    button_1=Button(quiz_game,text='EASY LEVEL',command=easy_level,font=('Chiller' ,'13','bold'),foreground='red').place(relx=0.5,rely=0.6,anchor='center')
    button_2=Button(quiz_game,text='MEDIUM LEVEL',command=medium_level,font=('Chiller' ,'13','bold'),foreground='red').place(relx=0.5,rely=0.7,anchor='center')
    button_3=Button(quiz_game,text='HARD LEVEL',command=HARD_level,font=('Chiller' ,'13','bold'),foreground='red').place(relx=0.5,rely=0.8,anchor='center')


