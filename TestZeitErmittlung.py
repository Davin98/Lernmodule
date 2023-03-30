#In diesem Test sollen anhand der vorgaengerreihe die gesamt lernzeit der Module errechnet werden
#1: Erstellen der Dummy-tabelle
#2: aufrufen der Tabellen funktion
#3: vergleichen der Rückgabewerte mit den Erwartungswerten
from pathlib import Path
import os
import TabelleAuslesen
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
appendtab("1","Git","2,3","20")
appendtab("2","Py","0","5")
appendtab("3","Sps","0","30")

#2:
Tabelle1 = TabelleAuslesen.Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")
#test




#3:

Modul1 = "1\tGit\t2,3\t20\t0\t20"
Modul2 = "2\tPy\t0\t5\t1\t25"
Modul3 = "3\tSps\t0\t30\t1\t50"


i = 0
while i < 3:
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

os.remove("Tabelle.txt")
#print(Tabelle1.inhaltget(1))
