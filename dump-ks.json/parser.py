import json, os

dir = os.path.join("parsed")
save_path = './parsed'

if not os.path.exists(dir):
    os.mkdir(dir)

def process(text):
    
    name0 = str(text[0])

    name1 = str(text[1][0][0])
    if name1 == "None":
        name1 = str(text[0])
    stc1 = str(text[1][0][1])

    name2 = str(text[1][1][0])
    if name2 == "None":
        name2 = str(text[0])
    stc2 = str(text[1][1][1])

    name3 = str(text[1][2][0])
    if name3 == "None":
        name3 = str(text[0])
    stc3 = str(text[1][2][1])

    return name0 + '\n' + name1 + " : " + stc1+'\n' + name2+ " : " + stc2+'\n' + name3 + " : " + stc3 + '\n'

def parse(filename):
    baseName = os.path.splitext(os.path.splitext(filename)[0])[0]
    completeName = os.path.join(save_path, baseName + ".txt")
    with open(filename, 'r', encoding = 'utf-8') as json_file:
        data = json.load(json_file)
    createFile = open(completeName, 'w', encoding = 'utf-8')      
    scnLength = (len(data['scenes']))
    for texts in range(scnLength):
        try:
            for i in range(len(data['scenes'][texts]['texts'])):
                scns = data['scenes'][texts]['texts'][i]
                rslt = process(scns)
                createFile.write(rslt + "\n")
        except KeyError:
            pass


for filename in os.listdir():
    if filename.endswith('.ks.json'):
        parse(filename)
print("Finished!")


