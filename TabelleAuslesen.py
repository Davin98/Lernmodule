# #in diesem programm sollen die Zeilen aus der Datei "Tabelle.txt" ausgelesen werden.

# print ("Bitte geben Sie an, welche Zeile Sie auslesen wollen. ")
# #der "input" Operator speichert den input als string, weshalb man diesen hier als int zu konvertieren
# x = int(input())
# x = x-1
# #Hier wird ie Zeile anhand der im input angegebenen Variable ausgegeben.
# with open("Tabelle.txt") as f:
#     data = f.readlines()[x]
# print(data)
# #In der if abfrage soll die letzte Zeile ermittelt werden und dann ein Text ausgegeben werden.
# if (x==data[-1]):
#     print("Glückwunsch, du hast die Lernsituation erfolgreich bestanden! ")




#Die Klasse soll die Lernmodulsammlung in Variablen konvertieren/ Klassenkürzel LM
class Lernmodul:
    Nr = int()
    Name = str(" ")
    nachgaenger = int()
    dauer = int()
#objekt Modul aus der Klasse Lernmodul
    def __init__(self, Nr, Name, nachgaenger, dauer):
        self.nr = Nr
        self.Name = Name
        self.nachgaenger = nachgaenger
        self.dauer = dauer
        
   
    
    
#die Klasse soll den Inhalt der Tabelle.txt in Variablen konvertieren/ Klassenkürzel LMS
class Lernmodulsammlung:

    def __init__(self,path):
        f = open("Tabelle.txt", "r")
#in der schleife sollen die Zeilen aus der Tabelle.txt importiert und in die Variablen geschrieben werden        
        for i in f.readlines():
            n = i.strip().split('\t')
            print(n)
            
            Nr = int(n[0])
            Name = n[1]
            nachgaenger = n[2]
            dauer = int(n[3])
            #Test print um zu gucken, ob die tabelle richtig gesplitted wird
            print(Nr, Name, nachgaenger, dauer)
            #Aufrufen der Klasse Lernmodul
            Lernmodul(Nr, Name, nachgaenger, dauer)
        f.close
        
#f.close schließt die Datei wieder

#test
a = Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")
print (a)
