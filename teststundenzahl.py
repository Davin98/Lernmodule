#1: die in korelation zueinander bringen
#2: abfrage ob in den lernmodulen ein vorgaenger existiert
#3: vorfolger richtig benennen
from pathlib import Path
import TabelleAuslesen
import os

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

tabelle1 = TabelleAuslesen.Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")

#1:

def korelation(self,path):
    
#jetzt soll die nachgaenger Variable so interpretiert werden, dass die Ziffern verweise auf die nachfolgenden Pos darstellen
    nachgaenger = tabelle1(2)
    Variablenachgaenger = nachgaenger.strip(',')
    print(Variablenachgaenger)

#als nächstes sollen den Modulen die vorgänger module zugeordnet werden
       
#wenn die Variable z.B. 3 eingegeben wird soll die Dauer für Modul 3 + alle vorherigen Module im Didaktischen flow ausgegeben werden. (Modul 3 = 30 + Modul 1 = 20 == 50std aufwand)


os.remove("Tabelle.txt")