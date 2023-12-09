from tkinter import*
from tkinter import messagebox
import grids
    
def buttons():
     
     global root1
     global root2
     root1.destroy()

     root2=Tk()
     root2.title("SUDOKU")
     root2.iconbitmap("images.ico")
     label2=Label(root2,bg="black")
     label2.place(width="1000",height="1000")
     '''starting with buttons'''
     #start_easy
     butE=Button(root2,text="EASY",width=10,bg="black",fg="gold",font=("Bold",10),command=lambda : display("EASY")).grid(row=0,column=5,padx=50,pady=10)
     #start_medium
     butM=Button(root2,text="MEDIUM",width=10,bg="black",fg="gold",font=("Bold",10),command=lambda : display("MEDIUM")).grid(row=1,column=5,padx=50,pady=10)
     #start_hard
     butH=Button(root2,text="HARD",width=10,bg="black",fg="gold",font=("Bold",10),command=lambda : display("HARD")).grid(row=2,column=5,padx=50,pady=10)
     #go_back_to_main_menu
     butMENU=Button(root2,text="Quit",width=10,bg="black",fg="gold",command=root2.destroy).grid(row=4,column=5,padx=50,pady=50)
     root2.mainloop()

def display(level):
    
    global Qg, Ag    
    global root2
    global root3
    global RE, CE, N
    root2.destroy()

    if level=="EASY" :
        L=grids.easy_puzzle()
    elif level=="MEDIUM":
        L=grids.medium_puzzle()
    elif level=="HARD":
        L=grids.hard_puzzle()

    Qg=L[0]
    Ag=L[1]


    root3=Tk()
    root3.title("SUDOKU")
    root3.iconbitmap("images.ico")
    label3=Label(root3,bg="black")
    label3.place(width="1000",height="1000")
    for x in range(0,9):
        for y in range(0,9):
            labS=Label(root3,text=Qg[x][y],width=6,height=3,bg='black',fg="gold",font=("Bold",12),borderwidth = 2,relief='groove')
            labS.grid(row=x+1,column=y+1)
            
    #choosing
    frame1=LabelFrame(root3,text="COORDINATES:",padx=50,pady=50,fg="gold",bg="black")
    frame1.grid(row=10,column=0,columnspan=9,padx=5,pady=5)
    
    labR=Label(frame1,text="ROW:",width=5,fg="gold",bg="black")
    labR.grid(row=11,column=0,)
    RE=Entry(frame1,width=5)#rowentry
    RE.grid(row=11, column = 2)

    labC=Label(frame1,text="COLUMN:",width=20,fg="gold",bg="black")
    labC.grid(row=12,column=0)
    CE=Entry(frame1,width=5)#COLUMNentry
    CE.grid(row= 12, column = 2)
    
    labN=Label(frame1,text="Enter The Number:",width=20,fg="gold",bg="black")
    labN.grid(row=13,column=0)        
    N=Entry(frame1,width=5)
    N.grid(row=13,column=2)
    
    #check_button
    butGO=Button(root3,text="GO!",width=5,bg="black",fg="gold",font=("Bold",10),command=GO)
    butGO.grid(row=15,column=5)


def GO():
    
               global Qg, Ag    
               global root2
               global root3
               re=0
               ce=0
               n=0

               checklist=('1','2','3','4','5','6','7','8','9')

               flag=False

               for i in range (0,9):
                   for j in range (0,9):
                       if Qg[i][j]!=Ag[i][j]:
                           flag=False
                           break
                       elif Qg[i][j]==Ag[i][j]:
                           flag=True
                           
               if (RE.get() in checklist and CE.get() in checklist and N.get() in checklist):
                   
                  
                   re=int(RE.get())
                   ce=int(CE.get())
                   n=int(N.get())

                   if re>9 or ce>9 or n>9:
                        messagebox.showerror("Error!","enter a valid number")
                   elif (n==Ag[re-1][ce-1]):
                        Qg[re-1][ce-1]=n
                        labUPDATE=Label(root3,text=n,width=6,height=3,bg="light green",fg="black",borderwidth=2,relief='groove')
                        labUPDATE.grid(row=re,column=ce)
                        RE.delete(0,END)
                        CE.delete(0,END)
                        N.delete(0,END)

                   elif (n!=Ag[re][ce]):
                        messagebox.showerror("Oops!","Try again with a different number!")
                        N.delete(0,END)

                   
               else:
                   messagebox.showerror("Error!","Please enter a number")

          if flag==True:
               messagebox.showinfo("YAY!","YOU HAVE SUCCESSFULLY COMPLETED THE PUZZLE")
               root3.destroy()

            
'''____INTRO____'''

from tkinter import*
from tkinter import messagebox
root1=Tk()
root1.title('SUDOKU')
root1.geometry("710x530")
root1.iconbitmap("images.ico")
bg=PhotoImage(file="suds.png")# Show image using label
label1=Label(root1,image=bg)
label1.place(x=0,y=0)
frame=LabelFrame(root1,text="",padx=30,pady=30,bg="black")
frame.place(x=400,y=10)
def Howtoplay():
     messagebox.showinfo("sudoku Rules:","Only use the numbers 1 to 9 \nAvoid trying to guess the solution to the puzzle \nOnly use each number once in each row, column, & grid")
b1=Button(frame,text="Start",padx=20,pady=5,command=buttons)
b1.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b2=Button(frame,text="How to play",command=Howtoplay,padx=20,pady=5)
b2.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b3=Button(frame,text="Quit",command=root1.destroy,padx=20,pady=5)
b3.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b1.pack()
b2.pack()
b3.pack()
root1.mainloop()





