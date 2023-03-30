#in diesem programm sollen die Zeilen aus der Datei "Tabelle.txt" ausgelesen werden.
from pathlib import Path
import os
#Die Klasse soll die Lernmodulsammlung in Variablen konvertieren/ Klassenkürzel LM
class Lernmodul:
    Nr = int()
    Name = str(" ")
    nachgaenger = int()
    dauer = int()
    vorgaenger = int()
#objekt Modul aus der Klasse Lernmodul
    def __init__(self, Nr, Name, nachgaenger, dauer):
        self.Nr = Nr
        self.Name = Name
        self.nachgaenger = nachgaenger
        self.dauer = dauer
        #Print zeile zum Visualisieren der Module
    def inhaltprint(self):
        print(self.Nr, self.Name, self.nachgaenger, self.dauer)
    def listeursprung(self):
        return (str(self.Nr) + "\t" + self.Name + "\t" + self.nachgaenger + "\t" + str(self.dauer))
    def inhaltget(self):
        return (str(self.Nr) + "\t" + self.Name + "\t" + self.nachgaenger + "\t" + str(self.dauer) + "\t" + str(self.vorgaenger))
        #gibt den wert "self.nachgaenger" auf abfrage aus
    def getnachgaenger(self):
        return self.nachgaenger
        #setzt den Wert "self.vorgaenger" auf abfrage
    def setvorgaenger(self,vorgaenger):
        self.vorgaenger = vorgaenger
        #gibt den wert "self.Nr" auf abfrage aus
    def getNr(self):
        return self.Nr
        #gibt den wert "self.dauer" auf abfrage aus
    def getdauer(self):
        return self.dauer
        #gibt den wert "self.vorgaenger" auf abfrage aus
    def getvorgaenger(self):
        return self.vorgaenger
    
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
            self.setvorgaenger()

    def Modulzeile(self,n):
        z = 0
        for y in self.ListeLM:
            
            if int(n) == y.getNr():

                return z
            z = z + 1
        return False
        #in der schleife wird der Index zur Lernmodulnummer n wiedergegeben
    # def vorgaengerpruefung(self,n):
    #     for y in self.ListeLM:
    #             if int(n) == y.getNr():
    #                 return True

    def inhaltprint(self):
        for i in self.ListeLM:
            i.inhaltprint()
    def inhaltget(self,pos):

        return self.ListeLM[pos].inhaltget()
    def listeursprung(self,pos):
        return self.ListeLM[pos].listeursprung()
    def setvorgaenger(self):
        #Erstellt eine Leere Liste Modulnachfolger
        Modulnachfolger =[]
        #Durchläuft jede Zeile der Tabelle.txt
        # for n in self.ListeLM:
            #füllt die Liste Modulnachfolger mit dem ergebnis aus der funktion getnachgaenger beispiel: Tabelle zeile 0 (1 Git n(2,3) 20)
            # Modulnachfolger.append(n.getnachgaenger())

        #Durchläuft jede Zeile der Tabelle.txt
        
        for i in self.ListeLM:
            
            #Durchläuft jeden wert in der Liste Modulnachfolger
            if len(str(i.getnachgaenger())) >= 2:
                for m in i.getnachgaenger():
                    m = m.strip(",")
                    #fragt ab, ob der Wert aus Modulnachfolger schon als Nr. vergeben ist 
                    #print("m= " + str(m) + "i.getNr= "+  str(i.getNr()) )
                    for n in m:
                        zeile = self.Modulzeile(n)
                        
                        #print("n= " + str(n) + "i.getNr= "+  str(i.getNr()) )
                        if type(zeile) ==int:
                        
                            
                        #ist dies der fall, so soll der Zeitwert des Moduls mit allen seinen vorgaengern addiert werden und in die Variable gespeichert werden.
                            self.ListeLM[zeile].setvorgaenger(i.getNr())
            else:
                n = i.getnachgaenger()    
                zeile = self.Modulzeile(n)
                
                #print("n= " + str(n) + "i.getNr= "+  str(i.getNr()) )
                if type(zeile) ==int:
                
                    
                #ist dies der fall, so soll der Zeitwert des Moduls mit allen seinen vorgaengern addiert werden und in die Variable gespeichert werden.
                    self.ListeLM[zeile].setvorgaenger(i.getNr())

                
             
    

            

        #Printet alle Module
        # for i in self.ListeLM:
        #    i.inhaltprint()
        # print(self.ListeLM)
        


# a = Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")
#test
#print (a.inhaltget(1))
# a.setvorgaenger()

