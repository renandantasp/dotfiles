#!/usr/bin/zsh

nitrogen --restore &
xrandr --output VGA-1-1 --mode 1366x768 --rate 59 --noprimary --right-of HDMI-0 &
compton &
numlockx on &
flameshot &