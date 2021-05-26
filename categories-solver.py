#!/usr/bin/python3

from pathlib  import Path 

import os

path = Path(".").resolve()

for file in path.glob("**/*.md"):
    flag = 0
    trigger = 0
    content = ""
    catego = ""
    with open(file, 'r') as f:
        
        for line in f.readlines():
            if line.startswith("---"):                
                flag = 1 - flag
            elif flag and line.startswith("tags"):
                trigger = 1
            elif trigger and line.strip().startswith("-"):
                catego = line.strip(" -")
                line = ""
                trigger = 0
            content += line
    
    newpath = path.parent / "temp" / catego 
    newpath.mkdir(mode=0o777, parents=True, exist_ok=True)
    with open(newpath / file.name, "w") as f:
        f.write(content)
        print(file.name + " is written to " + str(newpath.resolve()))