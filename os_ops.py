import os

paths = {
    'chrome' : "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'notepad' : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad",
    'cmd' : "C:\\Windows\\system32\\cmd"
}

#functions
def open_cmd():
    #os.system('start cmd')
    os.startfile(paths['cmd'])