# create an array of known extensions

import os
import shutil
import pathlib

known_extensions = []

for ext in known_extensions:
    print(ext)

pwd = os.getcwd()
# loop over the folders

print(pwd)
#input()

def remove_empty_dir(path):
    try:
        os.rmdir(path)
    except OSError:
        pass

def remove_empty_dirs(path):
    for root, dirnames, filenames in os.walk(path, topdown=False):
        for dirname in dirnames:
            remove_empty_dir(os.path.realpath(os.path.join(root, dirname)))

for subdir, dirs, files in os.walk(pwd):
    n_files = 0 
    for file in files:
        n_files = n_files + 1
        if file == "organizer.py":
            print("found script, skipping")
            continue
        source = os.path.join(subdir, file)
        file_extension = pathlib.Path(source).suffix
        file_extension = file_extension.replace(".", "")
        if file_extension in known_extensions:
            pass
        else:
            known_extensions.append(file_extension)
            pathlib.Path(os.path.join(pwd, file_extension)).mkdir(exist_ok=True)
            
        if file_extension == "":
            print(source, "file has no extension")
            pathlib.Path(os.path.join(pwd, "no_extension")).mkdir(exist_ok=True)
            destination = os.path.join(pwd, "no_extension", file)
        else:
            destination = os.path.join(pwd, file_extension, file)
        print(file_extension)
        print(source)
        print(destination)

        shutil.move(source, destination) 

    #print(f" {subdir} has {n_files} files ")

remove_empty_dirs(pwd)

print(known_extensions)
