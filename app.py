import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()							#Start of GUI

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#Logo
logo = Image.open('logo.png') 			#logo.png must be in same directory as app
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select PDF", font="Arial")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
	browse_text.set("Open")
	file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("APK file","*apk")])
	if file:
		print("File successfully loaded")
		#add obfuscator

		
#def savefile():
#   filename = filedialog.asksaveasfile(mode='w', defaultextension=".apk")
#    if not filename:
#        return
#    edge.save(filename)

#Browse Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

root.mainloop()					#End of GUI