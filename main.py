import os
from turtle import goto


def deleteFolder(path):
    wantToRemove = ""
    print(f"\nFolder Path: {path}")
    print("Do you Want to delete This folder?(Y/N)")
    while(True):
        wantToRemove = input()
        if wantToRemove == "Y" or wantToRemove == "y":
            print("Deleting Folder.....")
            # os.remove(path)
            print("Deleted Folder Successfully")
            return
        elif wantToRemove == "N" or wantToRemove == "n":
            return
        else:
            print("Please Type Y or N")


def findAndDeleteFolder(fromDir, folderToDelete, excludedDirs):
    allDeletedDirectory = []
    for roots, dirs, files in os.walk(fromDir):
        for i in range(0, len(dirs), 1):
            if(dirs[i] == folderToDelete):
                # checking if the current directory is 'folderToDelete'
                iterativeDir = os.path.join(
                    roots, dirs[i])
                # joining directory with root directory to find the full path of that directory
                splitDir = os.path.join(
                    iterativeDir.split(folderToDelete)[0], folderToDelete)
                if splitDir not in allDeletedDirectory:
                    # check if iterative Directory is excluded Directory
                    folderPath = os.path.join(
                        iterativeDir.split(folderToDelete)[0], folderToDelete)
                    if len(excludedDirs) == 0:
                        # Deleting folder
                        deleteFolder(folderPath)
                        allDeletedDirectory.append(folderPath)
                    else:
                        for i in range(0, len(excludedDirs), 1):
                            if excludedDirs[i] not in splitDir:
                                # Deleting Folder
                                deleteFolder(folderPath)
                                allDeletedDirectory.append(folderPath)


if __name__ == "__main__":
    folderToDelete = "node_modules"
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
    findAndDeleteFolder(fromDir, folderToDelete, excludedDirs)
