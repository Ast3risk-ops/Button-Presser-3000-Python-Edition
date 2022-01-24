from time import sleep
from guizero import App
from sys import exit
from os import system

# Windows Version (has the color thing)
# A dumb game idea I had based on some spectrum code I found in a book about bad, old games.
# It's been designed to be the worst game ever and also to be boring.
# It's been ported to Python, the info boxes and stuff are extras I added on for fun (It's kinda dumb, I know)
system("color f0")
system("cls")
app = App(title="Hey, you're not supposed to see this!")
while True:
    app.hide()
    print("Press T and Enter to win!")
    sleep(1)
    key = input(">")
    if key == "t":
        break
    elif key == "T":
        break
    elif key == "c":
        print("Cheat mode active!")
    elif key == "":
        app.info("Hey...", "You didn't type anything!")
        app.warn("!", "Don't do that AGAIN!")
        app.warn("!", "AGAIN, You hear me?")
        app.warn(
            "Oh no!"
            "If you don't read the instructions, you could lose your chance to win a copy of this game's sequel!"
        )
        app.error("ERR", "ERR_NO_INPUT")
        app.destroy()
        exit(["ERR_NO_INPUT"])
    else:

        app.info("It was so simple...", "Why didn't you press T?")
        app.info("INFO", "Try reading ihe instructions next time!")
        app.warn(
            "Oh No!",
            "If you don't read the instructions, you could lose your chance to win a copy of this game's sequel!",
        )
        app.error("ERR", "ERR_WRONG_KEY")
        exit(["ERR_WRONG_KEY"])
app.hide()
app.info("SUCCESS!", "You Win!")
app.info("Also..", "You now have a chance to win a copy of the game's sequel!")
app.info("INFO", "Enter your address at the next prompt to get your copy!")
address = app.question("Address Input Box(tm)", "Enter your address here!")
app.info("Thanks!", "Thank you for your address!")
app.warn("REQUEST(HTTP)", "SENDING ADDRESS...")
app.info("NEW MESSAGE!", "Order confirmation!")
print(address)
sleep(3)
exit(["SUCCESS"])
# Wow, you read all the code (I think)!





































































# Coded with Mu










































































































































# Wow, you scrolled to the bottom!
