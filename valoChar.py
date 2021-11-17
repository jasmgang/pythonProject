import random
from rich.console import Console

console = Console()

karakter = ['Astra', 'Breach', 'Brimstone', 'Cypher', 'Jett', 'Killjoy', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage',
            'Skye', 'Viper', 'Yoru']


def char(c):
    if "ja" in c or c == "j" or c == "":
        return f"Du skal spille" \
            f" [yellow]{random.choices(karakter, weights=(20, 2, 3, 12, 1, 40, 3, 2, 1, 1, 15, 12, 25, 1), k=1)[0]}[/yellow] i den næste kamp\n\n"
    else:
        return "Så gå et andet sted hen, tak.\n\n"


if __name__ == "__main__":
    while True:
        valg = input("Har du svært ved at vælge karakter? \n").lower()
        console.print(char(valg))
