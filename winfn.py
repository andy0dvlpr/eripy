import os

def programs():
    print("You have accessed 'Programs' for Windows.")
    print("Function hasn't been implemented yet.")

def power():
    print("""
    s) Shut Down
    r) Restart
    l) Logoff
    i) Network Shutdown
    """)
    # WARNING: Security risk if somebody places a shutdown.bat with malicious code in the same directory.
    while True:
        x = input()
        if x not in ("s", "r", "l", "i"):
            print("Invalid Command!")
            continue
        else:
            break
    if x == "s":
        os.system("shutdown -s -f -t 0")
    elif x == "r":
        os.system("shutdown -r -f -t 0")
    elif x == "l":
        os.system("shutdown -l")
    elif x == "i":
        os.system("shutdown -i")