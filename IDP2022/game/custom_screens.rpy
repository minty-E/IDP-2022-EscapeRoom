define endgamePage = 1
define towerPage = 1
define potionPage = 1
define blocksPage = 1
define clickPage = 1
screen clickInstructions():
    add "/Instructions/clickable{}.png".format(clickPage)
    button:
        xfill True
        yfill True 
        action [SetVariable("clickPage", If(clickPage == 2, true= 1, false= clickPage + 1)), Function(refresh), Play("sound", "audio/click.mp3")]
    imagebutton:
        idle "/UI/exitui.png"
        focus_mask True
        xpos 220
        ypos 27
        action [Hide("clickInstructions"), Play("sound", "audio/click.mp3"), Return()]
screen blocksInstructions():
    add "/Instructions/blocks{}.png".format(blocksPage)
    button:
        xfill True
        yfill True 
        action [SetVariable("blocksPage", If(blocksPage == 2, true= 1, false= blocksPage + 1)), Function(refresh), Play("sound", "audio/click.mp3")]
    imagebutton:
        idle "/UI/exitui.png"
        focus_mask True
        xpos 220
        ypos 27
        action [Hide("blocksInstructions"), Play("sound", "audio/click.mp3"), Return()]
screen potionInstructions:
    add "/Instructions/potion{}.png".format(potionPage)
    button:
        xfill True
        yfill True 
        action [SetVariable("potionPage", If(potionPage == 3, true= 1, false= potionPage + 1)), Function(refresh), Play("sound", "audio/click.mp3")]
    imagebutton:
        idle "/UI/exitui.png"
        focus_mask True
        xpos 220
        ypos 27
        action [Hide("potionInstructions"), Play("sound", "audio/click.mp3"), Return()]
screen towerInstructions:
    add "/Instructions/tower{}.png".format(towerPage)
    button:
        xfill True
        yfill True 
        action [SetVariable("towerPage", If(towerPage == 4, true= 1, false= towerPage + 1)), Function(refresh), Play("sound", "audio/click.mp3")]
    imagebutton:
        idle "/UI/exitui.png"
        focus_mask True
        xpos 220
        ypos 27
        action [Hide("towerInstructions"), Play("sound", "audio/click.mp3"), Return()]
screen endgameInstructions:
    add "/Instructions/endgame{}.png".format(endgamePage)
    button:
        xfill True
        yfill True 
        action [SetVariable("endgamePage", If(endgamePage == 5, true= 1, false= endgamePage + 1)), Function(refresh), Play("sound", "audio/click.mp3")]
    imagebutton:
        idle "/UI/exitui.png"
        focus_mask True
        xpos 220
        ypos 27
        action [Hide("endgameInstructions"), Play("sound", "audio/click.mp3"), Return()]
menu restartMenu:
    "Would you like to reset the potions?"

    "Yes":
        $takeoutpotions()
        $takeoutpotions()
        $takeoutpotions()
        $takeoutpotions()
        $takeoutpotions()
        $takeoutpotions()
        $takeoutpotions()
        $takeoutpotions()
        $takeoutpotions()
        $addToInventory(["note"])
        jump Potions
        hide screen restartMenu

    "No":
        hide screen restartMenu
        show screen UI
        call screen towerfloor1Potions
menu p1_1menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        $renpy.play("audio/static.mp3")
        $renpy.pause(delay=1, hard = True)
        company "Hello?"
        company "[name]?"
        company "We can solve this puzzle for you using our computers."
        $hintUsed = hintUsed + 1
        jump act1puzzle2

    "No":
        return
menu p1_2menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        $renpy.play("audio/static.mp3")
        $renpy.pause(delay=1, hard = True)
        company "Hello?"
        company "[name]?"
        company "We can solve this puzzle for you."
        $hintUsed = hintUsed + 1
        jump act1puzzle3

    "No":
        hide screen p1_2menu
        call screen pedestal3close


screen p1_3Hint:
    imagebutton auto "help-%s.png":
        focus_mask True
        action [Show("pedestal2close"), ShowMenu("p1_3menu")]
menu p1_3menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        $renpy.play("audio/static.mp3")
        $renpy.pause(delay=1, hard = True)
        company "Hello?"
        company "[name]?"
        company "We can solve this puzzle for you using our computers."
        $hintUsed = hintUsed + 1
        jump act1complete

    "No":
        show screen p1_3Hint
        hide screen p1_3menu
        call screen pedestal2close
screen p2_1int:
    imagebutton auto "help-%s.png":
        focus_mask True
        action [Show("torchpuzzle"), ShowMenu("p2_1menu")]
menu p2_1menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        $renpy.play("audio/static.mp3")
        $renpy.pause(delay=1, hard = True)
        company "Hello?"
        company "[name]?"
        company "The torch with the biggest flame points up. The torch with no flame points left. The flames get smaller when you go clockwise."
        $hintUsed = hintUsed + 1
        call screen torchpuzzle

    "No":
        hide screen p2_1menu
        call screen torchpuzzle

menu p2_2menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        $renpy.play("audio/static.mp3")
        $renpy.pause(delay=1, hard = True)
        company "Hello?"
        company "[name]?"
        company "They keys you need to play are _."
        $hintUsed = hintUsed + 1
        if atrightstatue == False:
            show screen UI
            call screen memorial

        else:
            show screen UI
            call screen rightstatueclose

    "No":
        hide screen p2_2menu with fade 
        if atrightstatue == False:
            show screen UI
            call screen memorial
        else:
            show screen UI
            call screen rightstatueclose

menu p2_3menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        $renpy.play("audio/static.mp3")
        $renpy.pause(delay=1, hard = True)
        company "Hello?"
        company "[name]?"
        company "The right plant is Huxtous. It's the spear shaped leaves plant that has alternating leaves."
        $hintUsed = hintUsed + 1
        show screen UI
        scene plantbox
        call screen plantboxclose


    "No":
        show screen UI
        call screen plantboxclose
menu p3_1menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        $renpy.play("audio/static.mp3")
        $renpy.pause(delay=1, hard = True)
        company "Hello?"
        company "[name]?"
        company "You have to make a light purple potion. Combine blue and red to make purple, then lighten it."
        $hintUsed = hintUsed + 1
        show screen UI
        scene towerfloor1
        call screen towerfloor1Potions


    "No":
        show screen UI
        call screen towerfloor1Potions
menu p3_2menu:
    "Would you like to request help from Odyssey7?. Having them help you will shorten the time that they have to get you."

    "Yes":
        scene bg blackScreen with fade
        $renpy.play("audio/static.mp3")
        $renpy.pause(delay=1, hard = True)
        company "Hello?"
        company "[name]?"
        company "You have to spell out the word tree by inserting the letters into the wall. Use the note in your inventory to translate the letters on the blocks."
        $hintUsed = hintUsed + 1
        show screen UI
        scene bg towerfloor2 
        call screen blocks


    "No":
        show screen UI
        call screen blocks
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