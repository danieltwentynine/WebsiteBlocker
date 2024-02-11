from tkinter import *

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('THE DESTROYER')
Label(root, text='THE DESTROYER', font='arial 20 bold').pack(side=TOP)
Label(root, text='GLADE', font='arial 10 bold').pack(side=BOTTOM)
Label(root, text='BLOCK THIS: ', font='arial 15 bold').place(x=5, y=60)
Websites = Text(root, font='arial 10', height=2, width=40, wrap=WORD, padx=5, pady=5)
Websites.place(x=140, y=60)

host_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'


def Blocker():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))

    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text='Already Blocked', font='arial 12 bold').place(x=200, y=200)
            else:
                host_file.write(redirect + " " + website + '\n')
                Label(root, text="Blocked", font='arial 12 bold').place(x=230, y=200)


block = Button(root, text='Block', font='arial 12 bold', pady=5, command=Blocker, width=6, bg='royal blue1',
               activebackground='sky blue')
block.place(x=230, y=150)
root.mainloop()
