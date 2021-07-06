import os
import pandas as pd

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = []
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)          
    return allFiles

def getAllFiles(allFiles):
    dirs = list()
    fileNames = list()
    exts = list()
    for i in range(len(allFiles)):
        path = allFiles[i].split('\\')
        file = path[-1]
        fileName, ext = file.split(".")
        dir = path[-2]
        dirs.append(dir)
        fileNames.append(fileName)
        exts.append(ext)
        print(ext)
    return dirs,fileNames,exts

currentDir  = os.getcwd()
allFiles = getListOfFiles(currentDir)
getAllFiles(allFiles)
rootDirectories, fileNames, exts = getAllFiles(allFiles)

data = {"rootDirectory": rootDirectories, "fileName": fileNames, "extension": exts}
df = pd.DataFrame(data= data)
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()