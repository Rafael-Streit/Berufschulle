status_text = {
    0: "frei",
    1: "belegt",
    2: "reserviert"
}

PP = [0] * 10

while True:
    for i, status in enumerate(PP, start=1):
        print(f"Parkplatz {i} ist {status_text[status]}")

    try:
        status = int(input("\nStatus (0=frei, 1=belegt, 2=reserviert): "))
        platz = int(input("Parkplatznummer: "))

        if status not in [0, 1, 2]:
            print("Status muss 0, 1 oder 2 sein!")
            continue

        if not 1 <= platz <= 10:
            print("Parkplatznummer muss zwischen 1 und 10 liegen!")
            continue

        PP[platz - 1] = status
        print(f"Parkplatz {platz} wurde {status_text[status]}")

    except ValueError:
        print("Fehler: Bitte nur ganze Zahlen eingeben!")

    print("-" * 40)