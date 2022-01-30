from tkinter import *
from tkinter.font import Font
from Ciphers import Piglatin, Ceaser, ReverseLetters, OnepadEncode, Polyalphabetic, Columnar, Emoji
from EasyFile import randomize
from random import randint
import pyglet

pyglet.font.add_file('PigpenCipher.otf')

obj = Tk()
obj.geometry("300x350")
obj.title("Cipher Game")
var = IntVar()

global message


message = [randomize("Messages.txt"), randomize("Messages.txt"), randomize("Messages.txt"), randomize("Messages.txt"),
           randomize("Messages.txt"), randomize("Messages.txt"), randomize("Messages.txt"), randomize("Messages.txt")]
while len(set(message)) < len(message):
    message = [randomize("Messages.txt"), randomize("Messages.txt"), randomize("Messages.txt"),
               randomize("Messages.txt"),
               randomize("Messages.txt"), randomize("Messages.txt"), randomize("Messages.txt"),
               randomize("Messages.txt")]

print(message)
key = [randint(0, 26) for i in range(len(message[3]))]
Ceaserkey = randint(0, 26)

userEnter = True
global did1,did2,did3,did4,did5,did6,did7,did8
did1,did2,did3,did4,did5,did6,did7,did8 = False,False,False,False,False,False,False,False


def guess():
    GuessFont = ("Times New Roman", fontsize)
    CodeFont = ("Times New Roman", 15)
    hint = ''
    # THIS IS THE GOOD STUFF
    if var.get() == 1:
        cipher = (Piglatin(message[var.get() - 1].lower())).upper()
        hint = "Igpay Atinlay!"
    elif var.get() == 2:
        cipher = Ceaser(message[var.get() - 1].upper(), Ceaserkey)
        hint = 'A equals ' + Ceaser('A', Ceaserkey) + ', and B equals ' + Ceaser('B', Ceaserkey)
    elif var.get() == 3:
        cipher = ReverseLetters(message[var.get() - 1].upper())
        hint = 'A equals Z, and Z equals A.'
    elif var.get() == 4:
        cipher = OnepadEncode(message[var.get() - 1].upper(), key)
        hint = 'The key is '+ (',').join([str(i) for i in key]) + '.'
    elif var.get() == 5:
        cipher = Polyalphabetic(message[var.get() - 1].upper())
        hint = '1st letter doesn\'t shift, while the 2nd letter shifts right 1. How many does the third letter shift?'
    elif var.get() == 6:
        cipher = Columnar(message[var.get() - 1].upper(), 4)
        hint = 'Unscramble each word into 4 different columns.'
    elif var.get() == 7:
        cipher = Emoji(message[var.get() - 1].upper())
        hint = 'The first letter of the emoji name should match what the letter should be.'
    elif var.get() == 8:
        CodeFont = ("PigpenCipher", fontsize)
        cipher = message[var.get() - 1]
        hint = 'You might want a picture of a pigpen decoder!'
    else:
        return 0

    TitleText.pack_forget()
    R1.pack_forget()
    R2.pack_forget()
    R3.pack_forget()
    R4.pack_forget()
    R5.pack_forget()
    R6.pack_forget()
    R7.pack_forget()
    R8.pack_forget()

    frame = Frame(obj)
    frame.pack()
    bottom = Frame(obj)
    bottom.pack(side=BOTTOM)
    middle = Frame(obj)
    middle.pack(side=BOTTOM)

    displayText = StringVar()
    codeText = StringVar()
    # add Hint stuff depending on var
    displayText.set("Hello, Try a Guess\nHint: " + hint +" \nThe Code is:")
    codeText.set(cipher + "\n\n\n\n\n")

    global displaySpace
    displaySpace = Label(frame, textvariable=displayText, justify="center", font=("Times New Roman", fontsize), wraplength=250)
    global codeSpace
    codeSpace = Label(frame, textvariable=codeText, justify="center", font=CodeFont)
    EntryDisplay = Label(middle, text="🔑")
    textbox = Entry(middle)



    def enterCallBack():
        userEnter = True
        global codeSpace,displaySpace,did1,did2,did3,did4,did5,did6,did7,did8

        def reset():
            cont.pack_forget()
            enterKey.pack_forget()
            backKey.pack_forget()
            textbox.pack_forget()
            EntryDisplay.pack_forget()
            displaySpace.pack_forget()
            codeSpace.pack_forget()
            middle.pack_forget()
            bottom.pack_forget()
            frame.pack_forget()

            TitleText.pack()
            R1.pack()
            R2.pack()
            R3.pack()
            R4.pack()
            R5.pack()
            R6.pack()
            R7.pack()
            R8.pack()

            if did1 and did2 and did3 and did4 and did5 and did6 and did7 and did8:
                userEnter = False
                endFrame = Frame(obj)

                final = Entry(endFrame)
                finalLabel = Label(endFrame, text="Enter the Secret Code")


                def finale():
                    if final.get().lower() == "tamuhack":
                        TitleText.pack_forget()
                        R1.pack_forget()
                        R2.pack_forget()
                        R3.pack_forget()
                        R4.pack_forget()
                        R5.pack_forget()
                        R6.pack_forget()
                        R7.pack_forget()
                        R8.pack_forget()
                        final.pack_forget()
                        finalbutton.pack_forget()

                        finalString = StringVar()
                        finalString.set("\n\nYOU WON!")
                        finalDisplay = Label(obj, textvariable=finalString, justify="center", font=("Times New Roman",25))
                        finalDisplay.pack()


                finalbutton = Button(obj,text="Continue?", command=finale)
                finalbutton.pack(side=BOTTOM)
                endFrame.pack(side=BOTTOM)
                finalLabel.pack(side=LEFT)
                final.pack(side=LEFT)




        temp = textbox.get()
        print(temp)


        cont = Button(bottom, text="Continue", command=reset)

        if temp.lower() == message[var.get() - 1]:
            displaySpace.pack_forget()
            displayText.set("Correct\n")
            displaySpace = Label(frame, textvariable=displayText, justify="center", font=("Times New Roman", 20), wraplength=250)
            displaySpace.pack()
            codeSpace.pack_forget()
            CodeFont = ("Times New Roman", fontsize)
            codeSpace = Label(frame, textvariable=codeText, justify="center", font=CodeFont)
            if var.get() == 1: did1 = True
            if var.get() == 2: did2 = True
            if var.get() == 3: did3 = True
            if var.get() == 4: did4 = True
            if var.get() == 5: did5 = True
            if var.get() == 6: did6 = True
            if var.get() == 7: did7 = True
            if var.get() == 8: did8 = True

            SecretMessage = ["Terrific!","Amazing!","Magnificent!","fabuloUs!","top notcH!","Awesome!","fantastiC!","sicK!"]
            codeText.set(SecretMessage[var.get()-1])
            codeSpace.pack()

            userEnter = False
            textbox.pack_forget()
            enterKey.pack_forget()
            backKey.pack_forget()
            EntryDisplay.pack_forget()

            # If ever I do the remove stuff dont forget that this should be where it goes
            cont.pack()
            userEnter = True
            #displaySpace.pack_forget()
           # displaySpace = Label(frame, textvariable=displayText, justify="center", font=("Times New Roman", fontsize),wraplength=250)
            #displaySpace.pack()

        elif len(temp) >= 20:
            displayText.set("Input was too long\nHint: " + hint +" \nThe Code is: ")
            codeText.set(cipher + "\n\n\n\n\n")
        else:
            displayText.set("\"" + temp + "\" was Incorrect\nHint: " + hint +" \nThe Code is: ")
            codeText.set(cipher + "\n\n\n\n\n")
        textbox.delete(0, len(temp))

    def reset2():
        enterKey.pack_forget()
        backKey.pack_forget()
        textbox.pack_forget()
        EntryDisplay.pack_forget()
        displaySpace.pack_forget()
        codeSpace.pack_forget()
        middle.pack_forget()
        bottom.pack_forget()
        frame.pack_forget()

        TitleText.pack()
        R1.pack()
        R2.pack()
        R3.pack()
        R4.pack()
        R5.pack()
        R6.pack()
        R7.pack()
        R8.pack()

    enterKey = Button(bottom, text="Enter", command=enterCallBack)
    backKey = Button(bottom, text="Back", command=reset2)

    def button_pressed(event):
        global userEnter
        #print(event.char)
        # print(event.keysym)
        if event.keysym == "Return" and userEnter: enterKey.invoke()

    obj.bind('<KeyPress>', button_pressed)

    displaySpace.pack()
    codeSpace.pack()

    EntryDisplay.pack(side=LEFT)
    textbox.pack()

    enterKey.pack()
    backKey.pack()


TitleText = Label(obj, text="Choose Your Level:\n\n", justify="center", font=("Times New Roman", 15))

fontsize = 10
R1 = Radiobutton(obj, text=Piglatin(message[0].lower()).upper(), variable=var, value=1, command=guess,
                 font=("Times New Roman", fontsize))
R2 = Radiobutton(obj, text=Ceaser(message[1].upper(), Ceaserkey).upper(), variable=var, value=2, command=guess,
                 font=("Times New Roman", fontsize))
R3 = Radiobutton(obj, text=ReverseLetters(message[2].upper()).upper(), variable=var, value=3, command=guess,
                 font=("Times New Roman", fontsize))
R4 = Radiobutton(obj, text=OnepadEncode(message[3].upper(), key), variable=var, value=4, command=guess,
                 font=("Times New Roman", fontsize))
R5 = Radiobutton(obj, text=Polyalphabetic(message[4].upper()).upper(), variable=var, value=5, command=guess,
                 font=("Times New Roman", fontsize))
R6 = Radiobutton(obj, text=Columnar(message[5].upper(), 4), variable=var, value=6, command=guess,
                 font=("Times New Roman", fontsize))
R7 = Radiobutton(obj, text=Emoji(message[6].upper()), variable=var, value=7, command=guess,
                 font=("Times New Roman", fontsize))
R8 = Radiobutton(obj, text=(message[7].upper()), variable=var, value=8, command=guess, font=("PigpenCipher", fontsize))

TitleText.pack()
R1.pack()
R2.pack()
R3.pack()
R4.pack()
R5.pack()
R6.pack()
R7.pack()
R8.pack()

obj.mainloop()
