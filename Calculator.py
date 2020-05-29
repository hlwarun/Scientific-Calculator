import math
from tkinter import *
import tkinter.messagebox
import parser

root = Tk()
root.title("Scientific Calculator")
root.resizable(width=False, height=False)
root.geometry("496x488+0+0")
root.configure(background="#c0c0c0")

#Frame is inside of root
calc = Frame(root)
calc.grid()

#Creating the top menubar
menubar = Menu(calc)
#Displaying the menubar
root.config(menu=menubar)

#-----------------------Functions for the menu commands-------------------------------
def standard():
    root.resizable(width=False, height=False)
    root.geometry("496x488+0+0")

def scientific():
    root.resizable(width=False, height=False)
    root.geometry("620x740+0+0")

def exit():
    confirmExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do You Want to Confirm Exit?")
    if confirmExit > 0:
        root.destroy()
        return

def helpfunc():
    help = tkinter.messagebox.showinfo("Scientific Calculator", "This is the calculator developed using Tkinter library and written in Python. "
                                        "This calculator is developed by Arun Ghimire. " 
                                        "This calculator works in two modes: Standard Mode and Scientific Mode.")

#Inorder for this functions to work you need to call these functions in command method below
#-------------------------------------------------------------------------------------

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_separator()
file.add_command(label =  "Standard", command = standard)
file.add_command(label =  "Scientific", command = scientific)
file.add_command(label =  "Exit",command = exit)
file.add_separator()

edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_separator()
edit.add_command(label = "Cut")
edit.add_command(label = "Copy")
edit.add_command(label = "Paste")
edit.add_separator()

help = Menu(menubar, tearoff=0)
menubar.add_command(label = "Help", command=helpfunc)

#----------------------------------Screen Display-------------------------------------
screen = Entry(calc, bg="#909090", font=('arial',20,'bold'), bd=10, width=28, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=4, ipady=5, pady=2)
screen.insert(0, '0')
#-------------------------------------------------------------------------------------


#-------------------Functions for standard calculator commands------------------------
class calculations():
    def __init__(self):
        self.current = ""
        self.operator = ""
        self.input_value = True
        self.check_sum = False
        self.total = 0
        self.result = False

    def display(self, value):
        screen.delete(0, END)
        screen.insert(0, value)

    def numEntry(self, num):
        self.result = False
        num1 = screen.get()
        num2 = str(num)
        if self.input_value:
            self.current = num2
            self.input_value = False
        else:
            if num2 == '.':
                if num2 in num1:
                    return
            self.current = num1 + num2
        self.display(self.current)

    def valid(self):
        if self.operator == 'add':
            self.total += self.current
        if self.operator == 'sub':
            self.total -= self.current
        if self.operator == 'mul':
            self.total *= self.current
        if self.operator == 'div':
            self.total /= self.current
        if self.operator == 'squared':
            self.total = math.pow(self.current, 2)
        if self.operator == 'powered':
            self.total = math.pow(self.total, self.current)
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def totalSum(self):
        self.current = float(self.current)
        self.result = True
        if self.check_sum == True:
            self.valid()
        else:
            self.total = float(screen.get())

    def operation(self, operator):
        self.current = float(self.current)
        if self.check_sum:
            self.valid()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.operator = operator
        self.result = False

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def clear(self):
        self.result =False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def clearall(self):
        self.clear()
        self.total = 0

    def squareRoot(self):
        self.result = False
        self.current = math.sqrt(float(screen.get()))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(screen.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(screen.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(screen.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(screen.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(screen.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(screen.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(math.radians(float(screen.get())))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(math.radians(float(screen.get())))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(math.radians(float(screen.get())))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(math.radians(float(screen.get())))
        self.display(self.current)

    def exmp1(self):
        self.result = False
        self.current = math.expm1(math.radians(float(screen.get())))
        self.display(self.current)

    def gamma(self):
        self.result = False
        self.current = math.gamma(math.radians(float(screen.get())))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(math.radians(float(screen.get())))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(math.radians(float(screen.get())))
        self.display(self.current)

    def radians(self):
        self.result = False
        self.current = math.radians(math.radians(float(screen.get())))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(math.radians(float(screen.get())))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(math.radians(float(screen.get())))
        self.display(self.current)

    def atanh(self):
        self.result = False
        self.current = math.atanh(math.radians(float(screen.get())))
        self.display(self.current)


objcall = calculations()
#-------------------------------------------------------------------------------------


numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, height=2, width =6, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]:objcall.numEntry(x)
        i+=1

btnclear = Button(calc, text="X", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", fg='red', command=objcall.clear).grid(row=1, column=3, pady=1)
btnclearall = Button(calc, text="C", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", fg='red', command=objcall.clearall).grid(row=1, column=2, pady=1)
btnsqrt = Button(calc, text="√", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.squareRoot).grid(row=1, column=0, pady=1)
btnsq = Button(calc, text="x²", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=lambda:objcall.operation('squared')).grid(row=1, column=1, pady=1)
btndiv = Button(calc, text="÷", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=lambda:objcall.operation('div')).grid(row=2, column=3, pady=1)
btnmult = Button(calc, text="×", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=lambda:objcall.operation('mul')).grid(row=3, column=3, pady=1)
btnsub = Button(calc, text="-", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=lambda:objcall.operation('sub')).grid(row=4, column=3, pady=1)
btnadd = Button(calc, text="+", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=lambda:objcall.operation('add')).grid(row=5, column=2, pady=1)
btnzero = Button(calc, text="0", height=2, width=6, font=('arial', 20, 'bold'), bd=4, command=lambda:objcall.numEntry(0)).grid(row=5, column=0, pady=1)
btndot = Button(calc, text=".", height=2, width=6, font=('arial', 20, 'bold'), bd=4, command=lambda:objcall.numEntry('.')).grid(row=5, column=1, pady=1)
btneq = Button(calc, text="=", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.totalSum).grid(row=5, column=3, pady=1)


#-------------------------------Scientific Calculator-----------------------------------

#Label(calc, text="Advanced Calculations", font=('arial', 20, 'bold'), justify=CENTER).grid(row=0, column=4, columnspan=4)

btnsin = Button(calc, text="sin", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.sin).grid(row=6, column=0, pady=1)
btncos = Button(calc, text="sin", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.cos).grid(row=6, column=1, pady=1)
btntan = Button(calc, text="tan", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.tan).grid(row=6, column=2, pady=1)
btnsinh = Button(calc, text="sinh", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.sinh).grid(row=6, column=3, pady=1)
btncosh = Button(calc, text="cosh", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.cosh).grid(row=7, column=0, pady=1)
btntanh = Button(calc, text="tanh", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.tanh).grid(row=7, column=1, pady=1)
btnpi = Button(calc, text="π", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.pi).grid(row=7, column=2, pady=1)
btne = Button(calc, text="e", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.e).grid(row=7, column=3, pady=1)
btnlog = Button(calc, text="log", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.log).grid(row=8, column=0, pady=1)
btnlog2 = Button(calc, text="log2", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.log2).grid(row=8, column=1, pady=1)
btnlog10 = Button(calc, text="log10", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.log10).grid(row=8, column=2, pady=1)
btnlog1p = Button(calc, text="log1p", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.log1p).grid(row=8, column=3, pady=1)

btnpow = Button(calc, text="^", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=lambda:objcall.operation('powered')).grid(row=1, column=4, pady=1)
btnasinh = Button(calc, text="asinh", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.asinh).grid(row=2, column=4, pady=1)
btnacosh = Button(calc, text="acosh", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.acosh).grid(row=3, column=4, pady=1)
btntanh = Button(calc, text="tanh", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.tanh).grid(row=4, column=4, pady=1)
btndeg = Button(calc, text="deg", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.degrees).grid(row=5, column=4, pady=1)
btnrad = Button(calc, text="rad", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.radians).grid(row=6, column=4, pady=1)
btnexmp1 = Button(calc, text="exmp1", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.exmp1).grid(row=7, column=4, pady=1)
btnlgamma = Button(calc, text="lgamma", height=2, width=6, font=('arial', 20, 'bold'), bd=4, bg="#b0b0b0", command=objcall.lgamma).grid(row=8, column=4, pady=1)

#---------------------------------------------------------------------------------------









#mainloop method will loop forever, waiting for events from the user, until the user exits the program
#mainloop blocks the code after it
root.mainloop()