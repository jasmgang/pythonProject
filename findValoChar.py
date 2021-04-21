from valoChar import char, karakter

def findAgent(agent):
    if agent in karakter:
        x = 1
        while True:
            if char("ja") == f"Du skal spille [yellow]{agent}[/yellow] i den næste kamp\n\n":
                break
            else:
                x+=1
        return f"Fandt {agent} i {x} forsøg"
    else:
        return "Den agent findes ikke"

if __name__ == "__main__":
    while True:
        inp = input("Hvem vil du finde? ").capitalize()
        print(findAgent(inp))