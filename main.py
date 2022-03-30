import os
import string


if __name__ == "__main__":
    folderToDelete = "node_modules"
    fromDir = string
    excludedDirNo = int
    excludedDirs = []
    fromDir = input(
        f"Enter Directory path from where you want to delete {folderToDelete} folder\n")
    excludedDirNo = input(
        f"Enter how many Directory you wan to exclude to search to delete {folderToDelete} folder: ")
    excludedDirNo = int(excludedDirNo)
    for i in range(0, excludedDirNo, 1):
        excludedDir = input(f"Enter {i+1}th Directory you want to exclude\n")
        excludedDirs.append(excludedDir)
