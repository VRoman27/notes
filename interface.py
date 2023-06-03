from methods import *
def mainMenu(notes):
    inputUser = input("Введите команду: ")
    if inputUser == "add":
        addNote(notes)
        return True
    if inputUser == "show":
        showAll(notes)
        return True
    if inputUser == "edit":
        return True
    if inputUser == "delete":
        return True
    if inputUser == "find":
        return True
    if inputUser == "save":
        return True
    if inputUser == "exit":
        return False