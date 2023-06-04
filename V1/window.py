from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x800")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 800,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 400.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 33, y = 166,
    width = 183,
    height = 26)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 33, y = 206,
    width = 183,
    height = 26)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 33, y = 338,
    width = 183,
    height = 26)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 33, y = 250,
    width = 183,
    height = 26)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 33, y = 294,
    width = 183,
    height = 26)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 33, y = 382,
    width = 183,
    height = 26)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 33, y = 426,
    width = 183,
    height = 26)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 276, y = 447,
    width = 131,
    height = 42)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    398.5, 176.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 296.0, y = 155,
    width = 205.0,
    height = 40)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    398.5, 379.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 296.0, y = 358,
    width = 205.0,
    height = 40)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    398.5, 547.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 296.0, y = 526,
    width = 205.0,
    height = 40)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    398.5, 277.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 296.0, y = 256,
    width = 205.0,
    height = 40)

window.resizable(False, False)
window.mainloop()
