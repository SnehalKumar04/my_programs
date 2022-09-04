from tkinter import *
from tkinter.filedialog import *
root=Tk()
root.title('calculator')
e=Entry(root,width=30)
e.grid(row=0,column=0,columnspan=5)
def display(n):
    k=e.get()
    e.delete(0, END)
    e.insert(0, str(k)+str(n))
def cleara():
    e.delete(0, END)
def clr1():
    k=e.get()
    e.delete(0, END)
    e.insert(0, k[:-1])
def equal():
    k=e.get()
    e.delete(0, END)
    for i in range(0,len(k)):
        if k[i]=='+':
            ans=float(k[:i])+float(k[i+1:])
            e.insert(0, str(ans))
        elif k[i]=='-':
            ans=float(k[:i])-float(k[i+1:])
            e.insert(0, str(ans))
        elif k[i]=='*':
            ans=float(k[:i])*float(k[i+1:])
            e.insert(0, str(ans))
        elif k[i]=='/':
            ans=float(k[:i])/float(k[i+1:])
            e.insert(0, str(ans))
        elif k[i]=='%':
            ans=float(k[:i])%float(k[i+1:])
            e.insert(0, str(ans))
def reciprocal():
    k=e.get()
    e.delete(0, END)
    ans=1/int(k)
    e.insert(0 ,str(ans))
def square():
    k=e.get()
    e.delete(0, END)
    ans=int(k)*int(k)
    e.insert(0, str(ans))
def sqroot():
    k=e.get()
    e.delete(0, END)
    ans=int(k)**(1/2)
    e.insert(0, str(ans))
def cube():
    k=e.get()
    e.delete(0, END)
    ans=int(k)**(3)
    e.insert(0, str(ans))
b7=Button(root,text='7',width=5,command=lambda:display(7)).grid(row=3,column=0,columnspan=1)
b8=Button(root,text='8',width=5,command=lambda:display(8)).grid(row=3,column=1,columnspan=1)
b9=Button(root,text='9',width=5,command=lambda:display(9)).grid(row=3,column=2,columnspan=1)
b4=Button(root,text='4',width=5,command=lambda:display(4)).grid(row=4,column=0,columnspan=1)
b5=Button(root,text='5',width=5,command=lambda:display(5)).grid(row=4,column=1,columnspan=1)
b6=Button(root,text='6',width=5,command=lambda:display(6)).grid(row=4,column=2,columnspan=1)
b1=Button(root,text='1',width=5,command=lambda:display(1)).grid(row=5,column=0,columnspan=1)
b2=Button(root,text='2',width=5,command=lambda:display(2)).grid(row=5,column=1,columnspan=1)
b3=Button(root,text='3',width=5,command=lambda:display(3)).grid(row=5,column=2,columnspan=1)
b0=Button(root,text='0',width=5,command=lambda:display(0)).grid(row=6,column=1,columnspan=1)
clr=Button(root,text='c',width=5,command=lambda:cleara()).grid(row=1,column=2,columnspan=1)
bck=Button(root,text=chr(8592),width=5,command=lambda:clr1()).grid(row=1,column=3,columnspan=1)
plus=Button(root,text='+',width=5,command=lambda:display('+')).grid(row=5,column=3,columnspan=1)
minus=Button(root,text='-',width=5,command=lambda:display('-')).grid(row=4,column=3,columnspan=1)
mul=Button(root,text='*',width=5,command=lambda:display('*')).grid(row=3,column=3,columnspan=1)
eq=Button(root,text='=',width=12,command=lambda:equal()).grid(row=6,column=2,columnspan=5)
div=Button(root,text='/',width=5,command=lambda:display('/')).grid(row=2,column=3,columnspan=1)
moddiv=Button(root,text='%',width=5,command=lambda:display('%')).grid(row=1,column=0,columnspan=1)
reci=Button(root,text='1/x',width=5,command=lambda:reciprocal()).grid(row=2,column=0,columnspan=1)
sqr=Button(root,text='x^2',width=5,command=lambda:square()).grid(row=2,column=1,columnspan=1)
rot=Button(root,text=chr(8730),width=5,command=lambda:sqroot()).grid(row=2,column=2,columnspan=1)
dot=Button(root,text='.',width=5,command=lambda:display('.')).grid(row=6,column=0,columnspan=1)
cub=Button(root,text='x^3',width=5,command=lambda:cube()).grid(row=1,column=1,columnspan=1)
root.mainloop()
