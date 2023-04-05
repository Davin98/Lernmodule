#In diesem Test werden die Modulzeiten der abgeschlossenen Module von der Gesamtzeit abgezogen
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
appendtab("1","Git","2,3,4,16,20","20")
appendtab("2","Py","0","5")
appendtab("3","Sps","4","30")
appendtab("4","C++","0","40")
appendtab("5","Git-Intermediate","20","100")
appendtab("6","Git-Masterclass","0","1000")

Tabelle1 = TabelleAuslesen.Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")

#2:
Modul1 = 20
Modul2 = 25
Modul3 = 30
Modul4 = 40 + Modul3 + Modul1 - Modul1 #Zeiten Modul4 + Modul3 + Modul1 - Modul1
Modul5 = 100 - Modul4 + Modul1#Zeiten Modul5 + Modul3 + Modul1 - Modul1
Modul6 = 1000

#Tabelle1.appendvorgaenger()
print(Tabelle1.abzuziehende_zeiten(4,6))

i = 0
n = 1
    #print(Tabelle1.abzuziehnde_zeiten(i,n))  
    
i = 0
while i < 6:
    match i:
        case 0:
            if (Tabelle1.abzuziehende_zeiten(i,n) == Modul1):
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("Test " + str(i) + " bestanden")
                i = 1
                n = 2
            else:
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("nicht bestanden")
                break
        case 1:
            if (Tabelle1.abzuziehende_zeiten(i,n) == Modul2):
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("Test " + str(i) + " bestanden")
                i = 2
                n = 3
            else:
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("nicht bestanden")
                break
        case 2:
            if (Tabelle1.abzuziehende_zeiten(i,n) == Modul3):
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("Test " + str(i) + " bestanden")
                i = 3
                n = 4
            else:
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("nicht bestanden")
                break
        case 3:
            if (Tabelle1.abzuziehende_zeiten(i,n) == Modul4):
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("Test " + str(i) + " bestanden")
                i = 4
                n = 5
            else:
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("nicht bestanden")
                break
        case 4:
            if (Tabelle1.abzuziehende_zeiten(i,n) == Modul5):
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("Test " + str(i) + " bestanden")
                i=5
                n = 6
            else:
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("nicht bestanden")
                break
        case 5:
            if (Tabelle1.abzuziehende_zeiten(i,n) == Modul6):
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("Test " + str(i) + " bestanden")
                print("Test bestanden")
                i=6
                n = 6
            else:
                print(Tabelle1.abzuziehende_zeiten(i,n))
                print("nicht bestanden")
                break
os.remove("Tabelle.txt")
#print(Tabelle1.inhaltget(1))