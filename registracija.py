from import_books import *
from json_files import *
def registracija():
    data = import_users()
    users = import_people()
    there_is = True

    while there_is:
        there_is = False
        username = input('unesite korisnicko ime: ')
        while username == '':
            print('unos nije validan \n')
            username = input('ponovo unesite zeljenu vrednost: ')
        for u in users:
            if username.lower() == u['username'].lower():
                print('ovo korisnicko ime postoji')
                print(f'morate uneti korisnicko ime koje nije {username.upper()}')
                there_is = True

    password = input('unesite lozinku: ')
    while password  == '':
        print('unos nije validan \n')
        password  = input('ponovo unesite zeljenu vrednost: ')
    name = input('unesite vase ime: ')
    while name == '':
        print('unos nije validan \n')
        name = input('ponovo unesite zeljenu vrednost: ')
    lastname = input('unesite vase prezime: ')
    while lastname == '':
        print('unos nije validan \n')
        lastname = input('ponovo unesite zeljenu vrednost: ')
    user_type = input('unesite tip korisnika (prodavac/menadzer): ')
    while user_type == '':
        print('unos nije validan \n')
        user_type = input('ponovo unesite zeljenu vrednost: ')
    keys = users[0].keys()
    vals = [username,password,name,lastname,user_type]
    d = {}
    for k, v in zip(keys, vals):
        if k not in d:
            d[k] = ''
            d[k] = v
    data['users'].append(d)
    add_users(data)
    print(f'uspesno ste registrovali korisnika {username.upper()} cija pozicija je {user_type.upper()} ')





if __name__ == '__main__':
    registracija()