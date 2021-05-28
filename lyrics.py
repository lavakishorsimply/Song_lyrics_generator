import sys
import pyfiglet
text = pyfiglet.figlet_format('MUSIC WORLD')
print(text)
print('Welcome to Music World')
print('-'*60)
def English():
    print('You have Choosen English Album')

    while True:
        print(' 1.Alone\n 2.BoneyM_Rasputin\n 3.Beliver\n 4.Dance_Monkey\n 5.Falling\n 6.Memories\n 7.Ma Baker\n 8.Show_me_the_meaning\n 0.To change the Album\n 9.EXIT')
        print('-'*60)
        song = input("Please Choose the song:--")

        if song == '1':
            text = pyfiglet.figlet_format('F.A.D.E.D')
            print(text,'SINGER:--ALAN_WALKER')
            with open ('Faded.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)   

        elif song == '2':
            text = pyfiglet.figlet_format('R.A.S.P.U.T.I.N')
            print(text,'SINGER:--BONEY.M')
            with open ('Rasputin.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)               
        elif song == '3':
            text = pyfiglet.figlet_format('B.E.L.I.V.E.R')
            print(text,'SINGER:--DAN_REYNOLDS')
            with open ('Beliver.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)
                     
        elif song == '4':
            text = pyfiglet.figlet_format('D.A.N.C.E_M.O.N.K.E.Y')
            print(text,'SINGER:--TONES AND I')
            with open ('Dance_Monkey.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)               

        elif song == '5':
            text = pyfiglet.figlet_format('F.A.L.L.I.N.G')
            print(text,'SINGER:--TREVOR_DANIEL')
            with open ('Falling.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)
                
        elif song == '6':
            text = pyfiglet.figlet_format('M.E.M.O.R.I.E.S')
            print(text,'SINGER:--MAROON_5')
            with open ('Memories.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)
                 
        elif song == '7':
            text = pyfiglet.figlet_format('M.A_B.A.K.E.R')
            print(text,'SINGER:--BONEY.M')
            with open ('Ma_Baker.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)
                
        elif song == '8':
            text = pyfiglet.figlet_format('SHOW_ME_THE_MEANING')
            print(text,'SINGER:--BACKSTREET_BOYS')
            with open ('Show_me_the_meaning.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)
                      
        elif song == '0':
            Choice()
            
        elif song == '9':
            sys.exit('Thank You!')
        
        else:
            print('Out Of Selection Choose Again')

def Telugu():
    print('You have Choosen Telugu Album')
    print('-'*60)

    while True:
        print(' 1.Chitti\n 2.Kutty\n 0.To change the Album\n 9.EXIT')

        song = input("Please Choose the song:--")
        if song == '1':
            text = pyfiglet.figlet_format('C.H.I.T.T.I')
            print(text,'SINGER:--RAM_MIRIYALA')
            with open ('Chitti.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)
                
        elif song == '2':
            text = pyfiglet.figlet_format('K.U.T.T.Y')
            print(text,'SINGER:--ANIRUDH')
            with open ('Kutty.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)
                
        elif song == '0':
            Choice()
            
        elif song == '9':
            sys.exit('Thank You!')
        else:
            print('Out Of Selection Choose Again')
    
def Hindi():
    print('You have Choosen Hindi Album')
    print('-'*60)
    while True:
        print(' 1.Agar_Tum_Saath_Ho\n 0.To change the Album\n 9.EXIT')  
        print('-'*60)
        song = input("Please Choose the song:--")
        if song == '1':
            text = pyfiglet.figlet_format('AgarTumSathHo')
            print(text,'SINGER:--ARIJIT_SINGH')
            with open ('Agar_Tum_Saath_Ho.txt','r') as song_lyries:
                for line in song_lyries.readlines():
                    print(line)
                
        elif song == '0':
            Choice()
            
        elif song == '9':
            sys.exit('Thank You!')
        
        else:
            print('Out Of Selection Choose Again')
                
def Choice():
    while True:
        print(' 1.English\n 2.Telugu\n 3.Hindi\n 0.Exit')
        user = input("Please Select a Language:--")
        print('-'*60)

        if user == '1':
            English()
        elif user == '2':
            Telugu()
        elif user == '3':
            Hindi()
        elif user == '0':
            sys.exit('Thank You!')
        else:
            print('Out Of Selection Choose Again')
Choice()