from timeit import default_timer as timer
import typing

words = "Wouldn't it be lovely to enjoy a week soaking up the culture?"
print(words)
text = input('Enter S to start\n')
if(text.lower()=='s'):
    start = timer()
def returnWpm(textin):
    #Calculation to measure wpm here
    #61 total characters
    #cps=61/totaltime cpm=cps*60 wpm=cpm/5
    if textin == words:
      end = timer()
      totaltime = end-start
      #math
      cps =61/totaltime
      cpm =cps*60
      wpm =cpm/5
      intwpm = int(wpm)
      print("Your typing speed is "+str(intwpm)+" WPM")
    else:
        print("Incorrect word list entered.")
userinput = input('Go!\n')
returnWpm(userinput)
exit = input('Press any key to exit')