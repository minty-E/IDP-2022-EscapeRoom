# The script of the game goes in this file.
init python:
    hintUsed = 0
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    show screen p1_2Hint()

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"



"""
label endingSurvey:
    #finish fail safe
    q1 = input("What was the best or worst puzzle in the game and why?")
    q2 = input("How would you rate the overall experience 1 to 5?")
    q3 = input("Would you recommend it to a friend?")
    q4 = input("On a scale from  1 to 5, how engaging were the puzzles?")
    q5 = input("How were you feeling throughout the game? Select all that apply.")

label endingSurvey:
    #finish fail safe
    q1 = input("What was the best or worst puzzle in the game and why?")
    q2 = input("How would you rate the overall experience 1 to 5?")
    q3 = input("Would you recommend it to a friend?")
    q4 = input("On a scale from  1 to 5, how engaging were the puzzles?")
    q5 = input("How were you feeling throughout the game? Select all that apply.")


label endingSurvey:
    #finish fail safe
    q1 = input("What was the best or worst puzzle in the game and why?")
    q2 = input("How would you rate the overall experience 1 to 5?")
    q3 = input("Would you recommend it to a friend?")
    q4 = input("On a scale from  1 to 5, how engaging were the puzzles?")
    q5 = input("How were you feeling throughout the game? Select all that apply.")


label endingSurvey:
    #finish fail safe
    q1 = input("What was the best or worst puzzle in the game and why?")
    q2 = input("How would you rate the overall experience 1 to 5?")
    q3 = input("Would you recommend it to a friend?")
    q4 = input("On a scale from  1 to 5, how engaging were the puzzles?")
    q5 = input("How were you feeling throughout the game? Select all that apply.")


    call screen rightcompartment()
    pause
"""
label endingSurvey:
    #finish fail safe
    q1 = input("What was the best or worst puzzle in the game and why?")
    q2 = input("How would you rate the overall experience 1 to 5?")
    q3 = input("Would you recommend it to a friend?")
    q4 = input("On a scale from  1 to 5, how engaging were the puzzles?")
    q5 = input("How were you feeling throughout the game? Select all that apply.")
    






    # This ends the game.

    return
