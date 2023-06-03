from datetime import datetime

def addNote(data):
    data.append({"id":1, 
                 "header": input("Введите заголовок: "), 
                 "body": input("Введите текст заметки: "), 
                 "date": datetime.now()})

def showAll(data):
    massage = ""
    for note in data:
        noteText = "{}\n{}|{}\n{}\n{}\n".format("-"*20, note["id"], note["date"], note["header"], note["body"])
        massage +=  noteText
    print(massage)