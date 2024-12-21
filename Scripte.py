import sys
import os
import shutil
import re


def CheckAndCreateDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def PrepareFileName(unappropriateName):

    for chart in ["?", ":", "/"]:
        unappropriateName = unappropriateName.replace(chart, "")
    return unappropriateName + ".md"


def GetNewfullPath(oldPath, newBasename):

    dirname = os.path.dirname(oldPath)

    new_directory_name = os.path.join(dirname, "treated")
    new_directory_name = new_directory_name.replace("\\", "/")

    CheckAndCreateDirectory(new_directory_name)
    return new_directory_name + "/" + newBasename


def fix_file(path):
    try:
        assert os.path.exists(path=path)

        with open(path, mode="r") as file:
            x = file.readline()
            x = x.removeprefix("#")
            NewFileName = x.strip()
            print(x)
        NewFileName = PrepareFileName(NewFileName)
        newFullPath = GetNewfullPath(path, NewFileName)

        shutil.move(path, newFullPath)

        print("Move " + path + " to " + newFullPath + " Done")
    except:
        print("Failed to move " + path)


fix_file(
    "C:/Users/User/Desktop/data/[18F]FDG-PET CT texture analysis in thyroid incide 715d7050c5664c1aa7b65f431871ed72.md")
