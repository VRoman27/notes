from methods import *
from fileManager import *
def mainMenu(notes, path):
    
    inputUser = input("Введите команду: ")
    if inputUser == "add":
        addNote(notes, path)
        return True
    if inputUser == "show":
        showAll(notes)
        return True
    if inputUser == "edit":
        return True
    if inputUser == "delete":
        deleteNote(notes, int(input("Введите id заметки: ")), path)
        return True
    if inputUser == "find":
        return True
    if inputUser == "save":
        saveFile(notes, path)
        return True
    if inputUser == "exit":
        return False