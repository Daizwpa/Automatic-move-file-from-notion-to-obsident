
import os
import argparse
from Core import move_file, AddYamlToFile, is_file_dotMD, get_title_in_file, Look_into_Json_for, DefineNewFullPath, get_metadata_in_md, readNoteContent, get_note_in_md


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            prog='Convert notion dataviwe to obisident ', description='Automatic convert dataviwe of notion to obisident Database folder', epilog='Text at the bottom of help')
        parser.add_argument("directory_path", help="Path of Directory that includes the notes")
        parser.add_argument("dic_path", help="better CEL JSON")

        args = parser.parse_args()
        directoryFile = args.directory_path
        json_path = args.dic_path
        files = os.listdir(directoryFile)
        not_found = []
        matrials = []
        for fname in files:

            if not is_file_dotMD(file_name=fname):
                continue
            
            md_file_path = os.path.join(directoryFile, fname)
            
            matrial_title = get_title_in_file(md_file_path)
            
            matrial = Look_into_Json_for(matrial_title, json_path)
            if matrial == None:
                not_found.append(matrial_title)
                continue

            md_file = readNoteContent(md_file_path)

            md_metadata = get_metadata_in_md(md_file)

            md_note = get_note_in_md(md_file)
            

        for name_files in not_found:
            print(name_files)
        print(len(not_found))
    except:
        print(matrial_title)
        raise

