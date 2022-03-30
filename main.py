import os
import string
from turtle import goto


def findDir(fromDir, folderToDelete, excludedDirs):
    allDirToDelete = []
    for roots, dirs, files in os.walk(fromDir):
        for i in range(0, len(dirs), 1):
            if(dirs[i] == folderToDelete):
                # checking if the current directory is 'folderToDelete'
                iterativeDir = os.path.join(
                    roots, dirs[i])
                # joining directory with root directory to find the full path of that directory
                splitDir = os.path.join(
                    iterativeDir.split(folderToDelete)[0], folderToDelete)
                if splitDir not in allDirToDelete:
                    # check if iterative Directory is excluded Directory
                    if len(excludedDirs) == 0:
                        allDirToDelete.append(os.path.join(
                            iterativeDir.split(folderToDelete)[0], folderToDelete))
                    else:
                        for i in range(0, len(excludedDirs), 1):
                            if excludedDirs[i] not in splitDir:
                                allDirToDelete.append(os.path.join(
                                    iterativeDir.split(folderToDelete)[0], folderToDelete))
    print(allDirToDelete)


if __name__ == "__main__":
    folderToDelete = "node_modules"
    fromDir = string
    excludedDirNo = int
    excludedDirs = []
    print(f"=============== {folderToDelete} Remover ===============")
    fromDir = input("Starting Directory to search: ")
    if os.path.exists(fromDir) is not True:
        print("Starting Directory doesn't exist")
        print("Please Try Again.....")
        exit()
    excludedDirNo = int(input(
        f"Number of Directory to exclude: "))
    for i in range(0, excludedDirNo, 1):
        excludedDir = input(f"Enter {i+1}th Directory to exclude: ")
        if(os.path.exists(excludedDir)):
            excludedDirs.append(excludedDir)
        else:
            print("Give excluded Directory doesn't exist")
            print("Please Try Again.....")
    isDir = os.path.exists(fromDir)
    findDir(fromDir, folderToDelete, excludedDirs)
