import sys
import os
import shutil
import re


def checkAndCreateDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def prepareFileName(unappropriateName):
    for chart in ["?", ":", "/", '"']:
        unappropriateName = unappropriateName.replace(chart, "")
    return unappropriateName + ".md"


def getNewFullPath(oldPath, newBasename):
    dirname = os.path.dirname(oldPath)

    new_directory_name = os.path.join(dirname, "treated")
    new_directory_name = new_directory_name.replace("\\", "/")

    checkAndCreateDirectory(new_directory_name)
    return new_directory_name + "/" + newBasename


def editlines(lines):
    NameFile = lines[0].removeprefix("#")
    NameFile = NameFile.strip()
    lines[0] = "---\n"
    lines[1] = 'Title: "' + NameFile + '"\n'
    for i, line in enumerate(lines):
        if line == "\n" or len(lines) == i+1:
            lines[i] = "---\n"
            break

    return lines


def readlines(path):
    with open(path, mode="r", encoding="UTF8") as source:
        return source.readlines()


def writefile(path, lines):
    with open(path, mode="w", encoding="UTF8") as destination:
        for line in lines:
            destination.write(line)


def UpdateFileName(path):
    try:
        assert os.path.exists(path=path)

        with open(path, mode="r",  encoding="utf8") as file:
            x = file.readline()
            x = x.removeprefix("#")
            NewFileName = x.strip()

        NewFileName = prepareFileName(NewFileName)
        newFullPath = getNewFullPath(path, NewFileName)

        shutil.move(path, newFullPath)

        print("Move " + path + " to " + newFullPath + " Done")
        return newFullPath
    except Exception as e:
        raise


def AddYamlToFile(filePath):
    try:
        lines = readlines(filePath)
        lines = editlines(lines)
        writefile(filePath, lines)
        print(filePath + " is updated")
    except Exception as e:
        raise


def FixFile(path):
    try:
        newpath = UpdateFileName(path)
        AddYamlToFile(newpath)
    except Exception as e:
        print(e)
