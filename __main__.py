import tkinter as tk
from timeit import default_timer as timer

from keyboard import start_recording

words = "Wouldn't it be lovely to enjoy a week soaking up the culture?"
def returnWpm(textin):
    #Calculation to measure wpm here
    #wpm = characters per second / 5 * 60
    if textin == words:
      end = timer()
      return end-start_recording
def start_timer():
  start = timer()
#Text Input Variable
textinput = tk.Entry(width=70)
#Create Gui Window
window = tk.Tk()
wordlist = tk.Label(text="Wouldn't it be lovely to enjoy a week soaking up the culture?")
prompt = tk.Label(text="Press Start to begin")
prompt.config(font=("Courier", 12))
wordlist.config(font=("Courier", 16))
b1 = tk.Button(text="Start", command=start_timer, width=12)
b2 = tk.Button(text="Done", command=returnWpm(textinput.get()), width=12)
wpm = tk.Label(font=('Helvetica', 24))


#Update every 300 milliseconds
def updatewindow():
  now = tk.StringVar()
  wpm["textvariable"] = now
  now.set(returnWpm(textinput.get()))
  #Everything before this line gets repeated
  window.after(300, updatewindow)



#Pack labels
wordlist.pack(padx=100,pady=20)
prompt.pack(padx=100,pady=10)
wpm.pack(padx=100,pady=10)
textinput.pack(padx=100,pady=40)
b1.pack(padx=100,pady=10)
b2.pack(padx=100,pady=10)
updatewindow()
window.mainloop()