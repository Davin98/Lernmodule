import tkinter as tk #Importier die Tkinter bibliothek und setzt den Name im Programm als tk
import tkinter.ttk as ttk # Importiert die ttk unterbibliothek (Modernerer Look) und setzt den Namen als ttk
# # # # # # # # window = tk.Tk() #erstellt ein fenster
# # # # # # # # greeting = tk.Label( #Hier wird eine Klasse greeting als Label generiert
# # # # # # # #     text="Name!", #Der inhalt des Textes
# # # # # # # #     fg="white", #Die Farbe des fordergrund (Text) des Textes| man kann auch mit fg abkürzen, sofern man tk nutzt anstelle von ttk
# # # # # # # #     bg="red", #Die Farbe des Hintergrund des Textes| man kann auch mit bg abkürzen, sofern man tk nutzt anstelle von ttk
# # # # # # # #     width=10,#gibt an, wie breit das Label sein wird
# # # # # # # #     height=1#gibt an, wie hoch das Label sein wird
# # # # # # # #     )
# # # # # # # # greeting.pack() #Instanziiert die Klasse greeting
# # # # # # # # entry = tk.Entry(#erstellt eine Klasse entry, in der der Nutzer einen Text eingeben kann
# # # # # # # #     fg="black", #same as Label or Button
# # # # # # # #     bg="white",#same as Label or Button
# # # # # # # #     width=50
# # # # # # # # )
# # # # # # # # entry.pack()#Instanziiert die Klasse entry

# # # # # # # # button = tk.Button( #Erstellt einer Klasse button als Button
# # # # # # # #     text="Namen Speichern", #Gibt dem Button einen Namen
# # # # # # # #     width=15,
# # # # # # # #     height=2,
# # # # # # # #     bg="white",
# # # # # # # #     fg="black"
# # # # # # # #     )
# # # # # # # # button.pack()#Instanziiert die Klasse button
# # # # # # # # #Name = entry.get() speichert die eingabe in aus dem Entry in die Variable "Name"
# # # # # # # # entry.insert(10,"Python")#speichert den Text "Python" in die Klasse entry als text mit der angegebenen Pos, wenn bereits ein text vorhanden ist
# # # # # # # # #oder an der 0ten stelle, wenn noch kein text vorhanden ist

# # # # # # # # text_box = tk.Text()#erstellt eine Klasse text_box als Text. der unterschied zum Label ist, dass der Text viel größer ist
# # # # # # # # text_box.pack()#instanziiert die klasse text_box
# # # # # # # # text_box.insert("1.0","Hello")
# # # # # # # # text_box.delete("1.0","1.2")#.delete("1.0","1.2") löscht die eingabe in zeile 1 stelle 0 bis zeile 1 stelle 2
# # # # # # # # text_box.insert("2.0","\nWorld")#\n wird genutzt um ein Zeilenumbruch zu generieren| ohne \n fügt er das wort an die letzte stelle aus zeile 1

# # # # # # # # #Text = text_box.get()speichert nur die erste stelle aus dem Text.
# # # # # # # # #Text = text_box.get("1.0")speichert die Eingabe in dem Text von zeile 1 und stelle 0
# # # # # # # # #Mit der zeile #window.destroy() schließt man die Klasse wieder
# # # # # # # # #Text = text_box.get("1.0","1.5")speichert die eingabe von zeile 1 stelle 0 bis zeile 1 stelle 4
# # # # # # # # #Text = text_box.get("1.0",tk.END)speichert alles ab zeile 1 stelle 0 (einschlieslich \n für jeden Zeilenumbruch)
# # # # # # # # #wenn alle eingaben aus einer zeile gelöscht werden, rücken die eingaben aller nachfolgenden zeilen einen auf.

# # # # # # # # frame = tk.Frame()
# # # # # # # # frame.pack()

# # # # # # # # #jedes argument muss vor .mainloop ausgeführt werden

# # # # # # # #window.mainloop()#Lädt das Fenster mit den Instanziierten Klassen

# # # # # # # window = tk.Tk()

# # # # # # # frame_a = tk.Frame()#.Frame nutzt man, um seine klassen geordnet anzeigen zu können.
# # # # # # # frame_b = tk.Frame()

# # # # # # # label_a = tk.Label(master=frame_a, text="I'm in Frame A")#mit dem master= befehl kann man eine klasse zu einem bestimmten Frame zuordnen

# # # # # # # label_a.pack()

# # # # # # # label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# # # # # # # label_b.pack()

# # # # # # # frame_b.pack()
# # # # # # # frame_a.pack()

# # # # # # # window.mainloop()

# # # # # # # Frames können visuell angepasst werden, der Nachfolgende Teil zeigt alle befehle von .FLAT bis .RIDGE
# # # # # # border_effects = {
# # # # # #     "flat": tk.FLAT,
# # # # # #     "sunken": tk.SUNKEN,
# # # # # #     "raised": tk.RAISED,
# # # # # #     "groove": tk.GROOVE,
# # # # # #     "ridge": tk.RIDGE,
# # # # # # }

# # # # # # window = tk.Tk()

# # # # # # for relief_name, relief in border_effects.items():
# # # # # #     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
# # # # # #     frame.pack(side=tk.LEFT)
# # # # # #     label = tk.Label(master=frame, text=relief_name)
# # # # # #     label.pack()
# # # # # # #.pack() erstellt eine rechteckige flaeche "parcel" welche gerade groß genug ist, dass es das widget abbilden kann
# # # # # # #.pack() zentriert das widget, es sei denn eine andere location ist angegeben

# # # # # # window.mainloop()

# # # # # #.pack() ist eins von 3 geometry manager tools. es gibt ausserdem .place() und .grid()
# # # # # #.grid() wird am heaufigsten verwendet. hierdurch wird das Frame oder Window in Zeilen und Spalten geteilt,
# # # # # #welche man dann direkt ansteuern kann.

# # # # # #.place() wird in der Regel bei karten verwendet. Denn durch den .place() befehl wird ein widget an einem exakten Ort
# # # # # #im window oder Frame gesetzt.
# # # # # window = tk.Tk()
# # # # # #in diesem beispiel wird ein grid im frame erstellt, welches 3 Reihen und spalten hat.
# # # # # #in jeder reihe und spalte wird ein Label mit der entsprechenden Reihen und Spalten Nr. eingefügt.
# # # # # for i in range(3):
# # # # #     #.columnconfigure und .rowconfigure erlauben den grits innerhalb des Window sich an die Window größe anzupassen
# # # # #     # weight gibt dabei die Rate der vergrößerung an z.B. 0 = keine veränderung 1 = 1zu1 veränderung und 2 = 2zu1 veränderung
# # # # #     #widgets sind normalerweise im grid zentriert
# # # # #     window.columnconfigure(i, weight=1, minsize=75)
# # # # #     window.rowconfigure(i, weight=1, minsize=50)
# # # # #     for j in range(3):
# # # # #         frame = tk.Frame(
# # # # #             master=window,
# # # # #             relief=tk.RAISED,
# # # # #             borderwidth=1
# # # # #         )
# # # # #         #um widgets nicht zentrisch auszurichten, muss man im .grid befehl den sticky parameter einfügen
# # # # #         #es gibt "n" für Top-Center
# # # # #         #"e" für Right-Center
# # # # #         #"s" für Bottom-Center
# # # # #         #und "w" für Left-Center
# # # # #         #die werte kann man sich anhand des Kompas merken "n"orth, "e"ast, "s"outh, "w"est
# # # # #         #die ausrichtungen können auch kombiniert werden. z.B. sticky=nw für obenlinks
# # # # #         #ohne sticky befehl füllt das widget die minimal mögliche größe des grids ohne dabei das Label zu croppen
# # # # #         #mit sticky=ns oder sticky=ew füllt das wigdet das grid entweder horizontal oder vertikal
# # # # #         #mit sticky=nsew füllt das widget das komplette grid aus
# # # # #         frame.grid(row=i, column=j, sticky="n")
# # # # #         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
# # # # #         #padx/y addiert 5 pixel an jeden x und y graphen der Label
# # # # #         label.pack(padx=5, pady=5)

# # # # # window.mainloop()

# # # # # Test
# # # # window = tk.Tk()

# # # # window.title("Address entry Form")

# # # # frame_main = tk.Frame(
# # # #     master=window,
# # # #     relief=tk.SUNKEN,
# # # #     borderwidth=1
# # # # )
# # # # frame_main.pack()


# # # # lbl_Vorname = tk.Label(master=frame_main,text="Vorname: ")
# # # # ent_Vorname = tk.Entry(master=frame_main,width=50)
# # # # lbl_Vorname.grid(row=0, column=0, sticky="e")
# # # # ent_Vorname.grid(row=0, column=1)

# # # # lbl_Nachname = tk.Label(master=frame_main,text="Nachname: ")
# # # # ent_Nachname = tk.Entry(master=frame_main,width=50)
# # # # lbl_Nachname.grid(row=1, column=0, sticky="e")
# # # # ent_Nachname.grid(row=1, column=1)

# # # # lbl_Adresse = tk.Label(master=frame_main,text="Adresse: ")
# # # # ent_Adresse = tk.Entry(master=frame_main,width=50)
# # # # lbl_Adresse.grid(row=2, column=0, sticky="e")
# # # # ent_Adresse.grid(row=2, column=1)

# # # # lbl_Adresszusatz = tk.Label(master=frame_main,text="Adresszusatz: ")
# # # # ent_Adresszusatz = tk.Entry(master=frame_main,width=50)
# # # # lbl_Adresszusatz.grid(row=3, column=0, sticky="e")
# # # # ent_Adresszusatz.grid(row=3, column=1)

# # # # lbl_Stadt = tk.Label(master=frame_main,text="Stadt: ")
# # # # ent_Stadt = tk.Entry(master=frame_main,width=50)
# # # # lbl_Stadt.grid(row=4, column=0, sticky="e")
# # # # ent_Stadt.grid(row=4, column=1)

# # # # lbl_Bundesland = tk.Label(master=frame_main,text="Bundesland: ")
# # # # ent_Bundesland = tk.Entry(master=frame_main,width=50)
# # # # lbl_Bundesland.grid(row=5, column=0, sticky="e")
# # # # ent_Bundesland.grid(row=5, column=1)

# # # # lbl_Postleitzahl = tk.Label(master=frame_main,text="Plz: ")
# # # # ent_Postleitzahl = tk.Entry(master=frame_main,width=50)
# # # # lbl_Postleitzahl.grid(row=6, column=0, sticky="e")
# # # # ent_Postleitzahl.grid(row=6, column=1)

# # # # lbl_Land = tk.Label(master=frame_main,text="Land: ")
# # # # ent_Land = tk.Entry(master=frame_main,width=50)
# # # # lbl_Land.grid(row=7, column=0, sticky="e")
# # # # ent_Land.grid(row=7, column=1)

# # # # frm_buttons = tk.Frame()
# # # # frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# # # # btn_Abschicken = tk.Button(master=frm_buttons,text="Abschicken")
# # # # btn_Abschicken.pack(side=tk.RIGHT, ipadx=10,ipady=10)

# # # # btn_Loeschen = tk.Button(master=frm_buttons,text="Loeschen")
# # # # btn_Loeschen.pack(side=tk.RIGHT, ipadx=10,ipady=10)




# # # # window.mainloop()

# # # #lösung

# # # # Create a new window with the title "Address Entry Form"
# # # window = tk.Tk()
# # # window.title("Address Entry Form")

# # # # Create a new frame `frm_form` to contain the Label
# # # # and Entry widgets for entering address information
# # # frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# # # # Pack the frame into the window
# # # frm_form.pack()

# # # # List of field labels
# # # labels = [
# # #     "Vorname:",
# # #     "Nachname:",
# # #     "Addresse:",
# # #     "Addresszusatz:",
# # #     "Stadt:",
# # #     "Bundesland:",
# # #     "Postleitzahl:",
# # #     "Land:",
# # # ]

# # # # Loop over the list of field labels
# # # for idx, text in enumerate(labels):
# # #     # Create a Label widget with the text from the labels list
# # #     label = tk.Label(master=frm_form, text=text)
# # #     # Create an Entry widget
# # #     entry = tk.Entry(master=frm_form, width=50)
# # #     # Use the grid geometry manager to place the Label and
# # #     # Entry widgets in the row whose index is idx
# # #     label.grid(row=idx, column=0, sticky="e")
# # #     entry.grid(row=idx, column=1)

# # # # Create a new frame `frm_buttons` to contain the
# # # # Submit and Clear buttons. This frame fills the
# # # # whole window in the horizontal direction and has
# # # # 5 pixels of horizontal and vertical padding.
# # # frm_buttons = tk.Frame()
# # # frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# # # # Create the "Submit" button and pack it to the
# # # # right side of `frm_buttons`
# # # btn_submit = tk.Button(master=frm_buttons, text="Abschicken")
# # # btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# # # # Create the "Clear" button and pack it to the
# # # # right side of `frm_buttons`
# # # btn_clear = tk.Button(master=frm_buttons, text="Löschen")
# # # btn_clear.pack(side=tk.RIGHT, ipadx=10)

# # # # Start the application
# # # window.mainloop()

# # window = tk.Tk()
# # window.title("Roll the Dice")
# # import random

# # # def increase():
# # #     value = int(lbl_value["text"])
# # #     lbl_value["text"] = f"{value + 1}"

# # # def decrease():
# # #     value = int(lbl_value["text"])
# # #     lbl_value["text"] = f"{value - 1}"

# # def roll():
# #     value = int(lbl_value["text"])
# #     value = 0
# #     lbl_value["text"] = f"{value + random.randint(1,6)}"

# # def zeroing():
# #     value = int(lbl_value["text"])
# #     value = 0
# #     lbl_value["text"] = f"{value}"

# # window.rowconfigure(0, minsize=50, weight=1)
# # window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# # btn_decrease = tk.Button(master=window, text="Set 0", command=zeroing)
# # btn_decrease.grid(row=0, column=0, sticky="nsew")

# # lbl_value = tk.Label(master=window, text="0")
# # lbl_value.grid(row=0, column=1)

# # btn_increase = tk.Button(master=window, text="Roll",command=roll)
# # btn_increase.grid(row=0, column=2, sticky="nsew")

# # window.mainloop()

# window = tk.Tk()
# window.title("Fahrenheit zu Celsius converter")
# window.resizable(width=False, height=False)

# def fahrenheit_to_celsius():
#     """Convert the value for Fahrenheit to Celsius and insert the
#     result into lbl_result.
#     """
#     fahrenheit = ent_temparatur.get()
#     celsius = (5 / 9) * (float(fahrenheit) - 32)
#     lbl_ergebnis["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# frm_entry = tk.Frame(master=window)
# ent_temparatur = tk.Entry(master=frm_entry, width=10)
# lbl_temp = tk.Label(master=frm_entry,text="\N{DEGREE FAHRENHEIT}")

# ent_temparatur.grid(row=0, column=0,sticky="e")
# lbl_temp.grid(row=0,column=1,sticky="w")

# btn_convert = tk.Button(
#     master=window,
#     text="\N{RIGHTBACKWARDS BLACK ARROW}",
#     command=fahrenheit_to_celsius
# )
# lbl_ergebnis = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# frm_entry.grid(row=0,column=0,padx=10)
# btn_convert.grid(row=0,column=1,pady=10)
# lbl_ergebnis.grid(row=0,column=2,padx=10)

# window.mainloop()

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Set up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()
