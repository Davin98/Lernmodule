#Hier soll die Hello world Datei ausgeführt werden.
import os
#tabelle wird erstellt und zeilen eingetragen
def appendtab(mdn,name,pos,dauer):
    f = open("Tabelle.txt", "a")
    f.write(mdn + "\t" + name + "\t" + pos + "\t" + dauer + "\n")
    f.close
#die Datei "Tabelle.txt" wird gelöscht
os.remove("Tabelle.txt")  
#in der Datei Tabelle.txt werden die folgenden zeilen eingetragen  
appendtab("1","Git","2,3","20")
appendtab("2","Py","0","5")
appendtab("3","Sps","0","30")
#einfacher input befehl, sodass das programm nicht sofort beendet wird

input ("")



