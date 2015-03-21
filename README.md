# Macaroonize

Macaroonize converts an image into a photomosaic-style display of macaroons. Here's a simple example:

Input: https://github.com/reverie/macaroonize/blob/master/example_input.png

Output: https://github.com/reverie/macaroonize/blob/master/example_output.png

The resulting images are quite large (270x original resolution), so you'll probably want to resize them before using.

## Installation

This project uses python3 and ImageMagick. Assuming you already have virtualenvwrapper,
python3, and homebrew installed on OSX, it goes something like:

1. `mkvirtualenv macaroonize`
1. `brew install imagemagick`
1. `pip install Pillow`

...and you should be ready to go. On other platforms, get Pillow installed according 
to that project's documentation.

## Usage

`./macaroonize.py input.png output.png`
