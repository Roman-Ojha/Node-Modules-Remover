import os
import string


def findDir(fromDir, folderToDelete):
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
                    allDirToDelete.append(os.path.join(
                        iterativeDir.split(folderToDelete)[0], folderToDelete))
    print(allDirToDelete)


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
    isDir = os.path.exists(fromDir)
    if(isDir):
        findDir(fromDir, folderToDelete)
    else:
        print("not exist")
