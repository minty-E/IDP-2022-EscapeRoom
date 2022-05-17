# i watched a youtube tutorial for this btw

define e = Character("")

# stores names of dragged items
init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop[0].drag_name

        return True

label start:
    scene bg room
    show screen drag_sample1A
    e ""
    if droppable == "box":
        $ xpos_var = 150
    else:
        $ xpos_var = 640

# declares what happens once cat is dragged on box
    if draggable == "cat":
        show screen catinbox
        hide screen drag_sample1A
        e "the [draggable] is in the [droppable]"

    return
# have different screens for different images that you want to be dragged
# add name, image (child), and position
# cannot move items marked as undraggable
# you can make items that are draggable also be droppable
# draggroup means the item you click will go to the top layer.
# can be replaced with fixed: to have the layers be set
screen drag_sample1A:
    draggroup:
        drag:
            drag_name "cat"
            child "cat.jpg"
            xpos 0.01
            ypos 1
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "box"
            xpos 0.1
            ypos 0.6
            child "cardboard.jpg"
            draggable False
            droppable True

# 2nd screen to show new image once cat is dropped on box
screen catinbox:
    draggroup:
        drag:
            drag_name "catinbox"
            child "catinbox.jpg"
            xpos 0.1
            ypos 0.6
            draggable False
            droppable False
