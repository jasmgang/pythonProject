import ast
import json

with open("stoffer.txt", "r") as f:
    indhold = f.read()
    densiteter = ast.literal_eval(indhold)


def densitet():
    ubek = input("rho = m / V, skriv den ubekendte faktor: ").lower()
    if ubek == "rho" or ubek == "r" or ubek == "p":
        try:
            mass = float(input("Skriv massen i g: "))
            vol = float(input("Skriv volumen i cm³: "))
        except ValueError:
            print("Skal være et tal")
            return densitet()
        print(f"{mass} g / {vol} cm³ = {round(mass/vol, 4)} g/cm³\n\n")

    elif ubek == "m":
        try:
            vol = float(input("Skriv volumen i cm³: "))
        except ValueError:
            print("Skal være et tal")
            return densitet()
        dens = getDensitet()
        if not dens:
            print("Ugyldigt input")
            return densitet()
        print(f"{vol} cm³ * {dens} g/cm³ = {round(vol*dens, 4)} g\n\n")

    elif ubek == "v":
        try:
            mass = float(input("Skriv massen i g: "))
        except ValueError:
            print("Skal være et tal")
            return densitet()
        dens = getDensitet()
        if not dens:
            print("Ugyldigt input")
            return densitet()
        print(f"{mass} g / {dens} g/cm³ = {round(mass / dens, 4)} cm³\n\n")
    elif ubek == "t":
        nynavn = input("Skriv navnet på det stof du ønsker at tilføje: ")
        try:
            nydens = float(input("Skriv densiteten på det nye stof i g/cm³: "))
            print("Hermed tilføjet\n")
        except ValueError:
            print("Skal være et tal")
            return densitet()
        densiteter[nynavn.capitalize()] = nydens
        with open('stoffer.txt', 'w') as f:
            f.write(json.dumps(densiteter))

    else:
        print("Ikke en mulighed")
    return densitet()


# Funktion til at finde et stofs densitet.
def getDensitet():
    global densiteter
    densinput = input("Hvilket stof vil du finde densiteten af? Her kan du også selv skrive en densitet i g/cm³: ")
    densinput = densinput.capitalize()
    if densinput in densiteter:
        return densiteter[densinput]
    else:
        try:
            densinput = float(densinput)
            return densinput
        except ValueError:
            return False

print(densitet())
