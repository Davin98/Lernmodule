#Hier soll die Hello world Datei ausgeführt werden.
import os
#tabelle erstellen nicht öffnen
def appendtab(mdn,name,pos,dauer):
    f = open("Tabelle.txt", "a")
    f.write(mdn + "\t" + name + "\t" + pos + "\t" + dauer + "\n")
    f.close
os.remove("Tabelle.txt")    
appendtab("1","Git","2,3","20")
appendtab("2","Py","0","5")
appendtab("3","Sps","0","30")

#abfrage des Ziellernmoduls
# if(x == 1):
#     print("Du hast bereits 20 Stunden geschafft. ")
# elif(x==3):
#     print("du hast bereits 30 Stunden geschafft. ")
# else:
#     print("Du hast bereits 25 Stunden geschafft.")
input ("")
# b = open (Hello_World())


