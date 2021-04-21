import random
from rich.console import Console

console = Console()

karakter = ['Astra', 'Breach', 'Brimstone', 'Cypher', 'Jett', 'Killjoy', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage',
            'Skye', 'Viper', 'Yoru']


def char(c):
    if "ja" in c or c == "j" or c == "":
        return f"Du skal spille" \
            f" [yellow]{random.choices(karakter, weights=(3, 2, 2, 12, 1, 20, 2, 2, 1, 1, 50, 5, 8, 1), k=1)[0]}[/yellow] i den næste kamp\n\n"
    else:
        return "Så gå et andet sted hen, tak.\n\n"


while True:
    valg = input("Har du svært ved at vælge karakter? \n").lower()
    console.print(char(valg))
