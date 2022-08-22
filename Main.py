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
def foundasin(filename):
    f = open(filename, "r")
    filecontent = f.read()
    if f"{asin}" in filecontent.lower():
        return True
    else:
        return False
if __name__ == "__main__":
    asin=input("Enter ASIN  = ")
    dir_content = os.listdir()
    #print(dir_content)
    nASIN= 0
    for item in dir_content:
        if item.endswith('xlsx'):
            print(f"Detecting ASIN in {item}")
            flag = foundasin(item)
            if (flag):
                print(f"*******ASIN found in {item}**********")
                nBinod +=1
        else:
            print(f"ASIN not found in {item}")
    print("*********ASIN Detector Summary********")
    print(f"{nASIN} files found with {asin} into them")