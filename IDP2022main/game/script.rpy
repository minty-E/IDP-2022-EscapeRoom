# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

python:
    inputName = input("What is your name? ")


# add color to characters later
define company = Character("Odyssey7")
define mc = Character(inputName)
define j = Character("Jeremy")
define a = Character("Audrey")
define vc = Character("Village Chief")
define hinter = Character("Puzzle Master")
define vt = Character("Voice in the Tower")

# declare images here
#image Odyssey7 default = "" 






# audrey photos
image audrey default = "/Audrey/audreyDefault.png"
image audrey confused = "/Audrey/audreyConfused.png"
image audrey evil = "/Audrey/audreyEvilLaugh.png"
image audrey happy = "/Audrey/audreyHappy.png"
image audrey mad = "/Audrey/audreyMad.png"




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    #show Odyssey7 default at center 

    #company "Dear valued customer, \n You have been selected to be an alpha tester of our brand new game! We have spent the last ___ years developing this exciting new open world fantasy adventure game!"
    # fix dialogue


    # entering the game

    "Huh..? Where am I?"
    "It's so dark..."
    "Wait, I see a light! I should head to it."

    # exits cave
    #scene bg outsideOfCave

    # introduction to jeremy and audrey
    #scene bg berries

    "Huh, are those people? They must be the new AI characters that Odyssey said they made. I should go up to them!"

    "..."

    mc "Hey, you two! Hey!"

    scene bg berriesWithout

    # talk to jeremy and audrey

    show audrey mad at left
    #show jeremy default at right

    a "Hello there!"

    j "Hi!"

    # This ends the game.

    return
