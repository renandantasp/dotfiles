from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os, subprocess
import topbar as tp


mod = "mod4"
terminal = 'kitty'
browser = 'brave-browser'
file_manager = 'thunar'

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
                        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    Key([mod], "w", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "d", lazy.spawn('rofi -show drun -modi drun'), desc="Launch browser"),
    Key([mod], "f", lazy.spawn(file_manager), desc="Launch File Manager"),
    Key([mod], "e", lazy.spawn('emacs'), desc="Launch Emacs"),
    Key([], "Print", lazy.spawn('flameshot gui'), desc="Screenshot"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod,"shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c %d -q set Master 2dB+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c %d -q set Master 2dB-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer -D pulse set Master toggle")
    ),

]


groups = [
   Group("1", label="\ufa9e", spawn="brave-browser"),
   Group("2", label=" "),
   Group("3", label=" "),
   Group("4", label="\uf6d7"),
   Group("5", label="\uf6d7"),
   Group("6", label="\uf6d7"),
   Group("7", label="\uf6d7"),
   Group("8", label="\ufb6e", spawn="discord"),
   Group("9", label="\uf9c6", spawn="spotify"),
   ]

# for i in range(len(groups)):
#     keys.append(Key([mod], str((i)), lazy.group[str(i)].toscreen()))
#     keys.append(
#         Key([mod, "shift"], str((i)), lazy.window.togroup(str(i), switch_group=True))
#     )



for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


layout_theme = {
    "border_width": 1,
    "margin": 8,
    "border_focus": "#d79921",
    "border_normal": "#282828",
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.TreeTab(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]

#layouts = [
    #layout.Columns(border_focus_stack=['#0042ff', '#0042ff'], border_width=2),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
#]

#==== Colors ====#
colors = [
    ["#282828", "#282828"],  # 0
    ["#928374", "#928374"],  # 1 
    ["#ebdbb2", "#ebdbb2"],  # 2
    ["#98971a", "#98971a"],  # 3
    ["#d79921", "#d79921"],  # 4
    ["#353535", "#353535"],  # 5
    ["#458588", "#458588"],  # 6
    ["#b16286", "#b16286"],  # 7
    ["#689d6a", "#689d6a"],  # 8
    ["#928374", "#928374"],  # 9
    ["#fb4934", "#fb4934"],  # 10
    ["#fabd2f", "#fabd2f"],  # 11
    ["#b8bb26", "#b8bb26"],  # 12
    ["#83a598", "#83a598"],  # 13
    ["#f3869b", "#f3869b"],  # 14
    ["#8ec07c", "#8ec07c"],  # 15
]


widget_defaults = dict(
    font='Iosevka',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            tp.top_bar1(colors),
            size=28,
            opacity=0.95,
            background=colors[0],
            margin=[8,8,8,8]
        ),
    ),
    Screen(
        top=bar.Bar(
            tp.top_bar2(colors),
            size=28,
            opacity=0.95,
            background=colors[0],
            margin=[4,4,0,4]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
wmname="qtile"
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/boot.sh"])