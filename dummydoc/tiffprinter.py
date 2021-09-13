from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from typing import List


def stringToTiffPrinter(inputList: List[str], dest: str) -> None:
    """
    * Takes a list of strings to print, and a destination to save it at

    * Creates a tiff at the given destination
      with each string in the list on its own line

    * Assumption: the dest value ends in .tiff (or .tif)

    * Assumption: the dest value is a valid path
    """

    # To figure out the dimensions required for our
    # tiff, we'll need to make an unused test img first
    img: Image = Image.new("1", (5, 5))
    d: ImageDraw = ImageDraw.Draw(img)
    # Calculate how much we need to print,
    # so we can create a tiff of a suitable size
    totalLinesToPrint: int = len(inputList)
    textWidth: int = 0
    textHeight: int = 0

    # We'll also need a font, to calculate size
    # and to actually make the text later!
    textFont = ImageFont.truetype("arial.ttf", 18)

    # Also figure out how tall and wide the strings are gonna be
    for s in inputList:
        tempWidth, tempHeight = d.textsize(s, font=textFont)
        textWidth = max(textWidth, tempWidth)
        textHeight += tempHeight

    textVerticalMargin: int = 10
    textHorizontalMargin: int = 10
    textVerticalSpacing: int = 2

    # Dimensions of image:
    #   Width:  Horizontal margin x 2
    #           + the width of the widest path
    #   Height: Vertical margin x 2
    #           + the height of all the text paths combined
    #           + (the number of paths - 1) x the spacing between each line
    tiffFile: Image = Image.new(
        "1",
        (
            textHorizontalMargin * 2 + textWidth,
            textVerticalMargin * 2
            + textHeight
            + (totalLinesToPrint - 1) * textVerticalSpacing,
        ),
        1,
    )
    tiffDraw: ImageDraw = ImageDraw.Draw(tiffFile)

    # ... and now we can finally draw the image!
    x_pos: int = textHorizontalMargin
    y_pos: int = textVerticalMargin

    for s in inputList:
        tiffDraw.text((x_pos, y_pos), s, fill=0, font=textFont)
        tempWidth, tempHeight = d.textsize(s, font=textFont)
        y_pos += tempHeight + textVerticalSpacing
    # !!! figure out how to draw it nicer-looking?
    # !!! Maybe some fonts?

    # And then save it
    tiffFile.save(dest)
