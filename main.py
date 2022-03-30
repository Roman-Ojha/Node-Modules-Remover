import os
import string


def findDir(fromDir):
    for roots, dirs, files in os.walk(fromDir):
        print(roots, len(dirs), len(files))
        print(dirs)


if __name__ == "__main__":
    folderToDelete = "node_modules"
    fromDir = string
    excludedDirNo = int
    excludedDirs = []
    fromDir = input(
        f"Enter Directory path from where you want to delete {folderToDelete} folder\n")
    # excludedDirNo = input(
    #     f"Enter how many Directory you wan to exclude to search to delete {folderToDelete} folder: ")
    # excludedDirNo = int(excludedDirNo)
    # for i in range(0, excludedDirNo, 1):
    #     excludedDir = input(f"Enter {i+1}th Directory you want to exclude\n")
    #     excludedDirs.append(excludedDir)
    isDirExist = os.path.exists(fromDir)
    if(isDirExist):
        findDir(fromDir)
    else:
        print("not exist")
