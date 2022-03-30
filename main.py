import os
import string


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
    excludedDirNo = int(input(
        f"Number of Directory to exclude: "))
    for i in range(0, excludedDirNo, 1):
        excludedDir = input(f"Enter {i+1}th Directory to exclude\n")
        excludedDirs.append(excludedDir)
    isDir = os.path.exists(fromDir)
    if(isDir):
        findDir(fromDir, folderToDelete, excludedDirs)
    else:
        print("not exist")
