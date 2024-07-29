import json, os

dir = os.path.join("parsed")
save_path = './parsed'

if not os.path.exists(dir):
    os.mkdir(dir)

def parse(filename):
    completeName = os.path.join(save_path, filename + ".txt")
    with open(filename, 'r', encoding = 'utf-8') as json_file:
        data = json.load(json_file)
    createFile = open(completeName, 'w', encoding = 'utf-8')      
    scnLength = (len(data['scenes']))
    for texts in range(scnLength):
        try:
        #    llnt = ""
            for i in range(len(data['scenes'][texts]['texts'])):
                scns = data['scenes'][texts]['texts'][i]
        #        for r in range(len(scns)):
        #            name = scns[r][0]
        #            name_jp = scns[r][1][0][0]
        #            name_en = scns[r][2][0][0]
        #            name_cn = scns[r][3][0][0]
        #            text_jp = scns[r][1][1][0]
        #            text_en = scns[r][2][1][0]
        #            text_cn = scns[r][3][1][0]
        #            oneline = (
        #                    f"name: {name}\n"
        #                    f"name_jp: {name_jp}\n"
        #                    f"text_jp: {text_jp}\n"
        #                    f"name_en: {name_en}\n"
        #                    f"text_en: {text_en}\n"
        #                    f"name_cn: {name_cn}\n"
        #                    f"text_cn: {text_cn}\n\n"
        #                )
        #            llnt += oneline
                createFile.write(str(scns) + "\n")
        except KeyError:
            pass


for filename in os.listdir():
    if filename.endswith('.ks.json'):
        parse(filename)
print("Finished!")


