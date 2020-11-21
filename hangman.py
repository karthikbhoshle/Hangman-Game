import tkinter
from tkinter import *
import random
import sys
##############
root=tkinter.Tk()
global t,total,wt,sm
t=0
total=0
w = '#FFFFFF'
g = '#20FF0F'
lg = '#778899'
r = '#8B0000'


sn=StringVar()
sn.set('')

word=['Computer','Science','Common']

#random.shuffle(word)
wt=word[0]
sm='-'*len(wt)

s1='_ _ _ _\n' \
   '|       |\n' \
   ' |       O \n' \
   ' |      -|-\n' \
   '|       |\n' \
   '||      /\\'
s2='_ _ _ _\n' \
   '|      |\n' \
   '|       \n' \
   '|       \n' \
   ' |        \n' \
   '  ||         '
s3='_ _ _ _\n' \
   '|      |\n' \
   ' |      O \n' \
   ' |     -|-\n' \
   ' |        \n' \
   '  ||         '
s4='_ _ _ _\n' \
   '|      |\n' \
   ' |      O \n' \
   '|       \n' \
   ' |        \n' \
   '  ||         '
s=[s2,s4,s3,s1]


#######################
def quit():
    sys.exit()
def win():

    frame1.destroy()
    l1 = Label(root, text=s2, fg=r, bg=w, font='Courier 20 ')
    l1.pack(pady=5)
    l2 = Label(root, text='You Won the  Game.', justify='center', fg=g, bg=w, font='Courier 20 ')
    l2.pack(pady=5)
    l6 = Button(root, text='Quit', font='Courier 12', activebackground=lg, relief='solid', bg=r, command=quit)
    l6.pack(pady=10)

def run():
    frame1.destroy()
    l1 = Label(root, text=s1, fg=r, bg=w, font='Courier 20 ')
    l1.pack(pady=5)
    l2 = Label(root, text='You lost Game.', justify='center', fg=r, bg=w, font='Courier 20 ')
    l2.pack(pady=5)
    l6 = Button(root, text='Quit', font='Courier 12', activebackground=lg, relief='solid', bg=r, command=quit)
    l6.pack(pady=10)
def change(event):
    global total,log,sm,l1
    global wt
    p=sn.get()
    sn.set('')
    if p in wt:
        print(sm,p)
        mn=''
        for i in wt:
            if i in sm or i==p:
                mn+=i
            else:
                mn+='-'
        sm=mn
        print(sm)
        l2.config(text=sm)
        if sm==wt:
            win()
    else:
        total+=1
        if total>=3:
            run()
            print(total)
        else:

           l2.config(text='You Entered Wrong character')# ' + str(sm.get()) + ' characters mached')
           log.config(text = 'Chance left:-' + str(3 - total))
           l1.config(text=s[total])




def Start():
    global word,l5,wt,frame1,l2,log,l1
    b1.destroy();log_col.destroy()
    frame1=Frame(root,bg=w)
    frame1.pack(pady=5)
    l1 = Label(frame1, text=s2, fg=r, bg=w, font='Courier 20 ')
    l1.pack(pady=5)
    l2 = Label(frame1, text=sm, justify='center', fg=lg, bg=w, font='Courier 20 ')
    l2.pack(pady=5)

    log_co = Label(frame1, text='Guess a letter', justify='center', bg=lg)  # , font='Courier 10')
    log_co.pack(pady=5)
    entry = Entry(frame1, text=sn, justify='center', font='Courier 12', width=30, bg=g)
    entry.pack(pady=5)
    log= Label(frame1, text='Chance left:-'+str(3-total), justify='center', bg=lg)  # , font='Courier 10')
    log.pack(pady=5)
    root.bind('<Return>', change)
    entry.focus_set()



    pass
#################################
root.title("Typing Speed Application")
root.geometry('700x600')
root.configure(background=w)
root.resizable(False,False)
l1=Label(root,text='Hangman Game Using Python.',fg=r, bg=w,font='Courier 20 underline')
l1.pack(pady=5)
log_col = Label(root, text='', justify='center', width=100,bg=g)#, font='Courier 10')
log_col.pack(pady=5)
b1=Button(root,justify='center',text='Start',font='Courier 12',activebackground=lg,relief='solid',bg=r,command=Start)
b1.pack(pady=10)
log_col = Label(root, text='', justify='center', width=100,bg=g)#, font='Courier 10')
log_col.pack(pady=5)
root.mainloop()