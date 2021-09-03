import argparse

from pathlib import Path

# Set up argparse stuff
# Not sure where this should go just yet - putting it 
# in dummydoc seems wrong? Since it's not relevant to what it does
# Maybe what's in dummydoc needs to be put in a different function, 
# and then dummydoc will handle this stuff instead
#   parser = argparse.ArgumentParser()
#   parser.add_argument("path", help = "the root path to search for dummy tiff files", 
#                               type = <path>)
#   parser.parse_args()


"""
    Skeleton outline of overall program structure
"""

def dummydoc():
    """
        * Takes a path to a root folder as parameter.
        
        * Prints a list of every dummy tiff file in the root folder structure

        (Potential) assumptions:
            The file structure adheres to the standard of folder -> folder(s)
                                                                 -> file        
    """
# Test if the given path parameter is valid!
#   if !Path.exists(<path>):
#       throw exception

# Define checksums to look for, put them in a list
    # dummy-checksums = [<checksum of first dummy tiff>, <checksum of second dummy tiff>, ...]

# Create lists for each dummy tiff to house the dummy files we find
# Pack them in a list?
    # dummy-lists = []
    # for i in dummy-checksums:
    #   dummy-lists.append([])
# This way the structure of the program is extensible and flexible 
# - if the dummy files change or new ones are added, the only thing 
# needed is to update the saved checksums
# To make it even easier, we COULD actually calculate the checksums,
# and have a folder with the dummy tiffs - then updating the program 
# would just mean modifying this folder!

# Now we'll throw it over to a different function that's gonna handle
# the recursive folder-searching
    # dummy_finder_rec(path, dummy-checksums, dummy-lists)

# Finally we'll loop thru the list and print the result
    # for ls in dummy-lists:
    #   for i in ls:
    #       print i

def dummy_finder_rec():
    """
        * Takes a path and a list of the checksums to look for
        * Searches thru the root folder recursively, calculates a checksum
          for every file and compares it to checksums of the dummy tiffs, 
          and keeps track of any dummy files found
        * At end of execution all dummy tiff files inside the given root
          structure has been added to the dummy-lists
    """
# REMEMBER - you're working with files here, you'll need a lot 
# of try-statements and error-handling in this code!

# Now, for each file and folder in this path, 
# recursively call this function
# Then finally return your dummy-list
#   if (Path.is_folder(<path>)):
#       for child in <path>.iterdir():
#           dummy_finder_rec(child, dummy-checksums, dummy-lists)

# if this path is empty
# or maybe if the path is to a file?
    # if Path.is_file(<path>):

# Then that's the end of the recursion!
# So that means we need to:

    # Calculate checksum for file
        # checksum = calc_checksum(<path>)

    # Compare checksum to those in the list
    # and if it matches one, add it to the corresponding list
        # for i, value in enumerate(dummy-checksums):
        #   if checksum == value:
        #       dummy-list[i].append(<path>)

    # Finally return the (potentially updated) list?
    # Actually Python uses call-by-reference for mutable objects like lists
    # so no need to return anything! 
        # return dummy-lists


# Potential avenues for optimization:
#   - Immediately print file somehow instead of storing it in a list?
#   - Make use of filedb instead of calculating all these checksums? 










