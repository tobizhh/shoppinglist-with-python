einkaufsliste = [] #empty array for articles

def item_hinzufuegen():
    name = input("Artikelname: ") #input for the article names
    
    menge = 0
    while menge <= 0:
        try:
            menge = int(input("Anzahl: ")) #input for amount
            if menge <= 0: #check if amount is positive, when yes we can break out of the while
                print("Bitte positive Zahl eingeben!")
        except ValueError:
            print("Ungültige Eingabe!")
    
    preis = -1
    while preis < 0:
        try:
            preis = float(input("Preis: "))
            if preis < 0: #check if amount is positive, when yes we can break out of the while
                print("Preis darf nicht negativ sein!")
        except ValueError:
            print("Ungültige Eingabe!")
    
    artikel = { #define the article with our inputs
        "Name": name,
        "Menge": menge,
        "Preis": preis
    }
    einkaufsliste.append(artikel) #array gets expanded with new article
    print(f"{name} hinzugefügt!") #print out the message that the article was added

def artikel_loeschen(): #function to delete an article from the list
    if not einkaufsliste:
        print("Die Liste ist leer!") #if there is nothing in the Array we print this
        return
    
    liste_anzeigen() #call the function to show the list
    
    gueltige_eingabe = False
    while not gueltige_eingabe:
        try:
            index = int(input("Welche Artikelnummer möchtest du löschen? ")) - 1 #input to delete article / -1 bcs Array starts at 0
            if 0 <= index < len(einkaufsliste):
                geloeschter_artikel = einkaufsliste.pop(index) #article gets deleted with pop
                print(f"{geloeschter_artikel['Name']} wurde gelöscht!") #message that we deleted article
                gueltige_eingabe = True
            else: #else statement that the article number doesnt exist
                print("Ungültige Artikelnummer!")
        except ValueError:
            print("Bitte eine Zahl eingeben!")

def liste_anzeigen(): #function to show the list
    if not einkaufsliste: #if its empty we print an error
        print("Die Einkaufsliste ist leer!")
        return
    
    sortierte_liste = sorted(einkaufsliste, key=lambda x: x['Name'])
    
    print("\n--- Meine Einkaufsliste ---")
    for index, artikel in enumerate(sortierte_liste, 1):
        print(f"{index}. {artikel['Name']} - " 
              f"Menge: {artikel['Menge']} - " 
              f"Preis: {artikel['Preis']}€")

def hauptmenue():
    programmlaeuft = True
    while programmlaeuft:
        print("\n--- Einkaufslisten-Programm ---")
        print("1. Artikel hinzufügen")
        print("2. Liste anzeigen")
        print("3. Artikel löschen")
        print("4. Beenden") #print home menu to select what we want to do
        
        auswahl = input("Wähle eine Option (1-4): ") #input to select function
        # if-elif-else statement to start functions based on the input
        if auswahl == "1":
            item_hinzufuegen()
        elif auswahl == "2":
            liste_anzeigen()
        elif auswahl == "3":
            artikel_loeschen()
        elif auswahl == "4":
            print("Auf Wiedersehen!")
            programmlaeuft = False
        else:
            print("Ungültige Auswahl. Bitte 1-4 wählen.")

def main():
    print("Willkommen zum Einkaufslisten-Programm!")
    hauptmenue()

if __name__ == "__main__":
    main()
