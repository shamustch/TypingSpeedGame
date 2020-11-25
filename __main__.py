import tkinter as tk
import time

def returnWpm():
    #Calculation to measure wpm here
    return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())

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
  now.set(returnWpm())
  #Everything before this line gets repeated
  window.after(500, updatewindow)

#Text Input
textinput = tk.Entry(width=70)

#Pack labels
wordlist.pack(padx=100,pady=20)
prompt.pack(padx=100,pady=10)
wpm.pack(padx=100,pady=10)
textinput.pack(padx=100,pady=40)
updatewindow()
window.mainloop()