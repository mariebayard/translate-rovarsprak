#testa om angivna filen finns
def try_file():
    while True:
        import os.path
        file1 = input ('Vilken fil vill du översätta; ')
        #ta bort mellanslag före och efter filnamnet
        path = file1.strip()
        check_file =os.path.isfile (path)
        #kontrollera om filen existerar,om filen finns; gå vidare i programmet
        if check_file == True:
            return file1
        #om filen inte finns får anv chans att skriva in filnamnet igen
        else:
            print ('Filen existerar inte, försök igen.')

#öppna filen
def open_file (file1):
    file = open (file1, 'r', encoding='utf-8')
    text = ''
    #läs in texten till variabeln text
    text = file.read()
    #stäng filen
    file.close 
    return text

#tom fil
#om tom fil ska anv bli uppmärksammad på detta.
def empty_file(text2):
    if text2=='':
        return print('OBS! Din fil innehåller ingen text.')

#tecken som inte ingår i svenska alfabetet.
def other_characters (text1):
    approved_characters = 'abscdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ  '
    non_approved = ''
    quantity = 0
    for j in text1:
        if j not in approved_characters:
            #lägg till alla bokstäver/tecken som inte kommer krypteras i icke_godkända, mellanrum mellan för att kunna splitta till lista
            non_approved +=j+' '
            #för att veta hur många tecken som inte krypteras räknas antal upp för varje tecken.
            quantity += 1
    #gör om till lista för att kunna loopa igenom tecknen        
    list = non_approved.split()
    #lista där alla dubbletter av tecknen tas bort för mer lättöverskådligt
    list2 = []
    for k in list:
        #för att enbart skriva tecknet 1 gång i utskriften
        if k not in list2: 
            #lägger till i lista2
            list2.append (k) 
    non_approved2 = ''
    #för att skriva de ej krypterade elementen i en sträng (snyggare utskrift i detta program)
    for l in list2: 
        non_approved2 +=l
    #om texten innehåller tecken som inte kommer krypteras görs anv uppmärksam på hur många och vilka tecken det gäller.
    if quantity !=0:
        return print (f'Observera att texten innehåller {quantity} tecken som inte kommer krypteras. Tecknen är;{non_approved2}')

#för att skriva som rövarspråk;
def rovarsprak (text):
    #Alla konsonanter i svenska alfabetet
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ' 
    translate = ''
    for i in text:
        #kollar för varje tecken i textfilen om det är konsonanter
        if i in consonants:
            #om bokstaven finns i konsonantlistan läggs o till mellan konsonanterna i översättningen
            #i.lower för att göra om den andra konsonanten till en gemen
            translate += i +'o'+i.lower()
        else:
            #om vokal/annat tecken läggs enbart det tecknet till i översättningen
            translate += i 
    return translate

#funktion som ger anv val att spara eller ej
def want_to_save ():
    while True:
        to_save = input('Vill du spara filen du har krypterat? (j/n) ')
        if to_save =='j':
            #True för att vi ska kunna anv det boolska värdet för nästa funktion i programmet
            return True 
        elif to_save== 'n':
            print ('Du har valt att inte spara filen')
            #False för att vi kör nästa funktion enbart om värdet på den här funktionen är True
            return False
        else:
            #för att säkra upp att anv anger ett tecken vi kan hantera i programmet. Om annat tecken får de nytt försök att skriva in
            print ('Du har angivit ett felaktigt tecken, försök igen') 
            
#för att spara filen
def save_file (translate):
    import os.path
    while True:
        save = input ('Vad vill du spara filen som? ')
        #för att programmet inte ska krascha om anv trycker enter direkt
        if save== '':
            print('Du måste skriva in ett filnamn.')
            #kör från början av whileloopen
            continue 
        save_text = translate
        #kontrollera om filen finns(vi vill inte att anv ska råka skriva över en existerande fil)
        test = os.path.isfile(save)
        if test != True:
            #filnamnet finns inte och det går bra att spara filen i detta namn. Loopen bryts
            break
        else:
            #ger nytt försök att spara filen till ett namn som inte redan finns. För att inte skriva över befintlig fil
            print('Filnamnet existerar redan, skriv in ett annat filnamn')
    file2 = open (save, 'w', encoding='utf-8')
    #skriver in den översatta texten till variabeln file1 och sparar i det namn anv angivit
    file2.write(save_text)
    file2.close
    #återger till anv att filen är sparad och valt filnamn
    return print (f'Filen är sparad som {save}')

#funktion för att ge anv val om de vill kryptera en ny fil utan att behöva stara om programmet.
def run_again():
    while True:
        again = input ('Vill du köra programmet igen och kryptera en ny fil? (j/n) ')
        #lower för att det inte ska spela någon roll om anv skriver versaler eller gemener
        again.lower()
        if again == 'j':
            #bryter loopen och går in i loopen som gör att programmet börjar från början
            break
        elif again == 'n':
            print ('Programmet avslutas')
            #avslutar programmet
            exit()
        else:
            print ('Du skrev ett felaktigt tecken, försök igen')
            #om anv skriver annat tecken än det som efterfrågas får de göra om. Loopen fortsätter tills anv angivit j eller n.
            continue
        