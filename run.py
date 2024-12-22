
import os
import argparse
from Core import fix_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Convert notion dataviwe to obisident ', description='Automatic convert dataviwe of notion to obisident Database folder', epilog='Text at the bottom of help')
    parser.add_argument("directory")

    args = parser.parse_args()
    directoryFile = args.directory
    files = os.listdir(directoryFile)
    for fname in files:
        name, extension = os.path.splitext(fname)
        if extension != ".md":
            continue

        fix_file(os.path.join(directoryFile, fname))
