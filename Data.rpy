# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:
    python:
        import requests
        URL = "https://script.google.com/macros/s/AKfycbwBiizSuSugcbzRMU5Ew2A3mFlIgDclbhwc9ZaqhB4V6W8DNNo/exec"
        hRate = renpy.input("hrate")
        requests.post(URL, json={'score' : hRate,}, timeout=2.5)
    "Good job nerd"

    jump leaderboard



label leaderboard:
    $ lb = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vSfkhPdkM2TOCXm4pHkcvPJcw1y1l0hWUJx46kSNKMHzVsZ5hvU3A6FJS2cL_5z7hGgSnx3yKBz1afL/pub?gid=14353808&single=true&output=csv")
    show screen leaderboard
    "Leaderboard:"

    return

screen leaderboard():
    vbox:
        xpos 50
        ypos 50
        text _("{color=#fff}{size=48}[lb.text]{/size}{/color}")


