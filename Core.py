import sys
import os
import shutil
import re


def CheckAndCreateDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def PrepareFileName(unappropriateName):

    for chart in ["?", ":", "/", '"']:
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

        with open(path, mode="r",  encoding="utf8") as file:
            x = file.readline()
            x = x.removeprefix("#")
            NewFileName = x.strip()

        NewFileName = PrepareFileName(NewFileName)
        newFullPath = GetNewfullPath(path, NewFileName)

        shutil.move(path, newFullPath)

        print("Move " + path + " to " + newFullPath + " Done")
    except Exception as e:
        print("Failed to move: " + path)
        print(e)


def Add_yaml_to_file(filePath):
    try:
        shutil.move(filePath, filePath+"~")
        destination = open(filePath, mode="w", encoding="UTF8")
        source = open(filePath, mode="r", encoding="UTF8")
        destination.
    except Exception as e:
        print(e)
    finally:
        if destination != None:
            destination.close()
            source.close()
