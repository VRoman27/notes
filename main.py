from interface import mainMenu
from fileManager import *

notes = list()
path = "file.csv"
loadFile(notes, path)
while(mainMenu(notes, path)):pass
