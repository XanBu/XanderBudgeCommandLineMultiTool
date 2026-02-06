import subprocess #used to execute other commands
import sys #for executable
import os #for system cls
import subprocess #for powershell commands

title = r"""
  __  __       _ _   _ _____           _ 
 |  \/  |_   _| | |_(_)_   _|__   ___ | |
 | |\/| | | | | | __| | | |/ _ \ / _ \| |
 | |  | | |_| | | |_| | | | (_) | (_) | |
 |_|  |_|\__,_|_|\__|_| |_|\___/ \___/|_|
                                         
"""

def main():
    command = "Start-Process -FilePath cmd -WindowStyle Maximized"
   # run(command)
    titleScreen()


def run(command):
  subprocess.run(["powershell", "-Command", command])


def clearScreen():
    os.system('cls') #windows

def titleScreen():
    # title
    clearScreen()
    print(title)
    print("=== Multitool ===")
    print("1) Calendar")
    print("q) Quit")

    # get user input
    choice = input("> ").strip().lower()

    if choice == "1":  # calcure calander *must be previously installed by user*
        subprocess.run([sys.executable, "-m", "calcure"])
        clearScreen()
        titleScreen()
    elif choice == "q":  # exit
        return
    else:
        print("Unknown option")  # other catch-all


if __name__ == "__main__":
    main()