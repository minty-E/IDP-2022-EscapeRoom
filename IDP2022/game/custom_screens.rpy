style centered_style:
    xalign 0.5
    yalign 0.5
    spacing 10

screen testImgButton:
    hbox:
        style "centered_style"
        textbutton "Add time by clicking!": 
            action [SetVariable("hintUsed", hintUsed + 1)]
# WORK ON TORCH PUZZLE
# https://www.reddit.com/r/RenPy/comments/sw540p/change_image_in_imagebutton_if_selected/
screen torchPuzzle:
    add "torch1.png"
    # etc
    modal True

    imagebutton auto "":
        focus_mask True
        action[]

# screens for image/textbuttons for hints`

screen p1_1Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("Shift the pieces to complete and solve the picture...")

screen p1_2Hint: 
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("You cannot place larger rings on smaller ones, try distributing the rings around first then stacking them in order.")


screen p1_3Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("Place pieces that fit together on the mirror in order for the light to reflect off of it.")

screen p2_1Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("Match the torches to the images above.")

screen p2_2Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("You could play the 4 keys to the melody.")

screen p2_3Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("You could find this plant located near the plant used to give height.")

screen p3_1Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("It seems like you’re having trouble figuring out what I am asking. What color did Yggdrasil turn after being touched by the outlander? And what color was the sky before it was cursed?")

screen p3_2Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("The middle of the village has a very large plant that was cursed many years ago.")

screen p3_3Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action Notify("Put the handle on the tree symbol and press down on it.")



    #imagemap:
        #ground "testButtonImg.png"
        #hotspot(0, 0, 420, 283) action hintUsed++