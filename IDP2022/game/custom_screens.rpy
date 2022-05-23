style centered_style:
    xalign 0.5
    yalign 0.5
    spacing 10

screen testImgButton:
    hbox:
        style "centered_style"
        textbutton "Add time by clicking!": 
            action [SetVariable("hintUsed", hintUsed + 1)]
            
screen torchPuzzle:
    add "torch1.png"
    # etc
    modal True

    imagebutton auto "ralsei.png":
        focus_mask True
        action[SetVariable("")]



    #imagemap:
        #ground "testButtonImg.png"
        #hotspot(0, 0, 420, 283) action hintUsed++