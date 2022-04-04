# renpy-achievement
Code for an Xbox-inspired achievement popup in Ren'Py

![achievement_gif](https://github.com/shawna-p/renpy-achievement/blob/main/achievement_gif.gif?raw=true)

## How to use

First, drop the file `achievement.rpy` into your `game/` folder, and add the images `trophy.png` and `star.png` to your `images/` folder. Then, to show the achievement popup in-game, just write:

```renpy
show screen achievement_unlock("Description")
```

in your game script. There are a few additional parameters you can pass the screen to adjust its behaviour:

* `box_len` adjusts the length of the achievement popup, in pixels. Its default value is controlled by the variable `max_achievement_len`, which you can adjust.
* `read_len` adjusts the time the player has to read the popup before it disappears. Its default value is controlled by the variable `read_achievement_time`, which you can adjust.

So, a more complete achievement call might look like:

```renpy
show screen achievement_unlock("Met Eileen", box_len=300, read_len=2.0)
```

This will show the achievement popup for 2 seconds (+ animation startup and finish time), and it will be 300 pixels wide to contain the achievement description text.

If you would like to use a larger circle for the popup, you can update the variable `circle_size` to be the new circle diameter, in pixels.

You can adjust the position of the popup with the variables `achievement_xoffset` and `achievement_yoffset`. By default it appears in the top-left corner of the screen.

There are also several styles you can adjust to customize the appearance of the description and "Achievement unlocked" text.

Finally, you can replace several of the defined images with your own. Note that if you are replacing the coloured circles, they expect to be the same size as is defined in the `circle_size` variable.

## Compatibility

This code has been tested to be backwards-compatible with Ren'Py 7.3.5 and was last tested on Ren'Py 7.4.11.

## Built With

* [Ren'Py 7.4.4](https://www.renpy.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Like my work?

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/L3L7QE3T)
