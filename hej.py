# hemmelig kode hovsa, ikke sig det til nogen
import random


def danielsvar(s):
    if "ja" in s or s == "si":
        return "liiihhh yay<3\n\n"
    else:
        return "Kom og få en krammer:)\n\n"


def dnivalo(v):
    if "jeppe" in v:
        return ":(\n\n"
    elif "ja" in v or "jae" in v or "jep" in v:
        return "lets goooo, carry mig pls<3\n\n"
    else:
        return ":( det var en ommer\n\n"


def secretkode(k):
    if k == "160920":
        return "<3 hvis jeg kunne havde jeg givet dig en.. øhm ... *billet*\n\n"
    elif k == "q":
        return "*Genstarter*\n\n"
    else:
        tryigen = input("Forkert kodeord, prøv igen:) (press q to restart)\n")
        return secretkode(tryigen)


def dnii(d):
    if "ja" in d:
        return "oh no, mig kan ikke være sur på dig:(\n\n"
    elif "nej" in d or "no" in d:
        return "Godtttttt<3\n\n"
    else:
        return "Kom og få en krammer!\n\n"


def math(en):
    try:
        en = int(en)
    except ValueError:
        return "Fejl under indtastning\n\n"
    tegn = input("Indsæt tegnet for din regnemetode:  \n")
    to = input("Indsæt 2. ciffer: \n")
    try:
        to = int(to)
    except ValueError:
        return "Fejl under indtastning\n\n"
    try:
        if tegn == "+":
            plus = en + to
            return f"Resultat: {plus}\n\n"
        elif tegn == "-":
            minus = en - to
            return f"Resultat: {minus}\n\n"
        elif tegn == "*":
            gange = en * to
            return f"Resultat: {gange}\n\n"
        elif tegn == "/":
            division = en / to
            return f"Resultat: {division}\n\n"
        elif tegn == "^" or "opløft" in tegn:
            oploft = en ** to
            return f"Resultat: {oploft}\n\n"
        elif "sqrt" in tegn or "kvadratrod" in tegn:
            sqrt = en ** (1 / to)
            return f"Resultat: {sqrt}\n\n"
        else:
            return "Det indtastede tegn er ikke et kendt og/eller understøttet regnesymbol\n\n"
    except ValueError:
        return "Fejl under indtastning\n\n"


def navn(hej):
    hej = hej.lower()
    if hej == "daniel philip nettelfield":
        dani = input("Goddag Hr; går det godt? \n").lower()
        return danielsvar(dani)

    elif hej == "daniel pilip nettofelt":
        return "Anne.... Lær at stave;)\n\n"

    elif hej == "daniel<3":
        kode = input("Så kom du så langt... Så hvad er kodeordet? (press q to restart)\n").lower()
        return secretkode(kode)

    elif "daniel" in hej:
        daniel = input("YAYYYY, har du så en god dag???\n").lower()
        return danielsvar(daniel)

    elif hej == "dnaiel":
        dna = input("Hej Dnaiel, mig ha' krammer?\n")
        if "ja" in dna or dna == "si":
            return "YAYAYAY<3\n\n"
        else:
            return "sorry ur answer is wrong\n\n"

    elif hej == "dni" or hej == "dani":
        dni = input("Tror du jeg er sur siden du skriver din forkortelse?\n").lower()
        return dnii(dni)

    elif "anne" in hej:
        return "Hejjjj Annee, jeg har savner dig <3\n\n"

    elif "mads" in hej:
        input("øhmm.... hvad laver du her?\n")
        return "Jamen okay..................................................\n\n"

    elif hej == "dniiboy":
        valo = input("Har du lyst til at spille valorant med mig?:) \n").lower()
        return dnivalo(valo)

    elif "kodeord" in hej:
        return "160920\n\n"

    elif "chris" in hej:
        return "ǝuᴉʇsᴉɹɥƆ THE SCIENCE QUEEN!! sᴉɹɥƆ-ǝuᴉʇ-THE-SCIENCE-QUEEN!!!\n\n"

    elif "cam" in hej:
        return "Cam.... Pro tip: Få dig en computer der kan have steam og fungere på samme tid;)\n\n"

    elif hej == "matpro":
        et = input("Indsæt 1. ciffer:  \n").lower()
        return math(et)

    elif hej == "jasmin fuglsang kristensen":
        jasnavn = input("Nej, det er mit navn, vil du købe det?\n").lower()
        if "ja" in jasnavn:
            return "Det var en joke din hat.\n\n"
        elif "nej" in jasnavn:
            return "Well, det var et forsøg værd. Så må jeg jo bare tage på arbejde for at tjene penge...\n\n"
        else:
            return "Du kan tydeligvis ikke finde ud af hverken at svare ja eller nej. Konklusion: Du er ubeslutsom," \
                   "gør noget ved det\n\n"

    elif "jas" in hej:
        return "Nej det er mit navn >:(, få dig et nyt.\n\n"

    elif "hej" in hej:
        hejsvar1 = random.choice(["Hejsa", "Hejjjj", "Goddag", "Øhmm hej", "BØH", "Hyggehejsa", "MOJN DO"])
        return f"{hejsvar1}\n\n"

    else:
        input("Goddag, undskyld men kender jeg dig?\n")
        return "nårh... jamen... goddag, I guess\n\n"


while True:
    x = input("Hej, hvad hedder du? \n")
    print(navn(x))

"hej"