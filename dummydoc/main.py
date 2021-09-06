import argparse
import sqlite3

from sqlite3.dbapi2 import Connection
from typing import List


def dummydoc(file: str) -> None:
    """
    * Takes a path to a database generated by Digiarch

    * Prints a list of every dummy tiff file entry in the database
    """
    # Define checksums to look for, put them in a list
    dummyChecksums: List[str] = []

    # "corrupted file" checksum
    dummyChecksums.append(
        "50a33547e3d47c5dba7282c9e7fd72f96415190131b6326ed72327dc1f966c23"
    )
    # "empty file" checksum
    dummyChecksums.append(
        "86b54cf579de41c77966110c6ea2cebcb463497741c0852c3a2fa0eb6147c6bb"
    )
    # "no known software" checksum
    dummyChecksums.append(
        "7505e62d0e47b61298916e49c394a013a2119527738cc072ad3eb2ae6407a913"
    )
    # "not preservable" checksum
    dummyChecksums.append(
        "180dddb2b4563c84caf9fb8eee919c22388b62d86b875613ecb88423b2a0b696"
    )
    # "password protected" checksum
    dummyChecksums.append(
        "1f02c224c2acc2110a8c04cf1232402ad18bf7a1c5404140dfd6cc1f0f61b764"
    )

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
    con: Connection = sqlite3.connect("file:" + file + "?mode=ro", uri=True)
    # Now, query the .db file, and look thru the result
    for path, checksum in con.execute("SELECT path, checksum FROM Files"):
        for idx, dummyChecksum in enumerate(dummyChecksums):
            if checksum == dummyChecksum:
                dummyLists[idx].append(path)

    # Finally we'll loop thru the list and print the result
    for ls in dummyLists:
        for i in ls:
            print(i)


# Potential avenues for optimization:
#   - Immediately print file somehow instead of storing it in a list?
#       Not sure if that's feasible when it needs to be
#       printed as a tiff file later


# Set up argparse stuff
# Not sure if this is where it should go

parser = argparse.ArgumentParser()
parser.add_argument(
    "file",
    help="the path to the database generated by Digiarch that's "
    + "to be searched for dummy tiff files",
    type=str,
)
args: argparse.Namespace = parser.parse_args()
dummydoc(args.file)