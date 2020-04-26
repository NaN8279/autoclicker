import keyboard
import mouse
import time
import tkinter
import tkinter.ttk

def autoclick():
    try:
        timestopf = float(secondsfirst.get())
    except:
        l6.config(text="Please enter a valid number for seconds!")
        return
    if timestopf <= 0:
        l6.config(text="Please enter a valid number for seconds!")
        return
    try:
        timestops = float(secondssecond.get())
    except:
        timestops = timestopf
    if mode.get() == "HOLD":
        l6.config(text="Starting with mode HOLD")
        while keyboard.is_pressed('F8') == False:
            mouse.press(mousebuttonfirst.get().lower())
            time.sleep(timestopf)
            mouse.release(mousebuttonfirst.get().lower())
            time.sleep(timestopf)
        l6.config(text="Stopped")
    elif mode.get() == "CLICK":
        if clicks.get() == "SINGLE":
            l6.config(text="Starting with mode SINGLE CLICK")
            while keyboard.is_pressed('F8') == False:
                mouse.click(mousebuttonfirst.get().lower())
                time.sleep(timestopf)
            l6.config(text="Stopped")
        else:
            l6.config(text="Starting with mode DOUBLE CLICK")
            while keyboard.is_pressed('F8') == False:
                mouse.click(mousebuttonfirst.get().lower())
                time.sleep(timestopf)
                mouse.click(mousebuttonsecond.get().lower())
                time.sleep(timestops)
            l6.config(text="Stopped")
    else:
        l6.config(text="Please make movements with the mouse. \n Wait a few seconds and then press middle click button when you are done")
        mouseevents = mouse.record(button=mouse.MIDDLE)
        l6.config(text="Replaying mouse events")
        while keyboard.is_pressed('F8') == False:
            mouse.play(mouseevents)
            time.sleep(timestopf)
        l6.config(text="Stopped")

def update_combobox(event):
    if mode.get() == "RECORD":
        mousebuttonfirst.config(state="disabled")
        mousebuttonsecond.config(state="disabled")
        clicks.config(state="disabled")
    else:
        mousebuttonfirst.config(state="readonly")
        clicks.config(state="readonly")
        if clicks.get() == "SINGLE" and mode.get() != "RECORD":
            mousebuttonsecond.config(state="disabled")
        else:
            mousebuttonsecond.config(state="readonly")

def update_button_combobox(event):
    if clicks.get() == "SINGLE" and mode.get() != "RECORD":
        mousebuttonsecond.config(state="disabled")
        secondssecond.config(state="disabled")
        mode.config(state="readonly")
    else:
        mousebuttonsecond.config(state="readonly")
        secondssecond.config(state="normal")
        mode.current(0)
        mode.config(state="disabled")

root = tkinter.Tk()
root.iconbitmap("./icon.ico")

root.title("OMEGA AUTO CLICKER OF DOOM")

root.minsize(350,100)

l1 = tkinter.Label(root, text="Enter the seconds after the first click:")
l1.grid(column=0,row=0)

secondsfirst = tkinter.Entry(root,width=10)
secondsfirst.insert(0,"0.1")
secondsfirst.grid(column=1,row=0)

l1A = tkinter.Label(root, text="Enter the seconds after the second click:")
l1A.grid(column=0,row=1)

secondssecond = tkinter.Entry(root,width=10,state="disabled")
secondssecond.grid(column=1,row=1)

l2 = tkinter.Label(root, text="Select the button to click first:")
l2.grid(column=0,row=2)

mousebuttonfirst = tkinter.ttk.Combobox(root,state="readonly")
mousebuttonfirst["values"] = ("LEFT", "RIGHT")
mousebuttonfirst.current(0)
mousebuttonfirst.grid(column=1,row=2)

l2A = tkinter.Label(root, text="Select the button to click second:")
l2A.grid(column=0,row=3)

mousebuttonsecond = tkinter.ttk.Combobox(root,state="disabled")
mousebuttonsecond["values"] = ("LEFT", "RIGHT")
mousebuttonsecond.current(0)
mousebuttonsecond.grid(column=1,row=3)

l3 = tkinter.Label(text="Select the mode:")
l3.grid(column=0,row=4)

mode = tkinter.ttk.Combobox(root, state="readonly")
mode["values"] = ("CLICK", "HOLD", "RECORD")
mode.bind("<<ComboboxSelected>>", update_combobox)
mode.current(0)
mode.grid(column=1,row=4)

l4 = tkinter.Label(root, text="Single click or double click?")
l4.grid(column=0,row=5)

clicks = tkinter.ttk.Combobox(root, state="readonly")
clicks["values"] = ("SINGLE", "DOUBLE")
clicks.current(0)
clicks.bind("<<ComboboxSelected>>", update_button_combobox)
clicks.grid(column=1,row=5)

l5 = tkinter.Label(root, text="Press F7 to start, hold F8 to stop")
l5.grid(column=0,row=6)

l6 = tkinter.Label(root)
l6.grid(column=0,row=7)

keyboard.add_hotkey('F7', autoclick)

root.mainloop()