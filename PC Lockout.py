import time
import ctypes
import csv


user32 = ctypes.windll.User32
OpenDesktop = user32.OpenDesktopW
SwitchDesktop = user32.SwitchDesktop

DESKTOP_SWITCHDESKTOP = 0x0100

def writeFile(state):
    with open('lockederno.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(state)
        

while 1:
    hDesktop = OpenDesktop("default", 0, False, DESKTOP_SWITCHDESKTOP)
    result = SwitchDesktop(hDesktop)
    if result:
        print(time.asctime(), "Unlocked")
        time.sleep(1.0)
      #  writeFile('Unlocked')
    else:
        print(time.asctime (), "Desktop is Locked")
       # writeFile('Locked')
        time.sleep(2)


