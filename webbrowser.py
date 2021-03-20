import tkinter as tk
import webbrowser

root=tk.Tk()
root.geometry('400x150')
root.title("web browser")
def fb():
    webbrowser.open_new("www.facebook.com")
def yt():
    webbrowser.open_new("www.youtube.com")
def hrr():
    webbrowser.open_new("www.hackerrank.com")
def tw():
    webbrowser.open_new("www.twitter.com")
def ed():
    webbrowser.open_new("www.eduyear.com")
    

def search():
    word=x.get()
    search ='https://www.google.com/search?q='+word
    webbrowser.open_new(search)

x=tk.StringVar()

b1=tk.Button(root,text='Facebook',fg='white',bg='#3b5998',command=fb)

b2=tk.Button(root,text='youtube',fg='white',bg='red',command=yt)

b3=tk.Button(root,text='hackerrank',fg='white',bg='green',command=hrr)

b4=tk.Button(root,text='twitter',fg='white',bg='#1DA1F2',command=tw)

b5=tk.Button(root,text='eduyear',fg='white',bg='black',command=ed)

b6=tk.Button(root,text='Search',fg='white',bg='black',command=search)
b6.place(x=10,y=70,width=300,height=40)

e1=tk.Entry(root,textvariable=x)
e1.place(x=10,y=10,width=300,height=40)

root.mainloop()
