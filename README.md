# wallpaper-changer
Arch linux python multi-wallpaper changer.
All files should be **.jpg or .png**.

# Dependencies:
`feh`

# Usage: <br>
`git clone https://github.com/magic-sudo/wallpaper-changer`<br>

In .xinitrc add<br>
`python PATH_TO_WALLPAPER_CHANGER PATH_WALLPAPERS_DIR TIMEOUT_IN_SECONDS &`<br>

In my case<br>
`python /path/to/wallpaper_changer.py /path/to/wallpapers $time_in_seconds &`<br>

Then just restart restart your wm.
