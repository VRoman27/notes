from interface import mainMenu
from fileManager import *

notes = list()
loadFile(notes, "file.csv")
while(mainMenu(notes)):pass
