from methods import *
from fileManager import *
def mainMenu(notes, path):
    
    inputUser = input("Введите команду: ")
    if inputUser.startswith("add"):
        addNote(notes, path)
        return True
    if inputUser.startswith("edit"):
        request = inputUser.partition(" ")
        if request[2] != "":
            editNote(notes, request[2], path)
            return True
        print("Повторите запрос")
        return True
    if inputUser.startswith("delete"):
        request = inputUser.partition(" ")
        if request[2] != "":
            deleteNote(notes, request[2], path)
            return True
        print("Повторите запрос")
        return True
    if inputUser.startswith("show"):
        request = inputUser.partition(" ")
        if request[2] != "":
            print(noteToString(findNote(notes, request[2])))
            return True
        else:
            showAll(notes)
            return True
    if inputUser.startswith("save"):
        request = inputUser.partition(" ")
        if request[2] != "":
            Counter.path = request[2] + ".csv"
        saveFile(notes, path)
        return True
    if inputUser.startswith("load"):
        request = inputUser.partition(" ")
        if request[2] != "":
            Counter.path = request[2] + ".csv"
        loadFile(notes, path)
        return True
    if inputUser.startswith("exit"):
        return False
    
    if inputUser.startswith("id"):
        print(Counter.index)
        return True