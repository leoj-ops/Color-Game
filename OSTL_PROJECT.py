from tkinter import *
import random
import time
import sqlite3
#from PIL import Image, ImageTk
colours = ['red','blue','green','pink','black','yellow','orange','white','purple','brown']
timeleft=30
score=0

def score_board():
        crsr.execute("SELECT * FROM board")
        l=crsr.fetchall()
        connection.commit()
        sco_bo = Tk()
        sco_bo.title("COLORGAME") 
        sco_bo.geometry("375x300")
        w=Label(sco_bo,text ='Score Board', font =("BOLD",10))  
        w.pack()
        text=Text(sco_bo,height=14,width=15,)
        text.pack()
        data="Name\tScore\n"
        for i in l:
            data=data+i[0]+"\t"+str(i[1])+"\n"
        text.insert(0.0,data)
        text.config(state=DISABLED)
        frame = Frame(sco_bo) 
        frame.pack() 
        exi=Button(sco_bo, text='EXIT', width=25, command=sco_bo.destroy) 
        exi.pack(side = BOTTOM)
        sco_bo.mainloop()

       
def start():
        def startGame(event):	
                if timeleft == 30:                          
                        countdown()
                nextColour() 

        def nextColour(): 
                global score 
                global timeleft
                if timeleft>0: 
                        e.focus_set() 
                        if e.get().lower()==colours[1].lower():      
                                score+=1
                        e.delete(0,END) 
                        random.shuffle(colours) 
                        label.config(fg = str(colours[1]),text=str(colours[0])) 
                        scoreLabel.config(text = "Score: "+ str(score))
                else:
                        e.focus_set()
                        label.config(text="Enter your name",font=('Helvetica',12))
                        exi=Button(root, text='EXIT', width=25, command=root.destroy) 
                        exi.pack(side = BOTTOM)
                        na=e.get()
                        crsr.execute("insert into board values (?, ?)", (na, score))
                     
                        
        def countdown(): 
                global timeleft 
                if timeleft > 0: 
                        timeleft -= 1
                        timeLabel.config(text = "Time left: "+str(timeleft))                                                   
                        timeLabel.after(1000, countdown) 

        global timeleft
        root = Tk() 
        root.title("COLORGAME") 
        root.geometry("375x300")
        timeleft=30
        instructions = Label(root,text ="Type in the colour of the words and not the word text!",font=('Helvetica',12)) 
        instructions.pack() 
        scoreLabel = Label(root,text="Press enter to start",font=('Helvetica',12)) 
        scoreLabel.pack() 
        timeLabel = Label(root,text="Time left: "+str(timeleft),font=('Helvetica',12))                                   
        timeLabel.pack()        
        label =Label(root,font=('Helvetica',60)) 
        label.pack() 
        e =Entry(root) 
        root.bind('<Return>',startGame) 
        e.pack() 
        e.focus_set() 
        root.mainloop() 
                            
def main():
    game = Tk()
    game.title("COLORGAME") 
    game.geometry("375x300")
    img=ImageTk.PhotoImage(Image.open('start2.jpg'))
    canvas = Canvas(game,  width=375, height=300)
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.pack() 
    exi=Button(canvas,text='EXIT',width=15,bg='orange',command=game.destroy)
    exi=canvas.create_window(190,250,anchor=S, window=exi)
    sco=Button(canvas, text='Score Board', width=15,bg='orange',command=score_board)
    sco= canvas.create_window(190,220,anchor=S, window=sco)
    sta=Button(canvas,text='Start game',width=15,bg='orange',command=start)
    sta = canvas.create_window(190,190,anchor=S,window=sta)
    game.mainloop()

connection = sqlite3.connect("myTable.db") 
crsr = connection.cursor() 
sql_command = """
CREATE TABLE IF NOT EXISTS board(name text,score integer)"""
crsr.executescript(sql_command)
connection.commit() 
main()


