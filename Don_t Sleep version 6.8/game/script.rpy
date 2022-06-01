style text_timer_ok:
    size 72
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

style text_timer_near:
    size 72
    color "#F22"
    outlines [(2, "#000", 0, 0)]




init:
    python:
        import requests

        timer_jump = 0
        timer_range = 0
        time = 0
        minutes = 0
        seconds = 0
        final_minutes = 0
        final_seconds = 0
        def countdown(st, at, length=0.0):
            global time
            global minutes
            global seconds
            minutes = time // 60
            seconds = time % 60
            for i in range(10):
                if seconds == i:
                    seconds = str("0" + str(i))
            return Text(str(str(minutes) + ":" + str(seconds)), color="#fff", size=48), .1
        def time_finish(st, at, length=0.0):
            global time
            global minutes
            global seconds
            global final_minutes
            global final_seconds
            final_minutes = minutes
            final_seconds = seconds
            return Text(str(str(final_minutes) + ":" + str(final_seconds)), color="#fff", size=48), .1



screen leaderboard():
    vbox xalign 0.5 yalign 0.0:
        spacing 1000
        text _("{color=#fff}{size=35}[response.text]{/size}")



label leaderboard:
    $ response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vT_vnNvqA-Ru2qdQoqF8r5E0JEqmmdGQVxQYAOB83VnAtcJ7RXFcRuqhPV3lJ8SAvzAXlRfm7Pm_nGt/pub?gid=551328511&single=true&output=csv')
    show screen leaderboard
    'Click when you\'re done gawking at the leaderboard'
    return

screen countdown():
    timer 1 repeat True action If(time >= 0, true = SetVariable("time", time + 1), false = [Hide("countdown"), Jump(timer_jump)])
    imagebutton:
        xpos 50
        ypos 50
        idle DynamicDisplayable(countdown, length = 0)
        hover DynamicDisplayable(countdown, length = 0)
        action Null

screen time_finish():
    imagebutton:
        xpos 50
        ypos 50
        idle DynamicDisplayable(time_finish, length = 0)
        hover DynamicDisplayable(time_finish, length = 0)
        action Null

label timer_start:
    $ time = 0
    $ timer_range = 0
    $ timer_jump = "lose"
    show screen countdown
    jump prologue2





define n = Character("Mary",color="#00db96")
default preferences.text_cps = 40

#of the many variables used

#act 1
default milk = False
default cookie = False
default cheese = False
default musket = False
default cream = False
default marble = False
#act 2
default toot = False
default parrot = False
default cake = False
default wiffle = False
default burger = False
default pop = False
#act 3
default lily = False
default knox = False
default pan = False
default jim = False
default sugar = False
default drpepper = False


#act 1 puzzle stuff
default riddle1input = "Ronny"
default riddle1answer = "storage room"
default basketinput = "Luis"
default basketanswer = "basketball"
default dancinginput = "horambe"
default dancinganswer = "729"

#act 2 puzzle stuff
default alphainput = "poo"
default alphaanswer = "geometry"
default mathinput = "english"
default mathanswer = "grammar"
default cesarinput = "scatman"
default cesaranswer = "four hundred twenty six"

#act 3 puzzle stuff
default morseinput = "Genesis"
default morseanswer = "three eight six"
default cryptoinput = "ballllllllllllll"
default cryptoanswer = "the code is access"
default riddle2input = "morty"
default riddle2answer = "doormat"

image dance1 = "dance happy.png"
image dance2 = "dance mad.png"


#hopefully the end is here

label start:
    $ n = renpy.input("What is your name? (You'll still have a girl sprite)")
    "{color=#a39390}Hint choices may send you back a bit.(We also recommend that the sound volume is below the music volume.)"
    "{color=#a39390}Make sure to left click to not interrupt this experience and that you may have to click notes again."
    "{color=#a39390}Read carefully and enjoy! (skip if you're just really mean)"
    show screen Begin
    $ renpy.pause(hard=True)


label prologue1:
    play music "audio/Prologue.mp3" loop
    hide screen Begin
    jump timer_start

label prologue2:
    show screen Home
    show bg bleachers
    show dora mask at left:
        yalign 1.0
    n '{cps=5}What . . . . {/cps} happened?'
    '{color=#a39390}You wake up under the bleachers.'
    '{color=#a39390}The last thing you remember was the boy\'s volleyball team training and you inside of your sweaty costume.'
    n 'No way...'
    n 'Did I actually fall asleep in my costume??'
    '{color=#393930}You did.'
    n 'But still!'
    n 'They just left me here??'
    n 'Oh no...'
    n 'I\'ve gotta get out of here quick before I get in trouble at home!'
    n 'But first!'
    n 'I\'m a little tired...'
    n 'I should grab a fire escape map thingy and use it just in case in the gym.'
    show screen mapaction
    '{color=#a39390}You pick up a map off the wall.'
    n 'I\'ll put it back later.'
    n 'Wait...'
    n 'Now what?'
    '{sc=8}{cps=10}{color=#e04826}Think . . . {/cps} How can you escape?{/sc}'
    stop music fadeout 2.5

label Act1Part1:
    play music "audio/Act 1.mp3" loop
    show screen hintAct1
    n 'Well first I have to put my costume away in the {sc=3}storage room.{/sc} '
    '{color=#a39390}You get up and you see a small note.'
    '{color=#a39390}Who knows what may be on it.'
    n 'I wonder what this is?' #curious face
    '{color=#a39390} You start to go over to the note.'
    $ milk = True

label Puzzle1:
    play sound "audio/note.mp3"
    hide screen Puzzle1Note
    hide screen Puzzle2Note
    hide screen Puzzle3Note
    hide riddle happy onlayer screens
    show screen Puzzle1Note
    $ renpy.pause(hard=True)

label Act1Part2:
    hide screen Puzzle1Note
    hide screen Puzzle2Note
    hide screen Puzzle3Note
    hide bg bleachers
    show bg storagedoor
    $ cookie = True
    "{color=#a39390}You walk to the storage room door."
    show dora mask at left:
        yalign 1.0
    "{color=#a39390}You remember the riddle."
    n 'Seems it\'s already unlocked.'
    '{color=#a39390}You enter inside.'
    play sound "audio/door.mp3"
    hide bg storagedoor
    show screen Puzzle2Note
    show bg storageint
    n 'Alright time to put away the costume.'
    '{color=#a39390}After putting the costume away, you feel a sense of relief and are ready to move on.'
    "{color=#a39390}You then notice a note on the locker."
    show dora irritated at left:
        yalign 1.0
    n 'Another one, of course.'
    '{color=#a39390}You reach for it.'
    $ cheese = True

label Puzzle2:
    play sound "audio/note.mp3"
    hide screen Puzzle1Note
    hide screen Puzzle2Note
    hide screen Puzzle3Note
    hide uppy happy onlayer screens
    show screen Puzzle2Note
    $ renpy.pause(hard=True)

label Act1Part3:
    hide screen Puzzle1Note
    hide screen Puzzle2Note
    hide screen Puzzle3Note
    hide bg storageint
    show bg coachdoor
    show dora thinking at left:
        yalign 1.0
    $ musket = True
    n "Obviously this one is locked too."
    n "But now that I\'ve solved 2 of these..."
    n 'It seems the answers for these puzzles are the hints or codes needed to progress and finally get the heck out of here.'
    "{color=#a39390}You\'re catching on..."
    "{color=#a39390}You type in the word from the last puzzle and get inside."
    play sound "audio/door.mp3"
    hide bg coachdoor
    show bg coachpl
    show screen coffee
    show dora normal at left:
        yalign 1.0
    n 'Hmmm...'
    n 'Should I be in here?'
    n 'Wait there\'s a note on the table.'
    hide dora normal at left
    hide screen coffee
    show desk happy onlayer screens
    n 'Guess I\'ll be heading over there.'
    show dora normal at left:
        yalign 1.0
    hide desk happy onlayer screens
    show bg coachpl
    "{color=#a39390}You see 2 papers stacked on top of each other at the desk."
    n "Those must be from the janitor!"
    '{color=#a39390}You go to pick them up and read them.'
    $ cream = True

label Puzzle3:
    play sound "audio/note.mp3"
    hide screen Puzzle1Note
    hide screen Puzzle2Note
    hide screen Puzzle3Note
    hide dance happy onlayer screens
    hide dance mad onlayer screens
    show screen Puzzle3Note
    $ renpy.pause(hard=True)

label Act1Part4:
    hide screen Puzzle1Note
    hide screen Puzzle2Note
    hide screen Puzzle3Note
    show dora normal at left:
        yalign 1.0
    hide bg coachpl
    show bg stairs
    $ marble = True
    n 'I\'m guessing the previous answer is the code here.'
    hide dora normal
    "{color=#a39390}You put the map back on the wall from before and then head downstairs and now you\'re out of the gym area."
    "{color=#a39390}You type in your answer and the door opens."
    stop music fadeout 2.5
    hide screen hintAct1
    show screen hintAct2
    hide screen mapaction
    $ act1_time = time
    $ act1_minutes = minutes
    $ act1_seconds = seconds
    $ act1_time_string = str(str(act1_minutes) + ":" + str(act1_seconds))
    jump Act2Part1

    
#
#
#Act 2
#
#
label Act2Part1:
    play music "audio/Act 2.mp3" loop
    show bg hall
    show screen hintAct2
    show dora thinking at left:
        yalign 1.0
    n 'Finally here...'
    n 'Nothing seems too different though.'
    '{color=#a39390}You stroll around and end up by the math door.'
    hide bg hall
    show bg mathdoor
    show screen Puzzle4Note
    show dora normal at left onlayer screens:
        yalign 1.0
    n 'Alright this seems to clearly be my next objective.'
    '{color=#a39390}There\'s a note pinned to the wall.'
    n 'What does he have in store for me this time.' #curious face
    '{color=#a39390} You go to note to read it closely.'
    $ toot = True

label Puzzle4:
    play sound "audio/note.mp3"
    hide screen Puzzle4Note
    hide screen Puzzle5Note
    hide screen Puzzle6Note
    hide math angry onlayer screens
    show screen Puzzle4Note
    $ renpy.pause(hard=True)

label Act2Part2:
    hide screen Puzzle4Note
    hide screen Puzzle5Note
    hide screen Puzzle6Note
    show bg mathdoor
    $ parrot = True
    show dora angry at left onlayer screens:
        yalign 1.0
    n 'Of course the answer was math related.'
    "{color=#a39390}You puff out angrily."
    n 'At least I have the darn code now.'
    '{color=#a39390}You enter the code into the door and head inside.'
    n 'Oh boy...'
    play sound "audio/door.mp3"
    hide bg mathdoor
    show bg mathclass
    n 'I hate this so much.'
    '{color=#a39390}You look around and remember that you have a test on sine and cosine soon.'
    n 'Oh right...'
    n 'Yeah I\'m positive that I\'m gonna fail that test'
    "{color=#a39390}You notice the paper on the whiteboard and a chill runs down your back."
    n 'Please don\'t tell me that\'s a new worksheet for homework...'
    '{color=#a39390}It isn\'t.'
    n 'I don\'t wanna look at it.'
    n 'It\'s definitely gonna be like 30 problems!'
    '{color=#a39390}After gathering the courage, you head over to get a better look.'
    $ cake = True

label Puzzle5:
    play sound "audio/note.mp3"
    hide screen Puzzle4Note
    hide screen Puzzle5Note
    hide screen Puzzle6Note
    hide math happy onlayer screens
    show screen Puzzle5Note
    $ renpy.pause(hard=True)

label Act2Part3:
    hide screen Puzzle4Note
    hide screen Puzzle5Note
    hide screen Puzzle6Note
    hide bg mathclass
    show bg hall
    show dora thinking at left onlayer screens:
        yalign 1.0
    $ wiffle = True
    n "I wonder which class will need the word \"grammar\"..."
    "{color=#a39390}It suddenly occured to you that the word is language related."
    n 'I have no idea how that didn\'t occur to me before.'
    "{color=#a39390}You start to head over to English class."
    hide bg hall
    show bg engdoor
    n 'Time to get to the next puzzle already.'
    '{color=#a39390}You enter the code and enter the English classroom.'
    play sound "audio/door.mp3"
    hide bg engdoor
    show bg engclass
    show dora irritated at left onlayer screens:
        yalign 1.0
    n 'Oh right I have to read for 20 minutes when I get home today.'
    '{color=#a39390}You look around and see the note left on the cabinet.'
    n 'That must be the note that the janitor left?'
    "{color=#a39390}You head over to the note to pick it up."
    $ burger = True

label Puzzle6:
    play sound "audio/note.mp3"
    hide screen Puzzle4Note
    hide screen Puzzle5Note
    hide screen Puzzle6Note
    hide cipher happy onlayer screens
    show screen Puzzle6Note
    $ renpy.pause(hard=True)

label Act2Part4:
    hide screen Puzzle4Note
    hide screen Puzzle5Note
    hide screen Puzzle6Note
    hide bg engclass
    show bg stairs
    $ pop = True
    show dora normal at left onlayer screens:
        yalign 1.0
    n 'After putting in the code, I\'ll be on the 1st floor and almost out of here.'
    play sound "audio/door.mp3"
    hide dora normal
    "{color=#a39390}You type in the code and the door opens."
    "{color=#a39390}You head downstairs and now you\'re lower-grade classes area."
    stop music fadeout 2.5
    hide screen hintAct2
    show screen hintAct3
    $ act2_time = float(time) - float(act1_time)
    $ act2_minutes = float(minutes) - float(act1_minutes)
    $ act2_seconds = float(seconds) - float(act1_seconds)
    $ act2_time_string = str(str(act2_minutes) + ":" + str(act2_seconds))
    jump Act3Part1


#
#
#
#
# Act 3


label Act3Part1:
    play music "audio/Act 3.mp3" loop
    show bg hall
    show screen hintAct3
    show dora irritated at left onlayer screens:
        yalign 1.0
    n 'Where now...?'
    n 'The janitor didn\'t leave any more info.'
    '{color=#a39390}You look around the senior classrooms but find nothing.'
    n 'Maybe the office!'
    n 'It makes sense to go their since I think that\'s right by the front door.'
    hide dora irritated
    '{color=#a39390}You walk over to the office door.'
    hide bg hall
    show bg officedoor
    show dora normal at left onlayer screens:
        yalign 1.0
    n 'Yeah this is definitely the right place.'
    '{color=#a39390}You see the symbols and the note on the door.'
    n 'What\'s with all the dots and dashes?' #curious face
    '{color=#a39390} You go up to the note to read it closely.'
    $ lily = True

label Puzzle7:
    play sound "audio/note.mp3"
    hide screen Puzzle7Note
    hide screen Puzzle8Note
    hide screen Puzzle9Note
    hide morse angry onlayer screens
    show screen Puzzle7Note
    $ renpy.pause(hard=True)

label Act3Part2:
    hide screen Puzzle7Note
    hide screen Puzzle8Note
    hide screen Puzzle9Note
    show bg officedoor
    $ knox = True
    show dora normal at left onlayer screens:
        yalign 1.0
    n 'Well now that that\'s done...'
    "{color=#a39390}You take a slow breath and you feel confident."
    n 'I\'ll be close to getting out of here!'
    '{color=#a39390}You enter the code into the door and walk inside.'
    play sound "audio/door.mp3"
    hide bg officedoor
    show bg office
    show dora thinking at left onlayer screens:
        yalign 1.0
    n 'Hmmmm....'
    '{color=#a39390}You look around and wonder what\'s your next move.'
    n 'Where do I go now?'
    '{color=#a39390}You see a note on the shelf.'
    n 'I wish the janitor put something cool or whatever..'
    n 'Right now it just sounds like he\'s ordering me around.'
    n 'I\'ll show him tomorrow...'
    '{color=#a39390}You walk up to the shelf to pick up the note.'
    $ pan = True

label Puzzle8:
    play sound "audio/note.mp3"
    hide screen Puzzle7Note
    hide screen Puzzle8Note
    hide screen Puzzle9Note
    hide pigeon happy onlayer screens
    hide bg comp
    show bg office 
    show screen Puzzle8Note
    $ renpy.pause(hard=True)

label Act3Part3:
    hide screen Puzzle7Note
    hide screen Puzzle8Note
    hide screen Puzzle9Note
    show bg office
    show dora normal at right onlayer screens:
        yalign 1.0
    $ jim = True
    n "Well now I should be able to open the drawer with the code."
    "{color=#a39390}You head over to the drawer and put in the code to unlock it."
    hide bg office
    show bg drawer
    n 'Seems that this may be my last puzzle...'
    "{color=#a39390}You feel determined and ready for your final challenge..."
    "{color=#a39390}You pick up the note."
    $ sugar = True

label Puzzle9:
    play sound "audio/note.mp3"
    hide screen Puzzle7Note
    hide screen Puzzle8Note
    hide screen Puzzle9Note
    hide riddle happy onlayer screens
    show screen Puzzle9Note
    $ renpy.pause(hard=True)

label Act3Part4:
    hide screen Puzzle7Note
    hide screen Puzzle8Note
    hide screen Puzzle9Note
    hide bg drawer
    show bg office
    show dora normal at right onlayer screens:
        yalign 1.0
    $ drpepper = True
    play sound "audio/note.mp3"
    show screen Doormat
    $ renpy.pause(hard=True)
    #art must be done
    stop music fadeout 2.5





#remember the renpy.pause is super duper mega useful for the hint and button features


label aa1:
    hide dora mask
    hide screen Puzzle1Note
    play sound "audio/pap.mp3"
    show riddle happy at center onlayer screens:
        xalign 0.5
        yalign 0.3
    #onlayer is essential
    $ puzzle_trigger1 = True
    "{color=#a39390}(Word Solution)"
    n 'Oh I think I know who did this...'
    '{color=#a39390}You certainly had the right idea.'
    n 'That darn janitor...'
    '{color=#a39390}You got to know him over the last few months so you already knew about his puzzle scheming.'
    '{color=#a39390}It seems he saw you sleeping and immediately knew what to do.'
    n 'Let\'s just get this over with.'

label aa2:
    $ riddle1input = renpy.input("I am unlocked just for this occasion. So you can put your costume away before its vacation. What am I?")
    $ riddle1input = riddle1input.lower()
    $ riddle1input = riddle1input.strip()
    if riddle1input == riddle1answer:
        $ puzzle_trigger1end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}Makes sense."
        n 'Guess I\'ll head to the storage room then.'
        hide riddle happy onlayer screens
        jump Act1Part2
    else:
        "{color=#a39390}That doesn't seem to be it."
        n 'Darn.'
        n 'I\'ll get it this time.'
        jump aa2
        return

label ab1:
    hide dora irritated
    hide screen Puzzle2Note
    play sound "audio/pap.mp3"
    show uppy happy at center onlayer screens:
        xalign 0.5
        yalign 0.3
    #onlayer is essential
    $ puzzle_trigger2 = True
    "{color=#a39390}(Word Solution)"
    n 'This note has been making me a little suspicious...'
    n 'Why do these words look so horrible?'
    '{color=#a39390}It\'s not their handwriting.'
    n 'Wait a minute!'
    n 'The letters are upside down!'
    n 'I think that one word is reversed too...'
    n 'Are they all like this...?'

label ab2:
    $ basketinput = renpy.input("What is the coach's favorite sport?")
    $ basketinput = basketinput.lower()
    $ basketinput = basketinput.strip()
    if basketinput == basketanswer:
        $ puzzle_trigger2end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}Seems to be correct."
        n 'Seems the coach may be involved so maybe I should check out his place.'
        hide uppy happy onlayer screens
        jump Act1Part3
    else:
        "{color=#a39390}Not quite."
        n 'Maybe I read it wrong...'
        jump ab2
        return

label ac1:
    hide dora normal
    hide screen Puzzle3Note
    play sound "audio/pap.mp3"
    show dance1 at right onlayer screens:
        yalign 0.4
    show dance2 at left onlayer screens:
        yalign 0.4
    #onlayer is essential
    $ puzzle_trigger3 = True
    "{color=#a39390}(Number Solution)"
    n 'Hey these guys look goofy.'
    n 'Though they seem to be another cipher to solve and get a code.'

label ac2:
    $ dancinginput = renpy.input("What do the dancers say?")
    $ dancinginput = dancinginput.strip()
    if dancinginput == dancinganswer:
        $ puzzle_trigger3end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}The dancers agree!"
        n 'Maybe these will help get to the lower floor since there\'s nowhere else to go.'
        hide dance1 onlayer screens
        hide dance2 onlayer screens
        jump Act1Part4
    else:
        "{color=#a39390}The dancers say otherwise."
        n 'I need to figure out what these groovy moves mean.'
        jump ac2
        return

label ae1:
    hide dora normal onlayer screens
    hide screen Puzzle4Note
    play sound "audio/pap.mp3"
    show math angry at center onlayer screens
    #onlayer is essential
    $ puzzle_trigger4 = True
    "{color=#a39390}(Word Solution)"
    n '...'
    n "He didn\'t actually give me a math problem...right?"
    "{color=#a39390}He did."
    n 'Alright now I really hate this.'

label ae2:
    $ alphainput = renpy.input("What does the cypher spell out?")
    $ alphainput = alphainput.lower()
    $ alphainput = alphainput.strip()
    if alphainput == alphaanswer:
        $ puzzle_trigger4end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}Good thing you know your abc\'s. Congrats."
        hide math angry at center onlayer screens
        jump Act2Part2
    else:
        "{color=#a39390}Seems you don\'t study."
        n 'I hate math.'
        return
        jump ae2


label af1:
    hide dora angry onlayer screens
    hide screen Puzzle5Note
    play sound "audio/pap.mp3"
    show math happy at center onlayer screens:
        yalign 0.4
    #onlayer is essential
    $ puzzle_trigger5 = True
    "{color=#a39390}(Hope you brought a pen and paper)"
    n 'Why...'
    n 'They\'re pretty easy but still...'
    n 'Why?'
    n 'Guess I\'ll solve them and get this done as fast as possible.'

label af2:
    $ mathinput = renpy.input("What do the problems spell out?")
    $ mathinput = mathinput.lower()
    $ mathinput = mathinput.strip()
    if mathinput == mathanswer:
        $ puzzle_trigger5end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}Your teacher would be proud!"
        n 'FINALLY!!!!'
        n 'This should be my next key word so maybe another class needs it.'
        hide math happy at center onlayer screens
        jump Act2Part3
    else:
        "{color=#a39390}Your little brother could get this done faster..."
        n 'My head hurts.'
        jump af2
        return

label ag1:
    hide dora irritated onlayer screens
    hide screen Puzzle6Note
    play sound "audio/pap.mp3"
    show cipher happy at center onlayer screens:
        yalign 0.3
    #onlayer is essential
    $ puzzle_trigger6 = True
    "{color=#a39390}(Word Solution with no line) Answer Ex: six hundred seventy four"
    n 'This looks way too complicated...'
    n 'What does all this mean??'
    '{color=#a39390}Looks like you\'ll need some time to figure this all out.'

label ag2:
    $ cesarinput = renpy.input("What number does the cipher say?")
    $ cesarinput = cesarinput.lower()
    $ cesarinput = cesarinput.strip()
    if cesarinput == cesaranswer:
        $ puzzle_trigger6end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}You did it!!"
        n 'I think I lost some brain cells...'
        n 'Anyways, time to head to the next floor!'
        hide cipher happy at center onlayer screens
        jump Act2Part4
    else:
        "{color=#a39390}To be honest, I don't even know it."
        n 'What hurts is that this isn\'t even the last one.'
        jump ag2
        return

label ah1:
    hide dora normal onlayer screens
    hide screen Puzzle7Note
    play sound "audio/pap.mp3"
    show morse angry at right onlayer screens:
        yalign 0.5
    #onlayer is essential
    $ puzzle_trigger7 = True
    "{color=#a39390}(Word Solution)"
    n 'Morse code...?'
    '{color=#a39390}You\'ve never heard of it.'
    n 'Might as well learn a bit about a new writing system I guess...'

label ah2:
    $ morseinput = renpy.input(" What number does \"- .... .-. . . / . .. --. .... - / ... .. -..-\" say? (no slashes, just spaces)")
    $ morseinput = morseinput.lower()
    $ morseinput = morseinput.strip()
    if morseinput == morseanswer:
        $ puzzle_trigger7end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}It seems you cracked it!"
        n 'That wasn\'t so hard!'
        hide morse angry at right onlayer screens
        jump Act3Part2
    else:
        "{color=#a39390}Don't beat yourself up about it."
        "{color=#a39390}It\'s a new language after all."
        n 'Guess I\'ll try it again.'
        jump ah2
        return

label ai1:
    hide dora thinking onlayer screens
    hide screen Puzzle8Note
    play sound "audio/pap.mp3"
    show pigeon happy at center onlayer screens:
        yalign 0.4
    #onlayer is essential
    $ puzzle_trigger8 = True
    "{color=#a39390}(Word Solution)"
    n 'Another weird thing I have to solve.'
    "{color=#a39390}It\'s been a big day for learning new things."
    n 'Where does the janitor even get this stuff??'
    n 'Whatever, guess I should head over to the computer.'
    hide bg office
    show bg comp
    hide pigeon happy at center onlayer screens
    show pigeon happy at center onlayer screens:
        xalign 0.86
        yalign 0.4
    n 'Hopefully this doesn\'t take too long to solve...'

label ai2:
    $ cryptoinput = renpy.input("What does the message say?? (Use spaces.)")
    $ cryptoinput = cryptoinput.lower()
    $ cryptoinput = cryptoinput.strip()
    if cryptoinput == cryptoanswer:
        $ puzzle_trigger8end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}You did it you super genius!"
        n 'Such a weird writing system to use.'
        hide pigeon happy at center onlayer screens
        jump Act3Part3
    else:
        "{color=#a39390}Don\'t worry!"
        "{color=#a39390}It\'s just blocks!"
        n 'Maybe I\'ll get it this time.'
        jump ai2
        return

label aj1:
    hide dora normal at left onlayer screens
    hide screen Puzzle9Note
    play sound "audio/pap.mp3"
    show riddle angry at center onlayer screens:
        xalign 0.5
        yalign 0.35
    #onlayer is essential
    $ puzzle_trigger9 = True
    "{color=#a39390}(Word Solution)"
    n 'A riddle...'
    n 'Just like how it all started.'
    '{color=#a39390}It seems that this will let you find the key and get out of here.'
    n 'Let\'s do this!'

label aj2:
    $ riddle2input = renpy.input("Part of me rhymes with cat, I\'m useful at the door, and I\'ll always greet you. What am I? (one word)")
    $ riddle2input = riddle2input.lower()
    $ riddle2input = riddle2input.strip()
    if riddle2input == riddle2answer:
        $ puzzle_trigger9end = True
        play sound "audio/cool.mp3"
        "{color=#a39390}Yeah that seems right!!!"
        n 'Now it\'s time to check under the doormat!'
        hide riddle angry at center onlayer screens
        jump Act3Part4
    else:
        "{color=#a39390}I don\'t know if that welcomes me at my door..."
        n 'Let me try again.'
        jump aj2
        return


label keystuff:
    hide screen Doormat
    hide screen hintAct3
    show key happy:
        yalign 0.4
        xalign 0.5
    stop music fadeout 0.5
    play music "audio/Key.mp3" loop
    n 'I finally have the key!'
    n 'Once I use this, it\'ll all be over.'
    n 'I can go home...'
    play sound "audio/door.mp3"
    '{color=#a39390}You insert the key, turn it, and take a step towards freedom.'
    hide key happy
    $ final_time = time
    $ act3_time = float(time) - float(act2_time)
    $ act3_minutes = float(minutes) - float(act2_minutes)
    $ act3_seconds = float(seconds) - float(act2_seconds)
    $ act3_time_string = str(str(act3_minutes) + ":" + str(act3_seconds))
    jump win

label win:
    stop music fadeout 1.0
    $ final_seconds = seconds
    $ final_minutes = minutes
    hide screen countdown
    hide screen Home
    play music "audio/Win.mp3" loop
    hide bg office
    show bg grass
    show dora irritated at left onlayer screens:
        yalign 1.0
    n 'I\'m finally out of here!'
    n 'Oh I can\'t wait to get home!'
    '{color=#a39390}Maybe find a bus first.'
    n 'TIme to head out!'
    "{color=#a39390}You head to bus stop and eventually make it home."
    '{color=#a39390}You head inside your room.'
    show bg room
    n 'Finally back in my own room!!'
    '{color=#a39390}You hop onto your bed and rest.'
    n 'Sleep......'
    hide dora irritated onlayer screens
    show bg thanks
    'Click to end.'
    show bg win
    '{color=#a39390}The End!'
    'Click for leaderboard. (wait a bit)'
    show bg blank
    jump api_madness
    return

    #The end
label api_madness:
    python:
        FinalTime = str(str(final_minutes) + ":" + str(final_seconds))
        Finaltimeseconds = (int(final_minutes) * 60) + int(final_seconds)
        URL = "https://script.google.com/macros/s/AKfycbxxnPeUzP8zfMGhZoxGp7F7zYes3UbLvC2VnAJBfTs6K4APE9k/exec"
        requests.post(URL, json={ 'time' : FinalTime, 'name' : n, 'Act 1' : act1_time_string,'Act 2' : act2_time, 'Act 3' : act3_time_string, 'final time seconds' : Finaltimeseconds,}, timeout=2.5)
    jump leaderboard
    return




label lose:
    stop music fadeout 1.0
    hide screen Home
    play music "audio/Lose.mp3" loop
    show bg lose
    '{color=#a39390}You took too long and now you\'re gonna get it.'
    'no more playtime for you'
    $ renpy.quit()
    return

label returnhome:
    'Would you like to go back to the main menu? (Click to continue)'
    menu:
        "Ye":
            return
        "Nah (This may send you back)":
            'Alrighty then.'
            if milk == False:
                jump Act1Part1
            elif cookie == False: 
                jump Puzzle1 
            elif cheese == False:
                jump Act1Part2
            elif musket == False:
                jump Puzzle2
            elif cream == False:
                jump Act1Part3
            elif marble == False:
                jump Puzzle3
            else:
                jump Act1Part4
                
            if toot == False:
                jump Act2Part1
            elif parrot == False: 
                jump Puzzle4 
            elif cake == False:
                jump Act2Part2
            elif wiffle == False:
                jump Puzzle5
            elif burger == False:
                jump Act2Part3
            elif pop == False:
                jump Puzzle6
            else:
                jump Act2Part4

            if lily == False:
                jump Act3Part1
            elif knox == False: 
                jump Puzzle7
            elif pan == False:
                jump Act3Part2
            elif jim == False:
                jump Puzzle8
            elif sugar == False:
                jump Act3Part3
            elif drpepper == False:
                jump Puzzle9
            else:
                jump Act3Part4

label mappy:
    show mappa happy onlayer screens:
        yalign 0.4
        xalign 0.5
    'Click to go back to the game. (This may send you back a bit.)'
    hide mappa happy onlayer screens
    if milk == False:
        jump Act1Part1
    elif cookie == False: 
        jump Puzzle1 
    elif cheese == False:
        jump Act1Part2
    elif musket == False:
        jump Puzzle2
    elif cream == False:
        jump Act1Part3
    elif marble == False:
        jump Puzzle3
    else:
        jump Act1Part4




#hint system
label pp:
    hide marco ez
    hide riddle happy onlayer screens
    hide uppy happy onlayer screens
    hide dance1 onlayer screens
    hide dance2 onlayer screens
    "Do you want a hint? (Click to continue when given a prompt and remember the penalty is 1 minute.)"
    menu:
        "No (This may send you back a bit)":
            if milk == False:
                jump Act1Part1
            elif cookie == False: 
                jump Puzzle1 
            elif cheese == False:
                jump Act1Part2
            elif musket == False:
                jump Puzzle2
            elif cream == False:
                jump Act1Part3
            elif marble == False:
                jump Puzzle3
            else:
                jump Act1Part4

        "Yes":
            if milk == False:
                "Reach the first puzzle first."
                jump Act1Part1
            else:
                "Do you want a hint for the first puzzle in the gym area?"
                menu:
                    "Yes":
                        $ time += 60
                        "The very room you need to be at."

                        if milk == False:
                            jump Act1Part1
                        elif cookie == False: 
                            jump Puzzle1 
                        elif cheese == False:
                            jump Act1Part2
                        elif musket == False:
                            jump Puzzle2
                        elif cream == False:
                            jump Act1Part3
                        elif marble == False:
                            jump Puzzle3
                        else:
                            jump Act1Part4
                        
                    "No (This may send you back a bit)":
                        if cheese == False:
                            "You either need to get to the second puzzle or don't ask for a hint if you don't need one."
                            if milk == False:
                                jump Act1Part1
                            elif cookie == False: 
                                jump Puzzle1 
                            elif cheese == False:
                                jump Act1Part2
                            elif musket == False:
                                jump Puzzle2
                            elif cream == False:
                                jump Act1Part3
                            elif marble == False:
                                jump Puzzle3
                            else:
                                jump Act1Part4
                        else: 
                            "Do you want a hint for the second puzzle in the gym area?"
                            menu:
                                "Yep":
                                    $ time += 60
                                    "A sport where you shoot a ball into a tall net."
                                   
                                    if milk == False:
                                        jump Act1Part1
                                    elif cookie == False: 
                                        jump Puzzle1 
                                    elif cheese == False:
                                        jump Act1Part2
                                    elif musket == False:
                                        jump Puzzle2
                                    elif cream == False:
                                        jump Act1Part3
                                    elif marble == False:
                                        jump Puzzle3
                                    else:
                                        jump Act1Part4

                                "No (This may send you back a bit)":
                                    if cream == False:
                                        "You either need to get to the third puzzle or don't ask for a hint if you don't need one."
                                    if milk == False:
                                        jump Act1Part1
                                    elif cookie == False: 
                                        jump Puzzle1 
                                    elif cheese == False:
                                        jump Act1Part2
                                    elif musket == False:
                                        jump Puzzle2
                                    elif cream == False:
                                        jump Act1Part3
                                    elif marble == False:
                                        jump Puzzle3
                                    elif marble:
                                        jump Act1Part4
                                    else: 
                                        "Do you want a hint for the third puzzle in the gym area?"
                                        menu:
                                            "Yep":
                                                $ time += 180
                                                "Kinda sad that you need this but here \"*29\"."
                                                
                                                if milk == False:
                                                    jump Act1Part1
                                                elif cookie == False: 
                                                    jump Puzzle1 
                                                elif cheese == False:
                                                    jump Act1Part2
                                                elif musket == False:
                                                    jump Puzzle2
                                                elif cream == False:
                                                    jump Act1Part3
                                                elif marble == False:
                                                    jump Puzzle3
                                                else:
                                                    jump Act1Part4
                                            "No (This may send you back a bit)":
                                                "Then why are you all the way here?"
                                                if milk == False:
                                                    jump Act1Part1
                                                elif cookie == False: 
                                                    jump Puzzle1 
                                                elif cheese == False:
                                                    jump Act1Part2
                                                elif musket == False:
                                                    jump Puzzle2
                                                elif cream == False:
                                                    jump Act1Part3
                                                elif marble == False:
                                                    jump Puzzle3
                                                else:
                                                    jump Act1Part4
                                    


#
#
#
#hint system 2
label ps:
    hide marco ez
    "Do you want a hint? (Click to continue when given a prompt and remember the penalty is 1 minute.)"
    menu:
        "No (This may send you back a bit)":
            if toot == False:
                jump Act2Part1
            elif parrot == False: 
                jump Puzzle4 
            elif cake == False:
                jump Act2Part2
            elif wiffle == False:
                jump Puzzle5
            elif burger == False:
                jump Act2Part3
            elif pop == False:
                jump Puzzle6
            else:
                jump Act2Part4

        "Yes":
            if toot == False:
                "Reach the first puzzle first."
                jump Act2Part1
            else:
                "Do you want a hint for the first puzzle in the hall?"
                menu:
                    "Yes":
                        $ time += 60
                        "The math class that students take after algebra 1."
                        
                        if toot == False:
                            jump Act2Part1
                        elif parrot == False: 
                            jump Puzzle4
                        elif cake == False:
                            jump Act2Part2
                        elif wiffle == False:
                            jump Puzzle5
                        elif burger == False:
                            jump Act2Part3
                        elif pop == False:
                            jump Puzzle6
                        else:
                            jump Act2Part4
                        
                    "No (This may send you back a bit)":
                        if parrot == False:
                            "You either need to get to the second puzzle or don't ask for a hint if you don't need one."
                            if toot == False:
                                jump Act2Part1
                            elif parrot == False: 
                                jump Puzzle4
                            elif cake == False:
                                jump Act2Part2
                            elif wiffle == False:
                                jump Puzzle5
                            elif burger == False:
                                jump Act2Part3
                            elif pop == False:
                                jump Puzzle6
                            else:
                                jump Act2Part4
                        else: 
                            "Do you want a hint for the second puzzle in the Math classroom?"
                            menu:
                                "Yep":
                                    $ time += 60
                                    "A very important skill your English teacher wants you to be good at."

                                    if toot == False:
                                        jump Act2Part1
                                    elif parrot == False: 
                                        jump Puzzle4
                                    elif cake == False:
                                        jump Act2Part2
                                    elif wiffle == False:
                                        jump Puzzle5
                                    elif burger == False:
                                        jump Act2Part3
                                    elif pop == False:
                                        jump Puzzle6
                                    else:
                                        jump Act2Part4

                                "No (This may send you back a bit)":
                                    if burger == False:
                                        "You either need to get to the third puzzle or don't ask for a hint if you don't need one."
                                        if toot == False:
                                            jump Act2Part1
                                        elif parrot == False: 
                                            jump Puzzle4 
                                        elif cake == False:
                                            jump Act2Part2
                                        elif wiffle == False:
                                            jump Puzzle5
                                        elif burger == False:
                                            jump Act2Part3
                                        elif pop == False:
                                            jump Puzzle6
                                        elif pop:
                                            jump Act2Part4
                                    else: 
                                        "Do you want a hint for the third puzzle in the English classroom?"
                                        menu:
                                            "Yep":
                                                $ time += 60
                                                "Each letter is shifted 7 times backwards. For example H decoded is A."
                                                
                                                if toot == False:
                                                    jump Act2Part1
                                                elif parrot == False: 
                                                    jump Puzzle4 
                                                elif cake == False:
                                                    jump Act2Part2
                                                elif wiffle == False:
                                                    jump Puzzle5
                                                elif burger == False:
                                                    jump Act2Part3
                                                elif pop == False:
                                                    jump Puzzle6
                                                else:
                                                    jump Act2Part4
                                            "No (This may send you back a bit)":
                                                "Then why are you all the way here?"
                                                if toot == False:
                                                    jump Act2Part1
                                                elif parrot == False: 
                                                    jump Puzzle4
                                                elif cake == False:
                                                    jump Act2Part2
                                                elif wiffle == False:
                                                    jump Puzzle5
                                                elif burger == False:
                                                    jump Act2Part3
                                                elif pop == False:
                                                    jump Puzzle6
                                                else:
                                                    jump Act2Part4


#
#
#
#
#
#
# Act 3
label pz:
    hide marco ez
    "Do you want a hint? (Click to continue when given a prompt and remember the penalty is 1 minute.)"
    menu:
        "No (This may send you back a bit)":
            if lily == False:
                jump Act3Part1
            elif knox == False: 
                jump Puzzle7
            elif pan == False:
                jump Act3Part2
            elif jim == False:
                jump Puzzle8
            elif sugar == False:
                jump Act3Part3
            elif drpepper == False:
                jump Puzzle9
            else:
                jump Act3Part4

        "Yes":
            if lily == False:
                "Reach the first puzzle first."
                jump Act3Part1
            else:
                "Do you want a hint for the first puzzle in the hall?"                
                menu:
                    "Yes":
                        $ time += 60
                        "The middle word of the morse code is \"eight\"."
                        
                        if lily == False:
                            jump Act3Part1
                        elif knox == False: 
                            jump Puzzle7
                        elif pan == False:
                            jump Act3Part2
                        elif jim == False:
                            jump Puzzle8
                        elif sugar == False:
                            jump Act3Part3
                        elif drpepper == False:
                            jump Puzzle9
                        else:
                            jump Act3Part4
                        
                    "No (This may send you back a bit)":
                        if pan == False:
                            "You either need to get to the second puzzle or don't ask for a hint if you don't need one."
                            if lily == False:
                                jump Act3Part1
                            elif knox == False: 
                                jump Puzzle7
                            elif pan == False:
                                jump Act3Part2
                            elif jim == False:
                                jump Puzzle8
                            elif sugar == False:
                                jump Act3Part3
                            elif drpepper == False:
                                jump Puzzle9
                            else:
                                jump Act3Part4
                        else: 
                            "Do you want a hint for the second puzzle which is in the office?"
                            menu:
                                "Yep":
                                    $ time += 60
                                    "The second word of the cryptograph is \"code\"."
                                   
                                    if lily == False:
                                        jump Act3Part1
                                    elif knox == False: 
                                        jump Puzzle7
                                    elif pan == False:
                                        jump Act3Part2
                                    elif jim == False:
                                        jump Puzzle8
                                    elif sugar == False:
                                        jump Act3Part3
                                    elif drpepper == False:
                                        jump Puzzle9
                                    else:
                                        jump Act3Part4

                                "No (This may send you back a bit)":
                                    if pan == False:
                                        "You either need to get to the third puzzle or don't ask for a hint if you don't need one."
                                        if lily == False:
                                            jump Act3Part1
                                        elif knox == False: 
                                            jump Puzzle7
                                        elif pan == False:
                                            jump Act3Part2
                                        elif jim == False:
                                            jump Puzzle8
                                        elif sugar == False:
                                            jump Act8Part3
                                        elif drpepper == False:
                                            jump Puzzle9
                                        elif drpepper:
                                            jump Act3Part4
                                    else: 
                                        "Do you want a hint for the third puzzle which is in the office?"
                                        menu:
                                            "Yep":
                                                $ time += 60
                                                "Part of your word is \"D**r*at\"."
                                                
                                                if lily == False:
                                                    jump Act3Part1
                                                elif knox == False: 
                                                    jump Puzzle7
                                                elif pan == False:
                                                    jump Act3Part2
                                                elif jim == False:
                                                    jump Puzzle8
                                                elif sugar == False:
                                                    jump Act3Part3
                                                elif drpepper == False:
                                                    jump Puzzle9
                                                else:
                                                    jump Act3Part4
                                            "No (This may send you back a bit)":
                                                "Then why are you all the way here?"
                                                if lily == False:
                                                    jump Act3Part1
                                                elif knox == False: 
                                                    jump Puzzle7
                                                elif pan == False:
                                                    jump Act3Part2
                                                elif jim == False:
                                                    jump Puzzle8
                                                elif sugar == False:
                                                    jump Act3Part3
                                                elif drpepper == False:
                                                    jump Puzzle9
                                                else:
                                                    jump Act3Part4