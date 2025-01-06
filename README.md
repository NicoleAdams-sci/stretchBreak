# Stretch Break

Let Mickey and friends remind you to take a  Stretch Break!

<img src="Mickey_and_Minnie_Mickey_Mouse_Funhouse.png" alt="Mickey and Minnie" width="400" height="400">

## What is Stretch Break?
This python code will play the Stretch Break song audio from Mickey Mouse FunHouse using your computer's default audio player.

## Stretch Break options
-i, --interval_minutes = time in minutes you want to be reminded to stretch [default 60 minutes]<br>
-t, --audio_type = choose from Stretch Break clip (short) or the full song (full) [default short]

## How to run Stretch Break?
Download repo contents via Download ZIP on GitHub<br>
Navigate to new directory<br>
`cd stretchBreak`<br>
Play short audio (default) with default interval (60 minutes)<br>
`python stretchBreak.py`<br>
Play full audio with custom interval<br>
`python stretchBreak.py -t full -i 30`<br>

### Fine print
The code should work with Python 3.x versions (Python 3.6 or newer recommended). The main modules used are all part of Python's standard library (time, argparse, datetime, os, platform, subprocess). You may need to specify `python3 strechBreak.py` to run the code.<br>

##
Mickey Mouse FunHouse is property of Disney Enterprises, Inc.<br>