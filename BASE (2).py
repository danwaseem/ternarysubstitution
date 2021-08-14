#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk


# In[2]:


from tkinter import ttk
import numpy as np
from tkinter import Tk, Label, StringVar, Button, Entry,Text
from tkinter import messagebox


# In[3]:


init=[[-1,-1,-1],[-1,-1,0],[-1,-1,1],[-1,0,-1],[-1,0,0],[-1,0,1],[-1,1,-1],[-1,1,0],[-1,1,1],[0,-1,-1],[0,-1,0],[0,-1,1],[0,0,-1],[0,0,0],[0,0,1],[0,1,-1],[0,1,0],[0,1,1],[1,-1,-1],[1,-1,0],[1,-1,1],[1,0,-1],[1,0,0],[1,0,1],[1,1,-1],[1,1,0],[1,1,1]]


# In[4]:


init=np.array(init)
init1=init+1
let=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nums=['0','1','2','3','4','5','6','7','8','9']


# In[5]:


def series(key):
    
    key=np.array(key)
    r=np.dot(init,key)
    m,n=r.shape
    for i in range(m):
        for j in range(n):
            if r[i][j]<0:
                r[i][j]=-1
            elif r[i][j]>0:
                r[i][j]=1
            else:
                r[i][j]=0
    e=[]
    for i in r:
        for j in range(m):
    
            if (init[j]==i).all():
                e.append(j)
                break
    e=np.array(e) 
    return e


# In[6]:


def fun(e):
    return len(e)


def subs(a2):
    a1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    s1=[]
    s2=[]
    s3=[]
    k=0
    s1.append(k)
    s1.append(a2[k])
    p=0
    n=len(s1)
    while p<n:
        for j in range(p,n):
            indices=[i for i, x in enumerate (a2) if x==s1[j]]
            s1.extend(indices)
        s1=list(set(s1))
        n=len(s1)
        p+=1
    s=[]
    t=[]
    t.extend(s1)
    for k in range(1,27):
        if a2[k] not in t and k not in t:
            s2=[]
            s2.append(k)
            s2.append(a2[k])
            p=0
            s2.sort()
            n=len(s2)
            while p<n:
                for j in range(p,n):
                    indices=[i for i, x in enumerate (a2) if x==s2[j]]
                    l=[]
                    for k in indices:
                        if k not in t:
                            l.append(k)
                    s2.extend(l)
    
                s2=list(set(s2))
                n=len(s2)
    

                p+=1
            s.append(s2)
            t.extend(s2)
    s.append(s1)
    n=len(s)
    if n>3:
        s.sort(key=fun)
    s1=s[-1]
    s2=s[-2]
    te=[]
    te.extend(s1)
    te.extend(s2)
    for i in range(27):
        if i not in te:
            s3.append(i)
    s=[s1,s2,s3]
    return s 


# In[7]:


def encrypt(s,alpha):
  
    alpha=alpha.upper()
    ENCRYPT=''
    if alpha.isdigit():
        ENCRYPT+=' '
        dif=48
    else:
        dif=64
        alpha=numrepl(alpha)
    for i in alpha:
        a=ord(i)-dif
        if a<0 or a>26:
            a=0
        x=init1[a]
        for j in x:
            b=np.random.choice(s[j])
            ENCRYPT+=let[b]
    return ENCRYPT


# In[8]:


def numrepl(TEXT):
    TEXT=TEXT.replace("1"," ONE ")
    TEXT=TEXT.replace("2"," TWO ")
    TEXT=TEXT.replace("3"," THREE ")
    TEXT=TEXT.replace("4"," FOUR ")
    TEXT=TEXT.replace("5"," FIVE ")
    TEXT=TEXT.replace("6"," SIX " )
    TEXT=TEXT.replace("7"," SEVEN ")
    TEXT=TEXT.replace("8"," EIGHT ")
    TEXT=TEXT.replace("9"," NINE ")
    TEXT=TEXT.replace("0"," ZERO ")
    return TEXT
    

def decrypt(s,TEXT):
    DECRYPT=''
    p=[]
    s1=s[0]
    s2=s[1]
    s3=s[2]

    initi=init1.tolist()
    for i in range(len(TEXT)):
        a=ord(TEXT[i])-64
        if a < 0 or a >26:
            a=0
        if a in s1:
            b=0
        elif a in s2:
            b=1
        elif a in s3:
            b=2
        p.append(b)
        if (i+1)%3==0:
            q=initi.index(p)
            DECRYPT+=let[q]
            p=[]
    return DECRYPT

def decryptnum(s,TEXT):
    DECRYPT=''
    p=[]
    s1=s[0]
    s2=s[1]
    s3=s[2]
    initi=init1.tolist()
    TEXT=TEXT[1:]
    for i in range(len(TEXT)):
        a=ord(TEXT[i])-64
        if a < 0 or a >26:
            a=0
        if a in s1:
            b=0
        elif a in s2:
            b=1
        elif a in s3:
            b=2
        p.append(b)
        if (i+1)%3==0:
            q=initi.index(p)
            DECRYPT+=nums[q]
            p=[]
    return DECRYPT
    


# In[ ]:





# In[9]:


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
def CreateToolTip(widget, text):
        toolTip = ToolTip(widget)
        def enter(event):
            toolTip.showtip(text)
        def leave(event):
            toolTip.hidetip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)
        


# In[10]:


def is_digit(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def main():
    
    window = Tk()
    window.title("Crypto Project")
    window.geometry("515x490+470+150")
    window.resizable(False, False)

# empty arrays for your Entrys and StringVars
    text_var = []
    entries = []

# callback function to get your StringVars
    def get_mat():
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                flag=1
                variable=text_var[i][j].get()
                if is_digit(variable):
                    if (i+j)%2==1:
                        flag=-1
                    element=flag*(float(variable))
                    matrix[i].append(element)
                else:
                    return 0
                    
        a=series(matrix)
        b=subs(a)
        return b
    
    def enc():
        b=get_mat()
        if b==0:
            messagebox.showerror("Error", "This is a invalid key")
        else:
            x=inputtxt.get("1.0",'end-1c')
            c=encrypt(b,x)
            outtxt.delete('1.0', 'end-1c') # clear the outputtext text widget
            outtxt.insert('1.0',c)
    

    def decr():
        b=get_mat()
        if b==0:
            messagebox.showerror("Error", "This is a invalid key")
        else:
            x=outtxt.get("1.0",'end-1c')
            if (len(x))%3==0:
                c=decrypt(b,x)
                inputtxt.delete('1.0', 'end-1c') # clear the outputtext text widge
                inputtxt.insert('1.0',c)
            elif (x[0]==' ') and (len(x)-1)%3==0:
                c=decryptnum(b,x)
                inputtxt.delete('1.0', 'end-1c') # clear the outputtext text widge
                inputtxt.insert('1.0',c)
                
            else:
                print(len(x))
                messagebox.showerror("Error", "This is a invalid cipher text")
                outtxt.delete('1.0', 'end-1c')
                

    

    Label(window, text="Enter Key (The Key should be 3 x 3 matrix) :", font=('calibri', 12, 'bold')).place(x=40, y=20)

    x2 = 0
    y2 = 0
    rows, cols = (3,3)
    for i in range(rows):
        text_var.append([])
        entries.append([])
        for j in range(cols):

            text_var[i].append(StringVar())
            entries[i].append((Entry(window, textvariable=text_var[i][j],width=3)))
            entries[i][j].place(x=60 + x2, y=50 + y2)
            x2 += 30

        y2 += 30
        x2 = 0

    Label(window, text="Enter Plain Text", font=('calibri', 12)).place(x=40, y=140)
    inputtxt = Text(window, height = 5, width = 50, bg = "white")
    inputtxt.place(x=60, y=163)
    encrypt_button= Button(window,text="Encrypt", width=15, command=enc)
    encrypt_button.place(x=200,y=255)
    CreateToolTip(encrypt_button, text = 'Generates a cipher text based on the text given above\nusing the key')
    Label(window, text="Enter Cipher Text", font=('calibri', 12)).place(x=40, y=280)
    outtxt = Text(window, height = 5, width = 50, bg = "white")
    outtxt.place(x=60, y=303)
    decrypt_button= Button(window,text="Decrypt", width=15,command=decr)
    decrypt_button.place(x=200,y=395)
    CreateToolTip(decrypt_button, text = 'Generates a plain text based on the cipher text given above\nusing the key')

    
    destroy_button=Button(window, text='Exit', width=15, command=window.destroy)
    destroy_button.place(x=200,y=440)
    messagebox.showinfo("Information", "This project is submitted to Alwyn Roshan Pais Sir of the Computer Science department of NITK, Surathkal, as part of the course requirements for CS350, Cryptography and Applications.\n\nThis project is the implementation of ternary based subsitution algorithm according to the paper mentioned in the abstract.\n\nSubmitted by:\nDanish Waseem\t181CO116\nRahul Agrawal\t181CO141\nYash Kumar\t181CO160") 
    messagebox.showinfo("Information","Plain Text does not accept special characters and negative numbers\n\nMatrix key may include any integer or decimal values.")
    window.mainloop()



if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




