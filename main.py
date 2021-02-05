#ERIB port to Python

import platform
import fn
import config

print("""
---------------------------------------------
- ERIPy: Explorer Replacement Inside Python -
---------------------------------------------
Visit the project's website: https://github.com/andy0dvlpr/eripy
Copyright (c) 2021 andy0dvlpr
""")
print("Version: %s" %config.eripyver)
print("You are running %s" %platform.system() + " %s" %platform.release())
if platform.system() != "Windows" and "Linux":
    print("Warning! Your platform '%s' is not supported. This may lead to errors." %platform.system())

print("""
1) Help
2) Programs
3) Internet
4) File Browser
5) Power
6) Settings
7) Exit ERIPy
""")
# If input is invalid, ask again. If it is correct, break the loop and proceed with the rest.
while True:
    x = input()
    if x not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Invalid Command!")
        continue
    else:
        break
# Now this is where it gets messy. I feel like YandereDev... Can anybody bless me with a better solution?
if x == "1":
    fn.help()
elif x == "2":
    fn.programs()
elif x == "3":
    fn.internet()
elif x == "4":
    fn.files()
elif x == "5":
    fn.power()
elif x == "6":
    fn.settings()
elif x == "7":
    exit()