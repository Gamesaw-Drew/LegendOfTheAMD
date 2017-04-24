import hashlib
phases = [1, 2, 3, 4, 5]

jsonString = '{\n"data": ['
for phase in phases:
    jsonString = jsonString + '{"Filename": "phase_%d", "sha256" : "%s"},\n' %(phase, hashlib.sha256(open("phase_%d.zip" %phase, 'rb').read()).hexdigest())
    
jsonString = jsonString[:-2] + '\n]}'
print(jsonString)
