from datetime import datetime
from fileManager import *
from counter import Counter
def addNote(data, path):
    Counter.index += 1
    data.append({"id" : Counter.index, 
                 "header" : input("Введите заголовок: "), 
                 "body" : input("Введите текст заметки: "), 
                 "date" : datetime.now()})
    saveFile(data, path)

def noteToString(note): return "{}\n{}|{}\n{}\n{}\n".format("-"*20, note["id"], note["date"], note["header"], note["body"])

def findNote(data, param):
    if isinstance(param, int):
        for note in data:
            if note["id"] == param:
                return note
    if isinstance(param, str):
        for note in data:
            if note["header"] == param:
                return note 
    print("Нет такой записи!")
    return False

def showAll(data):
    massage = ""
    for note in data:
        noteText = noteToString(note)
        massage +=  noteText
    print(massage)

def deleteNote(data, param, path):
    note = findNote(data, param)
    if not note: return
    print("Запись \"" + str(note["header"]) + "\" удалена")
    data.remove(note)            
    saveFile(data, path)

def editNote(data, param, path):
    note = findNote(data, param)
    if not note: return
    check = 0
    inputUser = input("Введите заголловок: ")
    if inputUser != "":
        note["header"] = inputUser
    else: check += 1
    inputUser = input("Введите текст заметки: ")
    if inputUser != "":
        note["body"] = inputUser
    else: check += 1
    if check < 2: 
        note["date"] = datetime.now()
        print("Запись \"" + str(note["header"]) + "\" измененна")            
        saveFile(data, path)