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

def showAll(data):
    massage = ""
    for note in data:
        noteText = "{}\n{}|{}\n{}\n{}\n".format("-"*20, note["id"], note["date"], note["header"], note["body"])
        massage +=  noteText
    print(massage)

def deleteNote(data, index, path):
    for note in data:
        if note["id"] == index:
            data.remove(note)
            return
    saveFile(data, path)

