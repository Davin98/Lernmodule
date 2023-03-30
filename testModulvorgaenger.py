#1: Dummy-Tabelle erstellen
#2: vergleichswerte erstellen
#3:Vergleichswerte mit der aufgerufenen funktion vergleichen
from pathlib import Path
import TabelleAuslesen
import os
#1:

#tabelle wird erstellt und zeilen eingetragen
def appendtab(Nr,name,pos,dauer):
#("Tabelle.txt", "a+") Öffnet eine .txt Datei, falls sie nicht vorhanden ist, wird diese vorher erstellt
    f = open("Tabelle.txt", "a+")
    f.write(Nr + "\t" + name + "\t" + pos + "\t" + dauer + "\n")
    f.close

#die Variable f hat den pfad zur Tabelle.txt
f = Path("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")
#ist die Tabelle bereits im pfad so wird diese gelöscht
if f.is_file():
#die Datei "Tabelle.txt" wird gelöscht
    os.remove("Tabelle.txt")  
#in der Datei Tabelle.txt werden die folgenden zeilen eingetragen  
appendtab("1","Git","2,3,4","20")
appendtab("2","Py","0","5")
appendtab("3","Sps","4","30")
appendtab("4","C++","0","40")

Tabelle1 = TabelleAuslesen.Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")

#2:
Modul1 = "1\tGit\t2,3,4\t20\t[0]\t20"
Modul2 = "2\tPy\t0\t5\t1\t25"
Modul3 = "3\tSps\t4\t30\t1\t50"
Modul4 = "4\tC++\t0\t40\t31\t90"

Tabelle1.appendvorgaenger()

#test
#print(Tabelle1.setvorgaenger())

#3:
# i = 0
# while i < 4:
#     print(Tabelle1.inhaltget(i)) 
#     i = i + 1  
    
i = 0
while i < 4:
    match i:
        case 0:
            if (Tabelle1.inhaltget(i) == Modul1):
                print(Tabelle1.inhaltget(i))
                print("Test " + str(i) + " bestanden")
                i = 1
            else:
                print(Tabelle1.inhaltget(i))
                print("nicht bestanden")
                break
        case 1:
            if (Tabelle1.inhaltget(i) == Modul2):
                print(Tabelle1.inhaltget(i))
                print("Test " + str(i) + " bestanden")
                i = 2
            else:
                print(Tabelle1.inhaltget(i))
                print("nicht bestanden")
                break
        case 2:
            if (Tabelle1.inhaltget(i) == Modul3):
                print(Tabelle1.inhaltget(i))
                print("Test " + str(i) + " bestanden")
                print("Test bestanden")
                i = 3
                
            else:
                print(Tabelle1.inhaltget(i))
                print("nicht bestanden")
                break
        case 3:
            if (Tabelle1.inhaltget(i) == Modul4):
                print(Tabelle1.inhaltget(i))
                print("Test " + str(i) + " bestanden")
                print("Test bestanden")
                i = 3
                
            else:
                print(Tabelle1.inhaltget(i))
                print("nicht bestanden")
                break
os.remove("Tabelle.txt")
#print(Tabelle1.inhaltget(1))
