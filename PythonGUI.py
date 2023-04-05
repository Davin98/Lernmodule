import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
import TabelleAuslesen
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename

startmodul = 0
endmodul = 0
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


def open_file():
    filepath = f()
    if not filepath:
        return
    txt_edit.delete("1.0",tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = f()
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
        window.title(f"Simple Text Editor - {filepath}")

Tabelle1 = TabelleAuslesen.Lernmodulsammlung("C:/Users/praktikant_software/Desktop/Davins_Git_Einstieg/Tabelle.txt")

#öffnen eines Fensters
window = tk.Tk()
window.title("Text Editor")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

#Funktion zum öffnen einer .txt datei
def open_file():
    if not f:
        return
    txt_edit.delete("1.0",tk.END)
    with open(f, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {f}")

def save_file():
    if not f:
        return
    with open(f, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
        window.title(f"Simple Text Editor - {f}")


def get_start_modul():
    with open(f, mode="r", encoding="utf-8"):
        text = ent_start_modul.get()
        global startmodul
        startmodul = int(text)
        return startmodul

def get_end_modul():
    with open(f, mode="r", encoding="utf-8"):
        text = ent_end_modul.get()
        global endmodul
        endmodul = int(text)
        return endmodul

def test_auführen():
    get_start_modul()
    get_end_modul()
    with open(f, mode="r", encoding="utf-8") as input_file:
        text = Tabelle1.abzuziehende_zeiten(startmodul,endmodul)
        txt_edit.insert(tk.END, text)
        



txt_edit = tk.Text(
    window,
    )
with open(f, mode="r", encoding="utf-8") as input_file:
    text = input_file.read()
    txt_edit.insert(tk.END, text)

frm_buttons = tk.Frame(
    master=window,
    relief=tk.RAISED,
    bd=2
    )

btn_open = tk.Button(
    master=frm_buttons,
    text="Refresh Text-File",
    command=open_file
)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save = tk.Button(
    master=frm_buttons,
    text="Save Text-File",
    command=save_file
)
btn_save.grid(row=1,column=0,sticky="ew",padx=5, pady=5)

btn_perform_test = tk.Button(
    master=frm_buttons,
    text=("Test ausführen"),
    command=test_auführen
    
)
btn_perform_test.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

lbl_start_modul = tk.Label(
    master=frm_buttons,
    text=("Bitte Start Modul eingeben"),
)
lbl_start_modul.grid(row=4, column=0, sticky="ew", padx=5, pady=5)


ent_start_modul = tk.Entry(
    master=frm_buttons,
)
ent_start_modul.grid(row=5,column=0,sticky="ew",padx=5, pady=5)

lbl_end_modul = tk.Label(
    master=frm_buttons,
    text=("Bitte End Modul eingeben"),
)
lbl_end_modul.grid(row=6, column=0, sticky="ew", padx=5, pady=5)

ent_end_modul = tk.Entry(
    master=frm_buttons,
)
ent_end_modul.grid(row=7,column=0,sticky="ew",padx=5, pady=5)


frm_buttons.grid(row=0,column=0,sticky="ns")

txt_edit.grid(row=0,column=1,sticky="nsew")



window.mainloop()