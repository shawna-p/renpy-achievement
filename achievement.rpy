## Screen to show an achievement unlocked notification. Takes three parameters:
## description = Description of the unlocked achievement.
## box_len = integer number of the width of the achievement popup, in pixels.
## read_len = float corresponding to the number of seconds this popup should
##            remain on-screen for before hiding itself.
screen achievement_unlock(description="Description", box_len=max_achievement_len,
        read_len=read_achievement_time):

    frame:
        # The background is shown at a transform since the circles begin
        # smaller than the full popup size.
        background At('achievement_bg', appear)
        pos ((box_len//2)+achievement_xoffset, (circle_size//2)+achievement_yoffset)
        # Anchor it so it grows out from the center.
        anchor (0.5, 0.5)
        padding (0, 0)
        # Fade this out when it disappears
        at transform:
            alpha 1.0
            pause 3.2+read_len
            easeout 1.0 alpha 0.0
        # Ensure this takes the size of the expanding fixed below
        has fixed:
            fit_first True
            align (0.5, 0.5)
        fixed:
            xysize (circle_size, circle_size)
            align (0.5, 0.5)
            # The achievement expands to fit the size of this fixed
            at transform:
                size (circle_size, circle_size)
                linear 1.3 size (circle_size, circle_size)
                easein 1.0 size (box_len*1.08, circle_size)
                easeout 0.25 size (box_len, circle_size)
                pause read_len
                easeout_back 1.3 size (circle_size, circle_size)
        # This fixed holds the overlapping circle animation
        fixed:
            xysize (circle_size, circle_size)
            # While the circles grow larger, the anchor is the center of
            # this frame. However, when it grows in size, we switch the
            # anchor to the middle-left.
            at transform:
                zoom 0.5 align (0.5, 0.5)
                linear 1.0 zoom 1.0
                pause 0.3
                align (0.0, 0.5)
            # These are the circles that grow in size
            add 'lime_circle' at grow_circle(0.0)
            add 'green_circle' at grow_circle(0.25)
            add 'dark_green_circle' at grow_circle(0.5)
            add 'lime_circle' at grow_circle(0.75)
            # This is the background behind the trophy symbol
            add 'trophy_bg' at appear(1.25)
            # This is the trophy symbol
            add 'trophy_icon':
                at transform:
                    zoom 0.0 align (0.5, 0.5)
                    pause 1.0
                    easein_back 0.6 zoom 0.7
        # The achievement text.
        vbox:
            xsize box_len-circle_size
            xoffset int(circle_size-(circle_size*0.1))
            style 'achievement_vbox'
            # This contains the achievement text. First is the header.
            text "Achievement unlocked":
                style 'achievement_unlocked_text'
                # Slide the text in after the area has expanded.
                at transform:
                    alpha 0.0 xoffset 20
                    pause 1.6
                    easein 1.0 alpha 1.0 xoffset 0
                    pause 1.25+read_len-1.6-1.0+1.3
                    easeout 0.2 alpha 0.0

            fixed:
                xsize box_len-circle_size xalign 0.5
                # This holds the achievement description, passed in
                # when the screen is called.
                text description:
                    style 'achievement_description_text'
                    # Make the text appear after the area has expanded.
                    at transform:
                        alpha 0.0
                        pause 2.5
                        linear 0.2 alpha 1.0
                        pause 1.25+read_len-2.5-0.2+1.3
                        easeout 0.2 alpha 0.0

    # Hide this screen once it's done showing the popup animation
    timer 4.3+read_len action Hide('achievement_unlock')

# Radius of the circle used for the unlock background
define circle_size = 50
# Default length the achievement should expand to in order to fit the text.
# Can be adjusted via passing an argument to the screen.
define max_achievement_len = 250
# Default # of seconds to show the achievement text for before disappearing.
define read_achievement_time = 4.0
# The number of pixels between the edge of the achievement popup and
# the left/top edge of the screen.
define achievement_xoffset = 15
define achievement_yoffset = 5

# Style for the vbox containing the achievement text
style achievement_vbox:
    spacing -5

# Style for the "Achievement unlocked" text
style achievement_unlocked_text:
    size 16
    align (0.5, 0.5)

# Style for the achievement description
style achievement_description_text:
    size 23
    align (0.5, 0.5)

# Transform for the layered circles getting larger
transform grow_circle(delay):
    zoom 0.0 align (0.5, 0.5)
    pause delay
    linear 0.5 zoom 1.0
    pause 1.5
    alpha 0.0

# Transform that prevents something from appearing for delay seconds
transform appear(delay=1.3):
    alpha 0.0
    pause delay
    alpha 1.0

init python:
    class Circle(renpy.Displayable):
        def __init__(self, color="#000", diameter=None, **kwargs):
            super(Circle, self).__init__(**kwargs)
            self.color = renpy.color.Color(color)
            self.diameter = diameter or (2*circle_size)

        def render(self, width, height, st, at):
            diameter = self.diameter or min(width, height)
            render = renpy.Render(diameter, diameter)
            cv = render.canvas()
            cv.circle(self.color, # the color
                      (diameter/2, diameter/2), # the center
                      diameter/2, # the radius
                      )
            return render

# You can replace this with your own image of a trophy or some other icon.
# This one begins as a star, then "rotates" to become the trophy icon.
image trophy_icon:
    'star.png'
    time 2.0
    squish_x
    'trophy.png'
    stretch_x

# Transforms used by the trophy icon definition.
transform squish_x():
    xzoom 1.0
    linear 0.5 xzoom 0.0
transform stretch_x():
    xzoom 0.0
    linear 0.5 xzoom 1.0

# These images overlap and grow larger over each other to make up the trophy
# effect. Uses the Circle displayable defined earlier.
image green_circle = Circle(color="#080")
image dark_green_circle = Circle(color="#045a04")
image lime_circle = Circle(color="#0f0")

# This is the image shown behind the trophy icon
image trophy_bg = 'lime_circle'

# This is the background for the entire achievement once the text slides out.
# Should be variable-width, likely inside a Frame as seen here.
image achievement_bg = Frame('green_circle', circle_size//2, circle_size//2)
