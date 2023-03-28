#in diesem programm sollen die Zeilen aus der Datei "Tabelle.txt" ausgelesen werden.

#Die Klasse soll die Lernmodulsammlung in Variablen konvertieren/ Klassenkürzel LM
class Lernmodul:
    Nr = int()
    Name = str(" ")
    nachgaenger = int()
    dauer = int()
#objekt Modul aus der Klasse Lernmodul
    def __init__(self, Nr, Name, nachgaenger, dauer):
        self.Nr = Nr
        self.Name = Name
        self.nachgaenger = nachgaenger
        self.dauer = dauer
        #Print zeile zum Visualisieren der Module
    def inhaltprint(self):
        print(self.Nr, self.Name, self.nachgaenger, self.dauer)
    def inhaltget(self):
        return (str(self.Nr) + "\t" + self.Name + "\t" + self.nachgaenger + "\t" + str(self.dauer))
   
    
    
#die Klasse soll den Inhalt der Tabelle.txt in Variablen konvertieren/ Klassenkürzel LMS
class Lernmodulsammlung:

    ListeLM = []
    def __init__(self,path):
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
    def inhaltprint(self):
        for i in self.ListeLM:
            i.inhaltprint()
    def inhaltget(self,pos):

        return self.ListeLM[pos].inhaltget()

        
        #(str(self.Nr) + "\t" + self.Name + "\t" + self.nachgaenger + "\t" + str(self.dauer))
        

        
            
        
        #Printet alle Module
        # for i in self.ListeLM:
        #    i.inhaltprint()
        # print(self.ListeLM)
        


#test
a = Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")
#print (a.inhaltget(1))

