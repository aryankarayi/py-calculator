from tkinter import *
import tkinter


def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    if num == "*":
        equation_label.set(equation_text[:-1] + "x")

    elif num == "/":
        equation_label.set(equation_text[:-1] + "÷")
    else:
        equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Zero Division Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")

def delete():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def main():
    window = Tk()
    window.title("Calculator")
    window.geometry("300x440")
    global equation_text
    equation_text = ""
    global equation_label
    equation_label = StringVar()
    label = Label(window, textvariable = equation_label, font = ("Arial", 25, "bold"), bg="white", width = 300, height = 100)
    label.place(bordermode=INSIDE, height = 60, width = 300, x = -7, y = 50)

    frame = Frame()
    frame.pack()


    top1 = Button(window, font= ("Arial", 12), text = "C", height = 4, width = 9, borderwidth=0, command = lambda: clear())
    top1.place(bordermode=INSIDE , height=40, width=140, x= 0, y= 158)


    top1 = Button(window, font= ("Arial", 12), text = "⌫", height = 4, width = 9, borderwidth=0, command = lambda: delete())
    top1.place(bordermode=INSIDE , height=40, width=70, x= 140, y= 158)

    divide = Button(window, font= ("Arial", 15), text = "÷", height = 4, width = 9, borderwidth=0, command = lambda: button_press("/"))
    divide.place(bordermode=INSIDE , height=40, width=90, x= 210, y= 158)

    # Row 1

    button1 = Button(window, font = ("Arial", 15), text = 1, height = 4, width = 9, borderwidth = 0, command = lambda: button_press(1))
    button1.place(bordermode=INSIDE , height=60, width=70, x= 0, y= 200)

    button2 = Button(window, font= ("Arial", 15), text = 2, height = 4, width = 9, borderwidth = 0, command = lambda: button_press(2))
    button2.place(bordermode=INSIDE , height=60, width=70, x= 70, y= 200)

    button3 = Button(window, font= ("Arial", 15), text = 3, height = 4, width = 9, borderwidth=0, command = lambda: button_press(3))
    button3.place(bordermode=OUTSIDE , height=60, width=70, x= 140, y= 200)

    button4 = Button(window, font= ("Arial", 15), text = "x", height = 4, width = 9, borderwidth=0, command = lambda: button_press("*"))
    button4.place(bordermode=OUTSIDE , height=60, width=90, x= 210, y= 200)


    button5 = Button(window, font= ("Arial", 15), text = 4, height = 4, width = 9, borderwidth= 0, command = lambda: button_press(4))
    button5.place(bordermode=INSIDE , height=60, width=70, x= 0, y= 260)

    button6 = Button(window, font= ("Arial", 15), text = 5, height = 4, width = 9, borderwidth=0, command = lambda: button_press(5))
    button6.place(bordermode=INSIDE , height=60, width=70, x= 70, y= 260)

    button7 = Button(window, font= ("Arial", 15), text = 6, height = 4, width = 9, borderwidth=0, command = lambda: button_press(6))
    button7.place(bordermode=OUTSIDE , height=60, width=70, x= 140, y= 260)

    minus = Button(window, font= ("Arial", 15), text = "-", height = 4, width = 9, borderwidth=0, command = lambda: button_press("-"))
    minus.place(bordermode=OUTSIDE , height=60, width=90, x= 210, y= 260)

    # Row 3

    button9 = Button(window, font= ("Arial", 15), text = 7, height = 4, width = 9, borderwidth=0, command = lambda: button_press(7))
    button9.place(bordermode=INSIDE , height=60, width=70, x= 0, y= 320)

    button10 = Button(window, font= ("Arial", 15), text = 8, height = 4, width = 9, borderwidth=0, command = lambda: button_press(8))
    button10.place(bordermode=INSIDE , height=60, width=70, x= 70, y= 320)

    button11 = Button(window, font= ("Arial", 15), text = 9, height = 4, width = 9, borderwidth=0, command = lambda: button_press(9))
    button11.place(bordermode=OUTSIDE , height=60, width=70, x= 140, y= 320)

    add = Button(window, font= ("Arial", 15), text = "+", height = 4, width = 9, borderwidth=0, command = lambda: button_press("+"))
    add.place(bordermode=OUTSIDE , height=60, width=90, x= 210, y= 320)

    # Row 4

    button9 = Button(window, text = ".", font= ("Arial", 20), height = 4, width = 9, borderwidth = 0, command = lambda: button_press("."))
    button9.place(bordermode=INSIDE , height=60, width=70, x= 0, y= 380)

    button10 = Button(window, font= ("Arial", 15), text = 0, height = 4, width = 9, borderwidth=0, command = lambda: button_press("0"))
    button10.place(bordermode=INSIDE , height=60, width=70, x= 70, y= 380)


    button12 = Button(window, bg = "#ADD8E6", font= ("Arial", 15), text = "=", height = 4, width = 9, borderwidth=0, command = lambda: equals())
    button12.place(bordermode=OUTSIDE , height=60, width=165, x= 140, y= 385)



    window.mainloop()

if __name__ == "__main__":
    main()