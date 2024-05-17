import json

# Nazwa pliku do przechowywania listy
NAZWA_PLIKU = "lista_todo.json"

# Lista rzeczy do zrobienia
lista_todo = []

# Funkcja wczytywania listy z pliku
def wczytaj_liste():
    global lista_todo
    try:
        with open(NAZWA_PLIKU, "r") as f:
            lista_todo = json.load(f)
    except FileNotFoundError:
        lista_todo = []

# Funkcja zapisywania listy do pliku
def zapisz_liste():
    with open(NAZWA_PLIKU, "w") as f:
        json.dump(lista_todo, f)

# Funkcja dodawania pozycji
def dodaj_pozycje(nazwa):
    while True:
        try:
            kategoria = input("Kategoria (zrobienia, zabrania, kupienia): ")
            if kategoria not in ("zrobienia", "zabrania", "kupienia"):
                raise ValueError
            break
        except ValueError:
            print("Niepoprawna kategoria. Wprowadź 'zrobienia', 'zabrania' lub 'kupienia'.")
    pozycja = {"nazwa": nazwa, "kategoria": kategoria}
    lista_todo.append(pozycja)

# Funkcja wyświetlania listy
def wyswietl_liste():
    if not lista_todo:
        print("Lista jest pusta.")
        return

    for i, pozycja in enumerate(lista_todo):
        print(f"{i+1}. {pozycja['nazwa']}: {pozycja['kategoria']}")

# Funkcja sortowania pozycji
def sortuj_pozycje():
    zrobienia = []
    zabrania = []
    kupienia = []

    for pozycja in lista_todo:
        if pozycja["kategoria"] == "zrobienia":
            zrobienia.append(pozycja)
        elif pozycja["kategoria"] == "zabrania":
            zabrania.append(pozycja)
        elif pozycja["kategoria"] == "kupienia":
            kupienia.append(pozycja)

    zrobienia.sort(key=lambda pozycja: pozycja["nazwa"])
    zabrania.sort(key=lambda pozycja: pozycja["nazwa"])
    kupienia.sort(key=lambda pozycja: pozycja["nazwa"])

    lista_todo.clear()
    lista_todo.extend(zrobienia)
    lista_todo.extend(zabrania)
    lista_todo.extend(kupienia)

# Funkcja usuwania pozycji
def usun_pozycje(indeks):
    if not lista_todo:
        print("Lista jest pusta. Nie ma nic do usunięcia.")
        return

    if indeks < 1 or indeks > len(lista_todo):
        print(f"Błędny indeks: {indeks}. Dostępne indeksy to 1-{len(lista_todo)}.")
        return

    usuwana_pozycja = lista_todo.pop(indeks - 1)
    print(f"Usunięto: {usuwana_pozycja['nazwa']} ({usuwana_pozycja['kategoria']})")

# Funkcja edycji pozycji
def edytuj_pozycje(indeks):
    if not lista_todo:
        print("Lista jest pusta. Nie ma nic do edycji.")
        return

    if indeks < 1 or indeks > len(lista_todo):
        print(f"Błędny indeks: {indeks}. Dostępne indeksy to 1-{len(lista_todo)}.")
        return

    pozycja = lista_todo[indeks - 1]
    nowa_nazwa = input(f"Podaj nową nazwę dla {pozycja['nazwa']}: ")
    nowy_rodzaj = input(f"Podaj nową kategorię (zrobienia, zabrania, kupienia) {pozycja['nazwa']}: ")

    pozycja["nazwa"] = nowa_nazwa
    pozycja["kategoria"] = nowy_rodzaj
    print(f"Edytowano: {pozycja['nazwa']} ({pozycja['kategoria']})")

# Wczytaj listę przy starcie programu
wczytaj_liste()

# Komunikaty powitalne
print("Witaj! Twoje osobiste remedium na skleroze !")
print("Nie daj się zaskoczyć! Dodawaj rzeczy do zrobienia, zabrania lub kupienia:")

while True:
    komenda = input("[dodaj/pokaz/sortuj/usun/edytuj/quit]: ")

    if komenda == "dodaj":
        nazwa = input("Nazwa rzeczy: ")
        dodaj_pozycje(nazwa)

    elif komenda == "pokaz":
        wyswietl_liste()

    elif komenda == "sortuj":
        sortuj_pozycje()
        wyswietl_liste()

    elif komenda == "usun":
        try:
            indeks = int(input("Podaj indeks pozycji do usunięcia: "))
        except ValueError:
            print("Niepoprawny format indeksu. Wprowadź liczbę całkowitą.")
            continue
        usun_pozycje(indeks)

    elif komenda == "edytuj":
        try:
            indeks = int(input("Podaj indeks pozycji do edycji: "))
        except ValueError:
            print("Niepoprawny format indeksu. Wprowadź liczbę całkowitą.")
            continue
        edytuj_pozycje(indeks)

    elif komenda == "quit":
        zapisz_liste()  # Zapisz listę przed wyjściem
        print("Zakończono działanie programu. Miłego zapominania!")
        break

    else:
        print("Nieznana komenda. Spróbuj ponownie.")
