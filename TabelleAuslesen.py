#in diesem programm sollen die Zeilen aus der Datei "Tabelle.txt" ausgelesen werden.
from pathlib import Path
import os
#Die Klasse soll die Lernmodulsammlung in Variablen konvertieren/ Klassenkürzel LM
class Lernmodul:
    Nr = int()
    Name = str(" ")
    nachgaenger = int()
    dauer = int()
    modulzeiten = int()
    
#objekt Modul aus der Klasse Lernmodul
    def __init__(self, Nr, Name, nachgaenger, dauer):
        self.Nr = Nr
        self.Name = Name
        self.nachgaenger = nachgaenger
        self.dauer = dauer
        self.vorgaenger = []

        #Print zeile zum Visualisieren der Module
    def inhaltprint(self):
        print(self.Nr, self.Name, self.nachgaenger, self.dauer)
    def listeursprung(self):
        return (str(self.Nr) + "\t" + self.Name + "\t" + self.nachgaenger + "\t" + str(self.dauer))
    def inhaltget(self):
        return (str(self.Nr) + "\t" + self.Name + "\t" + self.nachgaenger + "\t" + str(self.dauer) + "\t" + ",".join(map(str,self.vorgaenger)) + "\t" + str(self.modulzeiten))
        #gibt den wert "self.nachgaenger" auf abfrage aus
    def getnachgaenger(self):
        return self.nachgaenger
        #setzt den Wert "self.vorgaenger" auf abfrage
    def appendvorgaenger(self,vorgaenger):
        
            self.vorgaenger.append(vorgaenger)
            
        #gibt den wert "self.Nr" auf abfrage aus
    def getNr(self):
        return self.Nr
        #gibt den wert "self.dauer" auf abfrage aus
    def getdauer(self):
        return self.dauer
        #gibt den wert "self.vorgaenger" auf abfrage aus
    def getvorgaenger(self):
        return self.vorgaenger
    def setmodulzeiten(self, modulzeiten):
        self.modulzeiten = modulzeiten
    def getmodulzeiten(self):
         return self.modulzeiten
    
    
#die Klasse soll den Inhalt der Tabelle.txt in Variablen konvertieren/ Klassenkürzel LMS
class Lernmodulsammlung:

    ListeLM = []
    def __init__(self,path):
        #Problem: die .txt datei wird nicht erzeugt, sodass ein Error erscheint
        f = Path(path)
        if f.is_file():
            f = open(path, "r")
#in der schleife sollen die Zeilen aus der Tabelle.txt importiert und in die Variablen geschrieben werden        
            for i in f.readlines():
                n = i.strip().split('\t')
            ##Test um die bearbeitete Tabelle zu printen
            #print(n)
            
                Nr = int(n[0])
                Name = n[1]
                nachgaenger = n[2]
                dauer = int(n[3])
            ##Test print um zu gucken, ob die tabelle richtig gesplitted wird
            #print(Nr, Name, nachgaenger, dauer)
            ##Aufrufen der Klasse Lernmodul und hängt die Daten an der Liste an

                self.ListeLM.append(Lernmodul(Nr, Name, nachgaenger, dauer))
        #f.close schließt die Datei wieder
            f.close
            self.appendvorgaenger()
            self.setmodulzeiten()

    def Modulzeile(self,Zeilen):
        z = 0
        for y in self.ListeLM:
            
            if int(Zeilen) == y.getNr():

                return z
            z = z + 1
        return False
        #in der schleife wird der Index zur Lernmodulnummer n wiedergegeben
    

    # die funktion führt die funktion "inhaltprint" für jede zeile "i" in der funktion ListeLM aus
    def inhaltprint(self):
        for i in self.ListeLM:
            i.inhaltprint()
    def inhaltget(self,pos):

        return self.ListeLM[pos].inhaltget()
    def listeursprung(self,pos):
        return self.ListeLM[pos].listeursprung()
    def appendvorgaenger(self):

        #Durchläuft jede Zeile der Tabelle.txt
        
        for i in self.ListeLM:
            
            #fragt ab ob der rückgabewert länger ist als 2 spalten
            if len(str(i.getnachgaenger())) >= 2:

                a = i.getnachgaenger().split(",")
                #durchläuft jede spalte die in der aktuellen .getnachgaenger funtkion übergeben wurde
                for m in a:
                    #löscht die kommas, wenn das modul mehrere nachgaenger hat und speichert m als liste
                    #geht jede stelle in m durch
                    # for n in m:
                        #speichert das ergebnis der funktion Modulzeile in die variable "zeile"
                        zeile = self.Modulzeile(m)
                        
                        #wenn variable "zeile" vom typ int dann soll das ergebnis der Funktion setvorgaenger mit dem wert getNr aus der aktuellen zeile in die zeile der Tabelle eingetragen werden
                        if type(zeile) ==int:
                        #zählt innerhalb der zeile "zeile" in ListeLM wie oft der wert aus "getNr" in der Zeile vorkommt.
                            if self.ListeLM[zeile].vorgaenger.count(i.getNr()) == 0:
                                #wenn "getNr" nicht vorgekommen ist, wird er in die liste "appendvorgaenger" für die aktuelle Zeile eingetragen

                                self.ListeLM[zeile].appendvorgaenger(i.getNr())
            # ist das ergebnis aus getnachgaenger der Tabellenzeile "i" einstellig, so soll das ergebnis in die Variable "n" gespeichert werden
            else:
                n = i.getnachgaenger()    
                #das ergebnis der Funktion Modulzeile mit dem wert "n" wird in die variable "zeile" gespeichert
                zeile = self.Modulzeile(n)
                
                
                if type(zeile) ==int:
                
                    if self.ListeLM[zeile].vorgaenger.count(i.getNr()) == 0:
            
                        self.ListeLM[zeile].appendvorgaenger(i.getNr())
            if len(i.getvorgaenger()) == 0:
                i.appendvorgaenger(0)
                
                

    def setmodulzeiten(self):
        

        for i in self.ListeLM:
            spalte = 0
            komulierte_zeiten = i.getdauer()
            if i.getvorgaenger()[0] != 0:
                for n in i.getvorgaenger():
                    komulierte_zeiten = komulierte_zeiten + self.ListeLM[self.Modulzeile(i.getvorgaenger()[spalte])].getdauer() 
                    spalte =+1
                i.setmodulzeiten(komulierte_zeiten)
            else:
                i.setmodulzeiten(i.getdauer())
            
                
# a = Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")
#test
#print (a.inhaltget(1))
# a.setvorgaenger()

