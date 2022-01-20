import os
import subprocess
from libqtile import qtile
from libqtile.config import (
    Group,
    KeyChord,
    Key,
    Match,
    Screen,
    EzClick as Click,
    EzDrag as Drag,
)
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

def top_bar1(colors):

    return [
        widget.TextBox(
            text=" \uf002 ",
            font="Iosevka Nerd Font",
            fontsize="16",
            background=colors[2],
            foreground=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("rofi -show drun -modi drun")
            },
        ),
        
         widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[2],
        ),
        widget.GroupBox(
            font="Iosevka Nerd Font",
            fontsize=14,
            margin_y=3,
            margin_x=6,
            padding_y=7,
            padding_x=6,
            borderwidth=4,
            active=colors[4],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[3],
            highlight_method="block",
            this_current_screen_border=colors[4],
            other_screen_border=colors[3],

            other_current_screen_border=colors[4],
            this_screen_border=colors[3],
            block_highlight_text_color=colors[0],
        ),
        widget.Prompt(
            background=colors[2],
            foreground=colors[0],
            font="Inconsolata",
            fontsize=12,
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        # widget.Sep(
        #     padding=1,
        #     linewidth=0,
        #     background=colors[1],
        # ),
        widget.Sep(
            padding=5,
            linewidth=0,
            background=colors[5],
        ),
        widget.WindowName(
            font="Inconsolata",
            fontsize=12,
            background=colors[5],
            foreground=colors[2],
        ),
        # widget.Sep(
        #     padding=1,
        #     linewidth=0,
        #     background=colors[1],
        # ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            scale=0.45,
            padding=0,
            background=colors[0],
            foreground=colors[2],
            font="Iosevka Nerd Font",
            fontsize=14,
        ),
        # widget.CurrentLayout(
        #     font="Iosevka Nerd Font",
        #     fontsize=15,
        #     background=colors[0],
        #     foreground=colors[2],
        # ),
        widget.Sep(
            padding=10,
            linewidth=0,
            background=colors[0],
        ),
        widget.Sep(
            padding=1,
            linewidth=0,
            background=colors[5],
        ),
        widget.TextBox(
            # text="  ",
            text=" disk:",
            font="Iosevka Nerd Font",
            fontsize=15,
            padding=0,
            background=colors[0],
            foreground=colors[11],
        ),
        widget.DF(
            fmt="{}",
            font="Iosevka Nerd Font",
            fontsize=15,
            partition="/home",
            # format="{uf}{m} ({r:.0f}%)",
            format="{r:.0f}% ",
            visible_on_warn=False,
            background=colors[0],
            foreground=colors[2],
            padding=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("urxvt -e gotop")},
        ),

        # widget.Systray(
        #     background=colors[0],
        #     foreground=colors[2],
        #     icons_size=18,
        #     padding=4,
        # ),

        widget.Sep(
            padding=1,
            linewidth=0,
            background=colors[5],
        ),

        # widget.TextBox(
        #     # text="   ",
        #     text="cal:",
        #     font="Iosevka Nerd Font",
        #     fontsize="14",
        #     padding=0,
        #     background=colors[0],
        #     foreground=colors[11],
        # ),
        widget.TextBox(
            text=" vol:",
            font="Iosevka Nerd Font",
            fontsize=15,
            padding=0,
            foreground=colors[11],
        ),
        widget.Volume(
            font = 'Iosevka Nerd Font',
            fontsize = 14,
            foreground = colors[2]
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize=15,
            padding=0,
        ),
        widget.Sep(
            padding=1,
            linewidth=0,
            background=colors[5],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            background=colors[0],
            foreground=colors[11],
            fontsize=15,
            format=" %d %b, %a",
        ),
        # widget.TextBox(
        #     text="  ",
        #     font="Iosevka Nerd Font",
        #     fontsize="18",
        #     padding=0,
        #     background=colors[0],
        #     foreground=colors[2],
        # ),
        widget.Clock(
            font="Iosevka Nerd Font",
            background=colors[0],
            foreground=colors[11],
            fontsize=15,
            format="%I:%M %p ",
        ),    
    ]

def top_bar2(colors):
    return [
        widget.GroupBox(
            font="Iosevka Nerd Font",
            fontsize=14,
            margin_y=3,
            margin_x=6,
            padding_y=7,
            padding_x=6,
            borderwidth=4,
            active=colors[4],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[3],
            highlight_method="block",
            this_current_screen_border=colors[4],
            other_screen_border=colors[3],

            other_current_screen_border=colors[4],
            this_screen_border=colors[3],
            block_highlight_text_color=colors[0],
        ),
        widget.Prompt(
            background=colors[2],
            foreground=colors[0],
            font="Inconsolata Nerd Font",
            fontsize=18,
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        # widget.Sep(
        #     padding=1,
        #     linewidth=0,
        #     background=colors[1],
        # ),
        widget.Sep(
            padding=5,
            linewidth=0,
            background=colors[5],
        ),
        widget.WindowName(
            font="Inconsolata",
            fontsize=12,
            background=colors[5],
            foreground=colors[2],
        ),

        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            scale=0.45,
            padding=0,
            background=colors[0],
            foreground=colors[2],
            font="Iosevka Nerd Font",
            fontsize=14,
        ),
        widget.TextBox(
            text="   ",
            font="Iosevka Nerd Font",
            fontsize="14",
            padding=0,
            background=colors[0],
            foreground=colors[2],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            background=colors[0],
            foreground=colors[2],
            fontsize=15,
            format="%d %b, %a ",
        ),
        widget.TextBox(
            text="  ",
            font="Iosevka Nerd Font",
            fontsize="18",
            padding=0,
            background=colors[0],
            foreground=colors[2],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            background=colors[0],
            foreground=colors[2],
            fontsize=15,
            format="%I:%M %p ",
        ),    
    ]
