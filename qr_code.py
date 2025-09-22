import qrcode
from tkinter import *
from tkinter import colorchooser, filedialog
from PIL import Image, ImageTk


def generate_qr():
    url = url_entry.get()
    fill = fill_color_var.get()
    back = back_color_var.get()

    if not url:
        result_label.config(text="Please enter a URL")
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=back)

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files","*.png")])
    if save_path:
        img.save(save_path)
        result_label.config(text=f"QR code saved at {save_path}")

    img = img.resize((250, 250))
    img_tk = ImageTk.PhotoImage(img)
    preview_label.config(image=img_tk)
    preview_label.image = img_tk

def choose_fill_color():
    color = colorchooser.askcolor()[1]
    if color:
        fill_color_var.set(color)

def choose_back_color():
    color = colorchooser.askcolor()[1]
    if color:
        back_color_var.set(color)

# ----------------------------
# Tkinter GUI Setup
# ----------------------------
root = Tk()
root.title("QR Code Generator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")  # fills entire screen

root.configure(bg="#e0e0f8")  # light web-like background
root.resizable(False, False)

# Main container frame with rounded corners (simulate web card)
frame = Frame(root, bg="white", bd=0)
frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=screen_width*0.8, height=screen_height*0.8)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))


# Title
Label(frame, text="QR Code Generator", font=("Segoe UI", 22, "bold"), bg="white", fg="#333").pack(pady=20)

# URL input
url_entry = Entry(frame, width=30, font=("Segoe UI", 14), bd=2, relief=RIDGE, justify=CENTER)
url_entry.pack(pady=10, ipady=5)

# Color pickers
fill_color_var = StringVar(value="black")
back_color_var = StringVar(value="white")

def styled_button(master, text, command, bg="#4caf50"):
    btn = Button(master, text=text, command=command, font=("Segoe UI", 12, "bold"),
                 bg=bg, fg="white", bd=0, relief=FLAT, activebackground="#66bb6a", cursor="hand2")
    btn.pack(pady=8, ipady=5, ipadx=10)
    return btn

styled_button(frame, "Choose Fill Color", choose_fill_color, bg="#ff5722")
styled_button(frame, "Choose Background Color", choose_back_color, bg="#2196f3")
styled_button(frame, "Generate QR Code", generate_qr, bg="#9c27b0")

# QR Preview
preview_label = Label(frame, bg="white")
preview_label.pack(pady=15)

# Result label
result_label = Label(frame, text="", bg="white", fg="green", font=("Segoe UI", 12, "bold"))
result_label.pack(pady=5)

# Rounded corners and shadow effect simulation
def add_shadow(widget, color="#bbb"):
    shadow = Frame(root, bg=color)
    shadow.place(x=widget.winfo_x()+5, y=widget.winfo_y()+5,
                 width=widget.winfo_width(), height=widget.winfo_height())

root.mainloop()
