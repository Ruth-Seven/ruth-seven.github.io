#!/usr/bin/python3

from pathlib  import Path 

import os

path = Path(".").resolve()

# 删除所有md文件的categoriesw
for file in path.glob("**/*.md"):
    flag = 0
    trigger = 0
    content = ""
    catego = ""
    with open(file, 'r') as f:
        
        for line in f.readlines():
            if line.startswith("categories"):                
                flag = 1
            elif flag:
                if line.strip().startswith("-"):
                    trigger = 1
                    line = ""
                else:
                    flag = 0
            content += line
            
    with open(file, "w") as f:
        f.write(content)
        print(file.name + " is written to " + str(file.resolve()))