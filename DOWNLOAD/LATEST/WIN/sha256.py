import hashlib
phases = [1, 2, 3, 4, 5]

jsonString = '{\n'
for phase in phases:
    jsonString = jsonString + '"phase_%d": ' %phase + '"' + (hashlib.sha256(open("C:\lotaalpha\LOTA_GameData\phase_%d.zip" %phase, 'rb').read()).hexdigest()) + '",\n'
    
jsonString = jsonString[:-2] + '\n}'
print(jsonString)
