# Macaroonize

Macaroonize converts an image into a photomosaic-style display of macaroons.
Example input: https://github.com/reverie/macaroonize/blob/master/example_output.png
Example output: https://github.com/reverie/macaroonize/blob/master/example_output.png

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
