# Iteratie opdracht
# Start script voor opgave over sikkelcel
# (c) Martijn van der Bruggen, 2007-2010
# Updates:
# November 2010, code bijgewerkt met instructies voor de opdracht
# Hogeschool van Arnhem en Nijmegen

# Sequenties voor respectievelijk sikkelcel- en normale cellen
# Bekend is dat het gen coderend voor hemoglobine bij sikkelcel aandoening een andere nucleotide heeft
# De sequentie voor de sikkelcel en een "gezonde bloedcel" zijn hier onder gegeven
sikkel_seq = 'GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'
normaal_seq ='GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'

# In het bestand enzymen. txt staan kandidaat restrictie enzymen
# Opdracht schrijf een programma dat al deze enzymen doorloopt een suggestie
# geeft welk restrictie enzym welk knipt in de ene sequentie en niet in de andere sequentie
# Hiermee kunnen we diagnostisch enzym voorstellen om vast te stellen of een persoon
# drager is van het sikkelcel allel#
'''bestand = open ("enzymen.txt")


# Aanwijzingen voor het schrijven van je programma
# -------------------------------------------------------------
# Het lezen van een regel kan met bestand.readline()
# Lees door totdat je een lege regel aantreft
# Een regel bestaat uit twee stukken enzym en knipsequentie. Bijvoorbeeld: DdeI C^TGAG
# Het opsplitsen van een regel in twee stukken op de spatie kan middels: enzym, seq = regel.split()
# Door bovenstaande split verkrijg je twee variabelen enzym en seq, respectievelijk de naam van het enzym en de sequentie waar deze in knipt
# Verwijderen het dakje uit de seq met seq.replace("^","")
# --------------------------------------------------------------------

# Auteur:
# Datum:
# Functie:







for i in bestand:
    i = i.replace("^", "").split()      # Hier worden dakjes verwijderd uit sequenties en gesplits bij de spatie
    i.pop(0)                            # Eerste element word verwijderd uit de list dus namen van enzymen
    i = ''.join(i)                      # List word omgezet tot een string zodat het gebruikt kan worden in een if statement
    if i in normaal_seq and sikkel_seq:                 # Als de sequentie aanwezig is in sikkel_sequentie, word er ''knipt wel'' geprint
        print(i, "knipt WEL")
    else:                               # Als de sequentie niet aanwezig is in sikkel_sequentie, word er ''knipt niet'' geprint
        print(i, "knipt niet")



bestand.close()

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")'''
Bestand = open ("enzymen.txt")







# FINAL VERSION ###########################################################################################################################

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

for S in Bestand:
    S = S.replace("^", "").split()
    S.pop(0)
    S = ''.join(S)
    normaal = normaal_seq.find(S)
    sikkel = sikkel_seq.find(S)
    if normaal and sikkel == -1:
        print(S, "Knipt niet")
    else:
        print(S, "Knipt WEL in beide sequenties <----")




Bestand.close()
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

lijst = open("enzymen.txt")

list = lijst.readline().replace("^", "").split()

while list:
    print(list)
    list = lijst.readline().replace("^", "").split()




















