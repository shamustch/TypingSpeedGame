import tkinter as tk
import time
import keyboard
import datetime

def returnWpm(Time, textin):
    #Calculation to measure wpm here
    #wpm = characters per second / 5 * 60
    words = textin.split()
    lettercount = len(words)/5
    wordsperminute = lettercount/Time

#Create Gui Window
window = tk.Tk()
window.configure(bg='black')
wordlist = tk.Label(text="Wouldn't it be lovely to enjoy a week soaking up the culture?")
prompt = tk.Label(text="Press Enter to Begin.")
promptvar = tk.StringVar()
prompt["textvariable"] = now
prompt.config(font=("Courier", 12))
wordlist.config(font=("Courier", 16))
wpm = tk.Label(font=('Helvetica', 24))

#Update every 300 milliseconds
def updatewindow():
  now = tk.StringVar()
  wpm["textvariable"] = now
  ##Messed something up around here, will fix another time.
  if keyboard.is_pressed('Enter'):
    begintime=datetime.now()
    promptvar.set("Go!")
  now.set(returnWpm(begintime, textinput.get()))
  #Everything before this line gets repeated
  window.after(300, updatewindow)

#Text Input Variable
textinput = tk.Entry(width=70)

#Pack labels
wordlist.pack(padx=100,pady=20)
prompt.pack(padx=100,pady=10)
wpm.pack(padx=100,pady=10)
textinput.pack(padx=100,pady=40)
updatewindow()
window.mainloop()