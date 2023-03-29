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
appendtab("1","Git","2,3","20")
appendtab("2","Py","0","5")
appendtab("3","Sps","0","30")

Tabelle1 = TabelleAuslesen.Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")

#2:
Modul1 = 0
Modul2 = 1
Modul3 = 1

Tabelle1.setvorgaenger()

#test
#print(Tabelle1.setvorgaenger())

#3:

    
    
i = 0
while i < 3:
    match i:
        case 0:
            if (Tabelle1.setvorgaenger() == Modul1):
                print("Test " + str(i) + " bestanden")
                i = 1
            else:
                print("nicht bestanden")
                break
        case 1:
            if (Tabelle1.setvorgaenger() == Modul2):
                print("Test " + str(i) + " bestanden")
                i = 2
            else:
                print("nicht bestanden")
                break
        case 2:
            if (Tabelle1.setvorgaenger() == Modul3):
                print("Test " + str(i) + " bestanden")
                print("Test bestanden")
                i = 3
            else:
                print("nicht bestanden")
                break


os.remove("Tabelle.txt")
print(Tabelle1.inhaltget(1))
