# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess

from libqtile.config import Key, EzKey, Screen, Group, Drag, Click, hook
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
from libqtile.command_client import InteractiveCommandClient
#c = InteractiveCommandClient()

from typing import List  # noqa: F401

mod = "mod4"


night0 = '#2e3440'
night1 = '#3b4252'
night2 = '#434c5e'
night3 = '#4c566a'

snow0 = '#d8dee9'
snow1 = '#e5e9f0'
snow2 = '#eceff4'

frost0 = '#8fbcbb'
frost1 = '#88c0d0'
frost2 = '#81a1c1'
frost3 = '#5e81ac'

red = '#bf616a'
orange = '#d08770'
yellow = '#ebcb8b'
green = '#a3be8c'
purple = '#b48ead'


@hook.subscribe.startup_once
def autostart():
    start = '/home/dan/.config/qtile/autostart.sh'
    subprocess.call([start])
    lazy.group[' 爵 '].to_screen()
    
#@hook.subscribe.client_new
#def dialogs(window):
    #if (window.window.get_wm_type() == 'dialog'
            #or window.window.get_wm_transient_for()):
        #window.floating = True


#@hook.subscribe.client_new
#def vue_tools(window):
    #if((window.window.get_wm_class() == (
        #'sun-awt-X11-XWindowPeer', 'tufts-vue-VUE')
            #and window.window.get_wm_hints()['window_group'] != 0)
            #or (window.window.get_wm_class() == (
                #'sun-awt-X11-XDialogPeer', 'tufts-vue-VUE'))):
        #window.floating = True


#@hook.subscribe.client_new
#def idle_dialogues(window):
    #if((window.window.get_name() == 'Search Dialog') or
      #(window.window.get_name() == 'Module') or
      #(window.window.get_name() == 'Goto') or
      #(window.window.get_name() == 'IDLE Preferences')):
        #window.floating = True


#@hook.subscribe.client_new
#def libreoffice_dialogues(window):
    #if ((window.window.get_wm_class() == (
        #'VCLSalFrame', 'libreoffice-calc')) or
            #(window.window.get_wm_class() == (
                #'VCLSalFrame', 'LibreOffice 3.4'))):
        #window.floating = True
 
keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("konsole")),
    Key([mod], "e", lazy.spawn("dolphin")),
    EzKey('A-S-<space>', lazy.widget['keyboardlayout'].next_keyboard()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    #Key([mod], "r", lazy.spawncmd()),
    Key([mod], "r", lazy.spawn('rofi -show run')),
]

groupnames = [
    ' 爵 ', '  ', '  ', '  ', '  ', '  ', '  ', '  '
]

groupkeys = 'asdfuiop'

groups = []

groups.append(Group(groupnames[0], spawn=['firefox']))
groups.append(Group(groupnames[1], spawn=['code']))
groups.append(Group(groupnames[2], spawn=['slack', 'telegram-desktop', 'discord']))
groups.append(Group(groupnames[3], spawn=['dolphin', 'konsole']))
groups.append(Group(groupnames[4], spawn=['kate']))
groups.append(Group(groupnames[5]))
groups.append(Group(groupnames[6]))
groups.append(Group(groupnames[7]))

for groupkey, group in zip(groupkeys, groups):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], groupkey, lazy.group[group.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], groupkey, lazy.window.togroup(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layout_defaults = dict(
    border_normal=night3, border_focus=snow0, border_width=7, margin=7, columns=3
)

layouts = [
    layout.MonadTall(**layout_defaults),
    layout.Max(**layout_defaults),
    layout.Tile(**layout_defaults),
    #layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

font = 'DaddyTime Mono Nerd Font'
fontsize = 25

widget_defaults = dict(
    font=font,
    fontsize=25,
    padding=0,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(' ', background=frost2),
                widget.CurrentLayout(font=font, fontsize=fontsize, padding=0, foreground=snow2, background=frost2),
                widget.GroupBox(font=font, fontsize=fontsize, padding=0, background=night0, foreground=snow2, inactive=night3, active=snow2,
                                borderwidth=4, this_current_screen_border=frost1, urgent_border=yellow, urgent_text=yellow, spacing=10, margin=3,
                                highlight_method='line', highlight_color=frost3),
                widget.Prompt(font=font, fontsize=fontsize, padding=0, foreground=green, background=night0),
                widget.WindowName(font=font, fontsize=fontsize, padding=0, background=night0),
                widget.TextBox(text=' ' + u'\ue0b6', font=font, fontsize=34, padding=0, foreground=frost2, background=night0),
                widget.Systray(font=font, fontsize=fontsize, padding=7, background=frost2, foreground=snow2, icon_size=35),
                widget.TextBox(text=' ' + u'\ue0b6', font=font, fontsize=34, padding=0, foreground=night0, background=frost2),
                widget.KeyboardLayout(font=font, fontsize=fontsize, padding=0, configured_keyboards=['us', 'ru'], background=night0, foreground=snow2),
                widget.TextBox(text=' ' + u'\ue0b6', font=font, fontsize=34, padding=0, foreground=frost2, background=night0),
                widget.Clock(format='%H:%M %d/%m/%Y', font=font, fontsize=fontsize, padding=0, foreground=snow2, background=frost2),
                widget.TextBox(text=' ' + u'\ue0b6', font=font, fontsize=34, padding=0, foreground=night0, background=frost2),
                widget.QuickExit(font=font, fontsize=fontsize, default_text='襤 ', padding=0, countdown_format='{}  ', background=night0, foreground=red),
            ],
            35, opacity=0.7, margin=[5, 5, 0, 5]
        ), wallpaper='/home/dan/Pictures/wallpapers/Nord_21x9.png'
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
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
