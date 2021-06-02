from import_books import *

def prikaz_korisnika():
    users = import_people()
    while True:
        print('odaberite zeljenu akciju')
        print('1. soritranje po imenu')
        print('2. soritranje po prezimenu')
        print('3. soritranje po tipu korisnika')
        print('4. izlaz')

        izbor = input('unesite vas izbor: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')
        if izbor == '1':
            for i in range(len(users)):
                for j in range(len(users)):
                    if users[i]['name'].lower() < users[j]['name'].lower():
                        users[i], users[j] = users[j], users[i]
            break
        elif izbor == '2':
            for i in range(len(users)):
                for j in range(len(users)):
                    if users[i]['lastname'].lower() < users[j]['lastname'].lower():
                        users[i], users[j] = users[j], users[i]
            break
        elif izbor == '3':
            for i in range(len(users)):
                for j in range(len(users)):
                    if users[i]['user_type'].lower() < users[j]['user_type'].lower():
                        users[i], users[j] = users[j], users[i]
            break
        elif izbor == '4':
            return


    no_password = []
    for u in users:
        u.pop('password')
        no_password.append(u)

    pretty_print(no_password)



if __name__ == '__main__':
    prikaz_korisnika()