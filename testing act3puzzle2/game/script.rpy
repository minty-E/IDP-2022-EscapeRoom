
define e = Character("Eileen")



label start:
    scene tower
    e "move blocks"
    call screen blocks()

init python:
    spot = 0
    def blockdrag(drags, drop):
        if drop.drag_name == "firstspot":
            spot == 1
        if drop:
            drags[0].snap(drop.x, drop.y)
            renpy.set_child("wallblockBspot1.png")  

screen blocks():
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
