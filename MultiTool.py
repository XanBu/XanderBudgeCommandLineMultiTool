import subprocess #used to execute other commands
import sys #for executable
import os

def main():
    clearScreen()
    titleScreen()


def clearScreen():
    os.system('cls') #windows

def titleScreen():
    # title
    print("=== Multitool ===")
    print("1) Calendar")
    print("q) Quit")

    # get user input
    choice = input("> ").strip().lower()

    if choice == "1":  # calcure calander *must be previously installed by user*
        subprocess.run([sys.executable, "-m", "calcure"])
    elif choice == "q":  # exit
        return
    else:
        print("Unknown option")  # other catch-all


if __name__ == "__main__":
    main()