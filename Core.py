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

def make_Md_file(matrial, metadata, note):
    try:
        with open(f'./done/@{matrial["id"]}.md', 'w', encoding="UTF8") as md_file:
            # Write a main header
            # Write meta data
            md_file.write('---\n')
            md_file.write(f'title: "{matrial["title"]}"\n')
            add_author_to_file(md_file, matrial.get("author", []))
            md_file.write(f'year: {get_type_of_year(matrial)}\n')
            md_file.write(f'container-title: "{get_type_of_reference(matrial, metadata)}"\n')
            md_file.write(f'type: {matrial.get("type", "")}\n')
            md_file.write(f'DOI: {matrial.get("DOI", "")}\n')
            md_file.write(f'study-type: {metadata.get("Type of paper", "")}\n')
            md_file.write(f'Status: {metadata.get("Status", "").replace(" ", "_")}\n')
            md_file.write(f'Score: {metadata.get("Score", "TBD")}\n')
            md_file.write(f'Dataset: "{metadata.get("DataSet", "")}"\n')
            md_file.write(f'keyword: [{metadata.get("Key word", "")}]\n')
            md_file.write(f'tags: [{metadata.get("Task", "")}]\n')
            md_file.write(f'DataType: [{metadata.get("Data type", "")}]\n')
            md_file.write(f"Data Region: [{metadata.get('Data Region', '')}]\n")
            md_file.write(f"Muti-central Data: [{metadata.get('Muti-central Data', '')}]\n")
            md_file.write(f"Mentioned: [{metadata.get('Mentioned', '')}]\n")
            md_file.write('---\n\n')
            
            keys_to_write = [
            "Tool used",
            "Accuracy on test",
            "Specificity on test",
            "Sensitivity on test",
            "AUC on test",
            "Limitation",
            "Output",
            "Method",
            "Pre-processing",
            "Limitation",
            "Number Of Patient",
            "Explainability",
            "Features selection",
            "Optimization",
            "Transfer learning",
            "list of features",
            "Multimodal",
            "list of features"]
            
            for key in keys_to_write:
                add_to_file_if_exist(md_file, metadata, key)
            
            if note == []:
                md_file.write("No note content available.\n")
            else:
                for line in note:
                    md_file.write(line)
            
        print("Markdown file 'my_document.md' created successfully.")
    
    except:
        print("Error creating markdown file.")
        raise

def add_author_to_file(file, author):
    author_str = "authors:"
    for author in author:
        author_str += f' {author.get("family", "")} {author.get("given", "")},'
    author_str = author_str.rstrip(',')
    file.write(f'{author_str}\n')
    
def add_to_file_if_exist(file, metadata, key):
    if metadata.get(key) != None:
        file.write(f'{key}: {metadata.get(key)}\n')
        
def get_type_of_reference(matrial, metadata):
    if matrial.get("container-title"):
        return matrial.get("container-title")
    if metadata.get("Type"):
        return metadata.get("Type")
    return "Unknown"

def get_type_of_year(matrial):
    #matrial["issued"]["date-parts"][0][0]
    if matrial.get("issued"):
        return matrial["issued"]["date-parts"][0][0]
    if matrial.get("volume"):
        return matrial.get("volume")
    return ""