style centered_style:
    xalign 0.1
    yalign 0.15
    spacing 10
    xsize 50
    ysize 200

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

    imagebutton auto "help-%s.png":
        focus_mask True
        action [Show("slider"), ShowMenu("p1_1menu")]
menu p1_1menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        v "Hello?"
        v "[name]?"
        v "We can solve this puzzle for you using our computers."
        $hintUsed = hintUsed + 1
        jump act1puzzle2

    "No":
        show screen p1_1Hint
        hide screen p1_1menu with fade 
screen p1_2Hint:
    imagebutton auto "help-%s.png":
        focus_mask True
        action [Show("pedestal3close"), ShowMenu("p1_2menu")]
menu p1_2menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        v "Hello?"
        v "[name]?"
        v "We can solve this puzzle for you."
        $hintUsed = hintUsed + 1
        jump act1puzzle3

    "No":
        show screen p1_2Hint
        hide screen p1_2menu with fade 

screen p1_3Hint:
    imagebutton auto "help-%s.png":
        focus_mask True
        action [Show("pedestal2close"), ShowMenu("p1_3menu")]
menu p1_3menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        v "Hello?"
        v "[name]?"
        v "We can solve this puzzle for you using our computers."
        $hintUsed = hintUsed + 1
        jump act1complete

    "No":
        show screen p1_3Hint
        hide screen p1_3menu with fade 
screen p2_1Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action [Notify("Match the torches to the images above."), SetVariable("hintUsed", hintUsed + 1)]

screen p2_2Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action [Notify("You could play the 4 keys to the melody."), SetVariable("hintUsed", hintUsed + 1)]

screen p2_3Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action[Notify("You could find this plant located near the plant used to give height."), SetVariable("hintUsed", hintUsed + 1)]

screen p3_1Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action [Notify("It seems like you’re having trouble figuring out what I am asking. What color did Yggdrasil turn after being touched by the outlander? And what color was the sky before it was cursed?") , SetVariable("hintUsed", hintUsed + 1)]

screen p3_2Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action [Notify("The middle of the village has a very large plant that was cursed many years ago."), SetVariable("hintUsed", hintUsed + 1)]

screen p3_3Hint:
    hbox:
        style "centered_style"
        textbutton "Hint" action [Notify("Put the handle on the tree symbol and press down on it."), SetVariable("hintUsed", hintUsed + 1)]


    #imagemap:
        #ground "testButtonImg.png"
        #hotspot(0, 0, 420, 283) action hintUsed++