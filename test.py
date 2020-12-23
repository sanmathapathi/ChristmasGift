import os
import shutil

dst = "/Users/sannathmathapathi/Documents/"

global datafile

def createCategory():
    datafile = open("categories.txt", "a")

    tag = input("Category Tag (no spaces in tag itself!): ")
    updated_dst = input("Destination Folder:")

    datafile.write(tag + " " + updated_dst)

    datafile.close()
    print("Category Created")

def sort():
    src = "/Users/sannathmathapathi/Documents/"
    datafile = open("categories.txt", "r")
    with open("categories.txt", "r") as datafile:
        for line in datafile:
            if line == "\n":
                pass
            else:
                stats = line.split()
                tag = stats[0]
                updated_dst = stats[1]
                for file in os.listdir("/Users/sannathmathapathi/Documents/"):
                    if file.startswith(tag):
                        print(dst)
                        print(dst + updated_dst)
                        print()

                        src += file
                        shutil.move(src, dst + updated_dst)
                        src = "/Users/sannathmathapathi/Documents/"

    print("Process Completed")

start = input("Create new category or sort? (C/S)")

if start == "c" or start == "C":
    createCategory()

elif start == "s" or start == "S":
    sort()
