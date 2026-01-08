# Import Libraries
import pywhatkit as kit
import pywhatkit
import pyautogui
from tkinter import *

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message) 

    #win = Tk() # Some Tkinter stuff
    #screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
    #screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor

    #print(screen_width, screen_height) # prints your monitor's resolution

    #pywhatkit.sendwhatmsg("+91xxxxxxxxxx", "Enter Message", 0, 0) # Sends the message
    #pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964) # Moves the cursor the the message bar in Whatsapp
    #pyautogui.click() # Clicks the bar
    #pyautogui.press('enter') # Sends the message