from funktioner_inlam_marie_bayard import try_file
from funktioner_inlam_marie_bayard import open_file
from funktioner_inlam_marie_bayard import empty_file
from funktioner_inlam_marie_bayard import rovarsprak
from funktioner_inlam_marie_bayard import other_characters
from funktioner_inlam_marie_bayard import want_to_save
from funktioner_inlam_marie_bayard import save_file
from funktioner_inlam_marie_bayard import run_again

#whileloop för att anv ska kunna köra programmet (och kryptera fler filer) hur många gånger de vill utan att starta om programmet.
while True:
    print ('*' *40)
    print ('*'*10 +' Krypteringsprogram '+'*'*10)
    print ('*' *40)
    print()
    print ('För att avbryta programmet tryck Ctrl+C')
    print()
    
    try:
        exists= try_file()
        text = open_file (exists)
        empty = empty_file(text)
        translate = rovarsprak (text)
        not_swedish = other_characters (text)
        do_want_to_save = want_to_save()
        if do_want_to_save == True:
            save_file (translate)
        want_to_run_again = run_again()

    #om anv trycker Ctrl+C avslutas programmet och texten Programmet avslutas skrivs ut.    
    except KeyboardInterrupt: 
        print ('\nProgrammet avslutas!')
        exit()
