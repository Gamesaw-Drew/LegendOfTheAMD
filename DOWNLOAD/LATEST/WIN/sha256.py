import hashlib
import os
jsonString = '{\n"data": ['
rootDir = 'D:\Users\Drew\Documents\LegendofAMDSite\DOWNLOAD\LATEST\WIN\gamedata'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        jsonString = jsonString + '{"Filename": "%s", "sha256" : "%s"},\n' %(("%s\\%s" %(dirName.replace("D:\\Users\\Drew\\Documents\\LegendofAMDSite\\DOWNLOAD\\LATEST\\WIN\\", ""), fname)), hashlib.sha256(open("%s" %"%s\\%s" %(dirName, fname), 'rb').read()).hexdigest())
    
jsonString = jsonString[:-2] + '\n]}'
print(jsonString)
