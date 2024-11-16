import time

# Ask user if they want to repeat the program. If yes calls times() function. If not closes the program. If invalid value calls repeaterror() function
def repeat():
    s = input("\nDo you want to sing again? (Y/N) ").lower()
    if s =="y":
        times()
    elif s =="n":
        print("\nGoodbye!\n")
    else:
        repeaterror()

# Error message of loop() function. Tells to write again the value and calls time() function
def error():
    print("\nHey, I don't accept your imput. Let's try again...")
    time.sleep(2)
    times()

# Error message of repeat() function. Tells to write again the value and calls repeat() function
def repeaterror():
    print("\nHey, I don't accept your imput. Let's try again...")
    time.sleep(2)
    repeat()

# Ask user hoh many times to repeat the song
def times():
    a = input("Choose how many times to repeat the song: ")
    loop(a)

# Print the song how many times the user said
def lyrics():
    print("\nI'm a lumberjack and I'm ok")
    time.sleep(0.5)
    print("I sleep all night and work all day")

# checks that user imput is a number (.isnumeric())
# if not a number prints an error message
def loop(a):
    if a.isnumeric():
        print("\nOk, let's sing the lumberjack song!")
        for a in range(int(a)):
            time.sleep(1)
            lyrics()
        time.sleep(1.5)
        repeat()
    else:
        error()

# Clear terminal    
print(chr(27) + "[2J")

# Wtf is that? "That" is what prints the title, written in ASCII art
print("\n  _____ _____ _   _  _____               _____  ____  _   _  _____ \n / ____|_   _| \ | |/ ____|     /\      / ____|/ __ \| \ | |/ ____|\n| (___   | | |  \| | |  __     /  \    | (___ | |  | |  \| | |  __ \n \___ \  | | | . ` | | |_ |   / /\ \    \___ \| |  | | . ` | | |_ |\n ____) |_| |_| |\  | |__| |  / ____ \   ____) | |__| | |\  | |__| |\n|_____/|_____|_| \_|\_____| /_/    \_\ |_____/ \____/|_| \_|\_____|\n\n")

# start the program by calling times function
times()
