import sys
import os
import shutil
import re
import json


def Look_into_Json_for(query, source_path ):
    with open(source_path, 'r', encoding="UTF8") as file:
        data = json.load(file)
    query = query.strip().title()
    for material in data:

        if query == material["title"].strip().title():
             return material


def readNoteContent(path):
    with open(path, mode="r", encoding="UTF8") as source:
        return source.readlines()


def is_file_dotMD(file_name):
    name, extension = os.path.splitext(file_name)
    if extension != ".md":
        return False
    return True


def checkAndCreateDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def DefineNewFullPath(new_root, baseName):
    
    checkAndCreateDirectory(new_root)
    return os.path.join(new_root, baseName)


def get_title_in_file(path_file):
    try:
        x = readNoteContent(path_file)[0]
        x = x.removeprefix("#")
        name = x.strip()
        return name
    except:
        raise


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



def writefile(path, lines):
    with open(path, mode="w", encoding="UTF8") as destination:
        for line in lines:
            destination.write(line)



#TODO: fix function's name
def move_file(old_path, new_path):
    try:
        assert os.path.exists(path=old_path)
        #shutil.move(path, newFullPath)
        print("Move " + old_path + " to " + new_path + " Done")
        return new_path
    except Exception as e:
        raise




#TODO: fix function's name
def AddYamlToFile(filePath):
    try:
        lines = readNoteContent(filePath)
        lines = editlines(lines)
        writefile(filePath, lines)
        print(filePath + " is updated")
    except Exception as e:
        raise



def get_metadata_in_md(md_file_liens):
    try:
        metadata = {}
        lines = md_file_liens[2:]
        for i, line in enumerate(lines):
            if line == "\n" or len(lines) == i+1:
                break
            colum_index = line.index(":")
            key = line[0:colum_index]
            value = line[colum_index+1: -1].replace("\n", "").strip()
            metadata[key] = value.strip()

        return metadata
    except:
        raise


def get_note_in_md(md_file_liens):
    try:
        lines = md_file_liens[2:]
        for i, line in enumerate(lines):
            if line == "\n":
                break
            if len(lines) == i+1:
                return []
        return lines[i:]
    except:
        raise