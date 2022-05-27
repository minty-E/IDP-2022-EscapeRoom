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

# screens for image/textbuttons for hints

screen p1_1Hint:

screen p1_2Hint: 

screen p1_3Hint:

screen p2_1Hint:

screen p2_2Hint:

screen p2_3Hint:

screen p3_1Hint:

screen p3_2Hint:

screen p3_3Hint:



    #imagemap:
        #ground "testButtonImg.png"
        #hotspot(0, 0, 420, 283) action hintUsed++