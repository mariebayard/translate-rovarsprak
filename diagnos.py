'''
Psudokod för uppgiften;
Skapa en funktion, primtal, som tar in ett argument.
Argumentet ska referera till input från användaren.
Om input är <2 eller >99:
    Ange; Felaktigt värde.
    Avsluta programmet
Annars;
Kör programmet
Skapa en tom lista
Lägg in alla talen inom givna intervallet i listan
Loopa igenom tal för tal i listan (här benämnt med j)
    Loopa igenom resterande tal i listan och jämför med talet j i första listan.
        Om resterande tal är större än talet j och de är jämnt delbara med talet j -->
            Det jämförda talet är inte ett primtal. Ta bort det ur listan
returnera listan med kvarvarande tal som är primtal.
'''

def primtal (n):
    if n <2 or n>99:
        print ('Du har angivit ett felaktigt värde.')
        exit()
    tal = []
    for i in range (2,n+1): #loopar igenom alla tal från 2 till n (+1 för att få in sista värdet)
        tal.append (i) #lägger till alla värden inom angivna intervallet i listan tal

    for j in tal: #loopar igenom listan tal
        for k in tal: #loopar igenom listan för att kunna kontrollera k mot j.
            if k> j and k % j ==0: #jämför om k är större än j som är talet jag vill jämföra med (för att inte ta bort själva primtalet, därav störr än). Om k är jämnt delbart med j är det inte ett primtal.
                tal.remove (k) #tar bort k, dvs talen som inte är primtal.
    return (tal) #returnerar listan med primtal.

n= int (input('ange ett tal; '))
print (primtal(n))# anropar och printar funktionen.

