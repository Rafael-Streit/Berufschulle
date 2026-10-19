from enum import Enum

class Status(Enum):
    FREI = "frei"
    BELEGT = "belegt"
    RESERVIERT = "reserviert"


def bereich(eingabe, unten, oben) -> bool:
    return unten <= eingabe <= oben


PP = [Status.FREI] * 10

while True:
    for i, status in enumerate(PP, start=1):
        print(f"Parkplatz {i} ist {status.value}")

    status_input = input(
        "\nStatus eingeben (frei, belegt, reserviert): "
    ).lower()

    try:
        status = Status(status_input)

        platz = int(input("Parkplatznummer: "))

        if not bereich(platz, 1, 10):
            print("Parkplatznummer muss zwischen 1 und 10 liegen!")
            continue

        PP[platz - 1] = status
        print(f"Parkplatz {platz} wurde {status.value}")

    except ValueError:
        print("Ungültiger Status oder Parkplatznummer!")

    print("-" * 40)
