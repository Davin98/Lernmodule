#in diesem programm sollen die Zeilen aus der Datei "Tabelle.txt" ausgelesen werden.
f = open("Tabelle.txt", "r")
print ("Bitte geben Sie an, welche Zeile Sie auslesen wollen. ")
#der "input" Operator speichert den input als string, weshalb man diesen hier als int zu konvertieren
x = int(input())
x = x-1
#Hier wird ie Zeile anhand der im input angegebenen Variable ausgegeben.
with open("Tabelle.txt") as f:
    data = f.readlines()[x]
print(data)
if (x<=3):
    print("Glückwunsch, du hast die Lernsituation erfolgreich bestanden! ")





#f.close schließt die Datei wieder
f.close