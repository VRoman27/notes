def saveFile(data, path):
    tmp = list()
    for item in data:
        tmp.append(";".join(str(x) for x in item.values()) )
    text = "\n".join(tmp)
    with open(path, "w") as file:
        file.write(text)

def loadFile(data, path):
    tmp = list()
    with open(path, "r") as file:
        for line in file:
            tmp.append(line.replace("\n", "").split(";"))
    for item in tmp:
        data.append({"id" : item[0], 
                     "header" : item[1], 
                     "body" : item[2],
                     "date" : item[3]})
