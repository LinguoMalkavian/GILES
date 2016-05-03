import os
import glob
## added random
import random

def readFiles():
    mainChars = ["BUFFY", "WILLOW", "XANDER", "GILES"]

    all_tagged_lines = []
    for char in mainChars:
        path = "Data/%s" %(char)
        for filename in glob.glob(os.path.join(path, "*.txt")):
            getfile = open(filename, "r")
            script = getfile.read()
            if len(script)>0:
                all_tagged_lines.append((char,script))
            getfile.close()
   ## return (all_tagged_lines)
    random.shuffle(all_tagged_lines)
    return all_tagged_lines
