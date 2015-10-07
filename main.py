# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:14:23 2015

@author: fabiomainardi
"""

from Tkinter import Tk, W, E,END, CURRENT
from ttk import Frame, Button,Style
from ttk import Entry
operands=[]
operator=""

class FrameClass(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
     
    
    def initUI(self):
      
        self.parent.title("Calculator")
        
        Style().configure("TButton", padding=(0, 5, 0, 5), 
            font='serif 10')
        
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        
        def calculate():
            expression=entry.get()   
            entry.delete(0, END)
            entry.insert(0,str(eval(expression)))
            
        def evaluate(event):
            expression=entry.get()   
            entry.delete(0, END)
            entry.insert(0,str(eval(expression)))
       
        def selectNumber(char):
            entry.insert(END,char)
         
        def backSpace():
            entry.delete(len(entry.get())-1,END)
        
        def deleteAll():
            entry.delete(0, END)
            
        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        entry.bind("<Return>", evaluate)
        cls = Button(self, text="Cls", command=lambda: deleteAll())
        cls.grid(row=1, column=0)
        bck = Button(self, text="Back",command=lambda: backSpace())
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)    
        clo = Button(self, text="Close",command=self.destroy)
        clo.grid(row=1, column=3)        
        sev = Button(self, text="7",command=lambda: selectNumber("7"))
        sev.grid(row=2, column=0)        
        eig = Button(self, text="8",command=lambda: selectNumber("8"))
        eig.grid(row=2, column=1)         
        nin = Button(self, text="9",command=lambda: selectNumber("9"))
        nin.grid(row=2, column=2) 
        div = Button(self, text="/",command=lambda: selectNumber("/"))
        div.grid(row=2, column=3) 
        
        fou = Button(self, text="4",command=lambda: selectNumber("4"))
        fou.grid(row=3, column=0)        
        fiv = Button(self, text="5",command=lambda: selectNumber("5"))
        fiv.grid(row=3, column=1)         
        six = Button(self, text="6",command=lambda: selectNumber("6"))
        six.grid(row=3, column=2) 
        mul = Button(self, text="*",command=lambda: selectNumber("*"))
        mul.grid(row=3, column=3)    
        
        one = Button(self, text="1",command=lambda: selectNumber("1"))
        one.grid(row=4, column=0)        
        two = Button(self, text="2",command=lambda: selectNumber("2"))
        two.grid(row=4, column=1)         
        thr = Button(self, text="3",command=lambda: selectNumber("3"))
        thr.grid(row=4, column=2) 
        mns = Button(self, text="-",command=lambda: selectNumber("-"))
        mns.grid(row=4, column=3)         
        
        zer = Button(self, text="0",command=lambda: selectNumber("0"))
        zer.grid(row=5, column=0)        
        dot = Button(self, text=".",command=lambda: selectNumber("."))
        dot.grid(row=5, column=1)         
        equ = Button(self, text="=",command=lambda: calculate())
        equ.grid(row=5, column=2) 
        pls = Button(self, text="+",command=lambda: selectNumber("+"))
        pls.grid(row=5, column=3)
        
        self.pack()


        
#def selectNumber(char):
#        operands.append(char)
 

#def selectOperator(char):
#        operands.append(char)
   

#def calculate():# assume there is only one operator
  
#        temp=""
#        numbers=[]

#        for item in operands:
#            if(item.isdigit() or item=="."):
#                temp+=item              
#            else:
#                operator=item
#                numbers.append(float(temp))
#                temp=""
#        numbers.append(float(temp))
    
#        if operator=='+':
#            result= (numbers[0]+numbers[1])
#        if operator=='-':
#            result= (numbers[0]-numbers[1])
#        if operator=='*':
#            result= (numbers[0]*numbers[1])
#        if operator=='/':
#            if(numbers[1]!=0):
#               result= (float(numbers[0])/numbers[1])
       
#        print(result)   
        
        
def main():
  
    root = Tk()
    app = FrameClass(root)
    root.mainloop()  
    

if __name__ == '__main__':
    main()  