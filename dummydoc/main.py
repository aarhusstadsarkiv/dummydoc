import argparse
import sqlite3

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

        * Required: files.db inside _metadata folder inside given root folder parameter
        
        * Prints a list of every dummy tiff file in the root folder structure.
    """
# Test if the given path parameter is valid!
#   if !Path.exists(<path>):
#       throw exception

# Check for the existence of the .db file - if it's not found, then throw exception

# Define checksums to look for, put them in a list
    # dummy-checksums = [<checksum of first dummy tiff>, <checksum of second dummy tiff>, ...]
# Here's the checksums:
#   corrupted file:     50a33547e3d47c5dba7282c9e7fd72f96415190131b6326ed72327dc1f966c23
#   empty file:         86b54cf579de41c77966110c6ea2cebcb463497741c0852c3a2fa0eb6147c6bb
#   no known software:  7505e62d0e47b61298916e49c394a013a2119527738cc072ad3eb2ae6407a913
#   not preservable:    180dddb2b4563c84caf9fb8eee919c22388b62d86b875613ecb88423b2a0b696
#   password protected: 1f02c224c2acc2110a8c04cf1232402ad18bf7a1c5404140dfd6cc1f0f61b764

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

# "Connect" to the .db file
    # con = sqlite3.connect(<path> + "/_metadata/files.db")
    # cur = con.cursor

### Can this be done as
###      con = sqlite3.connect(<path> + "/_metadata/files.db")
###      for path, checksum in con.execute('SELECT path, checksum FROM Files')
### 'Cus that's certainly more compact, and easier to understand

# Now, query the .db file, and look thru the result
    # for path, checksum in cur.execute('SELECT path, checksum FROM Files')
    #   for i, dummy-checksum in enumerate(dummy-checksums):
    #       if checksum == dummy-checksum:
    #           dummy-lists[i].append(path)

# Finally we'll loop thru the list and print the result
    # for ls in dummy-lists:
    #   for i in ls:
    #       print i


# Potential avenues for optimization:
#   - Immediately print file somehow instead of storing it in a list?










