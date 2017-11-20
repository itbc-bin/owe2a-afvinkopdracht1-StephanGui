# Naam:
# Datum:
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.
def main():
    bestand = "alpaca1.fa" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    zoekwoord = input("Geef een zoekwoord op: ")
    for item in range(len(headers)):
        if zoekwoord in headers[item]:
            print(headers[item])
            print(seqs[item])
#-------------------------------------------------------------------------------------
def lees_inhoud():
    try:
        with open(input("Voer hier de naam in >")) as fasta:
            headers = []
            seqs = []
            lines = ""
            for line in fasta:
                lines += line
                sequences = lines.split(">")
        # de pop functie haalt de eerste index uit de lijst. Die is in dit geval leeg.
                sequences.pop(0)
                for i in range(len(sequences)):
                    header, seq = sequences[i].split("\n",1)
                    seq = seq.replace("\n","")
                    headers.append(header)
                    seqs.append(seq)
    except FileNotFoundError:
            print("Deze file bestaat niet probeer opnieuw.")
    return headers, seqs
#--------------------------------------------------------------------------------------
def is_dna(headers, seqs):
    for i in range(len(seqs)):
        valid = "ATCG"
        for letter in seqs[i]:
            if letter in valid:
                return True
            else:
                return False
#--------------------------------------------------------------------------------------
def knipt(header, seqs):
    try:
        bestand = open(input("Voer hier het bestand in >"))
        for regel in bestand.readlines():
            enzym,seq = regel.split()
            seq = seq.replace("^","")
            for i in range(len(seqs)):
                if seq in seqs[i]:
                    print(seq)
                    print(enzym, "knipt op plaats", seqs[i].index(seq))
                    print(seqs[i])
    except FileNotFoundError:
        print("De file is niet te vinden")
                #print(" " * (seqs[i].index(seq)-1), seq)
headers, seqs = lees_inhoud()
print("MAIN","-"*150)
main()
print("\n"*2)
print("DNA CHECKER","-"*150)
is_dna(headers, seqs)
print("\n"*2)
print("ENZYM CHECKER","-"*150)
knipt(headers, seqs)
