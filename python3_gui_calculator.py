import tkinter as needyamin
from tkinter import *
#Window Title Start 
window_needyamin = needyamin.Tk()
window_needyamin.title('Yamin\'s Ugly Calculator')
window_needyamin.geometry("487x600")
#Window Title End


#<-- YOU CAN REMOVE THIS CODE IF NOT NEEDED START-->
# Startup Notification For LINUX OS #
import os
import socket
mstr=(socket.gethostbyaddr(socket.gethostname())[0])
os.system('notify-send '+mstr)
# Startup Notification Ends #

#<-- Remove comment if your want to add an icon on your application-->#
#window_needyamin.protocol("WM_DELETE_window_needyamin", window_needyamin.iconify) 
#window_needyamin.iconphoto(True, needyamin.PhotoImage(file='love.png'))

#<-- YOU CAN REMOVE THIS CODE IF NOT NEEDED END-->



####### Start Calculation #########
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def equals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)  

def cleardisplay():
    global operator
    operator = ""
    text_input.set(operator)


operator = ""
text_input = StringVar()
text_Display = Entry(window_needyamin, font=('arial',30,'bold'), textvariable = text_input, bd = 20 ,insertwidth = 4, bg = 'powder blue', justify ='right').grid(columnspan=4)



########################## EQUALS START #################################
#row no 1 start
btnAdd=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='+',command=lambda: btnClick('+')).grid(row=1,column=0)

btnminer=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='-',command=lambda: btnClick('-')).grid(row=1,column=1)

btnmaltipul=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='*',command=lambda: btnClick('*')).grid(row=1,column=2)

btnvag=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='/',command=lambda: btnClick('/')).grid(row=1,column=3)
#row no 1 end
########################## EQUALS END #################################



####################### NUMBERS START ################################
#row no 2 start
btn7=Button(window_needyamin, padx=16,bd=8, fg='black',font=('arial',30,'bold'),text='1',command=lambda: btnClick(1)).grid(row=2,column=0)

btn8=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='2',command=lambda: btnClick(2)).grid(row=2,column=1)

btn9=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='3',command=lambda: btnClick(3)).grid(row=2,column=2)

btn4=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='4',command=lambda: btnClick(4)).grid(row=2,column=3)
#row no 2 end


#row no 3 start
btn5=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='5',command=lambda: btnClick(5)).grid(row=3,column=0)

btn6=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='6',command=lambda: btnClick(6)).grid(row=3,column=1)

btn1=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='7',command=lambda: btnClick(7)).grid(row=3,column=2)

btn2=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='8',command=lambda: btnClick(8)).grid(row=3,column=3)
#row no 3 end

#row no 4 start
btn3=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='9',command=lambda: btnClick(9)).grid(row=4,column=0)

btn0=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='0',command=lambda: btnClick(0)).grid(row=4,column=1)

#percentage
btn00=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='%',command=lambda: btnClick('/100')).grid(row=4,column=2)

#point
btn10=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',30,'bold'),text='.',command=lambda: btnClick('.')).grid(row=4,column=3)
#row no 4 end


#row no 5 start
equals=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',25,'bold'),text='=',command=equals).grid(row=5,column=3)

cleardisplay=Button(window_needyamin, padx=16, bd=8, fg='black',font=('arial',25,'bold'),text='clear',command=cleardisplay).grid(row=5,column=2)
#row no 5 end
####################### NUMBERS END ################################


#ending window_needyamin loop
window_needyamin.mainloop()
