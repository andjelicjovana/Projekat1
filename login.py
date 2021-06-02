from json_files import *
from import_books import *

def login():
    data = import_people()
    print(data)

    uspeh = False
    for pokusaj in range(3):
        prijava_user = input('unesite vase korisnicko ime: ')
        while prijava_user == '':
            print('unos nije validan \n')
            prijava_user = input('ponovo unesite zeljenu vrednost: ')
        prijava_pass = input('unesite vasu lozinku: ')
        while prijava_pass  == '':
            print('unos nije validan \n')
            prijava_pass  = input('ponovo unesite zeljenu vrednost: ')
        for podatak in data:
            if prijava_user == podatak['username'] and prijava_pass == podatak['password']:
                uspeh = True
                sta_si = podatak['user_type']
                ko_si = podatak['username']
                print(f'uspesno ste se prijavili kao {sta_si.upper()} sa korisnickim imenom {ko_si.upper()}')
                return uspeh, sta_si, ko_si
        print('pogresno korisnicko ime ili lozinka')

    print('niste uneli tacne podatke, pokusajte ponovo')
    quit()


if __name__ == '__main__':
    login()