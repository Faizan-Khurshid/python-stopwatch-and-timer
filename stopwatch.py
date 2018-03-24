from tkinter import*
import webbrowser
seconds = -1
minutes = 00
hours   = 00
root = Tk()
root.title("Counting Seconds")
Label(root, text='press start_button to start timer',font="Helvetica 16 bold italic").grid(row=0,column=0) 
Label(root, text='press clear text_button to clear the text',font="Helvetica 16 bold italic").grid(row=1,column=0)
label = Label(root, fg="green",font='Times 35 bold italic')
label.grid(row=2)
t=9#last row + 1
#to count the no oof times stopwsatch started
restart_n=1
def stop():
        global button,button8
        button1 = Button(root,text="start",font='arial 15 bold ',state=NORMAL, width=25,command=start).grid(row=3)
        button2 = Button(root, text='Stop',font='arial 15 bold ',state=DISABLED, width=25, command=stop).grid(row=4)
        l = root.grid_slaves(row=2)
        for h in l:
            h.destroy()
        Label(root,text=(str(hours)+ ":" + str(minutes)+":"+ str(seconds)),fg="green",font='Times 35 bold italic').grid(row=2)
        global t
        i = Label(root, text=str(restart_n)+") you stopped at " + (str(hours)+ ":" + str(minutes)+":"+ str(seconds)),fg="green",font='arial 15 bold italic')
        i.grid(row=t)
        t = t+1
        
        
def clear():
    i=9
    while i < 100:
        l= root.grid_slaves(row=i)
        i=i+1
        for h in l:
            h.destroy()


    
        
def restart():
    global restart_n,button,button8
    button1 = Button(root,text="start",font='arial 15 bold ',state=DISABLED, width=25,command=start).grid(row=3)
    button2 = Button(root, text='Stop',font='arial 15 bold ',state=NORMAL, width=25, command=stop).grid(row=4)
    restart_n+=1
    t = root.grid_slaves(row=2)
    for y in t:
        y.destroy()
    global seconds
    global minutes
    global hours
    seconds = -1
    minutes = 0
    hours = 0
    def counter_second(s):
            def count():
                global seconds
                global minutes
                global hours
                seconds += 1
                s.config(text=(str(hours)+ ":" + str(minutes)+":"+ str(seconds)))#i think so,jb text change horaha ho tb
                s.after(1000, count)
                if seconds == 60:
                    seconds = 0
                    minutes +=1
                if minutes == 60:
                    minutes = 0
                    hours+=1
            count()
    llabel = Label(root, fg="green",font='Times 35 bold italic')
    llabel.grid(row=2)
    counter_second(llabel)
        
def start():
    global button
    global button8,button2
    button3 = Button(root, text="restart", font='arial 15 bold ',state=NORMAL, width=25, command=restart).grid(row=5)
    button2 = Button(root, text='Stop',font='arial 15 bold ',state=NORMAL, width=25, command=stop).grid(row=4)
    button1 = Button(root,text="start",font='arial 15 bold ',state = DISABLED, width=25,command=start).grid(row=3)
    f = root.grid_slaves(row=2)
    for g in f:
        g.destroy()
        def counter_second(s):
            def count():
                global seconds
                global minutes
                global hours
                seconds += 1
                s.config(text=(str(hours)+ ":" + str(minutes)+":"+ str(seconds)))#i think so,jb text change horaha ho tb
                s.after(1000, count)
                if seconds == 60:
                    seconds = 0
                    minutes +=1
                if minutes == 60:
                    minutes = 0
                    hours+=1
                if minutes == 10:
                        webbrowser.open("www.youtube.com")
            count()
        llabel = Label(root, fg="green",font='Times 35 bold italic')
        llabel.grid(row=2)
        counter_second(llabel)
        #button_s = Button(root, text='start',font='arial 15 bold ', width=25, command=start).grid(row=3)
    


           




    

button2 = Button(root, text='Stop',font='arial 15 bold ',state=DISABLED, width=25, command=stop).grid(row=4)
button1 = Button(root,text="start",font='arial 15 bold ', width=25,command=start).grid(row=3)
button3 = Button(root, text="restart", font='arial 15 bold ',state=DISABLED, width=25, command=restart).grid(row=5)

button5= Button(root, text='Exit',font='arial 15 bold',width=25,command=root.destroy).grid(row=7)

button4 = Button(root, text='clear text', font='arial 15 bold',width=25,command=clear).grid(row=6)

root.mainloop()
