from tkinter import *
from tkinter import messagebox


def pressed(button, number):
    global currentUser, count
    data[number] = currentUser
    if button["text"] == " " and currentUser == userFirst:
        button["text"] = userFirst
        button["bg"] = "RED"
        count += 1
    elif button["text"] == " " and currentUser == userSecond:
        button["text"] = userSecond
        button["bg"] = "RED"
        count += 1

    isWinner = winner(currentUser)
    print(data)
    if count == 9 and isWinner is False:
        messagebox.showinfo("Nobody Wins")
        disableButtons()
    if isWinner:
        # labelWinner = Label(root, text = f'{currentUser} wins', padx = 240, pady = 20, bg = "BLUE")
        # labelWinner.grid(row = 3, column = 0, columnspan = 3)
        messagebox.showinfo(f'{currentUser} wins!!')
        disableButtons()

    if currentUser == userFirst:
        currentUser = userSecond
    else:
        currentUser = userFirst


def disableButtons():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)


def winner(currentUser):
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, data
    if data.get("1") == data.get("2") == data.get("3") == currentUser:
        button1.config(bg="BLUE")
        button2.config(bg="BLUE")
        button3.config(bg="BLUE")
        return True
    elif data.get("4") == data.get("5") == data.get("6") == currentUser:
        button4.config(bg="BLUE")
        button5.config(bg="BLUE")
        button6.config(bg="BLUE")
        return True
    elif data.get("7") == data.get("8") == data.get("9") == currentUser:
        button7.config(bg="BLUE")
        button8.config(bg="BLUE")
        button9.config(bg="BLUE")
        return True
    elif data.get("1") == data.get("4") == data.get("7") == currentUser:
        button1.config(bg="BLUE")
        button4.config(bg="BLUE")
        button7.config(bg="BLUE")
        return True
    elif data.get("2") == data.get("5") == data.get("8") == currentUser:
        button2.config(bg="BLUE")
        button5.config(bg="BLUE")
        button8.config(bg="BLUE")
        return True
    elif data.get("3") == data.get("6") == data.get("9") == currentUser:
        button3.config(bg="BLUE")
        button6.config(bg="BLUE")
        button9.config(bg="BLUE")
        return True
    elif data.get("1") == data.get("5") == data.get("9") == currentUser:
        button1.config(bg="BLUE")
        button5.config(bg="BLUE")
        button9.config(bg="BLUE")
        return True
    elif data.get("3") == data.get("5") == data.get("7") == currentUser:
        button3.config(bg="BLUE")
        button5.config(bg="BLUE")
        button7.config(bg="BLUE")
        return True
    else:
        return False

def reset():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, data
    button1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button1, '1'))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button2, '2'))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button3, '3'))

    button4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button4, '4'))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button5, '5'))
    button6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button6, '6'))

    button7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button7, '7'))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button8, '8'))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button9, '9'))

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)

    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    data = {x: " " for x in data.keys()}
    print(data)


if __name__ == "__main__":
    root = Tk()
    data = {'1': "",
            '2': "",
            '3': "",
            '4': "",
            '5': "",
            '6': "",
            '7': "",
            '8': "",
            '9': ""}
    userFirst = 'X'
    userSecond = 'O'
    currentUser = userFirst
    count = 0
    button1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button1, '1'))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button2, '2'))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button3, '3'))

    button4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button4, '4'))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button5, '5'))
    button6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button6, '6'))

    button7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button7, '7'))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button8, '8'))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: pressed(button9, '9'))

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)

    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

    mymenu = Menu(root)
    root.config(menu=mymenu)
    optionsMenu = Menu(mymenu, tearoff=False)
    mymenu.add_cascade(label="Options", menu=optionsMenu)
    optionsMenu.add_command(label="Reset Game", command=reset)

    root.mainloop()
