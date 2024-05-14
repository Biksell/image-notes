import tkinter.filedialog
import keyboard
import threading
import sys
from tkinter import *
from PIL import ImageTk
from os.path import basename
from os import system

images = []
img = None
img_width = 500
img_height = 500

hotkey_forward = "pg up"
hotkey_backward = "pg dn"

running = True

index = 0

def choose_files():
    global img, canvas, images
    images = tkinter.filedialog.askopenfilenames()
    if len(images) > 0:
        update_canvas()
    print(len(images))
    return

def update_canvas():
    global img, img_width, img_height, root, index
    if index == len(images):
        index = 0
    elif index < 0:
        index = len(images) - 1
    if len(images) <= 0:
        img = ImageTk.PhotoImage(file="default.png")
    else:
        img = ImageTk.PhotoImage(file=images[index])
    img_width = img.width()
    img_height = img.height()
    canvas.itemconfig(img_ref, image=img)
    root.geometry(f"{img_width}x{img_height + 20}")
    lblFile.config(text=f"Current file: {basename(images[index])}")
    return
'''
def setKey():
    global hotkey
    btnSetKey.configure(text="<Press a key>")
    hotkey = keyboard.read_event().name
    lblKey.configure(text="Current hotkey: {}".format(hotkey))
    btnSetKey.configure(text="Set new hotkey")
'''

def update():
    global hotkey_backward, hotkey_forward, img, root, index, images
    while running:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == hotkey_forward:
                index += 1
                update_canvas()
            elif event.name == hotkey_backward:
                index -= 1
                update_canvas()
    return

def handleClosing():
    global running
    running = False
    system("taskkill /f /im image_notes.exe")
    root.destroy()
    sys.exit()
    return

threading.Thread(target=update).start()

# Tkinter init
root = Tk()
root.configure(bg="#000000")
root.title("Image Notes v0.1")

topFrame = Frame(root, pady=10, bg="#000000")
topFrame.pack(side=TOP)
lblFile = Label(topFrame, text="Current file: ", padx=2, pady=2, bg="#000000", fg="white", font="Arial 10 bold")
lblFile.pack(side=LEFT)
btnFilePicker = Button(topFrame, text="Choose Files...", command=lambda: threading.Thread(target=choose_files).start())
btnFilePicker.pack(side=LEFT)

# Hotkey
lblKey = Label(topFrame, text=f"Hotkeys: {hotkey_forward}, {hotkey_backward}", padx=2, pady=2, bg="#10141a", fg="white", font='Arial 10 bold')
lblKey.pack(side=LEFT)

# Canvas
botFrame = Frame(root, pady=10, bg="#0f0f00")
botFrame.pack()
canvas = Canvas(root, width=img_width, height=img_height)
img = ImageTk.PhotoImage(file="default.png")
img_ref = canvas.create_image(0, 0, image=img, anchor=NW)
root.geometry(f"{img.width()}x{img.height() + 20}")
canvas.pack(fill=BOTH, expand=True, side=BOTTOM)

root.protocol("WM_DELETE_WINDOW", handleClosing)
root.mainloop()
