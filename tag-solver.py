#!/usr/bin/python3

from pathlib import Path

# path = Path(".")  # 路径需要修正

for file in path.glob("./*.md"):
    content = ""
    flag = 0 
    with open(file) as f:
        for line in f.readlines():
            if line.strip().startswith("---"):
                flag = 1 - flag
            elif flag and line.strip(" ").startswith("-"):
                line = " - " + "".join(line.strip(" -"))
            
            content += line
    
    with open(file, 'w') as f:
        f.write(content)
        print(file, "got it!")
    
        
