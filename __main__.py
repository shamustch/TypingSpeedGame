import tkinter as tk

#Create Gui Window
window = tk.Tk()
window.configure(bg='black')
wordlist = tk.Label(text="Wouldn't it be lovely to enjoy a week soaking up the culture?")
wordlist.config(font=("Courier", 18))
#Text Input
textinput = tk.Entry(width=80)
#Pack labels
wordlist.pack(padx=120,pady=20)
textinput.pack(padx=120,pady=40)
window.mainloop()