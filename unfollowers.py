#from tkinter import *
from tkinter import Tk, mainloop, TOP, Entry, Label, W, END, PhotoImage, Canvas
from tkinter.ttk import Button
import json, os, subprocess, tkinter.filedialog

# function to log values to console and clear fields on submission
def show_entry_fields():
    cwd=(tkinter.filedialog.askdirectory())
    followers = ''
    following = ''
#    delete = ''
    for dirpath, subdirs, files in os.walk(cwd):
        for x in files:
            if 'followers.json' in x:
                followers=os.path.join(dirpath, x)
            if 'following.json' in x:
                following=os.path.join(dirpath, x)
#        for y in subdirs:
#            if 'add-data-here' in y:
#                delete=os.path.join(dirpath, y)
    file = open(followers)
    data=json.load(file)
    followers=[]
    file.close()
    for i in data['relationships_followers']:
        followers.append(i['string_list_data'][0]['value'])
    file = open(following)
    data=json.load(file)
    file.close()
    following=[]
    for i in data['relationships_following']:
        following.append(i['string_list_data'][0]['value'])
    unfollowers=['Accounts that do not follow you back:','']
    for i in following:
        if i in followers:
            continue
        else:
            unfollowers.append(i)
#    print(unfollowers)
    file = open("unfollowers.txt","w")
    for i in unfollowers:
        file.write(i+'\n')
    file.close()
    os.system("start " + "unfollowers.txt")



root=Tk()
root.geometry('520x400')
canvas=Canvas(root, width=480, height=200)
Label(root, text="Step 1: Download your data from instagram in .JSON format", wraplength=300, justify="center").grid(row=1)
Label(root, text="Step 2: Unzip your data, using any file extractor", wraplength=300, justify="center").grid(row=2)
Label(root, text="Step 3: Select the folder where your data is unzipped", wraplength=300, justify="center").grid(row=3)
image1=PhotoImage(file='unfollowersLogo.gif')
canvas.grid(row=0)
canvas.create_image(20,20,image=image1,anchor='nw')

Button(root, text='Select Folder', command=show_entry_fields).grid(row=9, column=0, pady=4)

#listens for clicks
root.mainloop()
