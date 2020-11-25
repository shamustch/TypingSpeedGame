import tkinter as tk
import time

def returnWpm(textin):
    #Calculation to measure wpm here
    #wpm = characters per second / 5 * 60
    return textin

#Create Gui Window
window = tk.Tk()
window.configure(bg='black')
wordlist = tk.Label(text="Wouldn't it be lovely to enjoy a week soaking up the culture?")
prompt = tk.Label(text="Start typing to begin!")
prompt.config(font=("Courier", 12))
wordlist.config(font=("Courier", 16))
wpm = tk.Label(font=('Helvetica', 24))

#Update every 500 milliseconds
def updatewindow():
  now = tk.StringVar()
  wpm["textvariable"] = now
  now.set(returnWpm(textinput.get()))
  #Everything before this line gets repeated
  window.after(300, updatewindow)

#Text Input
textinput = tk.Entry(width=70)

#Pack labels
wordlist.pack(padx=100,pady=20)
prompt.pack(padx=100,pady=10)
wpm.pack(padx=100,pady=10)
textinput.pack(padx=100,pady=40)
updatewindow()
window.mainloop()