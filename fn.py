import webbrowser
import platform
import winfn
import linfn
import config

def help():
    webbrowser.open("https://github.com/andy0dvlpr/erib/wiki", new=2, autoraise=True)

def programs():
    if platform.system() == "Windows":
        winfn.programs()
    elif platform.system() == "Linux":
        linfn.programs()
    else:
        print("OS '%s' not supported." %platform.system())

def internet():
    print("Please enter a web adress.")
    print("Link will be opened in your default web browser, following your settings.")
    webaddr = input("https://www.") # I have to forcefully add https://www to the front, otherwise the link will be opened in IE.
    webbrowser.open("https://www.%s" %webaddr, new=config.setwebnew, autoraise=config.setwebautoraise)

def power():
    if platform.system() == "Windows":
        winfn.power()
    elif platform.system() == "Linux":
        linfn.power()
    else:
        print("OS '%s' not supported." %platform.system())