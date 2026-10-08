
tovary = [
    {"nazva": "Telefon", "cena": 18500.00, "zalishok": 6},
    {"nazva": "Mishka", "cena": 650.50, "zalishok": 12},
    {"nazva": "Klaviatura", "cena": 1250.00, "zalishok": 8},
    {"nazva": "Navushnyky", "cena": 2750.75, "zalishok": 5}
]

koszyk = []


def pokazaty_katalog():
    print("\n Katalog ")

    for tovar in tovary:
        print(tovar["nazva"], "-", tovar["cena"], "грн",
              "Zalishok:", tovar["zalishok"])


def dodaty_v_koszyk(nazva, kilkist):
    for tovar in tovary:
        if tovar["nazva"] == nazva:
            if tovar["zalishok"] >= kilkist:
                koszyk.append({
                    "nazva": tovar["nazva"],
                    "cena": tovar["cena"],
                    "kilkist": kilkist
                })
                print("Tovar dodano.")
                return
            else:
                print("Nedostatno tovaru.")
                return

    print("Tovar ne znajdeno.")


def pokazaty_koszyk():
    print("\n Koszyk ")

    if len(koszyk) == 0:
        print("Koszyk pustyi.")
        return

    suma = 0

    for tovar in koszyk:
        cena = tovar["cena"] * tovar["kilkist"]
        suma = suma + cena

        print(tovar["nazva"], "x", tovar["kilkist"], "-", cena, "грн")

    print("Suma:", suma, "грн")


def vydalyty_z_koshyka(nazva):
    for tovar in koszyk:
        if tovar["nazva"] == nazva:
            koszyk.remove(tovar)
            print("Tovar vydaleno.")
            return

    print("Tovar ne znajdeno.")


def kupyty():
    if len(koszyk) == 0:
        print("Koszyk pustyi.")
        return

    suma = sum(map(lambda tovar:
                   tovar["cena"] * tovar["kilkist"], koszyk))

    for element in koszyk:
        for tovar in tovary:
            if tovar["nazva"] == element["nazva"]:
                tovar["zalishok"] = tovar["zalishok"] - element["kilkist"]

    print("Pokupka zavershena.")
    print("Suma:", suma, "грн")

    koszyk.clear()


def administrator():
    login = input("Login: ")
    parol = input("Parol: ")

    if login == "admin" and parol == "5678":
        print("\n Zalishky ")

        for tovar in tovary:
            print(tovar["nazva"], "-", tovar["zalishok"])
    else:
        print("Nevirnyi login abo parol.")


def main():
    while True:
        print("\n MAGAZYN ")
        print("1 - Katalog")
        print("2 - Dodaty v koszyk")
        print("3 - Koszyk")
        print("4 - Vydalyty z koszyka")
        print("5 - Kupyty")
        print("6 - Administrator")
        print("0 - Vykhid")

        vybir = input("Vyberit: ")

        if vybir == "1":
            pokazaty_katalog()

        elif vybir == "2":
            nazva = input("Nazva tovaru: ")
            kilkist = int(input("Kilkist: "))
            dodaty_v_koszyk(nazva, kilkist)

        elif vybir == "3":
            pokazaty_koszyk()

        elif vybir == "4":
            nazva = input("Nazva tovaru: ")
            vydalyty_z_koshyka(nazva)

        elif vybir == "5":
            kupyty()

        elif vybir == "6":
            administrator()

        elif vybir == "0":
            break

        else:
            print("Nevirnyi vybir.")


main()
