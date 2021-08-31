# PixelFetch

## What is Pixel Fetch

PixelFetch is a fetch program similar to Neofetch in the concept that it gathers information of your OS and shares it,
But it is intended to be more minimal, but feel full at the same time!
The distro icons are also intended to have a pixel art unicode style isntead of the traditional ASCII art to look more full

## Running

because this is programmed in python, if you want to add this to your rc file, you will have to run
`python3 *insert full directory*/Pixelfetch.py` and the rest should run properly on its own.

## Configuration

You make your configurations in `config.json`. When configuring, make sure you do not destroy the config file, or else it will not work

 - **Distro** *auto* - The display name for your distro (leave auto to make it decide on its own) *does not work yet*
 - **Icon** *auto* - The icon that shows up if you want to add a custom one (leave auto to make it decide on its own) *does not work yet*
 - **Color** *auto* - The color that shows up if you want a custom color instead (leave auto to make it decide on its own) *does not work yet*
 - **UsesWindowManager** *false* - Set this to true if you use a window manager instead of a desktop environment

## Custom Icons
Want to make your own icons? here are the characters you can use:

**Icons should be 16x8 characters. they can be smaller, but they can not be taller or wider or THEY WILL crash**

Important for Main Shape:
Full Block - █
Up - ▀
Down - ▄

Wanna Add Details?
Right - ▐
Left - ▌
Corners - ▙ ▟ ▛ ▜
Lesser Corners - ▖▗ ▘▝

Shading I guess?:
Checkered - ▚ ▞

## Custom Quotes

Just create a text file in the Quotes folder, and type whatever you want in it as long as it is 61x6 Characters
