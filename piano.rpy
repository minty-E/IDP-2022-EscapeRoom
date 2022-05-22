# set up key variables for each key that needs to be pressed
# if the tune has 5 notes then there'll be key1 - key5
# only 1st and 2nd are clickable rn
# pretend like i imagemapped the 2nd key right

define e = Character("")
define key1 = 0
define key2 = 0
define key3 = 0
define key4 = 0

define keyspressed = 1
label start:
    call screen piano
    scene bg_piano
    screen piano():
        add "bg_piano.png"
        modal True
# make imagebutton in same format for each key if you want hover and idle state. the thing in "" depends on what you name each key.
        imagebutton auto "bg_piano_key1_%s":
            focus_mask True
            # this plays the sound and sets the key you pressed in the sequence to 1 (or whichever key you press
            # if i press key1 three times key1 = 1 key2 = 1 and key3 = 1.
            action [Play("sound", "audio/pianokey1.mp3"), SetVariable("key{}".format(keyspressed), 1), SetVariable("keyspressed", keyspressed + 1), Function(check)]
        imagebutton auto "bg_piano_key2_%s":
            focus_mask True
            # for this i just made them play the same sound but make sure to change
            xpos -62
            ypos -20
            action [Play("sound", "audio/pianokey1.mp3"), SetVariable("key{}".format(keyspressed), 2), SetVariable("keyspressed", keyspressed + 1), Function(check)]


init python:
    # function to check if it is the right sequence. change 4 to the number of keys you must press + 1.
    def check():
        global keyspressed
        if keyspressed == 4 :
            # change to the correct keys to press. ex: 1457 or smth
            if key1 == 1 and key2 == 2 and key3 == 2:
                #i kept getting an error if i didn't put interact = False so keep that in mind w/ dialogue
                renpy.say(e, "correct!", interact = False)
                keyspressed = 1
            else:
                # this resets the keys you pressed so you can try again
                renpy.say(e, "that wasn't right.. let me try again.", interact = False)
                keyspressed = 1
