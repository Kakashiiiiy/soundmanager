# soundmanager
soundmanager for tiling windows managers

Make a .Scripts directory in your Home folder.

audioswitchNEW.py changes the current sink, the difference between the most of the self written audio managers the sink numbers does not matter.

sway/i3-config:
```
bindsym XF86AudioRaiseVolume exec --no-startup-id ~/.Scripts/audiocontrol.py i
bindsym XF86AudioLowerVolume exec --no-startup-id ~/.Scripts/audiocontrol.py d
bindsym $mod+z exec ~/.Scripts/audioswitchNEW.py
```
