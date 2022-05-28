
define e = Character("Eileen")


define d = "B.png"
label start:
    scene tower
    e "move blocks"
    call screen blocks()


init python:
    spot = 0
    Bx = 0
    By = 820
    letter = "B"  
    def refresh():
        renpy.restart_interaction()
    def blockdrag(drags, drop):
        if drop:
            d = "wallblockBspot1.png"
            drags[0].child("wallblockBspot1.png")
            return 
screen blocks:
    draggroup:
        drag:
            drag_name "B"
            child "B.png"
            xpos 0 
            ypos 820
            xsize 291
            ysize 281
            draggable True
            droppable False
            dragged blockdrag
            drag_raise True
        drag:
            drag_name "firstspot"
            xpos 471
            ypos 146
            xsize 177
            ysize 173
            draggable False
            droppable True
