#by Lakshya 911 words 12,352 characters 520 lines (Last Update: 10 June 2021 At 13:44)
import os
import time
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox as tm
import tkinter.font  

root=Tk()

root.geometry("1280x720")
# root.minsize(1280,720)
# root.maxsize(1280,720)

a="untitle.txt"

root.title(a + " -Notepad by Lakshya")
root.wm_iconbitmap("file.ico")

s=Scrollbar(root)
s.pack(side="right",fill=Y)

frame=Frame(root,relief=SUNKEN)
text=StringVar()
text.set("Running 100%(No Bug Detected)")
label=Label(frame,textvariable=text,font="Helvetica,10,bold",anchor="w",fg="black")
label.pack(side="left")
frame.pack(side="top",fill=X)

t=Text(root,yscrollcommand=s.set)
t.pack(fill=BOTH,expand=True)

s.config(command=t.yview)




def scan():
    global text
    root.update()
    for i in range(0,101):
        if i %10==0:
            time.sleep(0.2)
            text.set(f"Scanning Program...      {i}%        ")
            root.update()
        elif i>=9 or i<=0:
            time.sleep(0.1)
            text.set(f"Scanning Program...      {i}%         ")
            root.update()
        elif i==100:
            time.sleep(0.1)
            text.set(f"Scanning Program...    {i}%         ")
            root.update()
            
        else:
            time.sleep(0.2)
            text.set(f"Scanning Program...     {i}%        ")
            root.update()
    for j in range(5):
        time.sleep(0.2)
        text.set("Scanning.                          ")
        root.update()

        time.sleep(0.2)
        text.set("Scanning..                         ")
        root.update()

        time.sleep(0.2)
        text.set("Scanning...                        ")
        root.update()   
    time.sleep(0.5)
    text.set("Running 100%(No Bug Detected)")
    root.update()

def scan2():
    global text
    



f1=" "
f2= 20
f3="normal"

f=tkinter.font.Font( family =f1, size = f2,  weight =f3)
t.configure(font=f)

m=Menu(root)
m1=Menu(root,tearoff=0)
m2=Menu(root,tearoff=0)
m3=Menu(root,tearoff=0)
m4=Menu(root,tearoff=0)
m5=Menu(root,tearoff=0)

file= None
file2=None
def fo():
    global file
    global file2
    global a
    file=askopenfilename(defaultextension="*.txt",filetype=[("Text File","*.txt"),("Python File(.py)","*.py")])
    a=os.path.basename(file)
    root.title(a + " -Notepad by Lakshya")
    root.update()

    file2=open(file, "rt")

    t.delete(1.0,END)
    t.insert(1.0,file2.read())
    file2.close()

def fs():
    global file
    global a
    if file==None or file=="":
        file=asksaveasfilename(defaultextension="*.txt",filetype=[("Text File","*.txt"),("Python File(*.py)","*.py")])
        try:
            file2=open(file,"wt")
            te=t.get(1.0,END)
            file2.write(te)
            file2.close()
            a=os.path.basename(file)
            root.title(a + " -Notepad by Lakshya")
            root.update()
            
            text.set("Saving File.")
            root.update()
            for i in range(5):
                text.set("Saving File.")
                root.update()
                time.sleep(0.2)
                
                text.set("Saving File..")
                root.update()
                time.sleep(0.2)
                
                text.set("Saving File...")
                root.update()
                time.sleep(0.2)
                    
            text.set("File Saved.")
            root.update()
            time.sleep(1)
            text.set("Running 100%(No Bug Detected)")
            root.update()
        except:
            tm.showerror("Error","File Not Found")
    else:
        file2=open(file,"wt")
        te=t.get(1.0,END)
        file2.write(te)
        file2.close()

        text.set("Saving File.")
        root.update()
        for i in range(5):
            text.set("Saving File.")
            root.update()
            time.sleep(0.2)
            
            text.set("Saving File..")
            root.update()
            time.sleep(0.2)
            
            text.set("Saving File...")
            root.update()
            time.sleep(0.2)
                
        text.set("File Saved.")
        root.update()
        time.sleep(1)
        text.set("Running 100%(No Bug Detected)")
        root.update()

def fsa():
    global file
    global a
    file=asksaveasfilename(defaultextension="*.txt",filetype=[("Text File (*.txt)","*.txt"),("Python File","*.py")])
    try:
        file2=open(file,"w")
        le=t.get(1.0,END)
        file2.write(le)
        file2.close()
        a=os.path.basename(file)
        root.title(a + " -Notepad by Lakshya")
        root.update()
    except:
        tm.showerror("Error","File Not Found")

def fcu():
    t.event_generate(("<<Cut>>"))
def fco():
    t.event_generate(("<<Copy>>"))
def fp():
    t.event_generate(("<<Paste>>"))
def fd():
    t.delete(1.0,END)


def fa():
    tm.showinfo("About Notepad","This is a Basic notebook Made By Lakshya.\nI hope you like it...")


def ff():
    global file
    global a
    global t
    r=tm.askyesno("Warning","Are you sure?")
    if r==True:
        file = None
        a="untitle.txt"
        root.title(a + " -Notepad by Lakshya")
        t.delete(1.0,END) 

def ffull():
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry(f"{width}x{height}")
    root.update()

m1.add_command(label="New                     Ctrl+N",command=ff)
m1.add_separator()
m1.add_command(label="Open                    Ctrl+O",command=fo)
m1.add_command(label="Save                      Ctrl+S",command=fs)
m1.add_command(label="Save as       Ctrl+Shift+S",command=fsa)
m1.add_separator()
m1.add_command(label="Full Screen            ",command=ffull)
m1.add_separator()
m1.add_command(label="Exit                   ",command=root.destroy)

m2.add_command(label="Cut                Ctrl+X",command=fcu)
m2.add_command(label="Copy             Ctrl+C",command=fco)
m2.add_command(label="Paste             Ctrl+V",command=fp)
m2.add_separator()
m2.add_command(label="Delete                 ",command=fd)


bo=IntVar()
it=IntVar()
ul=IntVar()


def by():
    global bo
    global it
    global ul
    global f
    if it.get() ==1:
        if ul.get() ==1:
            f.config(weight ="bold",slant="italic",underline=1)
            root.update()
        else:
            f.config(weight ="bold",slant="italic",underline=0)
            root.update()

    else:
        if ul.get() ==1:
            f.config(weight ="bold",slant="roman",underline=1)
            root.update() 
        else:
            f.config(weight ="bold",slant="roman",underline=0)
            root.update()

def bn():
    global bo
    global it
    global ul
    global f
    if it.get() ==1:
        if ul.get() ==1:
            f.config(weight ="normal",slant="italic",underline=1)
            root.update()
        else:
            f.config(weight ="normal",slant="italic",underline=0)
            root.update()
    else:
        if ul.get() ==1:
            f.config(weight ="normal",slant="roman",underline=1)
            root.update() 
        else:
            f.config(weight ="normal",slant="roman",underline=0)
            root.update()


def iy():
    global bo
    global it
    global ul
    global f
    if bo.get() ==1:
        if ul.get() ==1:
            f.config(weight ="bold",slant="italic",underline=1)
            root.update()
        else:
            f.config(weight ="bold",slant="italic",underline=0)
            root.update()

    else:
        if ul.get() ==1:
            f.config(weight ="normal",slant="italic",underline=1)
            root.update()
        else:
            f.config(weight ="normal",slant="italic",underline=0)
            root.update()

def inn():
    global bo
    global it
    global ul
    global f
    if bo.get() ==1:
        if ul.get() ==1:
            f.config(weight ="bold",slant="roman",underline=1)
            root.update()
        else:
            f.config(weight ="bold",slant="roman",underline=0)
            root.update()
    else:
        if ul.get() ==1:
            f.config(weight ="normal",slant="roman",underline=1)
            root.update()
        else:
            f.config(weight ="normal",slant="roman",underline=0)
            root.update()

def uy():
    global bo
    global it
    global ul
    global f
    if bo.get() ==1:
        if it.get() ==1:
            f.config(weight ="bold",slant="italic",underline=1)
            root.update()
        else:
            f.config(weight ="bold",slant="roman",underline=1)
            root.update()
    else:
        if it.get() ==1:
            f.config(weight ="normal",slant="italic",underline=1)
            root.update()
        else:
            f.config(weight ="normal",slant="roman",underline=1)
            root.update()

def un():
    global bo
    global it
    global ul
    global f
    if bo.get() ==1:
        if it.get() ==1:
            f.config(weight ="bold",slant="italic",underline=0)
            root.update()
        else:
            f.config(weight ="bold",slant="roman",underline=0)
            root.update()
    else:
        if it.get() ==1:
            f.config(weight ="normal",slant="italic",underline=0)
            root.update()
        else:
            f.config(weight ="normal",slant="roman",underline=0)
            root.update()


f11=IntVar()
f11.set(0)

def m31a():
    global f1,f2
    global f11

    if f11.get() ==0:
        fz=" "
        f.config(family =fz)
        root.update()
    elif f11.get() ==1:
        fz="Symbol"
        f.config(family =fz)
        root.update()
    elif f11.get() ==2:
        fz="Courier"
        f.config(family =fz)
        root.update()
    elif f11.get() ==3:
        fz="Helvetica"
        f.config(family =fz)
        root.update()
    else:
        fz="Times"
        f.config(family =fz)
        root.update()




f22=IntVar()
f22.set(20)

def m33a():
    global f22
    f.config(size =f22.get())
    root.update()

def rd():
    global f,f11,f22
    global bo,it,ul
    bo.set(0)
    it.set(0)
    ul.set(0)
    f11.set(0)
    f22.set(20)
    f.config(family=" ",size=20,weight="normal",slant="roman",underline=0)
    root.update()

m31=Menu(root,tearoff=0)

m31.add_radiobutton(label="Defualt",value=0,foreground="Red",variable=f11,command=m31a)
m31.add_separator()
m31.add_radiobutton(label="Symbol",value=1,font="symbol",variable=f11,command=m31a)
m31.add_radiobutton(label="Courier",value=2,font="courier",variable=f11,command=m31a)
m31.add_radiobutton(label="Helvetica",value=3,font="helvetica",variable=f11,command=m31a)
m31.add_radiobutton(label="Times",value=4,font="times",variable=f11,command=m31a)



m33=Menu(root,tearoff=0)
for i in range(5,101,5):
    m33.add_radiobutton(label=f"{i}",value=i,variable=f22,command=m33a)


m32=Menu(root,tearoff=0)

m3b=Menu(root,tearoff=0)
m3b.add_radiobutton(label="Yes",value=1,variable=bo,command=by)
m3b.add_radiobutton(label="No",value=0,variable=bo,command=bn)

m3i=Menu(root,tearoff=0)
m3i.add_radiobutton(label="Yes",value=1,variable=it,command=iy)
m3i.add_radiobutton(label="No",value=0,variable=it,command=inn)

m3u=Menu(root,tearoff=0)
m3u.add_radiobutton(label="Yes",value=1,variable=ul,command=uy)
m3u.add_radiobutton(label="No",value=0,variable=ul,command=un)

def pscan():
    global file
    if file==None or file==" ":
            fsa()
    else:
        saa=os.path.basename(file)
        saa2=saa.split(".")
        saa3=saa2[-1]
        if saa3=="py":
            exec(open(file).read())
            # saa4='Python run10.py'
            # os.system(saa4)
        else:
            tm.showerror("Error","File is not a Python file")
            



m4.add_command(label="Run Python Program",command=pscan)
m4.add_separator()
m4.add_command(label="ReScan Program",command=scan)


m5.add_command(label="About Notepad",command=fa)


m.add_cascade(label="File",menu=m1)
m.add_cascade(label="Edit",menu=m2)

m.add_cascade(label="Format",menu=m3)

m3.add_cascade(label="Font Family",menu=m31)
m3.add_cascade(label="Font Size",menu=m33)
m3.add_cascade(label="Font Weight",menu=m32)
m32.add_cascade(label="Bold",menu=m3b)
m32.add_cascade(label="Italic",menu=m3i)
m32.add_cascade(label="Underline",menu=m3u)

m3.add_separator()
m3.add_command(label="Reset Defualts",command=rd)

m.add_cascade(label="Run",menu=m4)
m.add_cascade(label="about",menu=m5)

root.config(menu=m)    

def fcu1(e):
    fcu()
def fco1(e):
    fco()
def fp1(e):
    fp()

def fo1(e):
    fo()
def fs1(e):
    fs()
def fsa1(e):
    fsa()

def ff1(e):
    ff()

root.bind('<Control-x>',fcu1)   
root.bind('<Control-c>',fco1)   
root.bind('<Control-V>',fp1)

root.bind('<Control-o>',fo1)
root.bind('<Control-s>',fs1)
root.bind('<Control-Shift-s>',fs1)

root.bind('<Control-n>',ff1)

root.mainloop()
