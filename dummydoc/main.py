import argparse
import sqlite3

from pathlib import Path
from sqlite3.dbapi2 import Connection
from typing import List

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

def dummydoc(file: str) -> None:
    """
        * Takes a path to a database generated by Digiarch
        
        * Prints a list of every dummy tiff file entry in the database
    """
# Define checksums to look for, put them in a list
    dummyChecksums: List[str] = []

    # "corrupted file" checksum
    dummyChecksums.append("50a33547e3d47c5dba7282c9e7fd72f96415190131b6326ed72327dc1f966c23")
    # "empty file" checksum
    dummyChecksums.append("86b54cf579de41c77966110c6ea2cebcb463497741c0852c3a2fa0eb6147c6bb")
    # "no known software" checksum
    dummyChecksums.append("7505e62d0e47b61298916e49c394a013a2119527738cc072ad3eb2ae6407a913")
    # "not preservable" checksum
    dummyChecksums.append("180dddb2b4563c84caf9fb8eee919c22388b62d86b875613ecb88423b2a0b696")
    # "password protected" checksum
    dummyChecksums.append("1f02c224c2acc2110a8c04cf1232402ad18bf7a1c5404140dfd6cc1f0f61b764")

# Create lists for each dummy tiff to house the dummy files we find
# Pack them in a list?
    dummyLists: List[List[str]] = []
    for i in dummyChecksums:
        dummyLists.append([])
# This way the structure of the program is extensible and flexible 
# - if the dummy files change or new ones are added, the only thing 
# needed is to update the saved checksums
# To make it even easier, we COULD actually calculate the checksums,
# and have a folder with the dummy tiffs - then updating the program 
# would just mean modifying this folder!

# "Connect" to the .db file
    # con: Connection = sqlite3.connect(file)
    # cur = con.cursor
    # for path, checksum in cur.execute('SELECT path, checksum FROM Files')

# "Connect" to the .db file
    con: Connection = sqlite3.connect(file)
# Now, query the .db file, and look thru the result
# Can this be done as
    for path, checksum in con.execute('SELECT path, checksum FROM Files'):
        for i, dummyChecksum in enumerate(dummyChecksums):
            if checksum == dummyChecksum:
                dummyLists[i].append(path)
# 'Cus that's certainly more compact, and easier to understand


# Finally we'll loop thru the list and print the result
    for ls in dummyLists:
        for i in ls:
            print(i)


# Potential avenues for optimization:
#   - Immediately print file somehow instead of storing it in a list?










