#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RANJEET
#
# Created:     22-08-2022
# Copyright:   (c) RANJEET 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
def foundtext(filename):
    f = open(filename, "r")
    filecontent = f.read()
    if f"{text}" in filecontent.lower():
        return True
    else:
        return False
if __name__ == "__main__":
    text=input("Enter any word  = ")
    dir_content = os.listdir()
    #print(dir_content)
    ntext= 0
    for item in dir_content:
        if item.endswith("txt"):
            print(f"Detecting {text} in {item}")
            flag = foundtext(item)
            if (flag):
                print(f"*******{text} found in {item}**********")
                nBinod +=1
        else:
            print(f"{text} not found in {item}")
    print("*********Text Detector Summary********")
    print(f"{ntext} files found with {text} into them")