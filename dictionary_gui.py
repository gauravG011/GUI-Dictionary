import json
from difflib import get_close_matches
from tkinter import *
window=Tk()
window.title("Welcome to the Dictionary")
window.geometry("400x250")
lb1=Label(window,text=" Enter the word\t",font=("Times New Roman",17))
lb1.grid(row=0,column=0)
txt1=Entry(window,width=30)
txt1.grid(row=0,column=25)
def clicked():
    word=txt1.get()
    data=json.load(open("data.json"))
    word=word.lower()
    if word in data:
        res=data[word]
        lb2=Label(window,text=res,font=("Times New Roman",11))
        lb2.place(x=20,y=110)
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        res='did you mean %s instead%get_close_matches(word,data.keys())[0])'
        lb2=Label(window,text=res,font=("Times New Roman",17))
        lb2.place(relx=0.8,rely=0.5,anchor=CENTER)
        decide=input("press y for yes or n for no ")
        if decide=='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=='n':
            return "please enter correct word"
        else:
            return "You have just entered wronf input please enter y or n"
    else:
        return "please enter correct word"
btn=Button(window,text="Search",font=("Times New Roman",17),command=clicked,fg="red",bg="black")
btn.place(x=170,y=40)
window.mainloop()
