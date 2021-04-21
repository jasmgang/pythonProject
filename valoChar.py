import random
karakter = ["Sage", "Killjoy", "Viper", "Cypher"]


def char(c):
    if "ja" in c or "j" in c or "" in c:
        return random.choices(karakter, weights=(50, 20, 10, 10), k=1)[0] + "\n\n"
    else:
        return "Så gå et andet sted hen, tak.\n\n"


while True:
    valg = input("Har du svært ved at vælge karakter? \n").lower()
    print(char(valg))
